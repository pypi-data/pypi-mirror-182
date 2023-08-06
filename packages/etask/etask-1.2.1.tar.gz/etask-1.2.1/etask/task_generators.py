#!/usr/bin/env python3


"""
"""  """

This file is part of python-etask - CLI interface to GNU Emacs in Python.
Copyright (c) 2022, Maciej Barć <xgqt@riseup.net>
Licensed under the GNU GPL v2 License
SPDX-License-Identifier: GPL-2.0-or-later

python-etask is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 2 of the License, or
(at your option) any later version.

python-etask is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with python-etask.  If not, see <https://www.gnu.org/licenses/>.
"""


def package_archives_generator(archive_dict):
    """!
    Create Emacs package-archives.
    """

    for name, remote in archive_dict.items():
        yield [
            "--eval",
            f"(add-to-list 'package-archives '(\"{name}\" . \"{remote}\"))"
        ]


def loader_generator(file_paths):
    """!
    Create a list of arguments to load specified files.
    """

    for file_path in file_paths:
        yield ["-l", file_path]
