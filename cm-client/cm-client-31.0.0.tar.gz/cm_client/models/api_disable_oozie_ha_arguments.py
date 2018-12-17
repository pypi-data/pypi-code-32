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


class ApiDisableOozieHaArguments(object):
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
        'active_name': 'str'
    }

    attribute_map = {
        'active_name': 'activeName'
    }

    def __init__(self, active_name=None):
        """
        ApiDisableOozieHaArguments - a model defined in Swagger
        """

        self._active_name = None

        if active_name is not None:
          self.active_name = active_name

    @property
    def active_name(self):
        """
        Gets the active_name of this ApiDisableOozieHaArguments.
        Name of the Oozie Server that will be active after HA is disabled.

        :return: The active_name of this ApiDisableOozieHaArguments.
        :rtype: str
        """
        return self._active_name

    @active_name.setter
    def active_name(self, active_name):
        """
        Sets the active_name of this ApiDisableOozieHaArguments.
        Name of the Oozie Server that will be active after HA is disabled.

        :param active_name: The active_name of this ApiDisableOozieHaArguments.
        :type: str
        """

        self._active_name = active_name

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
        if not isinstance(other, ApiDisableOozieHaArguments):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
