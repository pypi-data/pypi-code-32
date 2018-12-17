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
=======
library
=======

Validation for libraries
"""

import os
import simplejson

from . import loader
from . import utils


# ----------------------------------------------------------


class Storage(utils.CodeStorage):
    """Resolves paths for libraries

    Parameters:

      prefix (str): Establishes the prefix of
        your installation.

      name (str): The name of the library object in the format
        ``<user>/<name>/<version>``.

    """

    def __init__(self, prefix, name, language=None):

        if name.count('/') != 2:
            raise RuntimeError("invalid library name: `%s'" % name)

        self.username, self.name, self.version = name.split('/')
        self.fullname = name
        self.prefix = prefix

        path = utils.hashed_or_simple(self.prefix, 'libraries', name, suffix='.json')
        path = path[:-5]
        super(Storage, self).__init__(path, language)


# ----------------------------------------------------------


class Library(object):
    """Librarys represent independent algorithm components within the platform.

    This class can only parse the meta-parameters of the library. The actual
    library is not directly treated by this class - only by the associated
    algorithms.


    Parameters:

      prefix (str): Establishes the prefix of your installation.

      name (str): The fully qualified algorithm name (e.g. ``user/algo/1``)

      library_cache (:py:class:`dict`, Optional): A dictionary mapping library
        names to loaded libraries. This parameter is optional and, if passed,
        may greatly speed-up library loading times as libraries that are
        already loaded may be re-used.


    Attributes:

      name (str): The library name

      description (str): The short description string, loaded from the JSON
        file if one was set.

      documentation (str): The full-length docstring for this object.

      storage (object): A simple object that provides information about file
        paths for this library

      libraries (dict): A mapping object defining other libraries this library
        needs to load so it can work properly.

      uses (dict): A mapping object defining the required library import name
        (keys) and the full-names (values).

      errors (list): A list containing errors found while loading this
        library.

      data (dict): The original data for this library, as loaded by our JSON
        decoder.

      code (str): The code that is associated with this library, loaded as a
        text (or binary) file.

    """

    def __init__(self, prefix, name, library_cache=None):

        self._name = None
        self.storage = None
        self.prefix = prefix
        self.errors = []
        self.libraries = {}

        library_cache = library_cache if library_cache is not None else {}

        try:
            self._load(name, library_cache)
        finally:
            if self._name is not None: #registers it into the cache, even if failed
                library_cache[self._name] = self


    def _load(self, data, library_cache):
        """Loads the library"""

        self._name = data

        self.storage = Storage(self.prefix, data)
        json_path = self.storage.json.path
        if not self.storage.exists():
            self.errors.append('Library declaration file not found: %s' % json_path)
            return

        with open(json_path, 'rb') as f:
            self.data = simplejson.loads(f.read().decode('utf-8'))

        self.code_path = self.storage.code.path

        # if no errors so far, make sense out of the library data
        self.data.setdefault('uses', {})

        if self.uses is not None:
            for name, value in self.uses.items():
                self.libraries[value] = Library(self.prefix, value, library_cache)

        self.libraries[self._name] = self


    def uses_dict(self):
        """Returns the usage dictionary for all dependent modules"""

        if self.data['language'] == 'unknown':
            raise RuntimeError("library has no programming language set")

        if not self._name:
            raise RuntimeError("library has no name")

        retval = {}

        if self.uses is not None:

            for name, value in self.uses.items():
                retval[name] = dict(
                        path=self.libraries[value].storage.code.path,
                        uses=self.libraries[value].uses_dict(),
                        )

        return retval


    def load(self):
        """Loads the Python module for this library resolving all references

        Returns the loaded Python module.
        """

        if self.data['language'] == 'unknown':
            raise RuntimeError("library has no programming language set")

        if not self._name:
            raise RuntimeError("library has no name")

        return loader.load_module(self.name.replace(os.sep, '_'),
                self.storage.code.path, self.uses_dict())


    @property
    def name(self):
        """Returns the name of this object"""

        return self._name or '__unnamed_library__'


    @name.setter
    def name(self, value):

        if self.data['language'] == 'unknown':
            raise RuntimeError("library has no programming language set")

        self._name = value
        self.storage = Storage(self.prefix, value, self.data['language'])


    @property
    def schema_version(self):
        """Returns the schema version"""
        return self.data.get('schema_version', 1)


    @property
    def language(self):
        """Returns the current language set for the library code"""
        return self.data['language']


    @language.setter
    def language(self, value):
        """Sets the current executable code programming language"""
        if self.storage: self.storage.language = value
        self.data['language'] = value
        self._check_language_consistence()


    @property
    def valid(self):
        """A boolean that indicates if this library is valid or not"""

        return not bool(self.errors)


    @property
    def uses(self):
        return self.data.get('uses')


    @uses.setter
    def uses(self, value):
        self.data['uses'] = value
        return value


    @property
    def description(self):
        """The short description for this object"""
        return self.data.get('description', None)


    @description.setter
    def description(self, value):
        """Sets the short description for this object"""
        self.data['description'] = value


    @property
    def documentation(self):
        """The full-length description for this object"""

        if not self._name:
            raise RuntimeError("library has no name")

        if self.storage.doc.exists():
            return self.storage.doc.load()
        return None


    @documentation.setter
    def documentation(self, value):
        """Sets the full-length description for this object"""

        if not self._name:
            raise RuntimeError("library has no name")

        if hasattr(value, 'read'):
            self.storage.doc.save(value.read())
        else:
            self.storage.doc.save(value)


    def hash(self):
        """Returns the hexadecimal hash for the current library"""

        if not self._name:
            raise RuntimeError("library has no name")

        return self.storage.hash()


    def json_dumps(self, indent=4):
        """Dumps the JSON declaration of this object in a string


        Parameters:

          indent (int): The number of indentation spaces at every indentation level


        Returns:

          str: The JSON representation for this object

        """

        return simplejson.dumps(self.data, indent=indent,
            cls=utils.NumpyJSONEncoder)


    def __str__(self):
        return self.json_dumps()


    def write(self, storage=None):
        """Writes contents to prefix location.

        Parameters:

          storage (:py:class:`.Storage`, Optional): If you pass a new
            storage, then this object will be written to that storage point
            rather than its default.

        """

        if self.data['language'] == 'unknown':
            raise RuntimeError("library has no programming language set")

        if storage is None:
            if not self._name:
                raise RuntimeError("library has no name")
            storage = self.storage #overwrite

        storage.save(str(self), self.code, self.description)


    def export(self, prefix):
        """Recursively exports itself into another prefix

        Other required libraries are also copied.


        Parameters:

          prefix (str): Establishes the prefix of your installation.


        Returns:

          None


        Raises:

          RuntimeError: If prefix and self.prefix point to the same directory.

        """

        if not self._name:
            raise RuntimeError("library has no name")

        if not self.valid:
            raise RuntimeError("library is not valid")

        if prefix == self.prefix:
            raise RuntimeError("Cannot export library to the same prefix ("
                               "%s)" % (prefix))

        for k in self.libraries.values():
            k.export(prefix)

        self.write(Storage(prefix, self.name))
