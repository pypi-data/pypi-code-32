# coding: utf-8

"""
    Cloudera Manager API

    <h1>Cloudera Manager API v31</h1>       <p>Introduced in Cloudera Manager 6.1.0</p>       <p><a href=\"http://www.cloudera.com/documentation.html\">Cloudera Product Documentation</a></p>

    OpenAPI spec version: 6.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ApiReplicationState(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'incremental_export_enabled': 'bool'
    }

    attribute_map = {
        'incremental_export_enabled': 'incrementalExportEnabled'
    }

    def __init__(self, incremental_export_enabled=None):
        """
        ApiReplicationState - a model defined in Swagger
        """

        self._incremental_export_enabled = None

        if incremental_export_enabled is not None:
          self.incremental_export_enabled = incremental_export_enabled

    @property
    def incremental_export_enabled(self):
        """
        Gets the incremental_export_enabled of this ApiReplicationState.
        returns if incremental export is enabled for the given Hive service. Not applicable for HDFS service.

        :return: The incremental_export_enabled of this ApiReplicationState.
        :rtype: bool
        """
        return self._incremental_export_enabled

    @incremental_export_enabled.setter
    def incremental_export_enabled(self, incremental_export_enabled):
        """
        Sets the incremental_export_enabled of this ApiReplicationState.
        returns if incremental export is enabled for the given Hive service. Not applicable for HDFS service.

        :param incremental_export_enabled: The incremental_export_enabled of this ApiReplicationState.
        :type: bool
        """

        self._incremental_export_enabled = incremental_export_enabled

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, ApiReplicationState):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
