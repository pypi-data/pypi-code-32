#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

###############################################################################
#                                                                             #
# Copyright (c) 2016 Idiap Research Institute, http://www.idiap.ch/           #
# Contact: beat.support@idiap.ch                                              #
#                                                                             #
# This file is part of the beat.backend.python module of the BEAT platform.   #
#                                                                             #
# Commercial License Usage                                                    #
# Licensees holding valid commercial BEAT licenses may use this file in       #
# accordance with the terms contained in a written agreement between you      #
# and Idiap. For further information contact tto@idiap.ch                     #
#                                                                             #
# Alternatively, this file may be used under the terms of the GNU Affero      #
# Public License version 3 as published by the Free Software and appearing    #
# in the file LICENSE.AGPL included in the packaging of this file.            #
# The BEAT platform is distributed in the hope that it will be useful, but    #
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY  #
# or FITNESS FOR A PARTICULAR PURPOSE.                                        #
#                                                                             #
# You should have received a copy of the GNU Affero Public License along      #
# with the BEAT platform. If not, see http://www.gnu.org/licenses/.           #
#                                                                             #
###############################################################################

"""
=====
utils
=====

This module implements helper classes and functions.
"""

import os
import shutil
import collections
import numpy
import simplejson
import six

from . import hash


# ----------------------------------------------------------


def hashed_or_simple(prefix, what, path, suffix='.json'):
    """Returns a hashed path or simple path depending on where the resource is
    """

    username, right_bit = path.split('/', 1)
    hashed_prefix = hash.toUserPath(username)
    candidate = os.path.join(prefix, what, hashed_prefix, right_bit) + suffix

    if os.path.exists(candidate):
        return candidate

    return os.path.join(prefix, what, path + suffix)


# ----------------------------------------------------------


def safe_rmfile(f):
    """Safely removes a file from the disk"""

    if os.path.exists(f):
        os.unlink(f)


# ----------------------------------------------------------


def safe_rmdir(f):
    """Safely removes the directory containg a given file from the disk"""

    d = os.path.dirname(f)

    if not os.path.exists(d):
        return

    if not os.listdir(d):
        os.rmdir(d)


# ----------------------------------------------------------


def extension_for_language(language):
    """Returns the preferred extension for a given programming language

    The set of languages supported must match those declared in our
    ``common.json`` schema.

    Parameters:

      language (str) The language for which you'd like to get the extension for.


    Returns:

      str: The extension for the given language, including a leading ``.`` (dot)


    Raises:

      KeyError: If the language is not defined in our internal dictionary.

    """

    return dict(
        unknown = '',
        cxx = '.so',
        matlab = '.m',
        python = '.py',
        r = '.r',
    )[language]


# ----------------------------------------------------------


class Prefix(object):

    def __init__(self, paths=None):
        if isinstance(paths, list):
            self.paths = paths
        elif paths is not None:
            self.paths = [paths]
        else:
            self.paths = []

    def add(self, path):
        self.paths.append(path)

    def path(self, filename):
        for p in self.paths:
            fullpath = os.path.join(p, filename)
            if os.path.exists(fullpath):
                return fullpath

        return os.path.join(self.paths[0], filename)


# ----------------------------------------------------------


class File(object):
    """User helper to read and write file objects"""


    def __init__(self, path, binary=False):

        self.path = path
        self.binary = binary


    def exists(self):

        return os.path.exists(self.path)


    def load(self):

        mode = 'rb' if self.binary else 'rt'
        with open(self.path, mode) as f:
            return f.read()


    def try_load(self):

        if os.path.exists(self.path):
            return self.load()
        return None


    def backup(self):

        if not os.path.exists(self.path):
            return #no point in backing-up

        backup = self.path + '~'
        if os.path.exists(backup):
            os.remove(backup)

        shutil.copy(self.path, backup)


    def save(self, contents):

        d = os.path.dirname(self.path)
        if not os.path.exists(d):
            os.makedirs(d)

        if os.path.exists(self.path):
            self.backup()

        mode = 'wb' if self.binary else 'wt'
        if self.binary:
            mode = 'wb'
            if isinstance(contents, six.string_types):
                contents = contents.encode('utf-8')
        else:
            mode = 'wt'
            if not isinstance(contents, six.string_types):
                contents = contents.decode('utf-8')

        with open(self.path, mode) as f:
            f.write(contents)


    def remove(self):

        safe_rmfile(self.path)
        safe_rmfile(self.path + '~') #backup
        safe_rmdir(self.path) #remove containing directory


# ----------------------------------------------------------


class Storage(object):
    """Resolves paths for objects that provide only a description"""

    def __init__(self, path):

        self.path = path
        self.json = File(self.path + '.json')
        self.doc = File(self.path + '.rst')

    def hash(self, description='description'):
        """The 64-character hash of the database declaration JSON"""
        return hash.hashJSONFile(self.json.path, description)

    def exists(self):
        """If the database declaration file exists"""
        return self.json.exists()

    def load(self):
        """Loads the JSON declaration as a file"""
        tp = collections.namedtuple('Storage', ['declaration', 'description'])
        return tp(self.json.load(), self.doc.try_load())

    def save(self, declaration, description=None):
        """Saves the JSON declaration as files"""
        if description: self.doc.save(description.encode('utf8'))
        if not isinstance(declaration, six.string_types):
            declaration = simplejson.dumps(declaration, indent=4)
        self.json.save(declaration)

    def remove(self):
        """Removes the object from the disk"""
        self.json.remove()
        self.doc.remove()


# ----------------------------------------------------------


class CodeStorage(object):
    """Resolves paths for objects that provide a description and code

    Parameters:

      language (str): One of the valdid programming languages

    """

    def __init__(self, path, language=None):

        self.path = path
        self.json = File(self.path + '.json')
        self.doc = File(self.path + '.rst')

        self._language = language or self.__auto_discover_language()
        self.code = File(self.path + \
                extension_for_language(self._language), binary=True)

    def __auto_discover_language(self, json=None):
        """Discovers and sets the language from its own JSON descriptor"""
        try:
            text = json or self.json.load()
            json = simplejson.loads(text)
            return json['language']
        except IOError:
            return 'unknown'

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, value):
        self._language = value
        self.code = File(self.path + extension_for_language(self._language),
                binary=True)

    def hash(self):
        """The 64-character hash of the database declaration JSON"""

        if self.code.exists():
            return hash.hash(dict(
                json=hash.hashJSONFile(self.json.path, 'description'),
                code=hash.hashFileContents(self.code.path),
            ))
        else:
            return hash.hash(dict(
                json=hash.hashJSONFile(self.json.path, 'description'),
            ))

    def exists(self):
        """If the database declaration file exists"""
        return self.json.exists() and self.code.exists()

    def load(self):
        """Loads the JSON declaration as a file"""
        tp = collections.namedtuple('CodeStorage',
                ['declaration', 'code', 'description'])
        return tp(self.json.load(), self.code.try_load(), self.doc.try_load())

    def save(self, declaration, code=None, description=None):
        """Saves the JSON declaration and the code as files"""
        if description:
            self.doc.save(description.encode('utf8'))

        if not isinstance(declaration, six.string_types):
            declaration = simplejson.dumps(declaration, indent=4)
        self.json.save(declaration)

        if code:
            if self._language == 'unknown':
                self.language = self.__auto_discover_language(declaration)
            self.code.save(code)

    def remove(self):
        """Removes the object from the disk"""
        self.json.remove()
        self.doc.remove()
        self.code.remove()


# ----------------------------------------------------------


class NumpyJSONEncoder(simplejson.JSONEncoder):
    """Encodes numpy arrays and scalars

    See Also:

      :py:class:`simplejson.JSONEncoder`

    """

    def default(self, obj):
        if isinstance(obj, numpy.ndarray) or isinstance(obj, numpy.generic):
            return obj.tolist()
        elif isinstance(obj, numpy.dtype):
            if obj.name == 'str': return 'string'
            return obj.name
        return simplejson.JSONEncoder.default(self, obj)


# ----------------------------------------------------------


def has_argument(method, argument):
    try:
        from inspect import signature
        sig = signature(method)
        params = sig.parameters
    except ImportError:
        from inspect import getargspec
        params = getargspec(method).args

    return argument in params
