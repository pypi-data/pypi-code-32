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


class CreateSubmissionData(object):
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
        'test': 'bool',
        'data': 'object',
        'html': 'str',
        'css': 'str',
        'metadata': 'object',
        'data_requests': 'list[CreateSubmissionDataRequestData]'
    }

    attribute_map = {
        'test': 'test',
        'data': 'data',
        'html': 'html',
        'css': 'css',
        'metadata': 'metadata',
        'data_requests': 'data_requests'
    }

    def __init__(self, test=None, data=None, html=None, css=None, metadata=None, data_requests=None):  # noqa: E501
        """CreateSubmissionData - a model defined in OpenAPI"""  # noqa: E501

        self._test = None
        self._data = None
        self._html = None
        self._css = None
        self._metadata = None
        self._data_requests = None
        self.discriminator = None

        if test is not None:
            self.test = test
        self.data = data
        if html is not None:
            self.html = html
        if css is not None:
            self.css = css
        if metadata is not None:
            self.metadata = metadata
        if data_requests is not None:
            self.data_requests = data_requests

    @property
    def test(self):
        """Gets the test of this CreateSubmissionData.  # noqa: E501


        :return: The test of this CreateSubmissionData.  # noqa: E501
        :rtype: bool
        """
        return self._test

    @test.setter
    def test(self, test):
        """Sets the test of this CreateSubmissionData.


        :param test: The test of this CreateSubmissionData.  # noqa: E501
        :type: bool
        """

        self._test = test

    @property
    def data(self):
        """Gets the data of this CreateSubmissionData.  # noqa: E501


        :return: The data of this CreateSubmissionData.  # noqa: E501
        :rtype: object
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this CreateSubmissionData.


        :param data: The data of this CreateSubmissionData.  # noqa: E501
        :type: object
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

    @property
    def html(self):
        """Gets the html of this CreateSubmissionData.  # noqa: E501


        :return: The html of this CreateSubmissionData.  # noqa: E501
        :rtype: str
        """
        return self._html

    @html.setter
    def html(self, html):
        """Sets the html of this CreateSubmissionData.


        :param html: The html of this CreateSubmissionData.  # noqa: E501
        :type: str
        """

        self._html = html

    @property
    def css(self):
        """Gets the css of this CreateSubmissionData.  # noqa: E501


        :return: The css of this CreateSubmissionData.  # noqa: E501
        :rtype: str
        """
        return self._css

    @css.setter
    def css(self, css):
        """Sets the css of this CreateSubmissionData.


        :param css: The css of this CreateSubmissionData.  # noqa: E501
        :type: str
        """

        self._css = css

    @property
    def metadata(self):
        """Gets the metadata of this CreateSubmissionData.  # noqa: E501


        :return: The metadata of this CreateSubmissionData.  # noqa: E501
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this CreateSubmissionData.


        :param metadata: The metadata of this CreateSubmissionData.  # noqa: E501
        :type: object
        """

        self._metadata = metadata

    @property
    def data_requests(self):
        """Gets the data_requests of this CreateSubmissionData.  # noqa: E501


        :return: The data_requests of this CreateSubmissionData.  # noqa: E501
        :rtype: list[CreateSubmissionDataRequestData]
        """
        return self._data_requests

    @data_requests.setter
    def data_requests(self, data_requests):
        """Sets the data_requests of this CreateSubmissionData.


        :param data_requests: The data_requests of this CreateSubmissionData.  # noqa: E501
        :type: list[CreateSubmissionDataRequestData]
        """

        self._data_requests = data_requests

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
        if not isinstance(other, CreateSubmissionData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
