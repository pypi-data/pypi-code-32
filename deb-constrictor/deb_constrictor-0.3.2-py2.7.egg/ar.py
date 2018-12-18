import os
import os.path

from .helpers import READ_BUFFER_SIZE

AR_HEADER_TEXT = "!<arch>\n"


class ARWriter(object):
    def __init__(self, archive_path):
        self.archive_path = archive_path
        self.archive_ready = False
        self.fp = None

    def write_header(self):
        if not self.archive_ready:
            raise RuntimeError("Archive not yet created.")
        self.fp.write(AR_HEADER_TEXT.encode())

    def create_archive(self):
        if self.archive_ready:
            raise RuntimeError("Archive has already been created.")
        self.fp = open(self.archive_path, 'wb')
        self.archive_ready = True
        self.write_header()

    def _write_file_header(self, file_name, mod_timestamp, uid, gid, mode, file_size):
        if not self.archive_ready:
            self.create_archive()

        mode_string = '{:04o}'.format(mode)

        file_header = '{: <16}{: <12}{: <6}{: <6}{: <8}{: <10}`\n'.format(file_name, mod_timestamp, uid, gid,
                                                                          mode_string, file_size)

        self.fp.write(file_header.encode())

    def _write_file_content(self, source_path):
        source_file = open(source_path, 'rb')

        while True:
            data = source_file.read(READ_BUFFER_SIZE)
            if not data:
                break
            self.fp.write(data)
        source_file.close()

    def _write_file_alignment(self):
        """ar files are aligned to 2n bytes, this will write an extra byte to make sure they line up."""
        self.fp.write("\n".encode())

    def _write_text(self, text):
        self.fp.write(text.encode())

    def archive_file(self, file_path, mod_time_override=None, uid_override=None, gid_override=None, mode_override=None):
        if not self.archive_ready:
            self.create_archive()
        file_to_archive_name = os.path.basename(file_path)
        file_stat = os.stat(file_path)

        mod_time = mod_time_override or file_stat.st_mtime
        uid = uid_override or file_stat.st_uid
        gid = gid_override or file_stat.st_gid
        mode = mode_override or file_stat.st_mode
        file_size = file_stat.st_size
        self._write_file_header(file_to_archive_name, mod_time, uid, gid, mode, file_size)
        self._write_file_content(file_path)

        if file_size % 2 != 0:
            self._write_file_alignment()

    def archive_text(self, file_name, text, mod_time, uid, gid, mode):
        if not self.archive_ready:
            self.create_archive()
        file_size = len(text)
        self._write_file_header(file_name, mod_time, uid, gid, mode, file_size)
        self._write_text(text)

        if file_size % 2 != 0:
            self._write_file_alignment()

    def close(self):
        self.fp.close()
        self.archive_ready = False
