# coding: utf-8

"""
    VXC Services API

    API for methods pertaining to all VXC services  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class VehicleFinanceDetails(object):
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
        'balance': 'float',
        'end_date': 'date',
        'start_date': 'date',
        'title': 'bool'
    }

    attribute_map = {
        'balance': 'balance',
        'end_date': 'endDate',
        'start_date': 'startDate',
        'title': 'title'
    }

    def __init__(self, balance=None, end_date=None, start_date=None, title=None):  # noqa: E501
        """VehicleFinanceDetails - a model defined in Swagger"""  # noqa: E501

        self._balance = None
        self._end_date = None
        self._start_date = None
        self._title = None
        self.discriminator = None

        if balance is not None:
            self.balance = balance
        self.end_date = end_date
        self.start_date = start_date
        if title is not None:
            self.title = title

    @property
    def balance(self):
        """Gets the balance of this VehicleFinanceDetails.  # noqa: E501

        the amount owed/financed in the portfolio transaction  # noqa: E501

        :return: The balance of this VehicleFinanceDetails.  # noqa: E501
        :rtype: float
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this VehicleFinanceDetails.

        the amount owed/financed in the portfolio transaction  # noqa: E501

        :param balance: The balance of this VehicleFinanceDetails.  # noqa: E501
        :type: float
        """

        self._balance = balance

    @property
    def end_date(self):
        """Gets the end_date of this VehicleFinanceDetails.  # noqa: E501

        Date financing ending  # noqa: E501

        :return: The end_date of this VehicleFinanceDetails.  # noqa: E501
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this VehicleFinanceDetails.

        Date financing ending  # noqa: E501

        :param end_date: The end_date of this VehicleFinanceDetails.  # noqa: E501
        :type: date
        """
        if end_date is None:
            raise ValueError("Invalid value for `end_date`, must not be `None`")  # noqa: E501

        self._end_date = end_date

    @property
    def start_date(self):
        """Gets the start_date of this VehicleFinanceDetails.  # noqa: E501

        Date financing began  # noqa: E501

        :return: The start_date of this VehicleFinanceDetails.  # noqa: E501
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this VehicleFinanceDetails.

        Date financing began  # noqa: E501

        :param start_date: The start_date of this VehicleFinanceDetails.  # noqa: E501
        :type: date
        """
        if start_date is None:
            raise ValueError("Invalid value for `start_date`, must not be `None`")  # noqa: E501

        self._start_date = start_date

    @property
    def title(self):
        """Gets the title of this VehicleFinanceDetails.  # noqa: E501

        The indication of whether or not the vehicle title is in your possession  # noqa: E501

        :return: The title of this VehicleFinanceDetails.  # noqa: E501
        :rtype: bool
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this VehicleFinanceDetails.

        The indication of whether or not the vehicle title is in your possession  # noqa: E501

        :param title: The title of this VehicleFinanceDetails.  # noqa: E501
        :type: bool
        """

        self._title = title

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
        if not isinstance(other, VehicleFinanceDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
