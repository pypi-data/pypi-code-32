# coding: utf-8

"""
    Cloudera Manager API

    <h1>Cloudera Manager API v31</h1>       <p>Introduced in Cloudera Manager 6.1.0</p>       <p><a href=\"http://www.cloudera.com/documentation.html\">Cloudera Product Documentation</a></p>

    OpenAPI spec version: 6.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import cm_client
from cm_client.rest import ApiException
from cm_client.apis.role_commands_resource_api import RoleCommandsResourceApi


class TestRoleCommandsResourceApi(unittest.TestCase):
    """ RoleCommandsResourceApi unit test stubs """

    def setUp(self):
        self.api = cm_client.apis.role_commands_resource_api.RoleCommandsResourceApi()

    def tearDown(self):
        pass

    def test_format_command(self):
        """
        Test case for format_command

        Format HDFS NameNodes.
        """
        pass

    def test_hdfs_bootstrap_stand_by_command(self):
        """
        Test case for hdfs_bootstrap_stand_by_command

        Bootstrap HDFS stand-by NameNodes.
        """
        pass

    def test_hdfs_enter_safemode(self):
        """
        Test case for hdfs_enter_safemode

        Enter safemode for namenodes.
        """
        pass

    def test_hdfs_finalize_metadata_upgrade(self):
        """
        Test case for hdfs_finalize_metadata_upgrade

        Finalize HDFS NameNode metadata upgrade.
        """
        pass

    def test_hdfs_initialize_auto_failover_command(self):
        """
        Test case for hdfs_initialize_auto_failover_command

        Initialize HDFS HA failover controller metadata.
        """
        pass

    def test_hdfs_initialize_shared_dir_command(self):
        """
        Test case for hdfs_initialize_shared_dir_command

        Initialize HDFS NameNodes' shared edit directory.
        """
        pass

    def test_hdfs_leave_safemode(self):
        """
        Test case for hdfs_leave_safemode

        Leave safemode for namenodes.
        """
        pass

    def test_hdfs_save_namespace(self):
        """
        Test case for hdfs_save_namespace

        Save namespace for namenodes.
        """
        pass

    def test_jmap_dump(self):
        """
        Test case for jmap_dump

        Run the jmapDump diagnostic command.
        """
        pass

    def test_jmap_histo(self):
        """
        Test case for jmap_histo

        Run the jmapHisto diagnostic command.
        """
        pass

    def test_jstack(self):
        """
        Test case for jstack

        Run the jstack diagnostic command.
        """
        pass

    def test_lsof(self):
        """
        Test case for lsof

        Run the lsof diagnostic command.
        """
        pass

    def test_refresh_command(self):
        """
        Test case for refresh_command

        Refresh a role's data.
        """
        pass

    def test_restart_command(self):
        """
        Test case for restart_command

        Restart a set of role instances.
        """
        pass

    def test_role_command_by_name(self):
        """
        Test case for role_command_by_name

        Execute a role command by name.
        """
        pass

    def test_start_command(self):
        """
        Test case for start_command

        Start a set of role instances.
        """
        pass

    def test_stop_command(self):
        """
        Test case for stop_command

        Stop a set of role instances.
        """
        pass

    def test_sync_hue_db_command(self):
        """
        Test case for sync_hue_db_command

        Create / update the Hue database schema.
        """
        pass

    def test_zoo_keeper_cleanup_command(self):
        """
        Test case for zoo_keeper_cleanup_command

        Cleanup a list of ZooKeeper server roles.
        """
        pass

    def test_zoo_keeper_init_command(self):
        """
        Test case for zoo_keeper_init_command

        Initialize a list of ZooKeeper server roles.
        """
        pass


if __name__ == '__main__':
    unittest.main()
