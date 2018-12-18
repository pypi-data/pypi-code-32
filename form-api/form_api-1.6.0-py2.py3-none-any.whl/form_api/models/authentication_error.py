# coding: utf-8

"""
    API v1

    FormAPI is a service that helps you fill out and sign PDF templates.  # noqa: E501

    OpenAPI spec version: v1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class AuthenticationError(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'status': 'str',
        'error': 'str'
    }

    attribute_map = {
        'status': 'status',
        'error': 'error'
    }

    def __init__(self, status=None, error=None):  # noqa: E501
        """AuthenticationError - a model defined in OpenAPI"""  # noqa: E501

        self._status = None
        self._error = None
        self.discriminator = None

        if status is not None:
            self.status = status
        self.error = error

    @property
    def status(self):
        """Gets the status of this AuthenticationError.  # noqa: E501


        :return: The status of this AuthenticationError.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AuthenticationError.


        :param status: The status of this AuthenticationError.  # noqa: E501
        :type: str
        """
        allowed_values = ["error"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def error(self):
        """Gets the error of this AuthenticationError.  # noqa: E501


        :return: The error of this AuthenticationError.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this AuthenticationError.


        :param error: The error of this AuthenticationError.  # noqa: E501
        :type: str
        """
        if error is None:
            raise ValueError("Invalid value for `error`, must not be `None`")  # noqa: E501

        self._error = error

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if not isinstance(other, AuthenticationError):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
