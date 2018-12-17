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
from cm_client.apis.process_resource_api import ProcessResourceApi


class TestProcessResourceApi(unittest.TestCase):
    """ ProcessResourceApi unit test stubs """

    def setUp(self):
        self.api = cm_client.apis.process_resource_api.ProcessResourceApi()

    def tearDown(self):
        pass

    def test_get_config_file(self):
        """
        Test case for get_config_file

        Returns the contents of the specified config file.
        """
        pass

    def test_get_process(self):
        """
        Test case for get_process

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
