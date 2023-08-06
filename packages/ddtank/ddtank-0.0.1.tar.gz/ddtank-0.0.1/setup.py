#!/usr/bin/env python
# -*- coding:utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="ddtank",
    version="0.0.1",
    keywords=["pip", "ddtank"],
    description="A package used for writing ddtank game scripts.",
    license="MIT Licence",
    author="zx",
    author_email="jugking6688@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=["pywin32"]
)
