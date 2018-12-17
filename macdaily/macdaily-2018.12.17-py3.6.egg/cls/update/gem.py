# -*- coding: utf-8 -*-

import re
import sys
import traceback

from macdaily.cmd.update import UpdateCommand
from macdaily.core.gem import GemCommand
from macdaily.util.misc import (date, make_stderr, print_info, print_scpt,
                                print_text, sudo)

if sys.version_info[:2] == (3, 4):
    import subprocess32 as subprocess
else:
    import subprocess


class GemUpdate(GemCommand, UpdateCommand):

    def _parse_args(self, namespace):
        self._brew = namespace.get('brew', False)
        self._system = namespace.get('system', False)

        self._all = namespace.get('all', False)
        self._quiet = namespace.get('quiet', False)
        self._verbose = namespace.get('verbose', False)
        self._yes = namespace.get('yes', False)

        self._logging_opts = namespace.get('logging', str()).split()
        self._update_opts = namespace.get('update', str()).split()

    def _check_list(self, path):
        text = 'Updating RubyGems database'
        print_info(text, self._file, redirect=self._qflag)

        argv = [path, 'update', '--system']
        if self._quiet:
            argv.append('--quiet')
        if self._verbose:
            argv.append('--verbose')
        args = ' '.join(argv)
        print_scpt(args, self._file, redirect=self._qflag)
        sudo(argv, self._file, self._password,
             redirect=self._qflag, verbose=self._vflag)

        text = f'Checking outdated {self.desc[1]}'
        print_info(text, self._file, redirect=self._vflag)

        argv = [path, 'outdated']
        if self._quiet:
            argv.append('--quiet')
        if self._verbose:
            argv.append('--verbose')
        argv.extend(self._logging_opts)

        args = ' '.join(argv)
        print_scpt(args, self._file, redirect=self._vflag)
        with open(self._file, 'a') as file:
            file.write(f'Script started on {date()}\n')
            file.write(f'command: {args!r}\n')

        try:
            proc = subprocess.check_output(argv, stderr=make_stderr(self._vflag))
        except subprocess.SubprocessError:
            print_text(traceback.format_exc(), self._file, redirect=self._vflag)
            self._var__temp_pkgs = set()
        else:
            context = proc.decode()
            print_text(context, self._file, redirect=self._vflag)

            _temp_pkgs = list()
            for item in filter(lambda s: re.match(r'\w* \(.*\)', s), context.strip().splitlines()):
                _temp_pkgs.append(item.split()[0])
            self._var__temp_pkgs = set(_temp_pkgs)
            # self._var__temp_pkgs = set(map(lambda s: s.split()[0], filter(None, context.strip().splitlines())))
        finally:
            with open(self._file, 'a') as file:
                file.write(f'Script done on {date()}\n')

    def _proc_update(self, path):
        text = f'Upgrading outdated {self.desc[1]}'
        print_info(text, self._file, redirect=self._qflag)

        argv = [path, 'update']
        if self._quiet:
            argv.append('--quiet')
        if self._verbose:
            argv.append('--verbose')
        argv.extend(self._update_opts)

        argc = ' '.join(argv)
        for package in self._var__temp_pkgs:
            args = f'{argc} {package}'
            print_scpt(args, self._file, redirect=self._qflag)
            yes = 'y' if self._yes else None
            if sudo(argv, self._file, self._password, timeout=self._timeout,
                    redirect=self._qflag, verbose=self._vflag, yes=yes):
                self._fail.append(package)
            else:
                self._pkgs.append(package)
        del self._var__temp_pkgs
