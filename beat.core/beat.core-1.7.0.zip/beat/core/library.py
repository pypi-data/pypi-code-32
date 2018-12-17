#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

###############################################################################
#                                                                             #
# Copyright (c) 2016 Idiap Research Institute, http://www.idiap.ch/           #
# Contact: beat.support@idiap.ch                                              #
#                                                                             #
# This file is part of the beat.core module of the BEAT platform.             #
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

Forward imported from :py:mod:`beat.backend.python.library`:
:py:class:`beat.backend.python.library.Storage`
"""

import six

from . import schema
from . import prototypes

from beat.backend.python.library import Storage
from beat.backend.python.library import Library as BackendLibrary


class Library(BackendLibrary):
    """Librarys represent independent algorithm components within the platform.

    This class can only parse the meta-parameters of the library. The actual
    library is not directly treated by this class - only by the associated
    algorithms.


    Parameters:

      prefix (str): Establishes the prefix of your installation.

      data (:py:class:`object`, Optional): The piece of data representing the
        library. It must validate against the schema defined for libraries. If
        a string is passed, it is supposed to be a valid path to an library in
        the designated prefix area. If a tuple is passed (or a list), then we
        consider that the first element represents the library declaration,
        while the second, the code for the library (either in its source format
        or as a binary blob).  If ``None`` is passed, loads our default
        prototype for libraries (source code will be in Python).

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

    def __init__(self, prefix, data, library_cache=None):
        super(Library, self).__init__(prefix, data, library_cache)


    def _load(self, data, library_cache):
        """Loads the library"""

        self.errors = []
        self.data = None
        self.code = None

        self._name = None
        self.storage = None
        self.libraries = {}  # preloaded libraries
        code = None

        if data is None:  # loads prototype and validates it
            data = None
            code = None

        elif isinstance(data, (tuple, list)):  # user has passed individual info
            data, code = data  # break down into two components


        if isinstance(data, six.string_types):  # user has passed a file pointer
            # make sure to log this into the cache (avoids recursion)
            library_cache[data] = None

            self._name = data
            self.storage = Storage(self.prefix, self._name)
            if not self.storage.json.exists():
                self.errors.append('Library declaration file not found: %s' % data)
                return

            data = self.storage.json.path  # loads data from JSON declaration


        # At this point, `data' can be a dictionary or ``None``
        if data is None:  # loads the default declaration for an library
            self.data, self.errors = prototypes.load('library')
            assert not self.errors, "\n  * %s" % "\n  *".join(self.errors)
        else:  # just assign it
            # this runs basic validation, including JSON loading if required
            self.data, self.errors = schema.validate('library', data)


        if self.errors: return  # don't proceed with the rest of validation

        if self.storage is not None:  # loading from the disk, check code
            if not self.storage.code.exists():
                self.errors.append('Library code not found: %s' % \
                        self.storage.code.path)
                return
            else:
                code = self.storage.code.load()


        # At this point, `code' can be a string (or a binary blob) or ``None``
        if code is None:  # loads the default code for an library
            self.code = prototypes.binary_load('library.py')
            self.data['language'] = 'python'

        else:  # just assign it - notice that in this case, no language is set
            self.code = code


        if self.errors: return  # don't proceed with the rest of validation


        # if no errors so far, make sense out of the library data
        self.data.setdefault('uses', {})

        # now we check for consistence
        self._validate_required_libraries(library_cache)
        if self.errors: return  # don't proceed with the rest of validation

        self._check_language_consistence()


    def _validate_required_libraries(self, library_cache):

        # all used libraries must be loadable; cannot use self as a library

        if self.uses is not None:
            for name, value in self.uses.items():
                if value in library_cache:
                    if library_cache[value] is None:
                        self.errors.append("recursion for library `%s' detected" % value)
                        continue
                    self.libraries[value] = library_cache[value]
                else:
                    self.libraries[value] = Library(self.prefix, value, library_cache)

                if not self.libraries[value].valid:
                    self.errors.append("referred library `%s' (%s) is not valid" % \
                            (self.libraries[value].name, name))


    def _check_language_consistence(self):

        # all used libraries must be programmed with the same language
        if self.language == 'unknown': return  # bail out on unknown language

        if self.uses is not None:
            for name, library in self.uses.items():
                if library not in self.libraries: continue  # invalid

                if self.libraries[library].language != self.language:
                    self.errors.append("language for used library `%s' (`%s') " \
                            "differs from current language for this library (`%s')" % \
                            (library, self.libraries[library].language, self.language))
