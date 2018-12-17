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


class TimeSeriesCrossEntityMetadata(object):
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
        'max_entity_display_name': 'str',
        'max_entity_name': 'str',
        'min_entity_display_name': 'str',
        'min_entity_name': 'str',
        'num_entities': 'float'
    }

    attribute_map = {
        'max_entity_display_name': 'maxEntityDisplayName',
        'max_entity_name': 'maxEntityName',
        'min_entity_display_name': 'minEntityDisplayName',
        'min_entity_name': 'minEntityName',
        'num_entities': 'numEntities'
    }

    def __init__(self, max_entity_display_name=None, max_entity_name=None, min_entity_display_name=None, min_entity_name=None, num_entities=None):  # noqa: E501
        """TimeSeriesCrossEntityMetadata - a model defined in Swagger"""  # noqa: E501

        self._max_entity_display_name = None
        self._max_entity_name = None
        self._min_entity_display_name = None
        self._min_entity_name = None
        self._num_entities = None
        self.discriminator = None

        self.max_entity_display_name = max_entity_display_name
        if max_entity_name is not None:
            self.max_entity_name = max_entity_name
        self.min_entity_display_name = min_entity_display_name
        if min_entity_name is not None:
            self.min_entity_name = min_entity_name
        self.num_entities = num_entities

    @property
    def max_entity_display_name(self):
        """Gets the max_entity_display_name of this TimeSeriesCrossEntityMetadata.  # noqa: E501

        Display name for maximum entity  # noqa: E501

        :return: The max_entity_display_name of this TimeSeriesCrossEntityMetadata.  # noqa: E501
        :rtype: str
        """
        return self._max_entity_display_name

    @max_entity_display_name.setter
    def max_entity_display_name(self, max_entity_display_name):
        """Sets the max_entity_display_name of this TimeSeriesCrossEntityMetadata.

        Display name for maximum entity  # noqa: E501

        :param max_entity_display_name: The max_entity_display_name of this TimeSeriesCrossEntityMetadata.  # noqa: E501
        :type: str
        """
        if max_entity_display_name is None:
            raise ValueError("Invalid value for `max_entity_display_name`, must not be `None`")  # noqa: E501

        self._max_entity_display_name = max_entity_display_name

    @property
    def max_entity_name(self):
        """Gets the max_entity_name of this TimeSeriesCrossEntityMetadata.  # noqa: E501

        Name for maximum entity  # noqa: E501

        :return: The max_entity_name of this TimeSeriesCrossEntityMetadata.  # noqa: E501
        :rtype: str
        """
        return self._max_entity_name

    @max_entity_name.setter
    def max_entity_name(self, max_entity_name):
        """Sets the max_entity_name of this TimeSeriesCrossEntityMetadata.

        Name for maximum entity  # noqa: E501

        :param max_entity_name: The max_entity_name of this TimeSeriesCrossEntityMetadata.  # noqa: E501
        :type: str
        """

        self._max_entity_name = max_entity_name

    @property
    def min_entity_display_name(self):
        """Gets the min_entity_display_name of this TimeSeriesCrossEntityMetadata.  # noqa: E501

        Display name for minimum entity  # noqa: E501

        :return: The min_entity_display_name of this TimeSeriesCrossEntityMetadata.  # noqa: E501
        :rtype: str
        """
        return self._min_entity_display_name

    @min_entity_display_name.setter
    def min_entity_display_name(self, min_entity_display_name):
        """Sets the min_entity_display_name of this TimeSeriesCrossEntityMetadata.

        Display name for minimum entity  # noqa: E501

        :param min_entity_display_name: The min_entity_display_name of this TimeSeriesCrossEntityMetadata.  # noqa: E501
        :type: str
        """
        if min_entity_display_name is None:
            raise ValueError("Invalid value for `min_entity_display_name`, must not be `None`")  # noqa: E501

        self._min_entity_display_name = min_entity_display_name

    @property
    def min_entity_name(self):
        """Gets the min_entity_name of this TimeSeriesCrossEntityMetadata.  # noqa: E501

        Name for minimum entity  # noqa: E501

        :return: The min_entity_name of this TimeSeriesCrossEntityMetadata.  # noqa: E501
        :rtype: str
        """
        return self._min_entity_name

    @min_entity_name.setter
    def min_entity_name(self, min_entity_name):
        """Sets the min_entity_name of this TimeSeriesCrossEntityMetadata.

        Name for minimum entity  # noqa: E501

        :param min_entity_name: The min_entity_name of this TimeSeriesCrossEntityMetadata.  # noqa: E501
        :type: str
        """

        self._min_entity_name = min_entity_name

    @property
    def num_entities(self):
        """Gets the num_entities of this TimeSeriesCrossEntityMetadata.  # noqa: E501

        Number of entities  # noqa: E501

        :return: The num_entities of this TimeSeriesCrossEntityMetadata.  # noqa: E501
        :rtype: float
        """
        return self._num_entities

    @num_entities.setter
    def num_entities(self, num_entities):
        """Sets the num_entities of this TimeSeriesCrossEntityMetadata.

        Number of entities  # noqa: E501

        :param num_entities: The num_entities of this TimeSeriesCrossEntityMetadata.  # noqa: E501
        :type: float
        """
        if num_entities is None:
            raise ValueError("Invalid value for `num_entities`, must not be `None`")  # noqa: E501

        self._num_entities = num_entities

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
        if not isinstance(other, TimeSeriesCrossEntityMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
