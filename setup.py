#!/usr/bin/env python3

import setuptools
import os


def _read_reqs(relpath):
    fullpath = os.path.join(os.path.dirname(__file__), relpath)
    with open(fullpath) as f:
        return [s.strip() for s in f.readlines() if (s.strip() and not s.startswith("#"))]


_INSTALL_REQUIRES = []
_REQUIREMENTS_FILES = ["requirements/netprobify.txt"]

for req in _REQUIREMENTS_FILES:
    _REQUIREMENTS_TXT = _read_reqs(req)
    _INSTALL_REQUIRES.extend([line for line in _REQUIREMENTS_TXT if "://" not in line])

with open("VERSION") as version_file:
    version = version_file.read().splitlines()[0]

setuptools.setup(
    name="netprobify",
    version=version,
    include_package_data=True,
    install_requires=_INSTALL_REQUIRES,
    tests_require=_read_reqs("requirements/tests.txt"),
    dependency_links=[],
    entry_points={"console_scripts": ["netprobify = netprobify.main:entrypoint"]},
    packages=setuptools.find_packages(),
)
