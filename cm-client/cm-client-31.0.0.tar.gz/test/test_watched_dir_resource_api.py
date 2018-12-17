# coding: utf-8

"""
    Cloudera Manager API

    <h1>Cloudera Manager API v31</h1>       <p>Introduced in Cloudera Manager 6.1.0</p>       <p><a href=\"http://www.cloudera.com/documentation.html\">Cloudera Product Documentation</a></p>

    OpenAPI spec version: 6.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import cm_client
from cm_client.rest import ApiException
from cm_client.apis.watched_dir_resource_api import WatchedDirResourceApi


class TestWatchedDirResourceApi(unittest.TestCase):
    """ WatchedDirResourceApi unit test stubs """

    def setUp(self):
        self.api = cm_client.apis.watched_dir_resource_api.WatchedDirResourceApi()

    def tearDown(self):
        pass

    def test_add_watched_directory(self):
        """
        Test case for add_watched_directory

        Adds a directory to the watching list.
        """
        pass

    def test_list_watched_directories(self):
        """
        Test case for list_watched_directories

        Lists all the watched directories.
        """
        pass

    def test_remove_watched_directory(self):
        """
        Test case for remove_watched_directory

        Removes a directory from the watching list.
        """
        pass


if __name__ == '__main__':
    unittest.main()
