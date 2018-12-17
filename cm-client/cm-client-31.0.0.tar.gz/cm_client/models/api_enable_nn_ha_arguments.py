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


class ApiEnableNnHaArguments(object):
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
        'active_nn_name': 'str',
        'standby_nn_name': 'str',
        'standby_nn_host_id': 'str',
        'standby_name_dir_list': 'list[str]',
        'nameservice': 'str',
        'qj_name': 'str',
        'active_fc_name': 'str',
        'standby_fc_name': 'str',
        'zk_service_name': 'str',
        'jns': 'list[ApiJournalNodeArguments]',
        'force_init_z_node': 'bool',
        'clear_existing_standby_name_dirs': 'bool',
        'clear_existing_jn_edits_dir': 'bool'
    }

    attribute_map = {
        'active_nn_name': 'activeNnName',
        'standby_nn_name': 'standbyNnName',
        'standby_nn_host_id': 'standbyNnHostId',
        'standby_name_dir_list': 'standbyNameDirList',
        'nameservice': 'nameservice',
        'qj_name': 'qjName',
        'active_fc_name': 'activeFcName',
        'standby_fc_name': 'standbyFcName',
        'zk_service_name': 'zkServiceName',
        'jns': 'jns',
        'force_init_z_node': 'forceInitZNode',
        'clear_existing_standby_name_dirs': 'clearExistingStandbyNameDirs',
        'clear_existing_jn_edits_dir': 'clearExistingJnEditsDir'
    }

    def __init__(self, active_nn_name=None, standby_nn_name=None, standby_nn_host_id=None, standby_name_dir_list=None, nameservice=None, qj_name=None, active_fc_name=None, standby_fc_name=None, zk_service_name=None, jns=None, force_init_z_node=None, clear_existing_standby_name_dirs=None, clear_existing_jn_edits_dir=None):
        """
        ApiEnableNnHaArguments - a model defined in Swagger
        """

        self._active_nn_name = None
        self._standby_nn_name = None
        self._standby_nn_host_id = None
        self._standby_name_dir_list = None
        self._nameservice = None
        self._qj_name = None
        self._active_fc_name = None
        self._standby_fc_name = None
        self._zk_service_name = None
        self._jns = None
        self._force_init_z_node = None
        self._clear_existing_standby_name_dirs = None
        self._clear_existing_jn_edits_dir = None

        if active_nn_name is not None:
          self.active_nn_name = active_nn_name
        if standby_nn_name is not None:
          self.standby_nn_name = standby_nn_name
        if standby_nn_host_id is not None:
          self.standby_nn_host_id = standby_nn_host_id
        if standby_name_dir_list is not None:
          self.standby_name_dir_list = standby_name_dir_list
        if nameservice is not None:
          self.nameservice = nameservice
        if qj_name is not None:
          self.qj_name = qj_name
        if active_fc_name is not None:
          self.active_fc_name = active_fc_name
        if standby_fc_name is not None:
          self.standby_fc_name = standby_fc_name
        if zk_service_name is not None:
          self.zk_service_name = zk_service_name
        if jns is not None:
          self.jns = jns
        if force_init_z_node is not None:
          self.force_init_z_node = force_init_z_node
        if clear_existing_standby_name_dirs is not None:
          self.clear_existing_standby_name_dirs = clear_existing_standby_name_dirs
        if clear_existing_jn_edits_dir is not None:
          self.clear_existing_jn_edits_dir = clear_existing_jn_edits_dir

    @property
    def active_nn_name(self):
        """
        Gets the active_nn_name of this ApiEnableNnHaArguments.
        Name of the NameNode role that is going to be made Highly Available.

        :return: The active_nn_name of this ApiEnableNnHaArguments.
        :rtype: str
        """
        return self._active_nn_name

    @active_nn_name.setter
    def active_nn_name(self, active_nn_name):
        """
        Sets the active_nn_name of this ApiEnableNnHaArguments.
        Name of the NameNode role that is going to be made Highly Available.

        :param active_nn_name: The active_nn_name of this ApiEnableNnHaArguments.
        :type: str
        """

        self._active_nn_name = active_nn_name

    @property
    def standby_nn_name(self):
        """
        Gets the standby_nn_name of this ApiEnableNnHaArguments.
        Name of the new Standby NameNode role that will be created during the command (Optional).

        :return: The standby_nn_name of this ApiEnableNnHaArguments.
        :rtype: str
        """
        return self._standby_nn_name

    @standby_nn_name.setter
    def standby_nn_name(self, standby_nn_name):
        """
        Sets the standby_nn_name of this ApiEnableNnHaArguments.
        Name of the new Standby NameNode role that will be created during the command (Optional).

        :param standby_nn_name: The standby_nn_name of this ApiEnableNnHaArguments.
        :type: str
        """

        self._standby_nn_name = standby_nn_name

    @property
    def standby_nn_host_id(self):
        """
        Gets the standby_nn_host_id of this ApiEnableNnHaArguments.
        Id of the host on which new Standby NameNode will be created.

        :return: The standby_nn_host_id of this ApiEnableNnHaArguments.
        :rtype: str
        """
        return self._standby_nn_host_id

    @standby_nn_host_id.setter
    def standby_nn_host_id(self, standby_nn_host_id):
        """
        Sets the standby_nn_host_id of this ApiEnableNnHaArguments.
        Id of the host on which new Standby NameNode will be created.

        :param standby_nn_host_id: The standby_nn_host_id of this ApiEnableNnHaArguments.
        :type: str
        """

        self._standby_nn_host_id = standby_nn_host_id

    @property
    def standby_name_dir_list(self):
        """
        Gets the standby_name_dir_list of this ApiEnableNnHaArguments.
        List of directories for the new Standby NameNode. If not provided then it will use same dirs as Active NameNode.

        :return: The standby_name_dir_list of this ApiEnableNnHaArguments.
        :rtype: list[str]
        """
        return self._standby_name_dir_list

    @standby_name_dir_list.setter
    def standby_name_dir_list(self, standby_name_dir_list):
        """
        Sets the standby_name_dir_list of this ApiEnableNnHaArguments.
        List of directories for the new Standby NameNode. If not provided then it will use same dirs as Active NameNode.

        :param standby_name_dir_list: The standby_name_dir_list of this ApiEnableNnHaArguments.
        :type: list[str]
        """

        self._standby_name_dir_list = standby_name_dir_list

    @property
    def nameservice(self):
        """
        Gets the nameservice of this ApiEnableNnHaArguments.
        Nameservice to be used while enabling Highly Available. It must be specified if Active NameNode isn't configured with it. If Active NameNode is already configured, then this need not be specified. However, if it is still specified, it must match the existing config for the Active NameNode.

        :return: The nameservice of this ApiEnableNnHaArguments.
        :rtype: str
        """
        return self._nameservice

    @nameservice.setter
    def nameservice(self, nameservice):
        """
        Sets the nameservice of this ApiEnableNnHaArguments.
        Nameservice to be used while enabling Highly Available. It must be specified if Active NameNode isn't configured with it. If Active NameNode is already configured, then this need not be specified. However, if it is still specified, it must match the existing config for the Active NameNode.

        :param nameservice: The nameservice of this ApiEnableNnHaArguments.
        :type: str
        """

        self._nameservice = nameservice

    @property
    def qj_name(self):
        """
        Gets the qj_name of this ApiEnableNnHaArguments.
        Name of the journal located on each JournalNodes' filesystem. This can be optionally provided if the config hasn't already been set for the Active NameNode. If this isn't provided and Active NameNode doesn't also have the config, then nameservice is used by default. If Active NameNode already has this configured, then it much match the existing config.

        :return: The qj_name of this ApiEnableNnHaArguments.
        :rtype: str
        """
        return self._qj_name

    @qj_name.setter
    def qj_name(self, qj_name):
        """
        Sets the qj_name of this ApiEnableNnHaArguments.
        Name of the journal located on each JournalNodes' filesystem. This can be optionally provided if the config hasn't already been set for the Active NameNode. If this isn't provided and Active NameNode doesn't also have the config, then nameservice is used by default. If Active NameNode already has this configured, then it much match the existing config.

        :param qj_name: The qj_name of this ApiEnableNnHaArguments.
        :type: str
        """

        self._qj_name = qj_name

    @property
    def active_fc_name(self):
        """
        Gets the active_fc_name of this ApiEnableNnHaArguments.
        Name of the FailoverController role to be created on Active NameNode's host (Optional).

        :return: The active_fc_name of this ApiEnableNnHaArguments.
        :rtype: str
        """
        return self._active_fc_name

    @active_fc_name.setter
    def active_fc_name(self, active_fc_name):
        """
        Sets the active_fc_name of this ApiEnableNnHaArguments.
        Name of the FailoverController role to be created on Active NameNode's host (Optional).

        :param active_fc_name: The active_fc_name of this ApiEnableNnHaArguments.
        :type: str
        """

        self._active_fc_name = active_fc_name

    @property
    def standby_fc_name(self):
        """
        Gets the standby_fc_name of this ApiEnableNnHaArguments.
        Name of the FailoverController role to be created on Standby NameNode's host (Optional).

        :return: The standby_fc_name of this ApiEnableNnHaArguments.
        :rtype: str
        """
        return self._standby_fc_name

    @standby_fc_name.setter
    def standby_fc_name(self, standby_fc_name):
        """
        Sets the standby_fc_name of this ApiEnableNnHaArguments.
        Name of the FailoverController role to be created on Standby NameNode's host (Optional).

        :param standby_fc_name: The standby_fc_name of this ApiEnableNnHaArguments.
        :type: str
        """

        self._standby_fc_name = standby_fc_name

    @property
    def zk_service_name(self):
        """
        Gets the zk_service_name of this ApiEnableNnHaArguments.
        Name of the ZooKeeper service to be used for Auto-Failover. This MUST be provided if HDFS doesn't have a ZooKeeper dependency. If the dependency is already set, then this should be the name of the same ZooKeeper service, but can also be omitted in that case.

        :return: The zk_service_name of this ApiEnableNnHaArguments.
        :rtype: str
        """
        return self._zk_service_name

    @zk_service_name.setter
    def zk_service_name(self, zk_service_name):
        """
        Sets the zk_service_name of this ApiEnableNnHaArguments.
        Name of the ZooKeeper service to be used for Auto-Failover. This MUST be provided if HDFS doesn't have a ZooKeeper dependency. If the dependency is already set, then this should be the name of the same ZooKeeper service, but can also be omitted in that case.

        :param zk_service_name: The zk_service_name of this ApiEnableNnHaArguments.
        :type: str
        """

        self._zk_service_name = zk_service_name

    @property
    def jns(self):
        """
        Gets the jns of this ApiEnableNnHaArguments.
        Arguments for the JournalNodes to be created during the command. Must be provided only if JournalNodes don't exist already in HDFS.

        :return: The jns of this ApiEnableNnHaArguments.
        :rtype: list[ApiJournalNodeArguments]
        """
        return self._jns

    @jns.setter
    def jns(self, jns):
        """
        Sets the jns of this ApiEnableNnHaArguments.
        Arguments for the JournalNodes to be created during the command. Must be provided only if JournalNodes don't exist already in HDFS.

        :param jns: The jns of this ApiEnableNnHaArguments.
        :type: list[ApiJournalNodeArguments]
        """

        self._jns = jns

    @property
    def force_init_z_node(self):
        """
        Gets the force_init_z_node of this ApiEnableNnHaArguments.
        Boolean indicating if the ZNode should be force initialized if it is already present. Useful while re-enabling High Availability. (Default: TRUE)

        :return: The force_init_z_node of this ApiEnableNnHaArguments.
        :rtype: bool
        """
        return self._force_init_z_node

    @force_init_z_node.setter
    def force_init_z_node(self, force_init_z_node):
        """
        Sets the force_init_z_node of this ApiEnableNnHaArguments.
        Boolean indicating if the ZNode should be force initialized if it is already present. Useful while re-enabling High Availability. (Default: TRUE)

        :param force_init_z_node: The force_init_z_node of this ApiEnableNnHaArguments.
        :type: bool
        """

        self._force_init_z_node = force_init_z_node

    @property
    def clear_existing_standby_name_dirs(self):
        """
        Gets the clear_existing_standby_name_dirs of this ApiEnableNnHaArguments.
        Boolean indicating if the existing name directories for Standby NameNode should be cleared during the workflow. Useful while re-enabling High Availability. (Default: TRUE)

        :return: The clear_existing_standby_name_dirs of this ApiEnableNnHaArguments.
        :rtype: bool
        """
        return self._clear_existing_standby_name_dirs

    @clear_existing_standby_name_dirs.setter
    def clear_existing_standby_name_dirs(self, clear_existing_standby_name_dirs):
        """
        Sets the clear_existing_standby_name_dirs of this ApiEnableNnHaArguments.
        Boolean indicating if the existing name directories for Standby NameNode should be cleared during the workflow. Useful while re-enabling High Availability. (Default: TRUE)

        :param clear_existing_standby_name_dirs: The clear_existing_standby_name_dirs of this ApiEnableNnHaArguments.
        :type: bool
        """

        self._clear_existing_standby_name_dirs = clear_existing_standby_name_dirs

    @property
    def clear_existing_jn_edits_dir(self):
        """
        Gets the clear_existing_jn_edits_dir of this ApiEnableNnHaArguments.
        Boolean indicating if the existing edits directories for the JournalNodes for the specified nameservice should be cleared during the workflow. Useful while re-enabling High Availability. (Default: TRUE)

        :return: The clear_existing_jn_edits_dir of this ApiEnableNnHaArguments.
        :rtype: bool
        """
        return self._clear_existing_jn_edits_dir

    @clear_existing_jn_edits_dir.setter
    def clear_existing_jn_edits_dir(self, clear_existing_jn_edits_dir):
        """
        Sets the clear_existing_jn_edits_dir of this ApiEnableNnHaArguments.
        Boolean indicating if the existing edits directories for the JournalNodes for the specified nameservice should be cleared during the workflow. Useful while re-enabling High Availability. (Default: TRUE)

        :param clear_existing_jn_edits_dir: The clear_existing_jn_edits_dir of this ApiEnableNnHaArguments.
        :type: bool
        """

        self._clear_existing_jn_edits_dir = clear_existing_jn_edits_dir

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
        if not isinstance(other, ApiEnableNnHaArguments):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
