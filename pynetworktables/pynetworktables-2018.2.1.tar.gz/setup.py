
from __future__ import print_function

from os.path import dirname, exists, join
import sys, subprocess

import setuptools
from setuptools import find_packages, setup

try:
    # Does setuptools support Python version environment markers in extras_require?
    # Not using environment markers in install_requires for compatibility.
    is_modern_setuptools = int(setuptools.__version__.split('.', 1)[0]) >= 18
except Exception:
    is_modern_setuptools = False

setup_dir = dirname(__file__)
git_dir = join(setup_dir, '.git')
version_file = join(setup_dir, 'ntcore', 'version.py')

# Automatically generate a version.py based on the git version
if exists(git_dir):
    p = subprocess.Popen(["git", "describe", "--tags", "--long", "--dirty=-dirty"],
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    out, err = p.communicate()
    # Make sure the git version has at least one tag
    if err:
        print("Error: You need to create a tag for this repo to use the builder")
        sys.exit(1)

    # Convert git version to PEP440 compliant version
    # - Older versions of pip choke on local identifiers, so we can't include the git commit
    v, commits, local = out.decode('utf-8').rstrip().split('-', 2)
    if commits != '0' or '-dirty' in local:
        v = '%s.post0.dev%s' % (v, commits)

    # Create the version.py file
    with open(version_file, 'w') as fp:
        fp.write("# Autogenerated by setup.py\n__version__ = '{0}'".format(v))

with open(version_file, 'r') as fp:
    exec(fp.read(), globals())

with open(join(setup_dir, 'README.rst'), 'r') as readme_file:
    long_description = readme_file.read()

install_requires = []
extras = {}
if is_modern_setuptools:
    extras[':python_version<"3"'] = ['monotonic']
elif sys.version_info[0] <= 2:
    install_requires.append('monotonic')

setup(
    name='pynetworktables',
    version=__version__,
    description='A pure Python implementation of NetworkTables, used for robot communications in the FIRST Robotics Competition.',
    long_description=long_description,
    author='Dustin Spicuzza, Peter Johnson',
    author_email='robotpy@googlegroups.com',
    url='https://github.com/robotpy/pynetworktables',
    keywords='frc first robotics wpilib networktables',
    packages=find_packages(exclude='tests'),
    install_requires=install_requires,
    extras_require=extras,
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*',
    license="BSD-3-Clause",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Scientific/Engineering",
    ],
    )
