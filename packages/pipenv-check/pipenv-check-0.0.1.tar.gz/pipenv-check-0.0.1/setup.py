#!/usr/bin/env python
from sys import exit

from setuptools import find_packages, setup

long_description = u"\n\n".join((open("README.md").read(),))

setup(
    name="pipenv-check",
    version="0.0.1",
    description="View installed pip packages and their update status.",
    long_description=long_description,
    author="3bfab",
    author_email="info@3bfab.com",
    licence="MIT",
    url="https://github.com/3bfab/pipenv-check",
    classifiers=[],
    package_dir={"": "pipenv-check"},
    packages=find_packages(
        where='pipenv-check',
    ),
    package_data={},
    include_package_data=True,
    python_requires=">=3.6",
    install_requires=[
        "pip>=9",
        "toml==0.10.2",
    ],
)
