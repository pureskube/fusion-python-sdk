# coding: utf-8

"""
    Pure Fusion API

    Pure Fusion is fully API-driven. Most APIs which change the system (POST, PATCH, DELETE) return an Operation in status \"Pending\" or \"Running\". You can poll (GET) the operation to check its status, waiting for it to change to \"Succeeded\" or \"Failed\".   # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from fusion.api_client import ApiClient


class AvailabilityZonesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_availability_zone(self, body, region_name, **kwargs):  # noqa: E501
        """Creates an Availability Zone.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_availability_zone(body, region_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AvailabilityZonePost body: (required)
        :param str region_name: The Region name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Operation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_availability_zone_with_http_info(body, region_name, **kwargs)  # noqa: E501
        else:
            (data) = self.create_availability_zone_with_http_info(body, region_name, **kwargs)  # noqa: E501
            return data

    def create_availability_zone_with_http_info(self, body, region_name, **kwargs):  # noqa: E501
        """Creates an Availability Zone.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_availability_zone_with_http_info(body, region_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AvailabilityZonePost body: (required)
        :param str region_name: The Region name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Operation
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'region_name', 'x_request_id', 'authorization', 'x_correlation_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_availability_zone" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_availability_zone`")  # noqa: E501
        # verify the required parameter 'region_name' is set
        if ('region_name' not in params or
                params['region_name'] is None):
            raise ValueError("Missing the required parameter `region_name` when calling `create_availability_zone`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'region_name' in params:
            path_params['region_name'] = params['region_name']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_request_id' in params:
            header_params['X-Request-ID'] = params['x_request_id']  # noqa: E501
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'x_correlation_id' in params:
            header_params['X-Correlation-ID'] = params['x_correlation_id']  # noqa: E501

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
        auth_settings = ['accessToken', 'oauth']  # noqa: E501

        return self.api_client.call_api(
            '/regions/{region_name}/availability-zones', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Operation',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_availability_zone(self, region_name, availability_zone_name, **kwargs):  # noqa: E501
        """Deletes a specific Availability Zone.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_availability_zone(region_name, availability_zone_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str region_name: The Region name (required)
        :param str availability_zone_name: The Availability Zone name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Operation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_availability_zone_with_http_info(region_name, availability_zone_name, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_availability_zone_with_http_info(region_name, availability_zone_name, **kwargs)  # noqa: E501
            return data

    def delete_availability_zone_with_http_info(self, region_name, availability_zone_name, **kwargs):  # noqa: E501
        """Deletes a specific Availability Zone.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_availability_zone_with_http_info(region_name, availability_zone_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str region_name: The Region name (required)
        :param str availability_zone_name: The Availability Zone name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Operation
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['region_name', 'availability_zone_name', 'x_request_id', 'authorization', 'x_correlation_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_availability_zone" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'region_name' is set
        if ('region_name' not in params or
                params['region_name'] is None):
            raise ValueError("Missing the required parameter `region_name` when calling `delete_availability_zone`")  # noqa: E501
        # verify the required parameter 'availability_zone_name' is set
        if ('availability_zone_name' not in params or
                params['availability_zone_name'] is None):
            raise ValueError("Missing the required parameter `availability_zone_name` when calling `delete_availability_zone`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'region_name' in params:
            path_params['region_name'] = params['region_name']  # noqa: E501
        if 'availability_zone_name' in params:
            path_params['availability_zone_name'] = params['availability_zone_name']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_request_id' in params:
            header_params['X-Request-ID'] = params['x_request_id']  # noqa: E501
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'x_correlation_id' in params:
            header_params['X-Correlation-ID'] = params['x_correlation_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['accessToken', 'oauth']  # noqa: E501

        return self.api_client.call_api(
            '/regions/{region_name}/availability-zones/{availability_zone_name}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Operation',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_availability_zone(self, region_name, availability_zone_name, **kwargs):  # noqa: E501
        """Gets a specific Availability Zone.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_availability_zone(region_name, availability_zone_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str region_name: The Region name (required)
        :param str availability_zone_name: The Availability Zone name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: AvailabilityZone
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_availability_zone_with_http_info(region_name, availability_zone_name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_availability_zone_with_http_info(region_name, availability_zone_name, **kwargs)  # noqa: E501
            return data

    def get_availability_zone_with_http_info(self, region_name, availability_zone_name, **kwargs):  # noqa: E501
        """Gets a specific Availability Zone.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_availability_zone_with_http_info(region_name, availability_zone_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str region_name: The Region name (required)
        :param str availability_zone_name: The Availability Zone name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: AvailabilityZone
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['region_name', 'availability_zone_name', 'x_request_id', 'authorization', 'x_correlation_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_availability_zone" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'region_name' is set
        if ('region_name' not in params or
                params['region_name'] is None):
            raise ValueError("Missing the required parameter `region_name` when calling `get_availability_zone`")  # noqa: E501
        # verify the required parameter 'availability_zone_name' is set
        if ('availability_zone_name' not in params or
                params['availability_zone_name'] is None):
            raise ValueError("Missing the required parameter `availability_zone_name` when calling `get_availability_zone`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'region_name' in params:
            path_params['region_name'] = params['region_name']  # noqa: E501
        if 'availability_zone_name' in params:
            path_params['availability_zone_name'] = params['availability_zone_name']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_request_id' in params:
            header_params['X-Request-ID'] = params['x_request_id']  # noqa: E501
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'x_correlation_id' in params:
            header_params['X-Correlation-ID'] = params['x_correlation_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['accessToken', 'oauth']  # noqa: E501

        return self.api_client.call_api(
            '/regions/{region_name}/availability-zones/{availability_zone_name}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AvailabilityZone',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_availability_zone_by_id(self, availability_zone_id, **kwargs):  # noqa: E501
        """Gets a specific Availability Zone.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_availability_zone_by_id(availability_zone_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str availability_zone_id: The Availability Zone ID (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: AvailabilityZone
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_availability_zone_by_id_with_http_info(availability_zone_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_availability_zone_by_id_with_http_info(availability_zone_id, **kwargs)  # noqa: E501
            return data

    def get_availability_zone_by_id_with_http_info(self, availability_zone_id, **kwargs):  # noqa: E501
        """Gets a specific Availability Zone.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_availability_zone_by_id_with_http_info(availability_zone_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str availability_zone_id: The Availability Zone ID (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: AvailabilityZone
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['availability_zone_id', 'x_request_id', 'authorization', 'x_correlation_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_availability_zone_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'availability_zone_id' is set
        if ('availability_zone_id' not in params or
                params['availability_zone_id'] is None):
            raise ValueError("Missing the required parameter `availability_zone_id` when calling `get_availability_zone_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'availability_zone_id' in params:
            path_params['availability_zone_id'] = params['availability_zone_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_request_id' in params:
            header_params['X-Request-ID'] = params['x_request_id']  # noqa: E501
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'x_correlation_id' in params:
            header_params['X-Correlation-ID'] = params['x_correlation_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['accessToken', 'oauth']  # noqa: E501

        return self.api_client.call_api(
            '/resources/availability-zones/{availability_zone_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AvailabilityZone',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_availability_zones(self, region_name, **kwargs):  # noqa: E501
        """Gets a list of all Availability Zones.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_availability_zones(region_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str region_name: The Region name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: AvailabilityZoneList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_availability_zones_with_http_info(region_name, **kwargs)  # noqa: E501
        else:
            (data) = self.list_availability_zones_with_http_info(region_name, **kwargs)  # noqa: E501
            return data

    def list_availability_zones_with_http_info(self, region_name, **kwargs):  # noqa: E501
        """Gets a list of all Availability Zones.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_availability_zones_with_http_info(region_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str region_name: The Region name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: AvailabilityZoneList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['region_name', 'x_request_id', 'authorization', 'x_correlation_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_availability_zones" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'region_name' is set
        if ('region_name' not in params or
                params['region_name'] is None):
            raise ValueError("Missing the required parameter `region_name` when calling `list_availability_zones`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'region_name' in params:
            path_params['region_name'] = params['region_name']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_request_id' in params:
            header_params['X-Request-ID'] = params['x_request_id']  # noqa: E501
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'x_correlation_id' in params:
            header_params['X-Correlation-ID'] = params['x_correlation_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['accessToken', 'oauth']  # noqa: E501

        return self.api_client.call_api(
            '/regions/{region_name}/availability-zones', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AvailabilityZoneList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
