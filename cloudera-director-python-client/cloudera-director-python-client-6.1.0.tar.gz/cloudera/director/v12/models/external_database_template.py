# coding: utf-8

"""
Licensed to Cloudera, Inc. under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  Cloudera, Inc. licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""


import pprint
import re  # noqa: F401

import six


class ExternalDatabaseTemplate(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'name': 'str',
        'database_server_name': 'str',
        'database_name_prefix': 'str',
        'username_prefix': 'str'
    }

    attribute_map = {
        'name': 'name',
        'database_server_name': 'databaseServerName',
        'database_name_prefix': 'databaseNamePrefix',
        'username_prefix': 'usernamePrefix'
    }

    def __init__(self, name=None, database_server_name=None, database_name_prefix=None, username_prefix=None):  # noqa: E501
        """ExternalDatabaseTemplate - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._database_server_name = None
        self._database_name_prefix = None
        self._username_prefix = None
        self.discriminator = None

        self.name = name
        self.database_server_name = database_server_name
        self.database_name_prefix = database_name_prefix
        if username_prefix is not None:
            self.username_prefix = username_prefix

    @property
    def name(self):
        """Gets the name of this ExternalDatabaseTemplate.  # noqa: E501

        External database template name  # noqa: E501

        :return: The name of this ExternalDatabaseTemplate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ExternalDatabaseTemplate.

        External database template name  # noqa: E501

        :param name: The name of this ExternalDatabaseTemplate.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def database_server_name(self):
        """Gets the database_server_name of this ExternalDatabaseTemplate.  # noqa: E501

        External database server name  # noqa: E501

        :return: The database_server_name of this ExternalDatabaseTemplate.  # noqa: E501
        :rtype: str
        """
        return self._database_server_name

    @database_server_name.setter
    def database_server_name(self, database_server_name):
        """Sets the database_server_name of this ExternalDatabaseTemplate.

        External database server name  # noqa: E501

        :param database_server_name: The database_server_name of this ExternalDatabaseTemplate.  # noqa: E501
        :type: str
        """
        if database_server_name is None:
            raise ValueError("Invalid value for `database_server_name`, must not be `None`")  # noqa: E501

        self._database_server_name = database_server_name

    @property
    def database_name_prefix(self):
        """Gets the database_name_prefix of this ExternalDatabaseTemplate.  # noqa: E501

        Prefix to use when generating external database name  # noqa: E501

        :return: The database_name_prefix of this ExternalDatabaseTemplate.  # noqa: E501
        :rtype: str
        """
        return self._database_name_prefix

    @database_name_prefix.setter
    def database_name_prefix(self, database_name_prefix):
        """Sets the database_name_prefix of this ExternalDatabaseTemplate.

        Prefix to use when generating external database name  # noqa: E501

        :param database_name_prefix: The database_name_prefix of this ExternalDatabaseTemplate.  # noqa: E501
        :type: str
        """
        if database_name_prefix is None:
            raise ValueError("Invalid value for `database_name_prefix`, must not be `None`")  # noqa: E501

        self._database_name_prefix = database_name_prefix

    @property
    def username_prefix(self):
        """Gets the username_prefix of this ExternalDatabaseTemplate.  # noqa: E501

        Prefix to use when generating user name for access to database  # noqa: E501

        :return: The username_prefix of this ExternalDatabaseTemplate.  # noqa: E501
        :rtype: str
        """
        return self._username_prefix

    @username_prefix.setter
    def username_prefix(self, username_prefix):
        """Sets the username_prefix of this ExternalDatabaseTemplate.

        Prefix to use when generating user name for access to database  # noqa: E501

        :param username_prefix: The username_prefix of this ExternalDatabaseTemplate.  # noqa: E501
        :type: str
        """

        self._username_prefix = username_prefix

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ExternalDatabaseTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
