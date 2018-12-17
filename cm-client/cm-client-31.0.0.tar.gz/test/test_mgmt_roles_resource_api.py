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
from cm_client.apis.mgmt_roles_resource_api import MgmtRolesResourceApi


class TestMgmtRolesResourceApi(unittest.TestCase):
    """ MgmtRolesResourceApi unit test stubs """

    def setUp(self):
        self.api = cm_client.apis.mgmt_roles_resource_api.MgmtRolesResourceApi()

    def tearDown(self):
        pass

    def test_create_roles(self):
        """
        Test case for create_roles

        Create new roles in the Cloudera Management Services.
        """
        pass

    def test_delete_role(self):
        """
        Test case for delete_role

        Delete a role from the Cloudera Management Services.
        """
        pass

    def test_enter_maintenance_mode(self):
        """
        Test case for enter_maintenance_mode

        Put the Cloudera Management Service role into maintenance mode.
        """
        pass

    def test_exit_maintenance_mode(self):
        """
        Test case for exit_maintenance_mode

        Take the Cloudera Management Service role out of maintenance mode.
        """
        pass

    def test_get_full_log(self):
        """
        Test case for get_full_log

        Retrieves the log file for the role's main process.
        """
        pass

    def test_get_stacks_log(self):
        """
        Test case for get_stacks_log

        Retrieves the stacks log file, if any, for the role's main process.
        """
        pass

    def test_get_stacks_logs_bundle(self):
        """
        Test case for get_stacks_logs_bundle

        Download a zip-compressed archive of role stacks logs.
        """
        pass

    def test_get_standard_error(self):
        """
        Test case for get_standard_error

        Retrieves the role's standard error output.
        """
        pass

    def test_get_standard_output(self):
        """
        Test case for get_standard_output

        Retrieves the role's standard output.
        """
        pass

    def test_list_active_commands(self):
        """
        Test case for list_active_commands

        List active role commands.
        """
        pass

    def test_read_role(self):
        """
        Test case for read_role

        Retrieve detailed information about a Cloudera Management Services role.
        """
        pass

    def test_read_role_config(self):
        """
        Test case for read_role_config

        Retrieve the configuration of a specific Cloudera Management Services role.
        """
        pass

    def test_read_roles(self):
        """
        Test case for read_roles

        List all roles of the Cloudera Management Services.
        """
        pass

    def test_update_role_config(self):
        """
        Test case for update_role_config

        Update the configuration of a Cloudera Management Services role.
        """
        pass


if __name__ == '__main__':
    unittest.main()
