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


# Basic tests for the command line beat program: status

import os

import nose.tools
import simplejson
import click
from click.testing import CliRunner

from . import platform, disconnected, tmp_prefix, user
from ..common import Selector
from beat.core.test.utils import slow, cleanup, skipif
from beat.cmdline.scripts import main_cli
from beat.core.algorithm import Storage


def call(*args, **kwargs):
  '''A central mechanism to call the main routine with the right parameters'''

  use_prefix = kwargs.get('prefix', tmp_prefix)
  use_platform = kwargs.get('platform', platform)

  runner = CliRunner()
  with runner.isolated_filesystem():
    result = runner.invoke(
        main_cli.main,
        ['--test-mode', '--prefix', use_prefix, '--platform', use_platform,
        '--user', user] +
        list(args)
    )
  if result.exit_code != 0:
      click.echo(result.output)
  return result.exit_code

@skipif(disconnected, "missing test platform (%s)" % platform)
def test_status():
  nose.tools.eq_(call('status'), 0)
