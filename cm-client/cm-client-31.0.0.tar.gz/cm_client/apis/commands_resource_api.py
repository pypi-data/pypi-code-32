# coding: utf-8

"""
    Cloudera Manager API

    <h1>Cloudera Manager API v31</h1>       <p>Introduced in Cloudera Manager 6.1.0</p>       <p><a href=\"http://www.cloudera.com/documentation.html\">Cloudera Product Documentation</a></p>

    OpenAPI spec version: 6.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class CommandsResourceApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def abort_command(self, command_id, **kwargs):
        """
        Abort a running command.
        Abort a running command.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.abort_command(command_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param float command_id: The command id. (required)
        :return: ApiCommand
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.abort_command_with_http_info(command_id, **kwargs)
        else:
            (data) = self.abort_command_with_http_info(command_id, **kwargs)
            return data

    def abort_command_with_http_info(self, command_id, **kwargs):
        """
        Abort a running command.
        Abort a running command.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.abort_command_with_http_info(command_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param float command_id: The command id. (required)
        :return: ApiCommand
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['command_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method abort_command" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'command_id' is set
        if ('command_id' not in params) or (params['command_id'] is None):
            raise ValueError("Missing the required parameter `command_id` when calling `abort_command`")


        collection_formats = {}

        path_params = {}
        if 'command_id' in params:
            path_params['commandId'] = params['command_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['basic']

        return self.api_client.call_api('/commands/{commandId}/abort', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ApiCommand',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def read_command(self, command_id, **kwargs):
        """
        Retrieve detailed information on an asynchronous command.
        Retrieve detailed information on an asynchronous command.  <p>Cloudera Manager keeps the results and statuses of asynchronous commands, which have non-negative command IDs. On the other hand, synchronous commands complete immediately, and their results are passed back in the return object of the command execution API call. Outside of that return object, there is no way to check the result of a synchronous command.</p>
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.read_command(command_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param float command_id: The command id. (required)
        :return: ApiCommand
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.read_command_with_http_info(command_id, **kwargs)
        else:
            (data) = self.read_command_with_http_info(command_id, **kwargs)
            return data

    def read_command_with_http_info(self, command_id, **kwargs):
        """
        Retrieve detailed information on an asynchronous command.
        Retrieve detailed information on an asynchronous command.  <p>Cloudera Manager keeps the results and statuses of asynchronous commands, which have non-negative command IDs. On the other hand, synchronous commands complete immediately, and their results are passed back in the return object of the command execution API call. Outside of that return object, there is no way to check the result of a synchronous command.</p>
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.read_command_with_http_info(command_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param float command_id: The command id. (required)
        :return: ApiCommand
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['command_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method read_command" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'command_id' is set
        if ('command_id' not in params) or (params['command_id'] is None):
            raise ValueError("Missing the required parameter `command_id` when calling `read_command`")


        collection_formats = {}

        path_params = {}
        if 'command_id' in params:
            path_params['commandId'] = params['command_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['basic']

        return self.api_client.call_api('/commands/{commandId}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ApiCommand',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def retry(self, command_id, **kwargs):
        """
        Try to rerun a command.
        Try to rerun a command.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.retry(command_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param float command_id: ID of the command that needs to be run. (required)
        :return: ApiCommand
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.retry_with_http_info(command_id, **kwargs)
        else:
            (data) = self.retry_with_http_info(command_id, **kwargs)
            return data

    def retry_with_http_info(self, command_id, **kwargs):
        """
        Try to rerun a command.
        Try to rerun a command.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.retry_with_http_info(command_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param float command_id: ID of the command that needs to be run. (required)
        :return: ApiCommand
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['command_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retry" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'command_id' is set
        if ('command_id' not in params) or (params['command_id'] is None):
            raise ValueError("Missing the required parameter `command_id` when calling `retry`")


        collection_formats = {}

        path_params = {}
        if 'command_id' in params:
            path_params['commandId'] = params['command_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['basic']

        return self.api_client.call_api('/commands/{commandId}/retry', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ApiCommand',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
