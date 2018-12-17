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


class SellerCampaignMessage(object):
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
        'campaign_id': 'int',
        'campaign_name': 'str',
        'advertiser_id': 'int',
        'campaign_status': 'str',
        'campaign_bid': 'BidMessage'
    }

    attribute_map = {
        'campaign_id': 'campaignId',
        'campaign_name': 'campaignName',
        'advertiser_id': 'advertiserId',
        'campaign_status': 'campaignStatus',
        'campaign_bid': 'campaignBid'
    }

    def __init__(self, campaign_id=None, campaign_name=None, advertiser_id=None, campaign_status=None, campaign_bid=None):  # noqa: E501
        """SellerCampaignMessage - a model defined in OpenAPI"""  # noqa: E501

        self._campaign_id = None
        self._campaign_name = None
        self._advertiser_id = None
        self._campaign_status = None
        self._campaign_bid = None
        self.discriminator = None

        if campaign_id is not None:
            self.campaign_id = campaign_id
        if campaign_name is not None:
            self.campaign_name = campaign_name
        if advertiser_id is not None:
            self.advertiser_id = advertiser_id
        if campaign_status is not None:
            self.campaign_status = campaign_status
        if campaign_bid is not None:
            self.campaign_bid = campaign_bid

    @property
    def campaign_id(self):
        """Gets the campaign_id of this SellerCampaignMessage.  # noqa: E501


        :return: The campaign_id of this SellerCampaignMessage.  # noqa: E501
        :rtype: int
        """
        return self._campaign_id

    @campaign_id.setter
    def campaign_id(self, campaign_id):
        """Sets the campaign_id of this SellerCampaignMessage.


        :param campaign_id: The campaign_id of this SellerCampaignMessage.  # noqa: E501
        :type: int
        """

        self._campaign_id = campaign_id

    @property
    def campaign_name(self):
        """Gets the campaign_name of this SellerCampaignMessage.  # noqa: E501


        :return: The campaign_name of this SellerCampaignMessage.  # noqa: E501
        :rtype: str
        """
        return self._campaign_name

    @campaign_name.setter
    def campaign_name(self, campaign_name):
        """Sets the campaign_name of this SellerCampaignMessage.


        :param campaign_name: The campaign_name of this SellerCampaignMessage.  # noqa: E501
        :type: str
        """

        self._campaign_name = campaign_name

    @property
    def advertiser_id(self):
        """Gets the advertiser_id of this SellerCampaignMessage.  # noqa: E501


        :return: The advertiser_id of this SellerCampaignMessage.  # noqa: E501
        :rtype: int
        """
        return self._advertiser_id

    @advertiser_id.setter
    def advertiser_id(self, advertiser_id):
        """Sets the advertiser_id of this SellerCampaignMessage.


        :param advertiser_id: The advertiser_id of this SellerCampaignMessage.  # noqa: E501
        :type: int
        """

        self._advertiser_id = advertiser_id

    @property
    def campaign_status(self):
        """Gets the campaign_status of this SellerCampaignMessage.  # noqa: E501


        :return: The campaign_status of this SellerCampaignMessage.  # noqa: E501
        :rtype: str
        """
        return self._campaign_status

    @campaign_status.setter
    def campaign_status(self, campaign_status):
        """Sets the campaign_status of this SellerCampaignMessage.


        :param campaign_status: The campaign_status of this SellerCampaignMessage.  # noqa: E501
        :type: str
        """
        allowed_values = ["Running", "Archived", "NotRunning"]  # noqa: E501
        if campaign_status not in allowed_values:
            print("Unknown value `campaign_status` [{0}]".format(campaign_status))

        self._campaign_status = campaign_status

    @property
    def campaign_bid(self):
        """Gets the campaign_bid of this SellerCampaignMessage.  # noqa: E501


        :return: The campaign_bid of this SellerCampaignMessage.  # noqa: E501
        :rtype: BidMessage
        """
        return self._campaign_bid

    @campaign_bid.setter
    def campaign_bid(self, campaign_bid):
        """Sets the campaign_bid of this SellerCampaignMessage.


        :param campaign_bid: The campaign_bid of this SellerCampaignMessage.  # noqa: E501
        :type: BidMessage
        """

        self._campaign_bid = campaign_bid

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
        if not isinstance(other, SellerCampaignMessage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
