from setuptools import setup
from src import __version__

setup(
    name="irma-shared",
    version=__version__,
    author="irma-dev",
    author_email="irma-dev@quarkslab.com",
    description="Schemas and constants of the IRMA software",
    packages=(
        "irma.shared",
        "irma.shared.schemas",
    ),
    package_dir={
        "irma.shared": "src",
    },
    namespace_packages=(
        "irma",
    ),
    install_requires=(
        'marshmallow==3.0.0rc1',
    ),
    test_suite='nose.collector',
    tests_require=(
        'nose',
    )
)
