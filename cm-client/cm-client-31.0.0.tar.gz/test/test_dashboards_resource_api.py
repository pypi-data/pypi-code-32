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
from cm_client.apis.dashboards_resource_api import DashboardsResourceApi


class TestDashboardsResourceApi(unittest.TestCase):
    """ DashboardsResourceApi unit test stubs """

    def setUp(self):
        self.api = cm_client.apis.dashboards_resource_api.DashboardsResourceApi()

    def tearDown(self):
        pass

    def test_create_dashboards(self):
        """
        Test case for create_dashboards

        Creates the list of dashboards.
        """
        pass

    def test_delete_dashboard(self):
        """
        Test case for delete_dashboard

        Deletes a dashboard.
        """
        pass

    def test_get_dashboard(self):
        """
        Test case for get_dashboard

        Returns a dashboard definition for the specified name.
        """
        pass

    def test_get_dashboards(self):
        """
        Test case for get_dashboards

        Returns the list of all user-customized dashboards.
        """
        pass


if __name__ == '__main__':
    unittest.main()
