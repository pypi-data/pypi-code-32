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
from cm_client.apis.commands_resource_api import CommandsResourceApi


class TestCommandsResourceApi(unittest.TestCase):
    """ CommandsResourceApi unit test stubs """

    def setUp(self):
        self.api = cm_client.apis.commands_resource_api.CommandsResourceApi()

    def tearDown(self):
        pass

    def test_abort_command(self):
        """
        Test case for abort_command

        Abort a running command.
        """
        pass

    def test_read_command(self):
        """
        Test case for read_command

        Retrieve detailed information on an asynchronous command.
        """
        pass

    def test_retry(self):
        """
        Test case for retry

        Try to rerun a command.
        """
        pass


if __name__ == '__main__':
    unittest.main()
