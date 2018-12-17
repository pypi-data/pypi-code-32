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
from cm_client.apis.activities_resource_api import ActivitiesResourceApi


class TestActivitiesResourceApi(unittest.TestCase):
    """ ActivitiesResourceApi unit test stubs """

    def setUp(self):
        self.api = cm_client.apis.activities_resource_api.ActivitiesResourceApi()

    def tearDown(self):
        pass

    def test_get_metrics(self):
        """
        Test case for get_metrics

        Fetch metric readings for a particular activity.
        """
        pass

    def test_read_activities(self):
        """
        Test case for read_activities

        Read all activities in the system.
        """
        pass

    def test_read_activity(self):
        """
        Test case for read_activity

        Returns a specific activity in the system.
        """
        pass

    def test_read_child_activities(self):
        """
        Test case for read_child_activities

        Returns the child activities.
        """
        pass

    def test_read_similar_activities(self):
        """
        Test case for read_similar_activities

        Returns a list of similar activities.
        """
        pass


if __name__ == '__main__':
    unittest.main()
