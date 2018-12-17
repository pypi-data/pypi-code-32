#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) Smart Arcs Ltd registered in the United Kingdom.
# Unauthorized copying of this file, via any medium is strictly prohibited
#
# This file is provided under a license as specified in the "LICENSE" file, which is part
# of this software package.
#
# Written by Smart Arcs <support@smartarchitects.co.uk>, August 2018
import shlex
import subprocess

from foxyproxy.upstream.base_upstream import BaseUpstream

__author__ = "Smart Arcs"
__copyright__ = 'Smart Arcs Ltd'
__email__ = 'support@smartarchitects.co.uk'
__status__ = 'Beta'

import logging
import coloredlogs
import requests

# noinspection PyProtectedMember

logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)
# ch = logging.StreamHandler()
# ch.setLevel(logging.INFO)
# logger.addHandler(ch)
# fh = logging.FileHandler('foxyproxy.log')
# fh.setLevel(logging.INFO)
# logger.addHandler(fh)

coloredlogs.install(level='INFO', logger=logger)
# coloredlogs.install(level='DEBUG', logger=logger) # to suppress logs from libs

logging.basicConfig(level=logging.DEBUG)


class LinuxShell(BaseUpstream):
    """
    Class for Linux signer
    """
    def __init__(self, server_config):
        """
        Accepts a configuration of the upstream - using the SignerConfig object below

        :param server_config: an object with configuration parameters of the signing upstream, this object will be
                                stored in the attribute 'server'
        :type server_config: LinuxShellConfig
        """
        super(LinuxShell, self).__init__(server_config)
        pass

    # Function for parsing input request
    # ><reader name>|><cmd ID>:<"APDU" / "RESET" / "ENUM">:<optional hexa string, e.g. "00A4040304">|

    def cmd(self, payload, terminal, reset=0):
        """

        :type payload: str|list
        :type terminal: str
        :param reset: not used in this module
        :type reset:int
        """
        if (payload is None) or (terminal is None):
            logging.error("Requesting a command via LinuxShell requires the terminal and commands to be defined")
            exit(5)
        else:
            if isinstance(payload, str):
                payload = [payload]
            counter = len(payload)
            raw_data = self._get_request(self.server.upstream_cmd, payload, terminal)
            # TODO we may want to normalize commands and match them to responses from _get_request
            response = []
            for line in raw_data:
                line = ''.join(line.upper().split())
                if line.startswith('A<<'):
                    line_break = line.split(')')
                    if len(line_break) < 2:
                        logging.error("Response received by LinuxShell is in a wrong format. "
                                      "This is a critical error stopping processing %s" % '\\'.join(raw_data))
                    response.append(line_break[len(line_break) - 1])  # and take the last part
                    counter -= 1
                    if counter < 1:
                        break

            return response

    def downtime(self):
        """

        :return: time of the upstream server running time
        :rtype int
        """

        response_data = self._get_request(self.server.upstream_uptime, None)
        # we need to check readers and compare them with the state information
        self.server.up_time += 1
        for line in response_data:
            if line.startswith("SCardBeginTransaction"):
                if len(line.split('"')) > 1:
                    reader_name = line.split('"')[1]
                    if reader_name not in self.server.readers:
                        # keep the info about a token we need to enumerate
                        self.server.pending_readers[reader_name] = True
                    else:
                        # mark that it was found
                        self.server.readers[reader_name].up_time = self.server.up_time

        # first we remove readers that were unplugged
        for each_key in self.server.readers.keys():
            if self.server.readers[each_key].up_time < self.server.up_time:
                del self.server.readers[each_key]

        if len(self.server.pending_readers) > 0:
            self.server.stale = True

        return self.server.stale

    def inventory(self):
        """
        Returns a list of readers
        :return:
        """
        reader_list = []
        for each_key in self.server.pending_readers.keys():
            reader_list.append(each_key)
            self.server.pending_readers[each_key] = False

        return reader_list

    # #########################################################################
    # Private methods
    # #########################################################################
    def _get_request(self, cmd, payload_in='', token=None):
        """
        Upstream dependent request processing.
        :type cmd: str
        :type payload_in: str|list|None
        :type token: str|None
        """
        response_data = None
        if payload_in is None or len(payload_in) == 0:  # len should work for string as well as list
            payload = ''
        elif isinstance(payload_in, list):
            payload = payload_in.pop(0)
            for each_cmd in payload_in:
                payload += cmd + each_cmd
        else:
            payload = payload_in

        if token is None:
            terminal = ''
        else:
            terminal = ' -r "' + token + '"'

        # noinspection PyBroadException
        try:
            logging.debug('Going to send request to GPPro ...')
            p = subprocess.Popen(shlex.split(self.server.upstream_url + terminal + cmd + " " + payload),
                                 stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            r = p.communicate()[0]
        except requests.ConnectionError:
            logging.error('Problem with connection - check that the command is correct: %s' %
                          self.server.upstream_url)
        except Exception as ex:
            template = "Connection {0} error: an exception of type {1} occurred. Arguments:\n{2!r}"
            logging.error(template.format(self.server.upstream_url + cmd, type(ex).__name__, ex.args))
        else:
            # process response
            logging.debug('Response received: ' + r.decode('utf-8'))
            response_data = []
            for line in r.decode('utf-8').splitlines():
                if line != 'null' and len(line) > 0 and \
                        (line.startswith('SCardBeginTransaction') or line.startswith('A>>') or line.startswith('A<<')):
                    response_data.append(line)

        return response_data


class LinuxShellConfig(object):
    """
    Configuration for shell signer
    """
    SHELL_CMD = './signer.sh'

    def __init__(self, server=None, token='b'):
        self.token = token
        if server is None:
            self.upstream_url = LinuxShellConfig.SHELL_CMD
        else:
            self.upstream_url = server

        # self.upstream_url = 'java -jar ' + self.upstream_url + ' --bs 246 -d '
        self.upstream_url += ' '

        print("FoxyProxy will use CLI command %s" % self.upstream_url)

        #  rest proxy for CloudFoxy hardware platform, use basicj for more info
        self.upstream_cmd = ' -a '
        self.upstream_uptime = ''
        self.upstream_inventory = ' -l '
        self.test_local_reader = None

        self.upstream_headers = None
        # #####################################################################
        # status information

        # up-time of the signer, if it can return the value - detection of resets
        self.up_time = 0

        # a flag showing, whether the configuration of the upstream server / crypto providers needs to be updated
        self.stale = True

        # list of readers
        self.readers = dict()
        self.pending_readers = dict()
