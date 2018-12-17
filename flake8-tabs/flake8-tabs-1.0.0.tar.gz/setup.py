#!/usr/bin/env python
# setup.py generated by flit for tools that don't yet use PEP 517

from distutils.core import setup

extras_require = \
{'doc': ['sphinx'], 'test': ['flake8 > 3.0.0', 'pytest', 'pytest-cov']}

entry_points = \
{'flake8.extension': ['tabs.blank-lines = flake8_tabs:BlankLinesChecker',
                      'tabs.indentation = flake8_tabs:IndentationChecker']}

setup(name='flake8-tabs',
      version='1.0.0',
      description='Tab indentation style checker for flake8',
      author='Alexander Schlarb',
      author_email='alexander@ninetailed.ninja',
      url='https://gitlab.com/ntninja/flake8-tabs',
      py_modules=['flake8_tabs'],
      extras_require=extras_require,
      entry_points=entry_points,
      python_requires='~=3.4',
     )
