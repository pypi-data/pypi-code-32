# coding: utf-8

"""
    Marketing API v.1.0

    IMPORTANT: This swagger links to Criteo production environment. Any test applied here will thus impact real campaigns.  # noqa: E501

    OpenAPI spec version: v.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class SellerBidInfoMessage(object):
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
        'seller_name': 'str',
        'bid': 'float'
    }

    attribute_map = {
        'seller_name': 'sellerName',
        'bid': 'bid'
    }

    def __init__(self, seller_name=None, bid=None):  # noqa: E501
        """SellerBidInfoMessage - a model defined in OpenAPI"""  # noqa: E501

        self._seller_name = None
        self._bid = None
        self.discriminator = None

        if seller_name is not None:
            self.seller_name = seller_name
        if bid is not None:
            self.bid = bid

    @property
    def seller_name(self):
        """Gets the seller_name of this SellerBidInfoMessage.  # noqa: E501

        Seller name is case insensitive.  # noqa: E501

        :return: The seller_name of this SellerBidInfoMessage.  # noqa: E501
        :rtype: str
        """
        return self._seller_name

    @seller_name.setter
    def seller_name(self, seller_name):
        """Sets the seller_name of this SellerBidInfoMessage.

        Seller name is case insensitive.  # noqa: E501

        :param seller_name: The seller_name of this SellerBidInfoMessage.  # noqa: E501
        :type: str
        """

        self._seller_name = seller_name

    @property
    def bid(self):
        """Gets the bid of this SellerBidInfoMessage.  # noqa: E501

        New bid.  # noqa: E501

        :return: The bid of this SellerBidInfoMessage.  # noqa: E501
        :rtype: float
        """
        return self._bid

    @bid.setter
    def bid(self, bid):
        """Sets the bid of this SellerBidInfoMessage.

        New bid.  # noqa: E501

        :param bid: The bid of this SellerBidInfoMessage.  # noqa: E501
        :type: float
        """

        self._bid = bid

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
        if not isinstance(other, SellerBidInfoMessage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
