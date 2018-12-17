"""
pghoard - list and restore basebackups

Copyright (c) 2016 Ohmu Ltd
See LICENSE for details
"""
from . import common, config, logutil, version
from .postgres_command import PGHOARD_HOST, PGHOARD_PORT
# ignore pylint/distutils issue, https://github.com/PyCQA/pylint/issues/73
from distutils.version import LooseVersion  # pylint: disable=no-name-in-module,import-error
from pghoard.rohmu import compat, dates, get_transfer, rohmufile
from pghoard.rohmu.errors import Error, InvalidConfigurationError
from psycopg2.extensions import adapt
from requests import Session
from threading import RLock
import argparse
import datetime
import errno
import io
import logging
import multiprocessing
import multiprocessing.pool
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import uuid


class RestoreError(Error):
    """Restore error"""


def create_recovery_conf(dirpath, site, *,
                         port=PGHOARD_PORT,
                         primary_conninfo=None,
                         recovery_end_command=None,
                         recovery_target_action=None,
                         recovery_target_name=None,
                         recovery_target_time=None,
                         recovery_target_xid=None,
                         restore_to_master=None):
    restore_command = [
        "pghoard_postgres_command",
        "--mode", "restore",
        "--port", str(port),
        "--site", site,
        "--output", "%p",
        "--xlog", "%f",
    ]
    lines = [
        "# pghoard created recovery.conf",
        "recovery_target_timeline = 'latest'",
        "trigger_file = {}".format(adapt(os.path.join(dirpath, "trigger_file"))),
        "restore_command = '{}'".format(" ".join(restore_command)),
    ]
    if not restore_to_master:
        lines.append("standby_mode = 'on'")
    if primary_conninfo:
        lines.append("primary_conninfo = {}".format(adapt(primary_conninfo)))
    if recovery_end_command:
        lines.append("recovery_end_command = {}".format(adapt(recovery_end_command)))
    if recovery_target_action:
        with open(os.path.join(dirpath, "PG_VERSION"), "r") as fp:
            pg_version = fp.read().strip()
        if LooseVersion(pg_version) >= "9.5":
            lines.append("recovery_target_action = '{}'".format(recovery_target_action))
        elif recovery_target_action == "promote":
            pass  # default action
        elif recovery_target_action == "pause":
            lines.append("pause_at_recovery_target = True")
        else:
            print("Unsupported recovery_target_action {!r} for PostgreSQL {}, ignoring".format(
                recovery_target_action, pg_version))
    if recovery_target_name:
        lines.append("recovery_target_name = '{}'".format(recovery_target_name))
    if recovery_target_time:
        lines.append("recovery_target_time = '{}'".format(recovery_target_time))
    if recovery_target_xid:
        lines.append("recovery_target_xid = '{}'".format(recovery_target_xid))
    content = "\n".join(lines) + "\n"
    filepath = os.path.join(dirpath, "recovery.conf")
    filepath_tmp = filepath + ".tmp"
    with open(filepath_tmp, "w") as fp:
        fp.write(content)
    os.rename(filepath_tmp, filepath)
    return content


def print_basebackup_list(basebackups, *, caption="Available basebackups", verbose=True):
    print(caption, "\n")
    fmt = "{name:40}  {size:>11}  {orig_size:>11}  {time:20}".format
    print(fmt(name="Basebackup", size="Backup size", time="Start time", orig_size="Orig size"))
    print(fmt(name="-" * 40, size="-" * 11, time="-" * 20, orig_size="-" * 11))
    for b in sorted(basebackups, key=lambda b: b["name"]):
        meta = b["metadata"].copy()
        lm = meta.pop("start-time")
        if isinstance(lm, str):
            lm = dates.parse_timestamp(lm)
        if lm.tzinfo:
            lm = lm.astimezone(datetime.timezone.utc).replace(tzinfo=None)
        lm_str = lm.isoformat()[:19] + "Z"  # # pylint: disable=no-member
        size_str = "{} MB".format(int(meta.get("total-size-enc", b["size"])) // (1024 ** 2))
        orig_size = int(meta.get("total-size-plain", meta.get("original-file-size")) or 0)
        if orig_size:
            orig_size_str = "{} MB".format(orig_size // (1024 ** 2))
        else:
            orig_size_str = "n/a"
        print(fmt(name=b["name"], size=size_str, time=lm_str, orig_size=orig_size_str))
        if verbose:
            print("    metadata:", meta)


class Restore:
    log_tracebacks = False

    def __init__(self):
        self.config = None
        self.log = logging.getLogger("PGHoardRestore")
        self.storage = None

    def create_parser(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-D", "--debug", help="Enable debug logging", action="store_true")
        parser.add_argument("--version", action='version', help="show program version",
                            version=version.__version__)
        sub = parser.add_subparsers(help="sub-command help")

        def add_cmd(method):
            cp = sub.add_parser(method.__name__.replace("_", "-"), help=method.__doc__)
            cp.set_defaults(func=method)
            return cp

        def generic_args(require_config=True, require_site=False):
            config_path = os.environ.get("PGHOARD_CONFIG")
            cmd.add_argument("-v", "--verbose", help="verbose output", action="store_true")
            if config_path:
                cmd.add_argument("--config", help="pghoard config file", default=config_path)
            else:
                cmd.add_argument("--config", help="pghoard config file", required=require_config)

            cmd.add_argument("--site", help="pghoard site", required=require_site)

        def host_port_args():
            cmd.add_argument("--host", help="pghoard repository host", default=PGHOARD_HOST)
            cmd.add_argument("--port", help="pghoard repository port", default=PGHOARD_PORT)

        def target_args():
            cmd.add_argument("--basebackup", help="pghoard basebackup", default="latest")
            cmd.add_argument("--primary-conninfo", help="replication.conf primary_conninfo", default="")
            cmd.add_argument("--target-dir", help="pghoard restore target 'pgdata' dir", required=True)
            cmd.add_argument("--overwrite", help="overwrite existing target directory",
                             default=False, action="store_true")
            cmd.add_argument("--tablespace-dir", metavar="NAME=DIRECTORY", action="append",
                             help="map the given tablespace to an existing empty directory; "
                                  "this option can be used multiple times to map multiple tablespaces")
            cmd.add_argument("--tablespace-base-dir", required=False,
                             help="map all tablespaces in the backup against an existing empty base directory ")
            cmd.add_argument("--recovery-end-command", help="PostgreSQL recovery_end_command", metavar="COMMAND")
            cmd.add_argument("--recovery-target-action", help="PostgreSQL recovery_target_action",
                             choices=["pause", "promote", "shutdown"])
            cmd.add_argument("--recovery-target-name", help="PostgreSQL recovery_target_name", metavar="RESTOREPOINT")
            cmd.add_argument("--recovery-target-time", help="PostgreSQL recovery_target_time", metavar="ISO_TIMESTAMP")
            cmd.add_argument("--recovery-target-xid", help="PostgreSQL recovery_target_xid", metavar="XID")
            cmd.add_argument("--restore-to-master", help="Restore the database to a PG master", action="store_true")

        cmd = add_cmd(self.list_basebackups_http)
        host_port_args()
        generic_args(require_config=False, require_site=True)

        cmd = add_cmd(self.list_basebackups)
        generic_args()

        cmd = add_cmd(self.get_basebackup)
        target_args()
        generic_args()

        return parser

    def list_basebackups_http(self, arg):
        """List available basebackups from a HTTP source"""
        self.storage = HTTPRestore(arg.host, arg.port, arg.site)
        self.storage.show_basebackup_list(verbose=arg.verbose)

    def _get_object_storage(self, site, pgdata):
        storage_config = common.get_object_storage_config(self.config, site)
        storage = get_transfer(storage_config)
        return ObjectStore(storage, self.config["backup_sites"][site]["prefix"], site, pgdata)

    def list_basebackups(self, arg):
        """List basebackups from an object store"""
        self.config = config.read_json_config_file(arg.config, check_commands=False, check_pgdata=False)
        site = config.get_site_from_config(self.config, arg.site)
        self.storage = self._get_object_storage(site, pgdata=None)
        self.storage.show_basebackup_list(verbose=arg.verbose)

    def get_basebackup(self, arg):
        """Download a basebackup from an object store"""
        if not arg.tablespace_dir:
            tablespace_mapping = {}
        else:
            try:
                tablespace_mapping = dict(v.split("=", 1) for v in arg.tablespace_dir)
            except ValueError:
                raise RestoreError("Invalid tablespace mapping {!r}".format(arg.tablespace_dir))

        self.config = config.read_json_config_file(arg.config, check_commands=False, check_pgdata=False)
        site = config.get_site_from_config(self.config, arg.site)
        try:
            self.storage = self._get_object_storage(site, arg.target_dir)
            self._get_basebackup(
                pgdata=arg.target_dir,
                basebackup=arg.basebackup,
                site=site,
                debug=arg.debug,
                primary_conninfo=arg.primary_conninfo,
                recovery_end_command=arg.recovery_end_command,
                recovery_target_action=arg.recovery_target_action,
                recovery_target_name=arg.recovery_target_name,
                recovery_target_time=arg.recovery_target_time,
                recovery_target_xid=arg.recovery_target_xid,
                restore_to_master=arg.restore_to_master,
                overwrite=arg.overwrite,
                tablespace_mapping=tablespace_mapping,
                tablespace_base_dir=arg.tablespace_base_dir,
            )
        except RestoreError:  # pylint: disable=try-except-raise
            # Pass RestoreErrors thru
            raise
        except Exception as ex:
            if self.log_tracebacks:
                self.log.exception("Unexpected _get_basebackup failure")
            raise RestoreError("{}: {}".format(ex.__class__.__name__, ex))

    def _find_nearest_basebackup(self, recovery_target_time=None):
        applicable_basebackups = []

        basebackups = self.storage.list_basebackups()
        for basebackup in basebackups:
            if recovery_target_time:
                # We really need the backup end time here, but pg_basebackup based backup methods don't provide
                # it for us currently, so fall back to using start-time.
                if "end-time" in basebackup["metadata"]:
                    backup_ts = dates.parse_timestamp(basebackup["metadata"]["end-time"])
                else:
                    backup_ts = dates.parse_timestamp(basebackup["metadata"]["start-time"])
                if backup_ts >= recovery_target_time:
                    continue
            applicable_basebackups.append(basebackup)

        if not applicable_basebackups:
            raise RestoreError("No applicable basebackups found, exiting")

        # NOTE: as above, we may not have end-time so just sort by start-time, the order should be the same
        applicable_basebackups.sort(key=lambda basebackup: basebackup["metadata"]["start-time"])
        caption = "Found {} applicable basebackup{}".format(
            len(applicable_basebackups),
            "" if len(applicable_basebackups) == 1 else "s")
        print_basebackup_list(applicable_basebackups, caption=caption)

        selected = applicable_basebackups[-1]["name"]
        print("\nSelecting {!r} for restore".format(selected))
        return selected

    def _get_basebackup(self, pgdata, basebackup, site,
                        debug=False,
                        primary_conninfo=None,
                        recovery_end_command=None,
                        recovery_target_action=None,
                        recovery_target_name=None,
                        recovery_target_time=None,
                        recovery_target_xid=None,
                        restore_to_master=None,
                        overwrite=False,
                        tablespace_mapping=None,
                        tablespace_base_dir=None):
        targets = [recovery_target_name, recovery_target_time, recovery_target_xid]
        if sum(0 if flag is None else 1 for flag in targets) > 1:
            raise RestoreError("Specify at most one of recovery_target_name, "
                               "recovery_target_time or recovery_target_xid")

        # If basebackup that we want it set as latest, figure out which one it is
        if recovery_target_time:
            try:
                recovery_target_time = dates.parse_timestamp(recovery_target_time)
            except (TypeError, ValueError) as ex:
                raise RestoreError("recovery_target_time {!r}: {}".format(recovery_target_time, ex))
            basebackup = self._find_nearest_basebackup(recovery_target_time)
        elif basebackup == "latest":
            basebackup = self._find_nearest_basebackup()

        # Grab basebackup metadata to make sure it exists and to look up tablespace requirements
        metadata = self.storage.get_basebackup_metadata(basebackup)
        tablespaces = {}

        # Make sure we have a proper place to write the $PGDATA and possible tablespaces
        dirs_to_create = []
        dirs_to_recheck = []
        dirs_to_wipe = []

        if not os.path.exists(pgdata):
            dirs_to_create.append(pgdata)
        elif overwrite:
            dirs_to_create.append(pgdata)
            dirs_to_wipe.append(pgdata)
        elif os.listdir(pgdata) in ([], ["lost+found"]):
            # Allow empty directories as well as ext3/4 mount points to be used, but check that we can write to them
            dirs_to_recheck.append(["$PGDATA", pgdata])
        else:
            raise RestoreError("$PGDATA target directory {!r} exists, is not empty and --overwrite not specified, aborting."
                               .format(pgdata))

        if metadata.get("format") == "pghoard-bb-v2":
            # "Backup file" is a metadata object, fetch it to get more information
            bmeta_compressed = self.storage.get_file_bytes(basebackup)
            with rohmufile.file_reader(fileobj=io.BytesIO(bmeta_compressed), metadata=metadata,
                                       key_lookup=config.key_lookup_for_site(self.config, site)) as input_obj:
                bmeta = common.extract_pghoard_bb_v2_metadata(input_obj)
            self.log.debug("Backup metadata: %r", bmeta)

            tablespaces = bmeta["tablespaces"]
            basebackup_data_files = [
                [
                    os.path.join(self.config["backup_sites"][site]["prefix"], "basebackup_chunk", chunk["chunk_filename"]),
                    chunk["result_size"],
                ]
                for chunk in bmeta["chunks"]
            ]
            # We need the files from the main basebackup file too
            basebackup_data_files.append([(bmeta_compressed, metadata), 0])

        elif metadata.get("format") == "pghoard-bb-v1":
            # Tablespace information stored in object store metadata, look it up
            tsmetare = re.compile("^tablespace-name-([0-9]+)$")
            for kw, value in metadata.items():
                match = tsmetare.match(kw)
                if not match:
                    continue
                tsoid = match.group(1)
                tsname = value
                tspath = metadata["tablespace-path-{}".format(tsoid)]
                tablespaces[tsname] = {
                    "oid": int(tsoid),
                    "path": tspath,
                }

            basebackup_data_files = [[basebackup, -1]]

        else:
            # Object is a raw (encrypted, compressed) basebackup
            basebackup_data_files = [[basebackup, -1]]

        if tablespace_base_dir and not os.path.exists(tablespace_base_dir) and not overwrite:
            # we just care that the dir exists, but we're OK if there are other objects there
            raise RestoreError("Tablespace base directory {!r} does not exist, aborting."
                               .format(tablespace_base_dir))

        # Map tablespaces as requested and make sure the directories exist
        for tsname, tsinfo in tablespaces.items():
            tspath = tablespace_mapping.pop(tsname, tsinfo["path"])
            if tablespace_base_dir and not os.path.exists(tspath):
                tspath = os.path.join(tablespace_base_dir, str(tsinfo["oid"]))
                os.makedirs(tspath, exist_ok=True)
            if not os.path.exists(tspath):
                raise RestoreError("Tablespace {!r} target directory {!r} does not exist, aborting."
                                   .format(tsname, tspath))
            if os.listdir(tspath) not in ([], ["lost+found"]):
                # Allow empty directories as well as ext3/4 mount points to be used, but check that we can write to them
                raise RestoreError("Tablespace {!r} target directory {!r} exists but is not empty, aborting."
                                   .format(tsname, tspath))

            tsinfo["path"] = tspath
            print("Using existing empty directory {!r} for tablespace {!r}".format(tspath, tsname))
            dirs_to_recheck.append(["Tablespace {!r}".format(tsname), tspath])

        # We .pop() the elements of tablespace_mapping above - if mappings are given they must all exist or the
        # user probably made a typo with tablespace names, abort in that case.
        if tablespace_mapping:
            raise RestoreError("Tablespace mapping for {} was requested, but the tablespaces are not present in the backup"
                               .format(sorted(tablespace_mapping)))

        # First check that the existing (empty) directories are writable, then possibly wipe any directories as
        # requested by --overwrite and finally create the new dirs
        for diruse, dirname in dirs_to_recheck:
            try:
                tempfile.TemporaryFile(dir=dirname).close()
            except PermissionError:
                raise RestoreError("{} target directory {!r} is empty, but not writable, aborting."
                                   .format(diruse, dirname))

        for dirname in dirs_to_wipe:
            shutil.rmtree(dirname)
        for dirname in dirs_to_create:
            os.makedirs(dirname)
            os.chmod(dirname, 0o700)

        fetcher = BasebackupFetcher(
            app_config=self.config,
            data_files=basebackup_data_files,
            debug=debug,
            pgdata=pgdata,
            site=site,
            tablespaces=tablespaces,
        )
        fetcher.fetch_all()

        create_recovery_conf(
            dirpath=pgdata,
            site=site,
            port=self.config["http_port"],
            primary_conninfo=primary_conninfo,
            recovery_end_command=recovery_end_command,
            recovery_target_action=recovery_target_action,
            recovery_target_name=recovery_target_name,
            recovery_target_time=recovery_target_time,
            recovery_target_xid=recovery_target_xid,
            restore_to_master=restore_to_master,
        )

        print("Basebackup restoration complete.")
        print("You can start PostgreSQL by running pg_ctl -D %s start" % pgdata)
        print("On systemd based systems you can run systemctl start postgresql")
        print("On SYSV Init based systems you can run /etc/init.d/postgresql start")

    def run(self, args=None):
        parser = self.create_parser()
        args = parser.parse_args(args)
        logutil.configure_logging(level=logging.DEBUG if args.debug else logging.INFO)
        if not hasattr(args, "func"):
            parser.print_help()
            return 1
        try:
            exit_code = args.func(args)
            return exit_code
        except KeyboardInterrupt:
            print("*** interrupted by keyboard ***")
            return 1


class BasebackupFetcher():
    def __init__(self, *, app_config, debug, site, pgdata, tablespaces, data_files):
        self.log = logging.getLogger(self.__class__.__name__)
        self.completed_jobs = set()
        self.config = app_config
        self.data_files = [{"fn_or_data": item[0], "id": str(uuid.uuid4()), "size": item[1]} for item in data_files]
        self.debug = debug
        self.download_progress_per_file = {}
        self.errors = 0
        self.last_progress_ts = time.monotonic()
        self.last_total_downloaded = 0
        self.lock = RLock()
        self.manager_class = multiprocessing.Manager if self._process_count() > 1 else ThreadingManager
        self.max_stale_seconds = 120
        self.pending_jobs = set()
        self.pgdata = pgdata
        # There's no point in spawning child processes if process count is 1
        self.pool_class = multiprocessing.Pool if self._process_count() > 1 else multiprocessing.pool.ThreadPool
        self.site = site
        self.sleep_fn = time.sleep
        self.tablespaces = tablespaces
        self.total_download_size = 0

    def fetch_all(self):
        for retry in range(3):
            try:
                with self.manager_class() as manager:
                    self._setup_progress_tracking(manager)
                    with self.pool_class(processes=self._process_count()) as pool:
                        self._queue_jobs(pool)
                        self._wait_for_jobs_to_complete()
                        break
            except TimeoutError:
                self.pending_jobs.clear()
                self.last_progress_ts = time.monotonic()
                if self.errors:
                    break
                elif retry == 2:
                    self.log.error("Download stalled despite retries, aborting")
                    self.errors = 1
                    break

        if self.errors:
            raise RestoreError("Backup download/extraction failed with {} errors".format(self.errors))
        self._create_tablespace_symlinks()
        with compat.suppress(OSError):
            os.rmdir(os.path.join(self.pgdata, "pgdata"))

    def _create_tablespace_symlinks(self):
        if not self.tablespaces:
            return
        tblspc_dir = os.path.join(self.pgdata, "pg_tblspc")
        os.makedirs(tblspc_dir, exist_ok=True)
        for settings in self.tablespaces.values():
            if os.path.isdir(settings["path"]):
                link_name = os.path.join(self.pgdata, "pg_tblspc", str(settings["oid"]))
                try:
                    os.symlink(settings["path"], link_name)
                except OSError as e:
                    if e.errno != errno.EEXIST:
                        raise
        # Remove empty directories that could not be excluded when extracting tar due to
        # tar's limitations in exclude parameter behavior
        tsnames = [os.path.join("tablespaces", tsname) for tsname in self.tablespaces.keys()]
        for exclude in tsnames + ["tablespaces"]:
            with compat.suppress(OSError):
                os.rmdir(os.path.join(self.pgdata, exclude))

    def _process_count(self):
        return min(self.config["restore_process_count"], len(self.data_files))

    def _setup_progress_tracking(self, manager):
        self.total_download_size = sum(item["size"] for item in self.data_files)
        initial_progress = [[item["fn_or_data"], item["size"] if item["id"] in self.completed_jobs else 0]
                            for item in self.data_files if not isinstance(item["fn_or_data"], tuple)]
        self.download_progress_per_file = manager.dict(initial_progress)

    def current_progress(self):
        total_downloaded = sum(self.download_progress_per_file.values())
        if self.total_download_size <= 0:
            progress = 0
        else:
            progress = total_downloaded / self.total_download_size
        if total_downloaded != self.last_total_downloaded:
            self.last_total_downloaded = total_downloaded
            self.last_progress_ts = time.monotonic()
        return total_downloaded, progress

    def _print_download_progress(self, end=""):
        total_downloaded, progress = self.current_progress()
        print("\rDownload progress: {progress:.2%} ({dl_mib:.0f} / {total_mib:.0f} MiB)\r".format(
            progress=progress,
            dl_mib=total_downloaded / (1024 ** 2),
            total_mib=self.total_download_size / (1024 ** 2),
        ), end=end)
        sys.stdout.flush()

    def job_completed(self, key):
        self.last_progress_ts = time.monotonic()
        with self.lock:
            if key in self.pending_jobs:
                self.pending_jobs.remove(key)
                self.completed_jobs.add(key)

    def job_failed(self, key, exception):
        self.log.error("Got error from chunk download: %s", exception)
        self.last_progress_ts = time.monotonic()
        with self.lock:
            if key in self.pending_jobs:
                self.errors += 1
                self.pending_jobs.remove(key)
                self.completed_jobs.add(key)

    def jobs_in_progress(self):
        with self.lock:
            return len(self.completed_jobs) < len(self.data_files)

    def _queue_jobs(self, pool):
        for item in self.data_files:
            with self.lock:
                if item["id"] in self.completed_jobs or item["id"] in self.pending_jobs:
                    continue
                self.pending_jobs.add(item["id"])
            self._queue_job(pool, item["id"], item["fn_or_data"], item["size"])

    def _queue_job(self, pool, key, data_file, data_file_size):
        pool.apply_async(
            _fetch_and_process_chunk,
            [],
            {
                "app_config": self.config,
                "debug": self.debug,
                "data_file": data_file,
                "data_file_size": data_file_size,
                "download_progress_per_file": self.download_progress_per_file,
                "site": self.site,
                "pgdata": self.pgdata,
                "tablespaces": self.tablespaces,
            },
            lambda *args: self.job_completed(key),
            lambda exception: self.job_failed(key, exception),
        )

    def _wait_for_jobs_to_complete(self):
        while self.jobs_in_progress():
            self._print_download_progress()
            self.sleep_fn(1)
            stall_duration = time.monotonic() - self.last_progress_ts
            if stall_duration > self.max_stale_seconds:
                self.log.error("Download stalled for %r seconds, aborting downloaders", stall_duration)
                raise TimeoutError()

        self._print_download_progress(end="\n")


# Provides sufficient interface compatibility with multiprocessing.Manager for threaded use
class ThreadingManager:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False

    def dict(self, *args, **kwargs):
        return dict(*args, **kwargs)


def _fetch_and_process_chunk(*, app_config, debug, data_file, data_file_size,
                             download_progress_per_file, site, pgdata, tablespaces):
    logutil.configure_logging(level=logging.DEBUG if debug else logging.INFO)
    fetcher = ChunkFetcher(app_config, data_file, data_file_size,
                           download_progress_per_file, site, pgdata, tablespaces)
    fetcher.process_chunk()


class ChunkFetcher:
    def __init__(self, app_config, data_file, data_file_size,
                 download_progress_per_file, site, pgdata, tablespaces):
        self.config = app_config
        self.data_file = data_file
        self.data_file_size = data_file_size
        self.download_progress_per_file = download_progress_per_file
        self.log = logging.getLogger(self.__class__.__name__)
        self.pgdata = pgdata
        self.site = site
        self.tablespaces = tablespaces

    def _create_transfer(self):
        object_storage_config = common.get_object_storage_config(self.config, self.site)
        return get_transfer(object_storage_config)

    def _progress_callback(self, current_pos, expected_max):
        self.download_progress_per_file[self.data_file] = self.data_file_size * (current_pos / expected_max)

    def process_chunk(self):
        self.log.debug("Processing one chunk: %r", self.data_file)
        if isinstance(self.data_file, tuple):
            data, metadata = self.data_file
            src = io.BytesIO(data)
            self._fetch_and_extract_one_backup(metadata, len(data), lambda sink: shutil.copyfileobj(src, sink))
        else:
            transfer = self._create_transfer()
            metadata = transfer.get_metadata_for_key(self.data_file)

            def fetch_fn(sink):
                transfer.get_contents_to_fileobj(self.data_file, sink, progress_callback=self._progress_callback)
            self._fetch_and_extract_one_backup(metadata, self.data_file_size, fetch_fn)

    def _build_tar_args(self, metadata):
        base_args = [self.config["tar_executable"], "-xf", "-", "-C", self.pgdata]
        file_format = metadata.get("format")
        if not file_format:
            return base_args
        elif file_format in {"pghoard-bb-v1", "pghoard-bb-v2"}:
            extra_args = [
                "--exclude", ".pghoard_tar_metadata.json",
                "--transform", "s,^pgdata/,,"
            ]
            if self.tablespaces:
                extra_args.append("--absolute-names")
            for tsname, settings in self.tablespaces.items():
                extra_args.append("--transform")
                extra_args.append(r"s,^tablespaces/{}/\(.*\)$,{}/\1,".format(
                    tsname.replace("\\", "\\\\").replace(",", "\\,"), settings["path"].replace(",", "\\,")))
            return base_args + extra_args
        else:
            raise RestoreError("Unrecognized basebackup format {!r}".format(file_format))

    def _fetch_and_extract_one_backup(self, metadata, file_size, fetch_fn):
        with subprocess.Popen(self._build_tar_args(metadata),
                              bufsize=0,
                              stdin=subprocess.PIPE,
                              stdout=subprocess.DEVNULL,
                              stderr=subprocess.PIPE) as tar:
            common.increase_pipe_capacity(tar.stdin, tar.stderr)
            sink = rohmufile.create_sink_pipeline(file_size=file_size,
                                                  key_lookup=config.key_lookup_for_site(self.config, self.site),
                                                  metadata=metadata,
                                                  output=tar.stdin)
            # It would be prudent to read stderr while we're writing to stdin to avoid deadlocking
            # if stderr fills up but in practice tar should write very little to stderr and that
            # should not become a problem.
            try:
                fetch_fn(sink)
            except BrokenPipeError:
                self.log.error("External tar returned an error: %r", tar.stderr.read())
                raise

            tar.stdin.close()
            tar.stdin = None
            output = tar.stderr.read()
            exit_code = tar.wait()
            file_name = "<mem_bytes>" if isinstance(self.data_file, tuple) else self.data_file
            if exit_code != 0:
                raise Exception("tar exited with code {!r} for file {!r}, output: {!r}".format(
                    exit_code, file_name, output))
            self.log.info("Processing of %r completed successfully", file_name)


class ObjectStore:
    def __init__(self, storage, prefix, site, pgdata):
        self.storage = storage
        self.prefix = prefix
        self.site = site
        self.pgdata = pgdata
        self.log = logging.getLogger(self.__class__.__name__)

    def list_basebackups(self):
        return self.storage.list_path(os.path.join(self.prefix, "basebackup"))

    def show_basebackup_list(self, verbose=True):
        result = self.list_basebackups()
        caption = "Available %r basebackups:" % self.site
        print_basebackup_list(result, caption=caption, verbose=verbose)

    def get_basebackup_metadata(self, basebackup):
        return self.storage.get_metadata_for_key(basebackup)

    def get_basebackup_file_to_fileobj(self, basebackup, fileobj, *, progress_callback=None):
        return self.storage.get_contents_to_fileobj(basebackup, fileobj, progress_callback=progress_callback)

    def get_file_bytes(self, name):
        return self.storage.get_contents_to_string(name)[0]


class HTTPRestore(ObjectStore):
    def __init__(self, host, port, site, pgdata=None):
        super().__init__(storage=None, prefix=None, site=site, pgdata=pgdata)
        self.host = host
        self.port = port
        self.session = Session()

    def _url(self, path):
        return "http://{host}:{port}/{site}/{path}".format(
            host=self.host,
            port=self.port,
            site=self.site,
            path=path)

    def list_basebackups(self):
        response = self.session.get(self._url("basebackup"))
        return response.json()["basebackups"]


def main():
    try:
        restore = Restore()
        return restore.run()
    except (InvalidConfigurationError, RestoreError) as ex:
        print("FATAL: {}: {}".format(ex.__class__.__name__, ex))
        return 1


if __name__ == "__main__":
    sys.exit(main() or 0)
