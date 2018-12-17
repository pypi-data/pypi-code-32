# Copyright 2012-2013 Isotoma Limited
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from .configurator import TravisConfigurator
from buildbot.www.plugin import Application
from .api import Api

# create the interface for the setuptools entry point
ep = Application(__name__, "Buildbot travis custom ui")
api = Api(ep)
ep.resource.putChild(b"api", api.app.resource())


__all__ = ['TravisConfigurator', 'ep']
