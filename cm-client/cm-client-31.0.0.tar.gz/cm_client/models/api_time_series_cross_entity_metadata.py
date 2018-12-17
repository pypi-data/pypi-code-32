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


class ApiTimeSeriesCrossEntityMetadata(object):
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

    def __init__(self, max_entity_display_name=None, max_entity_name=None, min_entity_display_name=None, min_entity_name=None, num_entities=None):
        """
        ApiTimeSeriesCrossEntityMetadata - a model defined in Swagger
        """

        self._max_entity_display_name = None
        self._max_entity_name = None
        self._min_entity_display_name = None
        self._min_entity_name = None
        self._num_entities = None

        if max_entity_display_name is not None:
          self.max_entity_display_name = max_entity_display_name
        if max_entity_name is not None:
          self.max_entity_name = max_entity_name
        if min_entity_display_name is not None:
          self.min_entity_display_name = min_entity_display_name
        if min_entity_name is not None:
          self.min_entity_name = min_entity_name
        if num_entities is not None:
          self.num_entities = num_entities

    @property
    def max_entity_display_name(self):
        """
        Gets the max_entity_display_name of this ApiTimeSeriesCrossEntityMetadata.
        The display name of the entity that had the maximum value for the cross-entity aggregate metric.

        :return: The max_entity_display_name of this ApiTimeSeriesCrossEntityMetadata.
        :rtype: str
        """
        return self._max_entity_display_name

    @max_entity_display_name.setter
    def max_entity_display_name(self, max_entity_display_name):
        """
        Sets the max_entity_display_name of this ApiTimeSeriesCrossEntityMetadata.
        The display name of the entity that had the maximum value for the cross-entity aggregate metric.

        :param max_entity_display_name: The max_entity_display_name of this ApiTimeSeriesCrossEntityMetadata.
        :type: str
        """

        self._max_entity_display_name = max_entity_display_name

    @property
    def max_entity_name(self):
        """
        Gets the max_entity_name of this ApiTimeSeriesCrossEntityMetadata.
        The name of the entity that had the maximum value for the cross-entity aggregate metric. <p> Available since API v11.

        :return: The max_entity_name of this ApiTimeSeriesCrossEntityMetadata.
        :rtype: str
        """
        return self._max_entity_name

    @max_entity_name.setter
    def max_entity_name(self, max_entity_name):
        """
        Sets the max_entity_name of this ApiTimeSeriesCrossEntityMetadata.
        The name of the entity that had the maximum value for the cross-entity aggregate metric. <p> Available since API v11.

        :param max_entity_name: The max_entity_name of this ApiTimeSeriesCrossEntityMetadata.
        :type: str
        """

        self._max_entity_name = max_entity_name

    @property
    def min_entity_display_name(self):
        """
        Gets the min_entity_display_name of this ApiTimeSeriesCrossEntityMetadata.
        The display name of the entity that had the minimum value for the cross-entity aggregate metric.

        :return: The min_entity_display_name of this ApiTimeSeriesCrossEntityMetadata.
        :rtype: str
        """
        return self._min_entity_display_name

    @min_entity_display_name.setter
    def min_entity_display_name(self, min_entity_display_name):
        """
        Sets the min_entity_display_name of this ApiTimeSeriesCrossEntityMetadata.
        The display name of the entity that had the minimum value for the cross-entity aggregate metric.

        :param min_entity_display_name: The min_entity_display_name of this ApiTimeSeriesCrossEntityMetadata.
        :type: str
        """

        self._min_entity_display_name = min_entity_display_name

    @property
    def min_entity_name(self):
        """
        Gets the min_entity_name of this ApiTimeSeriesCrossEntityMetadata.
        The name of the entity that had the minimum value for the cross-entity aggregate metric. <p> Available since API v11.

        :return: The min_entity_name of this ApiTimeSeriesCrossEntityMetadata.
        :rtype: str
        """
        return self._min_entity_name

    @min_entity_name.setter
    def min_entity_name(self, min_entity_name):
        """
        Sets the min_entity_name of this ApiTimeSeriesCrossEntityMetadata.
        The name of the entity that had the minimum value for the cross-entity aggregate metric. <p> Available since API v11.

        :param min_entity_name: The min_entity_name of this ApiTimeSeriesCrossEntityMetadata.
        :type: str
        """

        self._min_entity_name = min_entity_name

    @property
    def num_entities(self):
        """
        Gets the num_entities of this ApiTimeSeriesCrossEntityMetadata.
        The number of entities covered by this point. For a raw cross-entity point this number is exact. For a rollup point this number is an average, since the number of entities being aggregated can change over the aggregation period.

        :return: The num_entities of this ApiTimeSeriesCrossEntityMetadata.
        :rtype: float
        """
        return self._num_entities

    @num_entities.setter
    def num_entities(self, num_entities):
        """
        Sets the num_entities of this ApiTimeSeriesCrossEntityMetadata.
        The number of entities covered by this point. For a raw cross-entity point this number is exact. For a rollup point this number is an average, since the number of entities being aggregated can change over the aggregation period.

        :param num_entities: The num_entities of this ApiTimeSeriesCrossEntityMetadata.
        :type: float
        """

        self._num_entities = num_entities

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
        if not isinstance(other, ApiTimeSeriesCrossEntityMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
