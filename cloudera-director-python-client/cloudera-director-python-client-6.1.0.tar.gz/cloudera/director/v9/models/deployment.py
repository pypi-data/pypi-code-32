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


class Deployment(object):
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
        'name': 'str',
        'hostname': 'str',
        'port': 'int',
        'username': 'str',
        'password': 'str',
        'manager_instance': 'Instance',
        'repository': 'str',
        'repository_key_url': 'str',
        'enable_enterprise_trial': 'bool',
        'unlimited_jce': 'bool',
        'krb_admin_username': 'str',
        'krb_admin_password': 'str',
        'java_installation_strategy': 'str',
        'cm_version': 'str'
    }

    attribute_map = {
        'name': 'name',
        'hostname': 'hostname',
        'port': 'port',
        'username': 'username',
        'password': 'password',
        'manager_instance': 'managerInstance',
        'repository': 'repository',
        'repository_key_url': 'repositoryKeyUrl',
        'enable_enterprise_trial': 'enableEnterpriseTrial',
        'unlimited_jce': 'unlimitedJce',
        'krb_admin_username': 'krbAdminUsername',
        'krb_admin_password': 'krbAdminPassword',
        'java_installation_strategy': 'javaInstallationStrategy',
        'cm_version': 'cmVersion'
    }

    def __init__(self, name=None, hostname=None, port=None, username=None, password=None, manager_instance=None, repository=None, repository_key_url=None, enable_enterprise_trial=None, unlimited_jce=None, krb_admin_username=None, krb_admin_password=None, java_installation_strategy=None, cm_version=None):  # noqa: E501
        """Deployment - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._hostname = None
        self._port = None
        self._username = None
        self._password = None
        self._manager_instance = None
        self._repository = None
        self._repository_key_url = None
        self._enable_enterprise_trial = None
        self._unlimited_jce = None
        self._krb_admin_username = None
        self._krb_admin_password = None
        self._java_installation_strategy = None
        self._cm_version = None
        self.discriminator = None

        self.name = name
        if hostname is not None:
            self.hostname = hostname
        if port is not None:
            self.port = port
        if username is not None:
            self.username = username
        if password is not None:
            self.password = password
        if manager_instance is not None:
            self.manager_instance = manager_instance
        if repository is not None:
            self.repository = repository
        if repository_key_url is not None:
            self.repository_key_url = repository_key_url
        if enable_enterprise_trial is not None:
            self.enable_enterprise_trial = enable_enterprise_trial
        if unlimited_jce is not None:
            self.unlimited_jce = unlimited_jce
        if krb_admin_username is not None:
            self.krb_admin_username = krb_admin_username
        if krb_admin_password is not None:
            self.krb_admin_password = krb_admin_password
        if java_installation_strategy is not None:
            self.java_installation_strategy = java_installation_strategy
        if cm_version is not None:
            self.cm_version = cm_version

    @property
    def name(self):
        """Gets the name of this Deployment.  # noqa: E501

        Deployment name  # noqa: E501

        :return: The name of this Deployment.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Deployment.

        Deployment name  # noqa: E501

        :param name: The name of this Deployment.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def hostname(self):
        """Gets the hostname of this Deployment.  # noqa: E501

        Hostname for existing Cloudera Manager installation  # noqa: E501

        :return: The hostname of this Deployment.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this Deployment.

        Hostname for existing Cloudera Manager installation  # noqa: E501

        :param hostname: The hostname of this Deployment.  # noqa: E501
        :type: str
        """

        self._hostname = hostname

    @property
    def port(self):
        """Gets the port of this Deployment.  # noqa: E501

        API port for an existing Cloudera Manager installation  # noqa: E501

        :return: The port of this Deployment.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this Deployment.

        API port for an existing Cloudera Manager installation  # noqa: E501

        :param port: The port of this Deployment.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def username(self):
        """Gets the username of this Deployment.  # noqa: E501

        Username for API access  # noqa: E501

        :return: The username of this Deployment.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this Deployment.

        Username for API access  # noqa: E501

        :param username: The username of this Deployment.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def password(self):
        """Gets the password of this Deployment.  # noqa: E501

        Password for API access [redacted on read]  # noqa: E501

        :return: The password of this Deployment.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this Deployment.

        Password for API access [redacted on read]  # noqa: E501

        :param password: The password of this Deployment.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def manager_instance(self):
        """Gets the manager_instance of this Deployment.  # noqa: E501

        Instance where Cloudera Manager is installed  # noqa: E501

        :return: The manager_instance of this Deployment.  # noqa: E501
        :rtype: Instance
        """
        return self._manager_instance

    @manager_instance.setter
    def manager_instance(self, manager_instance):
        """Sets the manager_instance of this Deployment.

        Instance where Cloudera Manager is installed  # noqa: E501

        :param manager_instance: The manager_instance of this Deployment.  # noqa: E501
        :type: Instance
        """

        self._manager_instance = manager_instance

    @property
    def repository(self):
        """Gets the repository of this Deployment.  # noqa: E501

        Custom Cloudera Manager repository URL  # noqa: E501

        :return: The repository of this Deployment.  # noqa: E501
        :rtype: str
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        """Sets the repository of this Deployment.

        Custom Cloudera Manager repository URL  # noqa: E501

        :param repository: The repository of this Deployment.  # noqa: E501
        :type: str
        """

        self._repository = repository

    @property
    def repository_key_url(self):
        """Gets the repository_key_url of this Deployment.  # noqa: E501

        Custom Cloudera Manager public GPG key  # noqa: E501

        :return: The repository_key_url of this Deployment.  # noqa: E501
        :rtype: str
        """
        return self._repository_key_url

    @repository_key_url.setter
    def repository_key_url(self, repository_key_url):
        """Sets the repository_key_url of this Deployment.

        Custom Cloudera Manager public GPG key  # noqa: E501

        :param repository_key_url: The repository_key_url of this Deployment.  # noqa: E501
        :type: str
        """

        self._repository_key_url = repository_key_url

    @property
    def enable_enterprise_trial(self):
        """Gets the enable_enterprise_trial of this Deployment.  # noqa: E501

        Whether to enable Cloudera Enterprise Trial  # noqa: E501

        :return: The enable_enterprise_trial of this Deployment.  # noqa: E501
        :rtype: bool
        """
        return self._enable_enterprise_trial

    @enable_enterprise_trial.setter
    def enable_enterprise_trial(self, enable_enterprise_trial):
        """Sets the enable_enterprise_trial of this Deployment.

        Whether to enable Cloudera Enterprise Trial  # noqa: E501

        :param enable_enterprise_trial: The enable_enterprise_trial of this Deployment.  # noqa: E501
        :type: bool
        """

        self._enable_enterprise_trial = enable_enterprise_trial

    @property
    def unlimited_jce(self):
        """Gets the unlimited_jce of this Deployment.  # noqa: E501

        Whether to install unlimited strength JCE policy files  # noqa: E501

        :return: The unlimited_jce of this Deployment.  # noqa: E501
        :rtype: bool
        """
        return self._unlimited_jce

    @unlimited_jce.setter
    def unlimited_jce(self, unlimited_jce):
        """Sets the unlimited_jce of this Deployment.

        Whether to install unlimited strength JCE policy files  # noqa: E501

        :param unlimited_jce: The unlimited_jce of this Deployment.  # noqa: E501
        :type: bool
        """

        self._unlimited_jce = unlimited_jce

    @property
    def krb_admin_username(self):
        """Gets the krb_admin_username of this Deployment.  # noqa: E501

        Username for Kerberos administrative principal used by Cloudera Manager  # noqa: E501

        :return: The krb_admin_username of this Deployment.  # noqa: E501
        :rtype: str
        """
        return self._krb_admin_username

    @krb_admin_username.setter
    def krb_admin_username(self, krb_admin_username):
        """Sets the krb_admin_username of this Deployment.

        Username for Kerberos administrative principal used by Cloudera Manager  # noqa: E501

        :param krb_admin_username: The krb_admin_username of this Deployment.  # noqa: E501
        :type: str
        """

        self._krb_admin_username = krb_admin_username

    @property
    def krb_admin_password(self):
        """Gets the krb_admin_password of this Deployment.  # noqa: E501

        Password for Kerberos administrative principal used by Cloudera Manager [redacted on read]  # noqa: E501

        :return: The krb_admin_password of this Deployment.  # noqa: E501
        :rtype: str
        """
        return self._krb_admin_password

    @krb_admin_password.setter
    def krb_admin_password(self, krb_admin_password):
        """Sets the krb_admin_password of this Deployment.

        Password for Kerberos administrative principal used by Cloudera Manager [redacted on read]  # noqa: E501

        :param krb_admin_password: The krb_admin_password of this Deployment.  # noqa: E501
        :type: str
        """

        self._krb_admin_password = krb_admin_password

    @property
    def java_installation_strategy(self):
        """Gets the java_installation_strategy of this Deployment.  # noqa: E501

        Cloudera Altus Director and Cloudera Manager's Java installation strategy  # noqa: E501

        :return: The java_installation_strategy of this Deployment.  # noqa: E501
        :rtype: str
        """
        return self._java_installation_strategy

    @java_installation_strategy.setter
    def java_installation_strategy(self, java_installation_strategy):
        """Sets the java_installation_strategy of this Deployment.

        Cloudera Altus Director and Cloudera Manager's Java installation strategy  # noqa: E501

        :param java_installation_strategy: The java_installation_strategy of this Deployment.  # noqa: E501
        :type: str
        """
        allowed_values = ["AUTO", "NONE", "DIRECTOR_MANAGED"]  # noqa: E501
        if java_installation_strategy not in allowed_values:
            raise ValueError(
                "Invalid value for `java_installation_strategy` ({0}), must be one of {1}"  # noqa: E501
                .format(java_installation_strategy, allowed_values)
            )

        self._java_installation_strategy = java_installation_strategy

    @property
    def cm_version(self):
        """Gets the cm_version of this Deployment.  # noqa: E501

        Cloudera Manager Version  # noqa: E501

        :return: The cm_version of this Deployment.  # noqa: E501
        :rtype: str
        """
        return self._cm_version

    @cm_version.setter
    def cm_version(self, cm_version):
        """Sets the cm_version of this Deployment.

        Cloudera Manager Version  # noqa: E501

        :param cm_version: The cm_version of this Deployment.  # noqa: E501
        :type: str
        """

        self._cm_version = cm_version

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
        if not isinstance(other, Deployment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
