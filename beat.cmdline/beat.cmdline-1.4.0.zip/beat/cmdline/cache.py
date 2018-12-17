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

import os
import click
import fnmatch
import logging

import simplejson

from beat.core.data import CachedDataSource, load_data_index
from beat.core.utils import NumpyJSONEncoder

from . import common
from .decorators import raise_on_error
from .click_helper import AliasedGroup


logger = logging.getLogger(__name__)


def get_paths(config):

    func = lambda z: z.split('.', 1)[0]

    retval = []

    for dirname, _, files in os.walk(config.cache):
        files = fnmatch.filter(files, '*.data') #avoid index-only files
        if not files:
            continue
        d = dirname.replace(config.cache, '').strip(os.sep)
        retval += list(set([os.path.join(d, func(k)) for k in files]))

    return retval


@click.group(cls=AliasedGroup)
@click.pass_context
@click.option('--start', type=click.INT, help='If set, allows the user to '
              'print only a few bits of the file')
@click.option('--end', type=click.INT, help='If set, allows the user to '
              'print only a few bits of the file')
def cache(ctx, start, end):
    """Configuration manipulation and display"""
    pass


@cache.command()
@click.pass_context
def clear(ctx):
    '''Deletes all available cache

    To clear all available cache:

        $ %(prog)s cache clear
    '''
    import shutil
    if os.path.isdir(ctx.meta['config'].cache):
        for k in os.listdir(ctx.meta['config'].cache):
            p = os.path.join(ctx.meta['config'].cache, k)
            shutil.rmtree(p)


@cache.command()
@click.argument('paths', nargs=-1, type=click.Path(exists=True))
@click.pass_context
@click.option('--sizes', help='If set, also print the size in bytes for '
              'objects in a file. This triggers the full file readout',
              is_flag=True)
def info(ctx, paths, sizes):
    '''Displays information about a particular cache file

    To collect information about a particular cache file:

    $ %(prog)s cache info 7f/d8/8d/a11178ac27075feaba8131fe878d6e3...
    '''
    config = ctx.meta['config']
    index_start = int(ctx.meta['start']) if 'start' in ctx.meta else None
    index_end = int(ctx.meta['end']) if 'end' in ctx.meta else None
    if not paths:
        paths = get_paths(config)

    for path in paths:

        logger.info('path: %s', path)
        fullpath = os.path.join(config.cache, path + '.data')

        f = CachedDataSource()
        status = f.setup(fullpath, config.path, index_start, index_end)
        if not status:
            logger.error("cannot setup data source with `%s' and prefix `%s'",
                         fullpath, config.path)
            return 1

        logger.info('  dataformat: %s', f.dataformat.name)

        if sizes:
            counter = 0
            logger.info('  index:')

            for data, start, end in f:
                size = len(data.pack())
                counter += size
                if start == end:
                    logger.info('  [%d] - %d bytes', start, size)
                else:
                    logger.info('  [%d:%d] - %d bytes', start, end, size)
                logger.info('  total (stripped-down) size: %d bytes', counter)

        else:
            index = load_data_index(config.cache, path + '.data')
            logger.info('  objects   : %d', len(index)-1)


@cache.command()
@click.argument('paths', nargs=-1)
@click.pass_context
@raise_on_error
def view(ctx, paths):
    '''Displays information about a particular cache file

    To view a particular cache file:

    $ %(prog)s cache view 7f/d8/8d/a11178ac27075feaba8131fe878d6e3...
    '''
    config = ctx.meta['config']
    index_start = int(ctx.meta['start']) if 'start' in ctx.meta else None
    index_end = int(ctx.meta['end']) if 'end' in ctx.meta else None
    if not paths:
        paths = get_paths(config)

    for path in paths:
        logger.info('path: %s', path)
        fullpath = os.path.join(config.cache, path + '.data')

        f = CachedDataSource()
        status = f.setup(fullpath, config.path, index_start, index_end)
        if not status:
            logger.error("cannot setup data source with `%s' and prefix `%s'",
                         fullpath, config.path)
            return 1

        logger.info('  dataformat: %s', f.dataformat.name)

        for data, start, end in f:
            logger.extra(80 * '-')

            if start == end:
                header = '[%d]: ' % start
            else:
                header = '[%d:%d]: ' % (start, end)

            json_data = data.as_dict()
            for name, value in json_data.items():
                json_data[name] = common.stringify(value)
            json_data = simplejson.dumps(
                json_data, indent=2,
                cls=NumpyJSONEncoder).\
                    replace('"BEAT_LIST_DELIMITER[', '[')\
                    .replace(']BEAT_LIST_DELIMITER"', ']')\
                    .replace('"...",', '...')\
                    .replace('"BEAT_LIST_SIZE(', '(')\
                    .replace(')BEAT_LIST_SIZE"', ')')
            logger.info(header + json_data)
