from mock import patch
import pytest

from orchestrate.common import Platform, current_platform

class TestCurrentPlatform(object):
  @pytest.mark.parametrize('platform', ['foobar.linux', 'foobar', ''])
  def test_bad_platform(self, platform):
    with patch('orchestrate.common.sys.platform', platform):
      with pytest.raises(Exception):
        current_platform()

  def test_mac_platform(self):
    with patch('orchestrate.common.sys.platform', 'darwin'):
      assert current_platform() == Platform.MAC

  @pytest.mark.parametrize('platform', ['linux', 'linux.foobar'])
  def test_linux_platform(self, platform):
    with patch('orchestrate.common.sys.platform', platform):
      assert current_platform() == Platform.LINUX
