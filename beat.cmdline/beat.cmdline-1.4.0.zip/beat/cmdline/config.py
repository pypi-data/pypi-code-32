#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

###############################################################################
#                                                                             #
# Copyright (c) 2016 Idiap Research Institute, http://www.idiap.ch/           #
# Contact: beat.support@idiap.ch                                              #
#                                                                             #
# This file is part of the beat.cmdline module of the BEAT platform.          #
#                                                                             #
# Commercial License Usage                                                    #
# Licensees holding valid commercial BEAT licenses may use this file in       #
# accordance with the terms contained in a written agreement between you      #
# and Idiap. For further information contact tto@idiap.ch                     #
#                                                                             #
# Alternatively, this file may be used under the terms of the GNU Affero      #
# Public License version 3 as published by the Free Software and appearing    #
# in the file LICENSE.AGPL included in the packaging of this file.            #
# The BEAT platform is distributed in the hope that it will be useful, but    #
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY  #
# or FITNESS FOR A PARTICULAR PURPOSE.                                        #
#                                                                             #
# You should have received a copy of the GNU Affero Public License along      #
# with the BEAT platform. If not, see http://www.gnu.org/licenses/.           #
#                                                                             #
###############################################################################
"""Configuration manipulation and display"""


import os
import sys
import copy
import logging
import getpass
import click
import simplejson

from .decorators import verbosity_option
from .click_helper import AliasedGroup


logger = logging.getLogger(__name__)


DEFAULTS = {
    'platform': 'https://www.beat-eu.org/platform/',
    'user': getpass.getuser(),
    'token': None,
    'prefix': os.path.realpath(os.path.join(os.curdir, 'prefix')),
    'cache': 'cache',
    'editor': None,
    }
"""Default values for the command-line utility"""


DOC = {
    'platform': 'Web address of the BEAT platform',
    'user': 'User name for operations that create, delete or edit objects',
    'token': 'Secret key of the user on the BEAT platform',
    'prefix': 'Directory containing BEAT objects',
    'cache': 'Directory to use for data caching (relative to prefix)',
    'editor': 'Editor to be used to edit local files',
    }
"""Documentation for configuration parameters"""


class Configuration(object):
    '''Keeps track of configuration elements'''

    def __init__(self, args):

        self.files = [
            os.path.expanduser('~/.beatrc'),
            os.path.realpath('./.beatrc'),
        ]

        self.__data = copy.deepcopy(DEFAULTS)
        for k in self.files:
            if os.path.exists(k):
                with open(k, 'rt') as f: tmp = simplejson.load(f)
                self.__data.update(tmp)
                logger.info("Loaded configuration file `%s'", k)

        for key in DEFAULTS:
            self.__data[key] = args.get('--%s' % key) or self.__data[key]


    @property
    def path(self):
        '''The directory for the prefix'''

        return self.__data['prefix']


    @property
    def cache(self):
        '''The directory for the cache'''

        if os.path.isabs(self.__data['cache']):
            return self.__data['cache']
        return os.path.join(self.__data['prefix'], self.__data['cache'])


    @property
    def database_paths(self):
        '''A dict of paths for databases'''

        return dict(
            (k, self.__data[k]) for k in self.__data if self.is_database_key(k)
        )


    def set(self, key, value, local=False):
        '''Sets or resets a field in the configuration'''

        if not self._is_valid_key(key):
            logger.error("Don't know about parameter `%s'", key)
            sys.exit(1)

        if value is not None:
            self.__data[key] = value
        elif key in DEFAULTS:
            self.__data[key] = DEFAULTS[key]

        self.save(local)


    def save(self, local=False):
        '''Saves contents to configuration file

        Parameters:

            local: bool, Optional
                if set to ``True``, then save
                configuration values to local configuration file (typically
                ``.beatrc``)
        '''

        path = self.files[0]
        if local:
            path = self.files[1]

        flags = os.O_WRONLY | os.O_CREAT | os.O_TRUNC
        with os.fdopen(os.open(path, flags, 0o600), 'wt') as f:
            f.write(simplejson.dumps(
                self.__data, sort_keys=True, indent=4,
                separators=(',', ': ')
            ))


    def _is_valid_key(self, key):
        return key in DEFAULTS or self.is_database_key(key)


    def is_database_key(self, key):
        return key.startswith('database/')


    def __str__(self):
        return simplejson.dumps(
            self.__data, sort_keys=True,
            indent=4, separators=(',', ': ')
        )


    def as_dict(self):
        return copy.copy(self.__data)


    def __getattr__(self, key):
        return self.__data[key]


@click.group(cls=AliasedGroup)
@verbosity_option()
@click.pass_context
def config(ctx):
    """The manager for beat cmdline configuration."""
    pass

@config.command()
@click.pass_context
def show(ctx):
    """Shows the configuration.

    Lists the configuration after resolving defaults and saved variables
    """
    click.echo(ctx.meta['config'])


@config.command()
@click.argument('key')
@click.pass_context
def get(ctx, key):
    """Prints out the contents of a single field.

    To query for a specific parameter:

    $ %(prog)s config get token
    1234567890abcdef1234567890abcde


    \b
    Arguments
    ---------
    key : str
        The key to return its value from the configuration.

    \b
    Fails
    -----
    * If the key is not found.
    """
    value = getattr(ctx.meta['config'], key)
    if value is None:
        # Exit the command line with ClickException in case of errors.
        raise click.ClickException(
            "The requested key `{}' does not exist".format(key))
    click.echo(value)


@config.command()
@click.argument('args', nargs=-1)
@click.option('--local/--not-local', default=False, help='Save values on the '
              'local configuration file (.beatrc) instead of using the global '
              'file (~/.beatrc)')
@click.pass_context
def set(ctx, args, local):
    """Sets the value for a key.

    Sets a specific known field to a value
    To save a different user name token to a file and save results locally - i.e.
    doesn't override the global configuration file (notice you can pass multiple
    parameters at once using key-value pairs):

    \b
    Arguments
    ---------
    key : str
        The key to set the value for.
    value : str
        The value of the key.
    local : bool
        Save locally or not

    \b
    Fails
    -----
    * If something goes wrong.
    """

    if len(args) % 2 != 0:
        raise click.BadParameter('You must provide pair(s) of key/value')

    try:
        for idx in range(0, len(args), 2):
            ctx.meta['config'].set(args[idx], args[idx + 1], local)
    except Exception:
        raise click.ClickException("Failed to change the configuration.")
