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


from setuptools import setup, find_packages

def load_requirements(f):
  retval = [str(k.strip()) for k in open(f, 'rt')]
  return [k for k in retval if k and k[0] not in ('#', '-')]

# The only thing we do in this file is to call the setup() function with all
# parameters that define our package.
setup(

    name='beat.cmdline',
    version=open("version.txt").read().rstrip(),
    description='Command-line client for the BEAT platform',
    url='https://gitlab.idiap.ch/beat/beat.cmdline',
    license='AGPLv3',
    author='Idiap Research Institute',
    author_email='beat.support@idiap.ch',
    long_description=open('README.rst').read(),

    # This line is required for any distutils based packaging.
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=load_requirements('requirements.txt'),

    entry_points={
        'console_scripts': [
            'beat = beat.cmdline.scripts.main_cli:main',
        ],
        'beat.cli': [
            'config = beat.cmdline.config:config',
            'status = beat.cmdline.status:status',
            'cache = beat.cmdline.cache:cache',
            'databases = beat.cmdline.databases:databases',
            'dataformats = beat.cmdline.dataformats:dataformats',
            'libraries = beat.cmdline.libraries:libraries',
            'algorithms = beat.cmdline.algorithms:algorithms',
            'plotters = beat.cmdline.plotters:plotters',
            'plotterparameters = beat.cmdline.plotterparameters:plotterparameters',
            'toolchains = beat.cmdline.toolchains:toolchains',
            'experiments = beat.cmdline.experiments:experiments',
        ],
        'beat.config.cli': [
            'show = beat.cmdline.config:show',
            'get = beat.cmdline.config:get',
            'set = beat.cmdline.config:set',
        ],
        'beat.cache.cli': [
            'clear = beat.cmdline.cache:clear',
            'info = beat.cmdline.cache:info',
            'view = beat.cmdline.cache:view',
        ],
        'beat.databases.cli': [
            'list = beat.cmdline.databases:list',
            'path = beat.cmdline.databases:path',
            'edit = beat.cmdline.databases:edit',
            'check = beat.cmdline.databases:check',
            'pull = beat.cmdline.databases:pull',
            'push = beat.cmdline.databases:push',
            'diff = beat.cmdline.databases:diff',
            'status = beat.cmdline.databases:status',
            'version = beat.cmdline.databases:version',
            'index = beat.cmdline.databases:index',
            'view = beat.cmdline.databases:view',
        ],
        'beat.dataformats.cli': [
            'list = beat.cmdline.dataformats:list',
            'path = beat.cmdline.dataformats:path',
            'edit = beat.cmdline.dataformats:edit',
            'check = beat.cmdline.dataformats:check',
            'pull = beat.cmdline.dataformats:pull',
            'push = beat.cmdline.dataformats:push',
            'diff = beat.cmdline.dataformats:diff',
            'status = beat.cmdline.dataformats:status',
            'create = beat.cmdline.dataformats:create',
            'version = beat.cmdline.dataformats:version',
            'fork = beat.cmdline.dataformats:fork',
            'rm = beat.cmdline.dataformats:rm',
        ],
        'beat.libraries.cli': [
            'list = beat.cmdline.libraries:list',
            'path = beat.cmdline.libraries:path',
            'edit = beat.cmdline.libraries:edit',
            'check = beat.cmdline.libraries:check',
            'pull = beat.cmdline.libraries:pull',
            'push = beat.cmdline.libraries:push',
            'diff = beat.cmdline.libraries:diff',
            'status = beat.cmdline.libraries:status',
            'create = beat.cmdline.libraries:create',
            'version = beat.cmdline.libraries:version',
            'fork = beat.cmdline.libraries:fork',
            'rm = beat.cmdline.libraries:rm',
        ],
        'beat.algorithms.cli': [
            'list = beat.cmdline.algorithms:list',
            'path = beat.cmdline.algorithms:path',
            'edit = beat.cmdline.algorithms:edit',
            'check = beat.cmdline.algorithms:check',
            'pull = beat.cmdline.algorithms:pull',
            'push = beat.cmdline.algorithms:push',
            'diff = beat.cmdline.algorithms:diff',
            'status = beat.cmdline.algorithms:status',
            'create = beat.cmdline.algorithms:create',
            'version = beat.cmdline.algorithms:version',
            'fork = beat.cmdline.algorithms:fork',
            'rm = beat.cmdline.algorithms:rm',
            'execute = beat.cmdline.algorithms:execute',
        ],
        'beat.plotters.cli': [
            'list = beat.cmdline.plotters:list',
            'path = beat.cmdline.plotters:path',
            'edit = beat.cmdline.plotters:edit',
            'check = beat.cmdline.plotters:check',
            'pull = beat.cmdline.plotters:pull',
            'plot = beat.cmdline.plotters:plot',
            'create = beat.cmdline.plotters:create',
            'version = beat.cmdline.plotters:version',
            'fork = beat.cmdline.plotters:fork',
            'rm = beat.cmdline.plotters:rm',
        ],
        'beat.plotterparameters.cli': [
            'list = beat.cmdline.plotterparameters:list',
            'path = beat.cmdline.plotterparameters:path',
            'edit = beat.cmdline.plotterparameters:edit',
            'check = beat.cmdline.plotterparameters:check',
            'pull = beat.cmdline.plotterparameters:pull',
            'create = beat.cmdline.plotterparameters:create',
            'version = beat.cmdline.plotterparameters:version',
            'fork = beat.cmdline.plotterparameters:fork',
            'rm = beat.cmdline.plotterparameters:rm',
        ],
        'beat.toolchains.cli': [
            'list = beat.cmdline.toolchains:list',
            'path = beat.cmdline.toolchains:path',
            'edit = beat.cmdline.toolchains:edit',
            'check = beat.cmdline.toolchains:check',
            'pull = beat.cmdline.toolchains:pull',
            'push = beat.cmdline.toolchains:push',
            'diff = beat.cmdline.toolchains:diff',
            'status = beat.cmdline.toolchains:status',
            'create = beat.cmdline.toolchains:create',
            'version = beat.cmdline.toolchains:version',
            'fork = beat.cmdline.toolchains:fork',
            'rm = beat.cmdline.toolchains:rm',
            'draw = beat.cmdline.toolchains:draw',
        ],
        'beat.experiments.cli': [
            'run = beat.cmdline.experiments:run',
            'caches = beat.cmdline.experiments:caches',
            'list = beat.cmdline.experiments:list',
            'path = beat.cmdline.experiments:path',
            'edit = beat.cmdline.experiments:edit',
            'check = beat.cmdline.experiments:check',
            'pull = beat.cmdline.experiments:pull',
            'push = beat.cmdline.experiments:push',
            'diff = beat.cmdline.experiments:diff',
            'status = beat.cmdline.experiments:status',
            'fork = beat.cmdline.experiments:fork',
            'rm = beat.cmdline.experiments:rm',
            'draw = beat.cmdline.experiments:draw',
            'plot = beat.cmdline.experiments:plot',
        ],
    },

    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
