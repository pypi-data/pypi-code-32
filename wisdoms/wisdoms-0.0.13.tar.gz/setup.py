# Created by Q-ays.
# whosqays@gmail.com


import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="wisdoms",
    version="0.0.13",
    author="tzxd group",
    author_email="whosqays@qq.com",
    description="those common functions of package for inner corporation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
