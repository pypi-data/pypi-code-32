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
OutboundMessageQueue Module.
"""


class OutboundMessageQueue:
    """Store messages on device before publishing to WolkAbout IoT Platform."""

    def put(self, message):
        """
        Place a message in storage.

        :param message: Message to be stored
        :type message: wolk.wolkcore.OutboundMessage.OutboundMessage
        """
        pass

    def get(self):
        """
        Get a message from storage.

        :returns: message
        :rtype: wolk.wolkcore.OutboundMessage.OutboundMessage
        """
        pass

    def peek(self):
        """
        Get a message without removing from storage.

        :returns: message
        :rtype: wolk.wolkcore.OutboundMessage.OutboundMessage
        """
        pass
