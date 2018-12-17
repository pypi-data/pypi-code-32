# Copyright (C) 2018  The Software Heritage developers
# See the AUTHORS file at the top-level directory of this distribution
# License: GNU General Public License version 3, or any later version
# See top-level LICENSE file for more information


from swh.loader.git.loader import GitLoader
from swh.loader.git.tests.test_from_disk import DirGitLoaderTest


class GitLoaderTest(GitLoader):
    def parse_config_file(self, *args, **kwargs):
        return {
            **super().parse_config_file(*args, **kwargs),
            'storage': {'cls': 'memory', 'args': {}}
        }


class TestGitLoader(DirGitLoaderTest):
    """Same tests as for the GitLoaderFromDisk, but running on GitLoader."""
    def setUp(self):
        super().setUp()
        self.loader = GitLoaderTest()
        self.storage = self.loader.storage

    def load(self):
        return self.loader.load(
            origin_url=self.repo_url)
