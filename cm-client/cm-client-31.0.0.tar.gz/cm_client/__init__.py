# coding: utf-8

"""
    Cloudera Manager API

    <h1>Cloudera Manager API v31</h1>       <p>Introduced in Cloudera Manager 6.1.0</p>       <p><a href=\"http://www.cloudera.com/documentation.html\">Cloudera Product Documentation</a></p>

    OpenAPI spec version: 6.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into sdk package
from .models.api_activity import ApiActivity
from .models.api_activity_status import ApiActivityStatus
from .models.api_activity_type import ApiActivityType
from .models.api_audit import ApiAudit
from .models.api_auth_role import ApiAuthRole
from .models.api_auth_role_authority import ApiAuthRoleAuthority
from .models.api_auth_role_metadata import ApiAuthRoleMetadata
from .models.api_auth_role_ref import ApiAuthRoleRef
from .models.api_batch_request_element import ApiBatchRequestElement
from .models.api_batch_response_element import ApiBatchResponseElement
from .models.api_cdh_upgrade_args import ApiCdhUpgradeArgs
from .models.api_cluster import ApiCluster
from .models.api_cluster_perf_inspector_args import ApiClusterPerfInspectorArgs
from .models.api_cluster_ref import ApiClusterRef
from .models.api_cluster_template import ApiClusterTemplate
from .models.api_cluster_template_config import ApiClusterTemplateConfig
from .models.api_cluster_template_host_info import ApiClusterTemplateHostInfo
from .models.api_cluster_template_host_template import ApiClusterTemplateHostTemplate
from .models.api_cluster_template_instantiator import ApiClusterTemplateInstantiator
from .models.api_cluster_template_role import ApiClusterTemplateRole
from .models.api_cluster_template_role_config_group import ApiClusterTemplateRoleConfigGroup
from .models.api_cluster_template_role_config_group_info import ApiClusterTemplateRoleConfigGroupInfo
from .models.api_cluster_template_service import ApiClusterTemplateService
from .models.api_cluster_template_variable import ApiClusterTemplateVariable
from .models.api_cluster_utilization import ApiClusterUtilization
from .models.api_cluster_version import ApiClusterVersion
from .models.api_clusters_perf_inspector_args import ApiClustersPerfInspectorArgs
from .models.api_cm_peer import ApiCmPeer
from .models.api_cm_peer_type import ApiCmPeerType
from .models.api_collect_diagnostic_data_arguments import ApiCollectDiagnosticDataArguments
from .models.api_command import ApiCommand
from .models.api_command_metadata import ApiCommandMetadata
from .models.api_commission_state import ApiCommissionState
from .models.api_config import ApiConfig
from .models.api_config_staleness_status import ApiConfigStalenessStatus
from .models.api_configure_for_kerberos_arguments import ApiConfigureForKerberosArguments
from .models.api_dashboard import ApiDashboard
from .models.api_deployment import ApiDeployment
from .models.api_deployment2 import ApiDeployment2
from .models.api_disable_jt_ha_arguments import ApiDisableJtHaArguments
from .models.api_disable_llama_ha_arguments import ApiDisableLlamaHaArguments
from .models.api_disable_nn_ha_arguments import ApiDisableNnHaArguments
from .models.api_disable_oozie_ha_arguments import ApiDisableOozieHaArguments
from .models.api_disable_rm_ha_arguments import ApiDisableRmHaArguments
from .models.api_disable_sentry_ha_args import ApiDisableSentryHaArgs
from .models.api_echo import ApiEcho
from .models.api_enable_jt_ha_arguments import ApiEnableJtHaArguments
from .models.api_enable_llama_ha_arguments import ApiEnableLlamaHaArguments
from .models.api_enable_llama_rm_arguments import ApiEnableLlamaRmArguments
from .models.api_enable_nn_ha_arguments import ApiEnableNnHaArguments
from .models.api_enable_oozie_ha_arguments import ApiEnableOozieHaArguments
from .models.api_enable_rm_ha_arguments import ApiEnableRmHaArguments
from .models.api_enable_sentry_ha_args import ApiEnableSentryHaArgs
from .models.api_entity_status import ApiEntityStatus
from .models.api_entity_type import ApiEntityType
from .models.api_event import ApiEvent
from .models.api_event_attribute import ApiEventAttribute
from .models.api_event_category import ApiEventCategory
from .models.api_event_severity import ApiEventSeverity
from .models.api_external_account import ApiExternalAccount
from .models.api_external_account_category import ApiExternalAccountCategory
from .models.api_external_account_type import ApiExternalAccountType
from .models.api_external_user_mapping import ApiExternalUserMapping
from .models.api_external_user_mapping_ref import ApiExternalUserMappingRef
from .models.api_external_user_mapping_type import ApiExternalUserMappingType
from .models.api_generate_host_certs_arguments import ApiGenerateHostCertsArguments
from .models.api_h_base_snapshot import ApiHBaseSnapshot
from .models.api_h_base_snapshot_error import ApiHBaseSnapshotError
from .models.api_h_base_snapshot_policy_arguments import ApiHBaseSnapshotPolicyArguments
from .models.api_h_base_snapshot_result import ApiHBaseSnapshotResult
from .models.api_hdfs_disable_ha_arguments import ApiHdfsDisableHaArguments
from .models.api_hdfs_failover_arguments import ApiHdfsFailoverArguments
from .models.api_hdfs_ha_arguments import ApiHdfsHaArguments
from .models.api_hdfs_replication_arguments import ApiHdfsReplicationArguments
from .models.api_hdfs_replication_counter import ApiHdfsReplicationCounter
from .models.api_hdfs_replication_result import ApiHdfsReplicationResult
from .models.api_hdfs_snapshot import ApiHdfsSnapshot
from .models.api_hdfs_snapshot_error import ApiHdfsSnapshotError
from .models.api_hdfs_snapshot_policy_arguments import ApiHdfsSnapshotPolicyArguments
from .models.api_hdfs_snapshot_result import ApiHdfsSnapshotResult
from .models.api_hdfs_usage_report_row import ApiHdfsUsageReportRow
from .models.api_health_check import ApiHealthCheck
from .models.api_health_summary import ApiHealthSummary
from .models.api_hive_replication_arguments import ApiHiveReplicationArguments
from .models.api_hive_replication_error import ApiHiveReplicationError
from .models.api_hive_replication_result import ApiHiveReplicationResult
from .models.api_hive_table import ApiHiveTable
from .models.api_hive_udf import ApiHiveUDF
from .models.api_host import ApiHost
from .models.api_host_install_arguments import ApiHostInstallArguments
from .models.api_host_ref import ApiHostRef
from .models.api_host_template import ApiHostTemplate
from .models.api_hosts_perf_inspector_args import ApiHostsPerfInspectorArgs
from .models.api_impala_cancel_response import ApiImpalaCancelResponse
from .models.api_impala_query import ApiImpalaQuery
from .models.api_impala_query_attribute import ApiImpalaQueryAttribute
from .models.api_impala_query_details_response import ApiImpalaQueryDetailsResponse
from .models.api_impala_query_response import ApiImpalaQueryResponse
from .models.api_impala_role_diagnostics_args import ApiImpalaRoleDiagnosticsArgs
from .models.api_impala_tenant_utilization import ApiImpalaTenantUtilization
from .models.api_impala_udf import ApiImpalaUDF
from .models.api_impala_utilization import ApiImpalaUtilization
from .models.api_impala_utilization_histogram import ApiImpalaUtilizationHistogram
from .models.api_impala_utilization_histogram_bin import ApiImpalaUtilizationHistogramBin
from .models.api_journal_node_arguments import ApiJournalNodeArguments
from .models.api_kerberos_info import ApiKerberosInfo
from .models.api_license import ApiLicense
from .models.api_licensed_feature_usage import ApiLicensedFeatureUsage
from .models.api_list_base import ApiListBase
from .models.api_map_entry import ApiMapEntry
from .models.api_metric import ApiMetric
from .models.api_metric_data import ApiMetricData
from .models.api_metric_schema import ApiMetricSchema
from .models.api_migrate_roles_arguments import ApiMigrateRolesArguments
from .models.api_mr2_app_information import ApiMr2AppInformation
from .models.api_mr_usage_report_row import ApiMrUsageReportRow
from .models.api_nameservice import ApiNameservice
from .models.api_parcel import ApiParcel
from .models.api_parcel_ref import ApiParcelRef
from .models.api_parcel_state import ApiParcelState
from .models.api_parcel_usage import ApiParcelUsage
from .models.api_parcel_usage_host import ApiParcelUsageHost
from .models.api_parcel_usage_parcel import ApiParcelUsageParcel
from .models.api_parcel_usage_rack import ApiParcelUsageRack
from .models.api_parcel_usage_role import ApiParcelUsageRole
from .models.api_perf_inspector_ping_args import ApiPerfInspectorPingArgs
from .models.api_process import ApiProcess
from .models.api_product_version import ApiProductVersion
from .models.api_replication_diagnostics_collection_args import ApiReplicationDiagnosticsCollectionArgs
from .models.api_replication_state import ApiReplicationState
from .models.api_restart_cluster_args import ApiRestartClusterArgs
from .models.api_role import ApiRole
from .models.api_role_config_group import ApiRoleConfigGroup
from .models.api_role_config_group_ref import ApiRoleConfigGroupRef
from .models.api_role_ref import ApiRoleRef
from .models.api_role_state import ApiRoleState
from .models.api_roles_to_include import ApiRolesToInclude
from .models.api_roll_edits_args import ApiRollEditsArgs
from .models.api_rolling_restart_args import ApiRollingRestartArgs
from .models.api_rolling_restart_cluster_args import ApiRollingRestartClusterArgs
from .models.api_rolling_upgrade_cluster_args import ApiRollingUpgradeClusterArgs
from .models.api_rolling_upgrade_services_args import ApiRollingUpgradeServicesArgs
from .models.api_schedule import ApiSchedule
from .models.api_schedule_interval import ApiScheduleInterval
from .models.api_scm_db_info import ApiScmDbInfo
from .models.api_service import ApiService
from .models.api_service_ref import ApiServiceRef
from .models.api_service_state import ApiServiceState
from .models.api_shutdown_readiness import ApiShutdownReadiness
from .models.api_simple_rolling_restart_cluster_args import ApiSimpleRollingRestartClusterArgs
from .models.api_snapshot_policy import ApiSnapshotPolicy
from .models.api_tenant_utilization import ApiTenantUtilization
from .models.api_time_series import ApiTimeSeries
from .models.api_time_series_aggregate_statistics import ApiTimeSeriesAggregateStatistics
from .models.api_time_series_cross_entity_metadata import ApiTimeSeriesCrossEntityMetadata
from .models.api_time_series_data import ApiTimeSeriesData
from .models.api_time_series_entity_attribute import ApiTimeSeriesEntityAttribute
from .models.api_time_series_entity_type import ApiTimeSeriesEntityType
from .models.api_time_series_metadata import ApiTimeSeriesMetadata
from .models.api_time_series_request import ApiTimeSeriesRequest
from .models.api_time_series_response import ApiTimeSeriesResponse
from .models.api_user import ApiUser
from .models.api_user2 import ApiUser2
from .models.api_user2_ref import ApiUser2Ref
from .models.api_user_session import ApiUserSession
from .models.api_version_info import ApiVersionInfo
from .models.api_watched_dir import ApiWatchedDir
from .models.api_yarn_application import ApiYarnApplication
from .models.api_yarn_application_attribute import ApiYarnApplicationAttribute
from .models.api_yarn_application_diagnostics_collection_args import ApiYarnApplicationDiagnosticsCollectionArgs
from .models.api_yarn_application_response import ApiYarnApplicationResponse
from .models.api_yarn_kill_response import ApiYarnKillResponse
from .models.api_yarn_tenant_utilization import ApiYarnTenantUtilization
from .models.api_yarn_utilization import ApiYarnUtilization
from .models.http_method import HTTPMethod
from .models.ha_status import HaStatus
from .models.replication_option import ReplicationOption
from .models.replication_strategy import ReplicationStrategy
from .models.scm_db_type import ScmDbType
from .models.shutdown_readiness_state import ShutdownReadinessState
from .models.storage import Storage
from .models.validation_state import ValidationState
from .models.zoo_keeper_server_mode import ZooKeeperServerMode
from .models.api_activity_list import ApiActivityList
from .models.api_audit_list import ApiAuditList
from .models.api_auth_role_list import ApiAuthRoleList
from .models.api_auth_role_metadata_list import ApiAuthRoleMetadataList
from .models.api_batch_request import ApiBatchRequest
from .models.api_batch_response import ApiBatchResponse
from .models.api_cluster_list import ApiClusterList
from .models.api_cluster_name_list import ApiClusterNameList
from .models.api_cm_peer_list import ApiCmPeerList
from .models.api_command_list import ApiCommandList
from .models.api_command_metadata_list import ApiCommandMetadataList
from .models.api_config_list import ApiConfigList
from .models.api_dashboard_list import ApiDashboardList
from .models.api_event_query_result import ApiEventQueryResult
from .models.api_external_account_category_list import ApiExternalAccountCategoryList
from .models.api_external_account_list import ApiExternalAccountList
from .models.api_external_account_type_list import ApiExternalAccountTypeList
from .models.api_external_user_mapping_list import ApiExternalUserMappingList
from .models.api_hdfs_cloud_replication_arguments import ApiHdfsCloudReplicationArguments
from .models.api_hdfs_usage_report import ApiHdfsUsageReport
from .models.api_hive_cloud_replication_arguments import ApiHiveCloudReplicationArguments
from .models.api_host_list import ApiHostList
from .models.api_host_name_list import ApiHostNameList
from .models.api_host_ref_list import ApiHostRefList
from .models.api_host_template_list import ApiHostTemplateList
from .models.api_impala_query_attribute_list import ApiImpalaQueryAttributeList
from .models.api_impala_tenant_utilization_list import ApiImpalaTenantUtilizationList
from .models.api_impala_utilization_histogram_bin_list import ApiImpalaUtilizationHistogramBinList
from .models.api_metric_list import ApiMetricList
from .models.api_metric_schema_list import ApiMetricSchemaList
from .models.api_mr_usage_report import ApiMrUsageReport
from .models.api_nameservice_list import ApiNameserviceList
from .models.api_parcel_list import ApiParcelList
from .models.api_principal_list import ApiPrincipalList
from .models.api_replication_command import ApiReplicationCommand
from .models.api_replication_command_list import ApiReplicationCommandList
from .models.api_replication_schedule import ApiReplicationSchedule
from .models.api_replication_schedule_list import ApiReplicationScheduleList
from .models.api_role_config_group_list import ApiRoleConfigGroupList
from .models.api_role_list import ApiRoleList
from .models.api_role_name_list import ApiRoleNameList
from .models.api_role_type_list import ApiRoleTypeList
from .models.api_service_list import ApiServiceList
from .models.api_service_type_list import ApiServiceTypeList
from .models.api_snapshot_command import ApiSnapshotCommand
from .models.api_snapshot_command_list import ApiSnapshotCommandList
from .models.api_snapshot_policy_list import ApiSnapshotPolicyList
from .models.api_tenant_utilization_list import ApiTenantUtilizationList
from .models.api_time_series_entity_attribute_list import ApiTimeSeriesEntityAttributeList
from .models.api_time_series_entity_type_list import ApiTimeSeriesEntityTypeList
from .models.api_time_series_response_list import ApiTimeSeriesResponseList
from .models.api_user2_list import ApiUser2List
from .models.api_user_list import ApiUserList
from .models.api_user_session_list import ApiUserSessionList
from .models.api_watched_dir_list import ApiWatchedDirList
from .models.api_yarn_application_attribute_list import ApiYarnApplicationAttributeList
from .models.api_yarn_tenant_utilization_list import ApiYarnTenantUtilizationList
from .models.api_bulk_command_list import ApiBulkCommandList
from .models.api_role_type_config import ApiRoleTypeConfig
from .models.api_service_config import ApiServiceConfig

# import apis into sdk package
from .apis.activities_resource_api import ActivitiesResourceApi
from .apis.all_hosts_resource_api import AllHostsResourceApi
from .apis.audits_resource_api import AuditsResourceApi
from .apis.auth_role_metadatas_resource_api import AuthRoleMetadatasResourceApi
from .apis.auth_roles_resource_api import AuthRolesResourceApi
from .apis.auth_service_resource_api import AuthServiceResourceApi
from .apis.auth_service_role_commands_resource_api import AuthServiceRoleCommandsResourceApi
from .apis.auth_service_role_config_groups_resource_api import AuthServiceRoleConfigGroupsResourceApi
from .apis.auth_service_roles_resource_api import AuthServiceRolesResourceApi
from .apis.batch_resource_api import BatchResourceApi
from .apis.cloudera_manager_resource_api import ClouderaManagerResourceApi
from .apis.clusters_resource_api import ClustersResourceApi
from .apis.cm_peers_resource_api import CmPeersResourceApi
from .apis.commands_resource_api import CommandsResourceApi
from .apis.dashboards_resource_api import DashboardsResourceApi
from .apis.events_resource_api import EventsResourceApi
from .apis.external_accounts_resource_api import ExternalAccountsResourceApi
from .apis.external_user_mappings_resource_api import ExternalUserMappingsResourceApi
from .apis.host_templates_resource_api import HostTemplatesResourceApi
from .apis.hosts_resource_api import HostsResourceApi
from .apis.impala_queries_resource_api import ImpalaQueriesResourceApi
from .apis.mgmt_role_commands_resource_api import MgmtRoleCommandsResourceApi
from .apis.mgmt_role_config_groups_resource_api import MgmtRoleConfigGroupsResourceApi
from .apis.mgmt_roles_resource_api import MgmtRolesResourceApi
from .apis.mgmt_service_resource_api import MgmtServiceResourceApi
from .apis.nameservices_resource_api import NameservicesResourceApi
from .apis.parcel_resource_api import ParcelResourceApi
from .apis.parcels_resource_api import ParcelsResourceApi
from .apis.process_resource_api import ProcessResourceApi
from .apis.replications_resource_api import ReplicationsResourceApi
from .apis.role_commands_resource_api import RoleCommandsResourceApi
from .apis.role_config_groups_resource_api import RoleConfigGroupsResourceApi
from .apis.roles_resource_api import RolesResourceApi
from .apis.services_resource_api import ServicesResourceApi
from .apis.snapshots_resource_api import SnapshotsResourceApi
from .apis.time_series_resource_api import TimeSeriesResourceApi
from .apis.tools_resource_api import ToolsResourceApi
from .apis.users_resource_api import UsersResourceApi
from .apis.watched_dir_resource_api import WatchedDirResourceApi
from .apis.yarn_applications_resource_api import YarnApplicationsResourceApi

# import ApiClient
from .api_client import ApiClient

from .configuration import Configuration

configuration = Configuration()
