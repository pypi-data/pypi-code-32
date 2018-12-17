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


class Status(object):
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
        'stage': 'str',
        'description': 'str',
        'description_details': 'list[str]',
        'remaining_steps': 'int',
        'completed_steps': 'int',
        'health': 'Health',
        'diagnostic_data_summaries': 'list[DiagnosticDataSummary]'
    }

    attribute_map = {
        'stage': 'stage',
        'description': 'description',
        'description_details': 'descriptionDetails',
        'remaining_steps': 'remainingSteps',
        'completed_steps': 'completedSteps',
        'health': 'health',
        'diagnostic_data_summaries': 'diagnosticDataSummaries'
    }

    def __init__(self, stage=None, description=None, description_details=None, remaining_steps=None, completed_steps=None, health=None, diagnostic_data_summaries=None):  # noqa: E501
        """Status - a model defined in Swagger"""  # noqa: E501

        self._stage = None
        self._description = None
        self._description_details = None
        self._remaining_steps = None
        self._completed_steps = None
        self._health = None
        self._diagnostic_data_summaries = None
        self.discriminator = None

        self.stage = stage
        self.description = description
        if description_details is not None:
            self.description_details = description_details
        self.remaining_steps = remaining_steps
        self.completed_steps = completed_steps
        self.health = health
        if diagnostic_data_summaries is not None:
            self.diagnostic_data_summaries = diagnostic_data_summaries

    @property
    def stage(self):
        """Gets the stage of this Status.  # noqa: E501

        Current stage of the process  # noqa: E501

        :return: The stage of this Status.  # noqa: E501
        :rtype: str
        """
        return self._stage

    @stage.setter
    def stage(self, stage):
        """Sets the stage of this Status.

        Current stage of the process  # noqa: E501

        :param stage: The stage of this Status.  # noqa: E501
        :type: str
        """
        if stage is None:
            raise ValueError("Invalid value for `stage`, must not be `None`")  # noqa: E501
        allowed_values = ["BOOTSTRAPPING", "BOOTSTRAP_FAILED", "READY", "UPDATING", "UPDATE_FAILED", "TERMINATING", "TERMINATE_FAILED", "TERMINATED", "UNKNOWN"]  # noqa: E501
        if stage not in allowed_values:
            raise ValueError(
                "Invalid value for `stage` ({0}), must be one of {1}"  # noqa: E501
                .format(stage, allowed_values)
            )

        self._stage = stage

    @property
    def description(self):
        """Gets the description of this Status.  # noqa: E501

        Status description  # noqa: E501

        :return: The description of this Status.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Status.

        Status description  # noqa: E501

        :param description: The description of this Status.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def description_details(self):
        """Gets the description_details of this Status.  # noqa: E501

        Detailed status description  # noqa: E501

        :return: The description_details of this Status.  # noqa: E501
        :rtype: list[str]
        """
        return self._description_details

    @description_details.setter
    def description_details(self, description_details):
        """Sets the description_details of this Status.

        Detailed status description  # noqa: E501

        :param description_details: The description_details of this Status.  # noqa: E501
        :type: list[str]
        """

        self._description_details = description_details

    @property
    def remaining_steps(self):
        """Gets the remaining_steps of this Status.  # noqa: E501

        Number of remaining steps planned for the process  # noqa: E501

        :return: The remaining_steps of this Status.  # noqa: E501
        :rtype: int
        """
        return self._remaining_steps

    @remaining_steps.setter
    def remaining_steps(self, remaining_steps):
        """Sets the remaining_steps of this Status.

        Number of remaining steps planned for the process  # noqa: E501

        :param remaining_steps: The remaining_steps of this Status.  # noqa: E501
        :type: int
        """
        if remaining_steps is None:
            raise ValueError("Invalid value for `remaining_steps`, must not be `None`")  # noqa: E501

        self._remaining_steps = remaining_steps

    @property
    def completed_steps(self):
        """Gets the completed_steps of this Status.  # noqa: E501

        Number of steps completed for the process  # noqa: E501

        :return: The completed_steps of this Status.  # noqa: E501
        :rtype: int
        """
        return self._completed_steps

    @completed_steps.setter
    def completed_steps(self, completed_steps):
        """Sets the completed_steps of this Status.

        Number of steps completed for the process  # noqa: E501

        :param completed_steps: The completed_steps of this Status.  # noqa: E501
        :type: int
        """
        if completed_steps is None:
            raise ValueError("Invalid value for `completed_steps`, must not be `None`")  # noqa: E501

        self._completed_steps = completed_steps

    @property
    def health(self):
        """Gets the health of this Status.  # noqa: E501

        Health reported for the entity being processed  # noqa: E501

        :return: The health of this Status.  # noqa: E501
        :rtype: Health
        """
        return self._health

    @health.setter
    def health(self, health):
        """Sets the health of this Status.

        Health reported for the entity being processed  # noqa: E501

        :param health: The health of this Status.  # noqa: E501
        :type: Health
        """
        if health is None:
            raise ValueError("Invalid value for `health`, must not be `None`")  # noqa: E501

        self._health = health

    @property
    def diagnostic_data_summaries(self):
        """Gets the diagnostic_data_summaries of this Status.  # noqa: E501

        Diagnostic data summaries  # noqa: E501

        :return: The diagnostic_data_summaries of this Status.  # noqa: E501
        :rtype: list[DiagnosticDataSummary]
        """
        return self._diagnostic_data_summaries

    @diagnostic_data_summaries.setter
    def diagnostic_data_summaries(self, diagnostic_data_summaries):
        """Sets the diagnostic_data_summaries of this Status.

        Diagnostic data summaries  # noqa: E501

        :param diagnostic_data_summaries: The diagnostic_data_summaries of this Status.  # noqa: E501
        :type: list[DiagnosticDataSummary]
        """

        self._diagnostic_data_summaries = diagnostic_data_summaries

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
        if not isinstance(other, Status):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
