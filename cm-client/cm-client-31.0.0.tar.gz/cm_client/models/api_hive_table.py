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


class ApiHiveTable(object):
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
        'database': 'str',
        'table_name': 'str'
    }

    attribute_map = {
        'database': 'database',
        'table_name': 'tableName'
    }

    def __init__(self, database=None, table_name=None):
        """
        ApiHiveTable - a model defined in Swagger
        """

        self._database = None
        self._table_name = None

        if database is not None:
          self.database = database
        if table_name is not None:
          self.table_name = table_name

    @property
    def database(self):
        """
        Gets the database of this ApiHiveTable.
        Name of the database to which this table belongs.

        :return: The database of this ApiHiveTable.
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        """
        Sets the database of this ApiHiveTable.
        Name of the database to which this table belongs.

        :param database: The database of this ApiHiveTable.
        :type: str
        """

        self._database = database

    @property
    def table_name(self):
        """
        Gets the table_name of this ApiHiveTable.
        Name of the table. When used as input for a replication job, this can be a regular expression that matches several table names. Refer to the Hive documentation for the syntax of regular expressions.

        :return: The table_name of this ApiHiveTable.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """
        Sets the table_name of this ApiHiveTable.
        Name of the table. When used as input for a replication job, this can be a regular expression that matches several table names. Refer to the Hive documentation for the syntax of regular expressions.

        :param table_name: The table_name of this ApiHiveTable.
        :type: str
        """

        self._table_name = table_name

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
        if not isinstance(other, ApiHiveTable):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
