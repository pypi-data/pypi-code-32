import errno
import os

import yaml

from orchestrate.common import safe_format
from orchestrate.core.cluster_metadata.errors import *
from orchestrate.core.paths import get_root_subdir, ensure_dir
from orchestrate.core.provider.constants import provider_to_string, string_to_provider
from orchestrate.core.services.base import Service


class ClusterMetadataService(Service):
  def __init__(self, services):
    super(ClusterMetadataService, self).__init__(services)
    self._metadata_dir = get_root_subdir('cluster')

  def read_metadata(self, cluster_name):
    metadata_path = self._cluster_metadata_path(cluster_name)

    if not os.path.isfile(metadata_path):
      raise MetadataNotFoundError(cluster_name)

    with open(metadata_path, 'r') as f:
      data = yaml.safe_load(stream=f)

    name = data['cluster_name']
    provider = string_to_provider(data['provider'])

    provider_service = self.services.provider_broker.get_provider_service(provider)
    cluster = provider_service.create_cluster_object(cluster_name=name)
    return cluster

  def write_metadata(self, cluster):
    data = dict(
      cluster_name=cluster.name,
      provider=provider_to_string(cluster.provider),
    )

    ensure_dir(self._metadata_dir)
    metadata_path = self._cluster_metadata_path(cluster.name)

    if os.path.isfile(metadata_path):
      raise MetadataAlreadyExistsError(cluster.name)

    with open(metadata_path, 'w') as f:
      yaml.safe_dump(data, stream=f)

  def _delete_metadata(self, cluster_name):
    try:
      os.remove(self._cluster_metadata_path(cluster_name))
    except OSError as e:
      if e.errno == errno.ENOENT:
        raise MetadataNotFoundError(cluster_name)
      raise

  def ensure_metadata_deleted(self, cluster_name):
    try:
      self._delete_metadata(cluster_name)
    except MetadataNotFoundError:
      pass

  def _cluster_metadata_path(self, cluster_name):
    filename = safe_format('metadata-{}', cluster_name)
    return os.path.join(self._metadata_dir, filename)
