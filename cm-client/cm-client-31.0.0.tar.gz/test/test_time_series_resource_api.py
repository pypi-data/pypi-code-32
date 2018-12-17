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
from cm_client.apis.time_series_resource_api import TimeSeriesResourceApi


class TestTimeSeriesResourceApi(unittest.TestCase):
    """ TimeSeriesResourceApi unit test stubs """

    def setUp(self):
        self.api = cm_client.apis.time_series_resource_api.TimeSeriesResourceApi()

    def tearDown(self):
        pass

    def test_get_entity_type_attributes(self):
        """
        Test case for get_entity_type_attributes

        Retrieve all metric entity type attributes monitored by Cloudera Manager.
        """
        pass

    def test_get_entity_types(self):
        """
        Test case for get_entity_types

        Retrieve all metric entity types monitored by Cloudera Manager.
        """
        pass

    def test_get_metric_schema(self):
        """
        Test case for get_metric_schema

        Retrieve schema for all metrics.
        """
        pass

    def test_query_time_series(self):
        """
        Test case for query_time_series

        Retrieve time-series data from the Cloudera Manager (CM) time-series data store using a tsquery.
        """
        pass

    def test_query_time_series_0(self):
        """
        Test case for query_time_series_0

        Retrieve time-series data from the Cloudera Manager (CM) time-series data store accepting HTTP POST request.
        """
        pass


if __name__ == '__main__':
    unittest.main()
