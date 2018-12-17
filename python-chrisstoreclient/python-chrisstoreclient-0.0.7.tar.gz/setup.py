import sys

# Make sure we are running python3.5+
if 10 * sys.version_info[0]  + sys.version_info[1] < 35:
    sys.exit("Sorry, only Python 3.5+ is supported.")

from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
      name             =   'python-chrisstoreclient',
      version          =   '0.0.7',
      description      =   '(Python) client for the ChRIS store API',
      long_description =   readme(),
      author           =   'FNNDSC',
      author_email     =   'dev@babymri.org',
      url              =   'https://github.com/FNNDSC/python-chrisstoreclient',
      packages         =   ['chrisstoreclient'],
      install_requires =   ['requests==2.21.0', 'collection-json==0.1.1'],
      test_suite       =   'nose.collector',
      tests_require    =   ['nose'],
      scripts          =   ['bin/chrisstoreclient'],
      license          =   'MIT',
      zip_safe=False
)
