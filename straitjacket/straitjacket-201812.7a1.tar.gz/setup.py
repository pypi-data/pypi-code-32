# This file is part of the straitjacket project
# https://gitlab.com/mbarkhau/straitjacket
#
# Copyright (c) 2018 Manuel Barkhau (mbarkhau@gmail.com) - MIT License
# SPDX-License-Identifier: MIT

import os
import setuptools


def project_path(*sub_paths):
    project_dirpath = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(project_dirpath, *sub_paths)


def read(*sub_paths):
    with open(project_path(*sub_paths), mode="rb") as fh:
        return fh.read().decode("utf-8")


install_requires = [
    line.strip()
    for line in read("requirements", "pypi.txt").splitlines()
    if line.strip() and not line.startswith("#")
]


long_description = "\n\n".join((read("README.md"), read("CHANGELOG.md")))


setuptools.setup(
    name="straitjacket",
    license="MIT",
    author="Manuel Barkhau",
    author_email="mbarkhau@gmail.com",
    url="https://gitlab.com/mbarkhau/straitjacket",
    version="201812.7a1",
    keywords="formatter yapf black pyfmt gofmt",
    description="Another Uncompromising Code Formatter for Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["straitjacket"],
    package_dir={"": "src"},
    install_requires=install_requires,
    entry_points="""
        [console_scripts]
        sjfmt=straitjacket.sjfmt:main
        sjfmtd=straitjacket.sjfmtd:main
    """,
    python_requires=">=3.6",
    zip_safe=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS :: MacOS X",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
