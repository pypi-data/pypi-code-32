#!/usr/bin/env python

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from selenium import webdriver
from ..mobilecommand import MobileCommand as Command


class Context(webdriver.Remote):
    @property
    def contexts(self):
        """
        Returns the contexts within the current session.

        :Usage:
            driver.contexts
        """
        return self.execute(Command.CONTEXTS)['value']

    @property
    def current_context(self):
        """
        Returns the current context of the current session.

        :Usage:
            driver.current_context
        """
        return self.execute(Command.GET_CURRENT_CONTEXT)['value']

    @property
    def context(self):
        """
        Returns the current context of the current session.

        :Usage:
            driver.context
        """
        return self.current_context
