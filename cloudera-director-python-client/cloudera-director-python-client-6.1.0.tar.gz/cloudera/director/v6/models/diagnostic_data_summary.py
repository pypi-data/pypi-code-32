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


class DiagnosticDataSummary(object):
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
        'status': 'str',
        'collection_time': 'int',
        'local_file_path': 'str',
        'details': 'list[str]',
        'diagnostic_data_collected': 'bool',
        'diagnostic_data_downloaded': 'bool',
        'cloudera_manager_logs_downloaded': 'bool'
    }

    attribute_map = {
        'status': 'status',
        'collection_time': 'collectionTime',
        'local_file_path': 'localFilePath',
        'details': 'details',
        'diagnostic_data_collected': 'diagnosticDataCollected',
        'diagnostic_data_downloaded': 'diagnosticDataDownloaded',
        'cloudera_manager_logs_downloaded': 'clouderaManagerLogsDownloaded'
    }

    def __init__(self, status=None, collection_time=None, local_file_path=None, details=None, diagnostic_data_collected=None, diagnostic_data_downloaded=None, cloudera_manager_logs_downloaded=None):  # noqa: E501
        """DiagnosticDataSummary - a model defined in Swagger"""  # noqa: E501

        self._status = None
        self._collection_time = None
        self._local_file_path = None
        self._details = None
        self._diagnostic_data_collected = None
        self._diagnostic_data_downloaded = None
        self._cloudera_manager_logs_downloaded = None
        self.discriminator = None

        self.status = status
        self.collection_time = collection_time
        if local_file_path is not None:
            self.local_file_path = local_file_path
        if details is not None:
            self.details = details
        if diagnostic_data_collected is not None:
            self.diagnostic_data_collected = diagnostic_data_collected
        if diagnostic_data_downloaded is not None:
            self.diagnostic_data_downloaded = diagnostic_data_downloaded
        if cloudera_manager_logs_downloaded is not None:
            self.cloudera_manager_logs_downloaded = cloudera_manager_logs_downloaded

    @property
    def status(self):
        """Gets the status of this DiagnosticDataSummary.  # noqa: E501

        Status of the collection effort  # noqa: E501

        :return: The status of this DiagnosticDataSummary.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DiagnosticDataSummary.

        Status of the collection effort  # noqa: E501

        :param status: The status of this DiagnosticDataSummary.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["COLLECTING", "READY", "FAILED"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def collection_time(self):
        """Gets the collection_time of this DiagnosticDataSummary.  # noqa: E501

        Time of collection  # noqa: E501

        :return: The collection_time of this DiagnosticDataSummary.  # noqa: E501
        :rtype: int
        """
        return self._collection_time

    @collection_time.setter
    def collection_time(self, collection_time):
        """Sets the collection_time of this DiagnosticDataSummary.

        Time of collection  # noqa: E501

        :param collection_time: The collection_time of this DiagnosticDataSummary.  # noqa: E501
        :type: int
        """
        if collection_time is None:
            raise ValueError("Invalid value for `collection_time`, must not be `None`")  # noqa: E501

        self._collection_time = collection_time

    @property
    def local_file_path(self):
        """Gets the local_file_path of this DiagnosticDataSummary.  # noqa: E501

        Local path to the diagnostic data file  # noqa: E501

        :return: The local_file_path of this DiagnosticDataSummary.  # noqa: E501
        :rtype: str
        """
        return self._local_file_path

    @local_file_path.setter
    def local_file_path(self, local_file_path):
        """Sets the local_file_path of this DiagnosticDataSummary.

        Local path to the diagnostic data file  # noqa: E501

        :param local_file_path: The local_file_path of this DiagnosticDataSummary.  # noqa: E501
        :type: str
        """

        self._local_file_path = local_file_path

    @property
    def details(self):
        """Gets the details of this DiagnosticDataSummary.  # noqa: E501

        Details on the collection effort  # noqa: E501

        :return: The details of this DiagnosticDataSummary.  # noqa: E501
        :rtype: list[str]
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this DiagnosticDataSummary.

        Details on the collection effort  # noqa: E501

        :param details: The details of this DiagnosticDataSummary.  # noqa: E501
        :type: list[str]
        """

        self._details = details

    @property
    def diagnostic_data_collected(self):
        """Gets the diagnostic_data_collected of this DiagnosticDataSummary.  # noqa: E501

        Whether diagnostic data was collected successfully by Cloudera Manager  # noqa: E501

        :return: The diagnostic_data_collected of this DiagnosticDataSummary.  # noqa: E501
        :rtype: bool
        """
        return self._diagnostic_data_collected

    @diagnostic_data_collected.setter
    def diagnostic_data_collected(self, diagnostic_data_collected):
        """Sets the diagnostic_data_collected of this DiagnosticDataSummary.

        Whether diagnostic data was collected successfully by Cloudera Manager  # noqa: E501

        :param diagnostic_data_collected: The diagnostic_data_collected of this DiagnosticDataSummary.  # noqa: E501
        :type: bool
        """

        self._diagnostic_data_collected = diagnostic_data_collected

    @property
    def diagnostic_data_downloaded(self):
        """Gets the diagnostic_data_downloaded of this DiagnosticDataSummary.  # noqa: E501

        Whether diagnostic data was downloaded successfully from Cloudera Manager  # noqa: E501

        :return: The diagnostic_data_downloaded of this DiagnosticDataSummary.  # noqa: E501
        :rtype: bool
        """
        return self._diagnostic_data_downloaded

    @diagnostic_data_downloaded.setter
    def diagnostic_data_downloaded(self, diagnostic_data_downloaded):
        """Sets the diagnostic_data_downloaded of this DiagnosticDataSummary.

        Whether diagnostic data was downloaded successfully from Cloudera Manager  # noqa: E501

        :param diagnostic_data_downloaded: The diagnostic_data_downloaded of this DiagnosticDataSummary.  # noqa: E501
        :type: bool
        """

        self._diagnostic_data_downloaded = diagnostic_data_downloaded

    @property
    def cloudera_manager_logs_downloaded(self):
        """Gets the cloudera_manager_logs_downloaded of this DiagnosticDataSummary.  # noqa: E501

        Whether Cloudera Manager logs were also downloaded from Cloudera Manager  # noqa: E501

        :return: The cloudera_manager_logs_downloaded of this DiagnosticDataSummary.  # noqa: E501
        :rtype: bool
        """
        return self._cloudera_manager_logs_downloaded

    @cloudera_manager_logs_downloaded.setter
    def cloudera_manager_logs_downloaded(self, cloudera_manager_logs_downloaded):
        """Sets the cloudera_manager_logs_downloaded of this DiagnosticDataSummary.

        Whether Cloudera Manager logs were also downloaded from Cloudera Manager  # noqa: E501

        :param cloudera_manager_logs_downloaded: The cloudera_manager_logs_downloaded of this DiagnosticDataSummary.  # noqa: E501
        :type: bool
        """

        self._cloudera_manager_logs_downloaded = cloudera_manager_logs_downloaded

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
        if not isinstance(other, DiagnosticDataSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
