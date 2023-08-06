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


from os.path import abspath, isdir, isfile


def path(path_string):
    """!
    Check if path is a directory or file.
    Throw an error if it is not.

    @param path_string: path to a directory or file

    @returns absolute path to a directory or file
    """

    absolute_path = abspath(path_string)

    if isdir(absolute_path) or isfile(absolute_path):
        return absolute_path

    raise FileNotFoundError(absolute_path)


def dir_path(path_string):
    """!
    Check if path is a directory.
    Throw an error if it is not.

    @param path_string: path to a directory

    @returns absolute path to a directory
    """

    absolute_path = abspath(path_string)

    if isdir(absolute_path):
        return absolute_path

    raise NotADirectoryError(absolute_path)


def file_path(path_string):
    """!
    Check if path is a file.
    Throw an error if it is not.

    @param path_string: path to a file

    @returns absolute path to a file
    """

    absolute_path = abspath(path_string)

    if isfile(absolute_path):
        return absolute_path

    raise FileNotFoundError(absolute_path)
