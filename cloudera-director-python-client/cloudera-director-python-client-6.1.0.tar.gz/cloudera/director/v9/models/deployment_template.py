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


class DeploymentTemplate(object):
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
        'manager_virtual_instance': 'VirtualInstance',
        'external_database_templates': 'dict(str, ExternalDatabaseTemplate)',
        'external_databases': 'dict(str, ExternalDatabase)',
        'configs': 'dict(str, dict(str, str))',
        'external_accounts': 'dict(str, ExternalAccount)',
        'hostname': 'str',
        'port': 'int',
        'username': 'str',
        'password': 'str',
        'repository': 'str',
        'repository_key_url': 'str',
        'enable_enterprise_trial': 'bool',
        'unlimited_jce': 'bool',
        'krb_admin_username': 'str',
        'krb_admin_password': 'str',
        'java_installation_strategy': 'str',
        'license': 'str',
        'billing_id': 'str',
        'post_create_scripts': 'list[str]',
        'csds': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'manager_virtual_instance': 'managerVirtualInstance',
        'external_database_templates': 'externalDatabaseTemplates',
        'external_databases': 'externalDatabases',
        'configs': 'configs',
        'external_accounts': 'externalAccounts',
        'hostname': 'hostname',
        'port': 'port',
        'username': 'username',
        'password': 'password',
        'repository': 'repository',
        'repository_key_url': 'repositoryKeyUrl',
        'enable_enterprise_trial': 'enableEnterpriseTrial',
        'unlimited_jce': 'unlimitedJce',
        'krb_admin_username': 'krbAdminUsername',
        'krb_admin_password': 'krbAdminPassword',
        'java_installation_strategy': 'javaInstallationStrategy',
        'license': 'license',
        'billing_id': 'billingId',
        'post_create_scripts': 'postCreateScripts',
        'csds': 'csds'
    }

    def __init__(self, name=None, manager_virtual_instance=None, external_database_templates=None, external_databases=None, configs=None, external_accounts=None, hostname=None, port=None, username=None, password=None, repository=None, repository_key_url=None, enable_enterprise_trial=None, unlimited_jce=None, krb_admin_username=None, krb_admin_password=None, java_installation_strategy=None, license=None, billing_id=None, post_create_scripts=None, csds=None):  # noqa: E501
        """DeploymentTemplate - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._manager_virtual_instance = None
        self._external_database_templates = None
        self._external_databases = None
        self._configs = None
        self._external_accounts = None
        self._hostname = None
        self._port = None
        self._username = None
        self._password = None
        self._repository = None
        self._repository_key_url = None
        self._enable_enterprise_trial = None
        self._unlimited_jce = None
        self._krb_admin_username = None
        self._krb_admin_password = None
        self._java_installation_strategy = None
        self._license = None
        self._billing_id = None
        self._post_create_scripts = None
        self._csds = None
        self.discriminator = None

        self.name = name
        if manager_virtual_instance is not None:
            self.manager_virtual_instance = manager_virtual_instance
        if external_database_templates is not None:
            self.external_database_templates = external_database_templates
        if external_databases is not None:
            self.external_databases = external_databases
        if configs is not None:
            self.configs = configs
        if external_accounts is not None:
            self.external_accounts = external_accounts
        if hostname is not None:
            self.hostname = hostname
        if port is not None:
            self.port = port
        if username is not None:
            self.username = username
        if password is not None:
            self.password = password
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
        if license is not None:
            self.license = license
        if billing_id is not None:
            self.billing_id = billing_id
        if post_create_scripts is not None:
            self.post_create_scripts = post_create_scripts
        if csds is not None:
            self.csds = csds

    @property
    def name(self):
        """Gets the name of this DeploymentTemplate.  # noqa: E501

        Deployment name  # noqa: E501

        :return: The name of this DeploymentTemplate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DeploymentTemplate.

        Deployment name  # noqa: E501

        :param name: The name of this DeploymentTemplate.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def manager_virtual_instance(self):
        """Gets the manager_virtual_instance of this DeploymentTemplate.  # noqa: E501

        Instance definition for a Cloudera Manager instance created from scratch  # noqa: E501

        :return: The manager_virtual_instance of this DeploymentTemplate.  # noqa: E501
        :rtype: VirtualInstance
        """
        return self._manager_virtual_instance

    @manager_virtual_instance.setter
    def manager_virtual_instance(self, manager_virtual_instance):
        """Sets the manager_virtual_instance of this DeploymentTemplate.

        Instance definition for a Cloudera Manager instance created from scratch  # noqa: E501

        :param manager_virtual_instance: The manager_virtual_instance of this DeploymentTemplate.  # noqa: E501
        :type: VirtualInstance
        """

        self._manager_virtual_instance = manager_virtual_instance

    @property
    def external_database_templates(self):
        """Gets the external_database_templates of this DeploymentTemplate.  # noqa: E501

        External database template definitions  # noqa: E501

        :return: The external_database_templates of this DeploymentTemplate.  # noqa: E501
        :rtype: dict(str, ExternalDatabaseTemplate)
        """
        return self._external_database_templates

    @external_database_templates.setter
    def external_database_templates(self, external_database_templates):
        """Sets the external_database_templates of this DeploymentTemplate.

        External database template definitions  # noqa: E501

        :param external_database_templates: The external_database_templates of this DeploymentTemplate.  # noqa: E501
        :type: dict(str, ExternalDatabaseTemplate)
        """

        self._external_database_templates = external_database_templates

    @property
    def external_databases(self):
        """Gets the external_databases of this DeploymentTemplate.  # noqa: E501

        External database definitions  # noqa: E501

        :return: The external_databases of this DeploymentTemplate.  # noqa: E501
        :rtype: dict(str, ExternalDatabase)
        """
        return self._external_databases

    @external_databases.setter
    def external_databases(self, external_databases):
        """Sets the external_databases of this DeploymentTemplate.

        External database definitions  # noqa: E501

        :param external_databases: The external_databases of this DeploymentTemplate.  # noqa: E501
        :type: dict(str, ExternalDatabase)
        """

        self._external_databases = external_databases

    @property
    def configs(self):
        """Gets the configs of this DeploymentTemplate.  # noqa: E501

        Optional configurations for Cloudera Manager and its management services  # noqa: E501

        :return: The configs of this DeploymentTemplate.  # noqa: E501
        :rtype: dict(str, dict(str, str))
        """
        return self._configs

    @configs.setter
    def configs(self, configs):
        """Sets the configs of this DeploymentTemplate.

        Optional configurations for Cloudera Manager and its management services  # noqa: E501

        :param configs: The configs of this DeploymentTemplate.  # noqa: E501
        :type: dict(str, dict(str, str))
        """

        self._configs = configs

    @property
    def external_accounts(self):
        """Gets the external_accounts of this DeploymentTemplate.  # noqa: E501

        External account definitions  # noqa: E501

        :return: The external_accounts of this DeploymentTemplate.  # noqa: E501
        :rtype: dict(str, ExternalAccount)
        """
        return self._external_accounts

    @external_accounts.setter
    def external_accounts(self, external_accounts):
        """Sets the external_accounts of this DeploymentTemplate.

        External account definitions  # noqa: E501

        :param external_accounts: The external_accounts of this DeploymentTemplate.  # noqa: E501
        :type: dict(str, ExternalAccount)
        """

        self._external_accounts = external_accounts

    @property
    def hostname(self):
        """Gets the hostname of this DeploymentTemplate.  # noqa: E501

        Hostname for existing Cloudera Manager installation  # noqa: E501

        :return: The hostname of this DeploymentTemplate.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this DeploymentTemplate.

        Hostname for existing Cloudera Manager installation  # noqa: E501

        :param hostname: The hostname of this DeploymentTemplate.  # noqa: E501
        :type: str
        """

        self._hostname = hostname

    @property
    def port(self):
        """Gets the port of this DeploymentTemplate.  # noqa: E501

        Port for existing Cloudera Manager installation  # noqa: E501

        :return: The port of this DeploymentTemplate.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this DeploymentTemplate.

        Port for existing Cloudera Manager installation  # noqa: E501

        :param port: The port of this DeploymentTemplate.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def username(self):
        """Gets the username of this DeploymentTemplate.  # noqa: E501

        Web UI and API username  # noqa: E501

        :return: The username of this DeploymentTemplate.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this DeploymentTemplate.

        Web UI and API username  # noqa: E501

        :param username: The username of this DeploymentTemplate.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def password(self):
        """Gets the password of this DeploymentTemplate.  # noqa: E501

        Web UI and API password [redacted on read]  # noqa: E501

        :return: The password of this DeploymentTemplate.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this DeploymentTemplate.

        Web UI and API password [redacted on read]  # noqa: E501

        :param password: The password of this DeploymentTemplate.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def repository(self):
        """Gets the repository of this DeploymentTemplate.  # noqa: E501

        Custom Cloudera Manager repository URL  # noqa: E501

        :return: The repository of this DeploymentTemplate.  # noqa: E501
        :rtype: str
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        """Sets the repository of this DeploymentTemplate.

        Custom Cloudera Manager repository URL  # noqa: E501

        :param repository: The repository of this DeploymentTemplate.  # noqa: E501
        :type: str
        """

        self._repository = repository

    @property
    def repository_key_url(self):
        """Gets the repository_key_url of this DeploymentTemplate.  # noqa: E501

        Custom Cloudera Manager public GPG key  # noqa: E501

        :return: The repository_key_url of this DeploymentTemplate.  # noqa: E501
        :rtype: str
        """
        return self._repository_key_url

    @repository_key_url.setter
    def repository_key_url(self, repository_key_url):
        """Sets the repository_key_url of this DeploymentTemplate.

        Custom Cloudera Manager public GPG key  # noqa: E501

        :param repository_key_url: The repository_key_url of this DeploymentTemplate.  # noqa: E501
        :type: str
        """

        self._repository_key_url = repository_key_url

    @property
    def enable_enterprise_trial(self):
        """Gets the enable_enterprise_trial of this DeploymentTemplate.  # noqa: E501

        Whether to enable Cloudera Enterprise Trial  # noqa: E501

        :return: The enable_enterprise_trial of this DeploymentTemplate.  # noqa: E501
        :rtype: bool
        """
        return self._enable_enterprise_trial

    @enable_enterprise_trial.setter
    def enable_enterprise_trial(self, enable_enterprise_trial):
        """Sets the enable_enterprise_trial of this DeploymentTemplate.

        Whether to enable Cloudera Enterprise Trial  # noqa: E501

        :param enable_enterprise_trial: The enable_enterprise_trial of this DeploymentTemplate.  # noqa: E501
        :type: bool
        """

        self._enable_enterprise_trial = enable_enterprise_trial

    @property
    def unlimited_jce(self):
        """Gets the unlimited_jce of this DeploymentTemplate.  # noqa: E501

        Whether to install unlimited strength JCE policy files  # noqa: E501

        :return: The unlimited_jce of this DeploymentTemplate.  # noqa: E501
        :rtype: bool
        """
        return self._unlimited_jce

    @unlimited_jce.setter
    def unlimited_jce(self, unlimited_jce):
        """Sets the unlimited_jce of this DeploymentTemplate.

        Whether to install unlimited strength JCE policy files  # noqa: E501

        :param unlimited_jce: The unlimited_jce of this DeploymentTemplate.  # noqa: E501
        :type: bool
        """

        self._unlimited_jce = unlimited_jce

    @property
    def krb_admin_username(self):
        """Gets the krb_admin_username of this DeploymentTemplate.  # noqa: E501

        Username for Kerberos administrative principal used by Cloudera Manager  # noqa: E501

        :return: The krb_admin_username of this DeploymentTemplate.  # noqa: E501
        :rtype: str
        """
        return self._krb_admin_username

    @krb_admin_username.setter
    def krb_admin_username(self, krb_admin_username):
        """Sets the krb_admin_username of this DeploymentTemplate.

        Username for Kerberos administrative principal used by Cloudera Manager  # noqa: E501

        :param krb_admin_username: The krb_admin_username of this DeploymentTemplate.  # noqa: E501
        :type: str
        """

        self._krb_admin_username = krb_admin_username

    @property
    def krb_admin_password(self):
        """Gets the krb_admin_password of this DeploymentTemplate.  # noqa: E501

        Password for Kerberos administrative principal used by Cloudera Manager [redacted on read]  # noqa: E501

        :return: The krb_admin_password of this DeploymentTemplate.  # noqa: E501
        :rtype: str
        """
        return self._krb_admin_password

    @krb_admin_password.setter
    def krb_admin_password(self, krb_admin_password):
        """Sets the krb_admin_password of this DeploymentTemplate.

        Password for Kerberos administrative principal used by Cloudera Manager [redacted on read]  # noqa: E501

        :param krb_admin_password: The krb_admin_password of this DeploymentTemplate.  # noqa: E501
        :type: str
        """

        self._krb_admin_password = krb_admin_password

    @property
    def java_installation_strategy(self):
        """Gets the java_installation_strategy of this DeploymentTemplate.  # noqa: E501

        Cloudera Altus Director and Cloudera Manager's Java installation strategy  # noqa: E501

        :return: The java_installation_strategy of this DeploymentTemplate.  # noqa: E501
        :rtype: str
        """
        return self._java_installation_strategy

    @java_installation_strategy.setter
    def java_installation_strategy(self, java_installation_strategy):
        """Sets the java_installation_strategy of this DeploymentTemplate.

        Cloudera Altus Director and Cloudera Manager's Java installation strategy  # noqa: E501

        :param java_installation_strategy: The java_installation_strategy of this DeploymentTemplate.  # noqa: E501
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
    def license(self):
        """Gets the license of this DeploymentTemplate.  # noqa: E501

        License for Cloudera Manager [redacted on read]  # noqa: E501

        :return: The license of this DeploymentTemplate.  # noqa: E501
        :rtype: str
        """
        return self._license

    @license.setter
    def license(self, license):
        """Sets the license of this DeploymentTemplate.

        License for Cloudera Manager [redacted on read]  # noqa: E501

        :param license: The license of this DeploymentTemplate.  # noqa: E501
        :type: str
        """

        self._license = license

    @property
    def billing_id(self):
        """Gets the billing_id of this DeploymentTemplate.  # noqa: E501

        Billing ID for usage-based billing [redacted on read]  # noqa: E501

        :return: The billing_id of this DeploymentTemplate.  # noqa: E501
        :rtype: str
        """
        return self._billing_id

    @billing_id.setter
    def billing_id(self, billing_id):
        """Sets the billing_id of this DeploymentTemplate.

        Billing ID for usage-based billing [redacted on read]  # noqa: E501

        :param billing_id: The billing_id of this DeploymentTemplate.  # noqa: E501
        :type: str
        """

        self._billing_id = billing_id

    @property
    def post_create_scripts(self):
        """Gets the post_create_scripts of this DeploymentTemplate.  # noqa: E501

        A list of scripts to be run after deployment creation  # noqa: E501

        :return: The post_create_scripts of this DeploymentTemplate.  # noqa: E501
        :rtype: list[str]
        """
        return self._post_create_scripts

    @post_create_scripts.setter
    def post_create_scripts(self, post_create_scripts):
        """Sets the post_create_scripts of this DeploymentTemplate.

        A list of scripts to be run after deployment creation  # noqa: E501

        :param post_create_scripts: The post_create_scripts of this DeploymentTemplate.  # noqa: E501
        :type: list[str]
        """

        self._post_create_scripts = post_create_scripts

    @property
    def csds(self):
        """Gets the csds of this DeploymentTemplate.  # noqa: E501

        A list of CSD package URLs  # noqa: E501

        :return: The csds of this DeploymentTemplate.  # noqa: E501
        :rtype: list[str]
        """
        return self._csds

    @csds.setter
    def csds(self, csds):
        """Sets the csds of this DeploymentTemplate.

        A list of CSD package URLs  # noqa: E501

        :param csds: The csds of this DeploymentTemplate.  # noqa: E501
        :type: list[str]
        """

        self._csds = csds

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
        if not isinstance(other, DeploymentTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
