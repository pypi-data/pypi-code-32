#   Copyright 2018 WolkAbout Technology s.r.o.
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

"""
Device Module.
"""


class Device:
    """Hold all the necessary information to communicate with the platform."""

    def __init__(self, key, password, actuator_references=None):
        """
        Credentials and optionally actuator references.

        :param key: Username used to connect to the platform
        :type key: str
        :param password: Password used to authenticate the connection
        :type password: str
        :param actuator_references: Actuator references enabled on device
        :type actuator_references: list or None
        """
        self.key = key
        self.password = password
        self.actuator_references = actuator_references
