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


# Basic tests for the command line beat program: toolchains

import os
import nose.tools
import click
from click.testing import CliRunner
from . import platform, disconnected, prefix, tmp_prefix, user, token
from ..common import Selector
from beat.cmdline.scripts import main_cli
from beat.core.test.utils import slow, cleanup, skipif
from beat.core.toolchain import Storage, Toolchain


def call(*args, **kwargs):
  '''A central mechanism to call the main routine with the right parameters'''

  use_prefix = kwargs.get('prefix', prefix)
  use_platform = kwargs.get('platform', platform)

  runner = CliRunner()
  with runner.isolated_filesystem():
    result = runner.invoke(
        main_cli.main,
        ['--test-mode', '--prefix', use_prefix, '--token', token,
        '--user', user, '--platform', use_platform, 'toolchains'] +
        list(args)
    )
  if result.exit_code != 0:
      click.echo(result.output)
  return result.exit_code

@slow
@nose.tools.with_setup(teardown=cleanup)
@skipif(disconnected, "missing test platform (%s)" % platform)
def test_remote_list():
  nose.tools.eq_(call('list', '--remote'), 0)


@slow
@nose.tools.with_setup(teardown=cleanup)
@skipif(disconnected, "missing test platform (%s)" % platform)
def test_pull_one(obj=None):
  obj = obj or 'user/single/1'
  nose.tools.eq_(call('pull', obj, prefix=tmp_prefix), 0)
  s = Storage(tmp_prefix, obj)
  assert s.exists()


@slow
@nose.tools.with_setup(teardown=cleanup)
@skipif(disconnected, "missing test platform (%s)" % platform)
def test_pull_all():
  nose.tools.eq_(call('pull', prefix=tmp_prefix), 0)


@slow
@nose.tools.with_setup(teardown=cleanup)
@skipif(disconnected, "missing test platform (%s)" % platform)
def test_diff():
  obj = 'user/single/1'
  nose.tools.eq_(call('pull', obj, prefix=tmp_prefix), 0)

  # quickly modify the user toolchain:
  f = Toolchain(tmp_prefix, obj)
  f.data['representation']['blocks']['echo']['height'] = 2
  f.write()

  nose.tools.eq_(call('diff', obj, prefix=tmp_prefix), 0)


@slow
@nose.tools.with_setup(teardown=cleanup)
@skipif(disconnected, "missing test platform (%s)" % platform)
def test_status():
  test_diff()
  test_pull_one()
  nose.tools.eq_(call('status', prefix=tmp_prefix), 0)


def test_check_valid():
  obj = 'user/single/1'
  nose.tools.eq_(call('check', obj), 0)


def test_check_invalid():
  obj = 'user/does_not_exist/1'
  nose.tools.eq_(call('check', obj), 1)


@nose.tools.with_setup(teardown=cleanup)
def test_create(obj=None):
  obj = obj or 'user/toolchain/1'
  nose.tools.eq_(call('create', obj, prefix=tmp_prefix), 0)
  s = Storage(tmp_prefix, obj)
  assert s.exists()
  return s


@nose.tools.with_setup(teardown=cleanup)
def test_new_version():
  obj = 'user/toolchain/1'
  test_create(obj)
  obj2 = 'user/toolchain/2'
  nose.tools.eq_(call('version', obj, prefix=tmp_prefix), 0)
  s = Storage(tmp_prefix, obj2)
  assert s.exists()

  # check version status
  with Selector(tmp_prefix) as selector:
    assert selector.version_of('toolchain', obj2) == obj


@nose.tools.with_setup(teardown=cleanup)
def test_fork():
  obj = 'user/toolchain/1'
  test_create(obj)
  obj2 = 'user/different/1'
  nose.tools.eq_(call('fork', obj, obj2, prefix=tmp_prefix), 0)
  s = Storage(tmp_prefix, obj2)
  assert s.exists()

  # check fork status
  with Selector(tmp_prefix) as selector:
    assert selector.forked_from('toolchain', obj2) == obj


@nose.tools.with_setup(teardown=cleanup)
def test_delete_local():
  obj = 'user/toolchain/1'
  storage = test_create(obj)
  nose.tools.eq_(call('rm', obj, prefix=tmp_prefix), 0)
  assert not storage.exists()


@nose.tools.with_setup(teardown=cleanup)
@skipif(disconnected, "missing test platform (%s)" % platform)
def test_push_and_delete():
  obj = 'user/newobject/1'
  test_create(obj)

  # now push the new object and then delete it remotely
  nose.tools.eq_(call('push', obj, prefix=tmp_prefix), 0)
  nose.tools.eq_(call('rm', '--remote', obj, prefix=tmp_prefix), 0)


@nose.tools.with_setup(teardown=cleanup)
@skipif(disconnected, "missing test platform (%s)" % platform)
def test_draw():
  obj = 'user/double_triangle/1'
  test_pull_one(obj)

  # now push the new object and then delete it remotely
  nose.tools.eq_(call('draw', '--path=%s' % tmp_prefix, prefix=tmp_prefix), 0)

  assert os.path.exists(os.path.join(tmp_prefix, 'toolchains', obj + '.dot'))
  assert os.path.exists(os.path.join(tmp_prefix, 'toolchains', obj + '.png'))
