# coding: utf-8

"""
    Nomad Envoy

    This is the API descriptor for the Nomad Envoy API, responsible for order creation and product lists.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: paul@samarkand.global
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from nomad_envoy_cli.api_client import ApiClient


class ProductApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_product(self, store, **kwargs):  # noqa: E501
        """Add a product to a store.  # noqa: E501

        Adds a product to store listing.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_product(store, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str store: Add product to store. (required)
        :param Product body: Product details
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_product_with_http_info(store, **kwargs)  # noqa: E501
        else:
            (data) = self.add_product_with_http_info(store, **kwargs)  # noqa: E501
            return data

    def add_product_with_http_info(self, store, **kwargs):  # noqa: E501
        """Add a product to a store.  # noqa: E501

        Adds a product to store listing.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_product_with_http_info(store, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str store: Add product to store. (required)
        :param Product body: Product details
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['store', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_product" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'store' is set
        if ('store' not in params or
                params['store'] is None):
            raise ValueError("Missing the required parameter `store` when calling `add_product`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'store' in params:
            path_params['store'] = params['store']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/product/{store}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_product(self, store, product_id, **kwargs):  # noqa: E501
        """Remove a product from this store.  # noqa: E501

        Remove a product from this store.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_product(store, product_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str store: Store that lists products. (required)
        :param str product_id: ID of product to cancel. (required)
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_product_with_http_info(store, product_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_product_with_http_info(store, product_id, **kwargs)  # noqa: E501
            return data

    def delete_product_with_http_info(self, store, product_id, **kwargs):  # noqa: E501
        """Remove a product from this store.  # noqa: E501

        Remove a product from this store.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_product_with_http_info(store, product_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str store: Store that lists products. (required)
        :param str product_id: ID of product to cancel. (required)
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['store', 'product_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_product" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'store' is set
        if ('store' not in params or
                params['store'] is None):
            raise ValueError("Missing the required parameter `store` when calling `delete_product`")  # noqa: E501
        # verify the required parameter 'product_id' is set
        if ('product_id' not in params or
                params['product_id'] is None):
            raise ValueError("Missing the required parameter `product_id` when calling `delete_product`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'store' in params:
            path_params['store'] = params['store']  # noqa: E501

        query_params = []
        if 'product_id' in params:
            query_params.append(('product_id', params['product_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/product/{store}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_products_by_field(self, store, **kwargs):  # noqa: E501
        """Get a list of products this store supplies.  # noqa: E501

        Requests a list of products store supplies.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_products_by_field(store, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str store: Store to get product list from. (required)
        :param str product_id: product ID for product to get.
        :param str client_product_ref: Client product ref for product to get.
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_products_by_field_with_http_info(store, **kwargs)  # noqa: E501
        else:
            (data) = self.get_products_by_field_with_http_info(store, **kwargs)  # noqa: E501
            return data

    def get_products_by_field_with_http_info(self, store, **kwargs):  # noqa: E501
        """Get a list of products this store supplies.  # noqa: E501

        Requests a list of products store supplies.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_products_by_field_with_http_info(store, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str store: Store to get product list from. (required)
        :param str product_id: product ID for product to get.
        :param str client_product_ref: Client product ref for product to get.
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['store', 'product_id', 'client_product_ref']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_products_by_field" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'store' is set
        if ('store' not in params or
                params['store'] is None):
            raise ValueError("Missing the required parameter `store` when calling `get_products_by_field`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'store' in params:
            path_params['store'] = params['store']  # noqa: E501

        query_params = []
        if 'product_id' in params:
            query_params.append(('product_id', params['product_id']))  # noqa: E501
        if 'client_product_ref' in params:
            query_params.append(('client_product_ref', params['client_product_ref']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/product/{store}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_product(self, store, **kwargs):  # noqa: E501
        """Update a product in a store.  # noqa: E501

        Update a product.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_product(store, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str store: Update product to store. (required)
        :param Product body: Product details
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_product_with_http_info(store, **kwargs)  # noqa: E501
        else:
            (data) = self.update_product_with_http_info(store, **kwargs)  # noqa: E501
            return data

    def update_product_with_http_info(self, store, **kwargs):  # noqa: E501
        """Update a product in a store.  # noqa: E501

        Update a product.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_product_with_http_info(store, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str store: Update product to store. (required)
        :param Product body: Product details
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['store', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_product" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'store' is set
        if ('store' not in params or
                params['store'] is None):
            raise ValueError("Missing the required parameter `store` when calling `update_product`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'store' in params:
            path_params['store'] = params['store']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/product/{store}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
