#!/usr/bin/env python3


"""
Setup for etask.
"""


from setuptools import setup

from etask import __description__
from etask import __version__


setup(
    name="etask",
    version=__version__,
    description=__description__,
    author="Maciej Barć",
    author_email="xgqt@riseup.net",
    url="https://gitlab.com/xgqt/python-etask",
    license="GPL-2-or-later",
    keywords="emacs",
    python_requires=">=3.6.*",
    install_requires=["colorama"],
    packages=["etask"],
    include_package_data=True,
    zip_safe=False,
    entry_points={"console_scripts": ["etask = etask.main:main"]},
)
