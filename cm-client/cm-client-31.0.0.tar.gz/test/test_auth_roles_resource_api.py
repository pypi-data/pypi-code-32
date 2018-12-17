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
from cm_client.apis.auth_roles_resource_api import AuthRolesResourceApi


class TestAuthRolesResourceApi(unittest.TestCase):
    """ AuthRolesResourceApi unit test stubs """

    def setUp(self):
        self.api = cm_client.apis.auth_roles_resource_api.AuthRolesResourceApi()

    def tearDown(self):
        pass

    def test_create_auth_roles(self):
        """
        Test case for create_auth_roles

        Creates a list of auth roles.
        """
        pass

    def test_delete_auth_role(self):
        """
        Test case for delete_auth_role

        Deletes an auth role from the system.
        """
        pass

    def test_read_auth_role(self):
        """
        Test case for read_auth_role

        Returns detailed information about an auth role.
        """
        pass

    def test_read_auth_roles(self):
        """
        Test case for read_auth_roles

        Returns a list of the auth roles configured in the system.
        """
        pass

    def test_read_auth_roles_metadata(self):
        """
        Test case for read_auth_roles_metadata

        Returns a list of the auth roles' metadata for the built-in roles.
        """
        pass

    def test_update_auth_role(self):
        """
        Test case for update_auth_role

        Updates the given auth role's information.
        """
        pass


if __name__ == '__main__':
    unittest.main()
