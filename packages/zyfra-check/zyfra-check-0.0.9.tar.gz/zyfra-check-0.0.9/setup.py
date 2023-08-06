#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


setup(
    name="zyfra-check",
    version="0.0.9",
    description="A plugin that allows multiple failures per test.",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=["pytest>=3.1.1", "jira>=3.4.1", "testit-adapter-pytest>=1.1.2"],
    entry_points={"pytest11": ["check = zyfra_check.plugin"]},
)
