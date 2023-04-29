"""
    estela API v1.0 Documentation

    estela API Swagger Specification  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""

import re  # noqa: F401
import sys  # noqa: F401

from estela_client.api_client import ApiClient, Endpoint as _Endpoint
from estela_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types,
)
from estela_client.model.inline_response2004 import InlineResponse2004
from estela_client.model.spider_cron_job import SpiderCronJob
from estela_client.model.spider_cron_job_create import SpiderCronJobCreate
from estela_client.model.spider_cron_job_update import SpiderCronJobUpdate

class SpiderCronjobsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.api_projects_spiders_cronjobs_create_endpoint = _Endpoint(
            settings={
                "response_type": (SpiderCronJobCreate,),
                "auth": ["Basic"],
                "endpoint_path": "/api/projects/{pid}/spiders/{sid}/cronjobs",
                "operation_id": "api_projects_spiders_cronjobs_create",
                "http_method": "POST",
                "servers": None,
            },
            params_map={
                "all": [
                    "pid",
                    "sid",
                    "data",
                ],
                "required": [
                    "pid",
                    "sid",
                    "data",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "pid": (str,),
                    "sid": (str,),
                    "data": (SpiderCronJobCreate,),
                },
                "attribute_map": {
                    "pid": "pid",
                    "sid": "sid",
                },
                "location_map": {
                    "pid": "path",
                    "sid": "path",
                    "data": "body",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": ["application/json"],
            },
            api_client=api_client,
        )
        self.api_projects_spiders_cronjobs_delete_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["Basic"],
                "endpoint_path": "/api/projects/{pid}/spiders/{sid}/cronjobs/{cjid}",
                "operation_id": "api_projects_spiders_cronjobs_delete",
                "http_method": "DELETE",
                "servers": None,
            },
            params_map={
                "all": [
                    "cjid",
                    "pid",
                    "sid",
                ],
                "required": [
                    "cjid",
                    "pid",
                    "sid",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "cjid": (int,),
                    "pid": (str,),
                    "sid": (str,),
                },
                "attribute_map": {
                    "cjid": "cjid",
                    "pid": "pid",
                    "sid": "sid",
                },
                "location_map": {
                    "cjid": "path",
                    "pid": "path",
                    "sid": "path",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": [],
                "content_type": [],
            },
            api_client=api_client,
        )
        self.api_projects_spiders_cronjobs_list_endpoint = _Endpoint(
            settings={
                "response_type": (InlineResponse2004,),
                "auth": ["Basic"],
                "endpoint_path": "/api/projects/{pid}/spiders/{sid}/cronjobs",
                "operation_id": "api_projects_spiders_cronjobs_list",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "pid",
                    "sid",
                    "tag",
                    "page",
                    "page_size",
                ],
                "required": [
                    "pid",
                    "sid",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "pid": (str,),
                    "sid": (str,),
                    "tag": (str,),
                    "page": (int,),
                    "page_size": (int,),
                },
                "attribute_map": {
                    "pid": "pid",
                    "sid": "sid",
                    "tag": "tag",
                    "page": "page",
                    "page_size": "page_size",
                },
                "location_map": {
                    "pid": "path",
                    "sid": "path",
                    "tag": "query",
                    "page": "query",
                    "page_size": "query",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )
        self.api_projects_spiders_cronjobs_partial_update_endpoint = _Endpoint(
            settings={
                "response_type": (SpiderCronJob,),
                "auth": ["Basic"],
                "endpoint_path": "/api/projects/{pid}/spiders/{sid}/cronjobs/{cjid}",
                "operation_id": "api_projects_spiders_cronjobs_partial_update",
                "http_method": "PATCH",
                "servers": None,
            },
            params_map={
                "all": [
                    "cjid",
                    "pid",
                    "sid",
                    "data",
                ],
                "required": [
                    "cjid",
                    "pid",
                    "sid",
                    "data",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "cjid": (int,),
                    "pid": (str,),
                    "sid": (str,),
                    "data": (SpiderCronJob,),
                },
                "attribute_map": {
                    "cjid": "cjid",
                    "pid": "pid",
                    "sid": "sid",
                },
                "location_map": {
                    "cjid": "path",
                    "pid": "path",
                    "sid": "path",
                    "data": "body",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": ["application/json"],
            },
            api_client=api_client,
        )
        self.api_projects_spiders_cronjobs_read_endpoint = _Endpoint(
            settings={
                "response_type": (SpiderCronJob,),
                "auth": ["Basic"],
                "endpoint_path": "/api/projects/{pid}/spiders/{sid}/cronjobs/{cjid}",
                "operation_id": "api_projects_spiders_cronjobs_read",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "cjid",
                    "pid",
                    "sid",
                ],
                "required": [
                    "cjid",
                    "pid",
                    "sid",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "cjid": (int,),
                    "pid": (str,),
                    "sid": (str,),
                },
                "attribute_map": {
                    "cjid": "cjid",
                    "pid": "pid",
                    "sid": "sid",
                },
                "location_map": {
                    "cjid": "path",
                    "pid": "path",
                    "sid": "path",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )
        self.api_projects_spiders_cronjobs_run_once_endpoint = _Endpoint(
            settings={
                "response_type": (SpiderCronJob,),
                "auth": ["Basic"],
                "endpoint_path": "/api/projects/{pid}/spiders/{sid}/cronjobs/{cjid}/run_once",
                "operation_id": "api_projects_spiders_cronjobs_run_once",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "cjid",
                    "pid",
                    "sid",
                ],
                "required": [
                    "cjid",
                    "pid",
                    "sid",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "cjid": (int,),
                    "pid": (str,),
                    "sid": (str,),
                },
                "attribute_map": {
                    "cjid": "cjid",
                    "pid": "pid",
                    "sid": "sid",
                },
                "location_map": {
                    "cjid": "path",
                    "pid": "path",
                    "sid": "path",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )
        self.api_projects_spiders_cronjobs_update_endpoint = _Endpoint(
            settings={
                "response_type": (SpiderCronJobUpdate,),
                "auth": ["Basic"],
                "endpoint_path": "/api/projects/{pid}/spiders/{sid}/cronjobs/{cjid}",
                "operation_id": "api_projects_spiders_cronjobs_update",
                "http_method": "PUT",
                "servers": None,
            },
            params_map={
                "all": [
                    "cjid",
                    "pid",
                    "sid",
                    "data",
                ],
                "required": [
                    "cjid",
                    "pid",
                    "sid",
                    "data",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "cjid": (int,),
                    "pid": (str,),
                    "sid": (str,),
                    "data": (SpiderCronJobUpdate,),
                },
                "attribute_map": {
                    "cjid": "cjid",
                    "pid": "pid",
                    "sid": "sid",
                },
                "location_map": {
                    "cjid": "path",
                    "pid": "path",
                    "sid": "path",
                    "data": "body",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": ["application/json"],
            },
            api_client=api_client,
        )
    def api_projects_spiders_cronjobs_create(self, pid, sid, data, **kwargs):
        """api_projects_spiders_cronjobs_create  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_projects_spiders_cronjobs_create(pid, sid, data, async_req=True)
        >>> result = thread.get()

        Args:
            pid (str):
            sid (str):
            data (SpiderCronJobCreate):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            SpiderCronJobCreate
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["_request_auths"] = kwargs.get("_request_auths", None)
        kwargs["pid"] = pid
        kwargs["sid"] = sid
        kwargs["data"] = data
        return self.api_projects_spiders_cronjobs_create_endpoint.call_with_http_info(
            **kwargs
        )
    def api_projects_spiders_cronjobs_delete(self, cjid, pid, sid, **kwargs):
        """api_projects_spiders_cronjobs_delete  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_projects_spiders_cronjobs_delete(cjid, pid, sid, async_req=True)
        >>> result = thread.get()

        Args:
            cjid (int): A unique integer value identifying this cron job.
            pid (str):
            sid (str):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["_request_auths"] = kwargs.get("_request_auths", None)
        kwargs["cjid"] = cjid
        kwargs["pid"] = pid
        kwargs["sid"] = sid
        return self.api_projects_spiders_cronjobs_delete_endpoint.call_with_http_info(
            **kwargs
        )
    def api_projects_spiders_cronjobs_list(self, pid, sid, **kwargs):
        """api_projects_spiders_cronjobs_list  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_projects_spiders_cronjobs_list(pid, sid, async_req=True)
        >>> result = thread.get()

        Args:
            pid (str):
            sid (str):

        Keyword Args:
            tag (str): Cron job tag.. [optional]
            page (int): A page number within the paginated result set.. [optional]
            page_size (int): Number of results to return per page.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InlineResponse2004
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["_request_auths"] = kwargs.get("_request_auths", None)
        kwargs["pid"] = pid
        kwargs["sid"] = sid
        return self.api_projects_spiders_cronjobs_list_endpoint.call_with_http_info(
            **kwargs
        )
    def api_projects_spiders_cronjobs_partial_update(
        self, cjid, pid, sid, data, **kwargs
    ):
        """api_projects_spiders_cronjobs_partial_update  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_projects_spiders_cronjobs_partial_update(cjid, pid, sid, data, async_req=True)
        >>> result = thread.get()

        Args:
            cjid (int): A unique integer value identifying this cron job.
            pid (str):
            sid (str):
            data (SpiderCronJob):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            SpiderCronJob
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["_request_auths"] = kwargs.get("_request_auths", None)
        kwargs["cjid"] = cjid
        kwargs["pid"] = pid
        kwargs["sid"] = sid
        kwargs["data"] = data
        return self.api_projects_spiders_cronjobs_partial_update_endpoint.call_with_http_info(
            **kwargs
        )
    def api_projects_spiders_cronjobs_read(self, cjid, pid, sid, **kwargs):
        """api_projects_spiders_cronjobs_read  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_projects_spiders_cronjobs_read(cjid, pid, sid, async_req=True)
        >>> result = thread.get()

        Args:
            cjid (int): A unique integer value identifying this cron job.
            pid (str):
            sid (str):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            SpiderCronJob
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["_request_auths"] = kwargs.get("_request_auths", None)
        kwargs["cjid"] = cjid
        kwargs["pid"] = pid
        kwargs["sid"] = sid
        return self.api_projects_spiders_cronjobs_read_endpoint.call_with_http_info(
            **kwargs
        )
    def api_projects_spiders_cronjobs_run_once(self, cjid, pid, sid, **kwargs):
        """api_projects_spiders_cronjobs_run_once  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_projects_spiders_cronjobs_run_once(cjid, pid, sid, async_req=True)
        >>> result = thread.get()

        Args:
            cjid (int): A unique integer value identifying this cron job.
            pid (str):
            sid (str):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            SpiderCronJob
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["_request_auths"] = kwargs.get("_request_auths", None)
        kwargs["cjid"] = cjid
        kwargs["pid"] = pid
        kwargs["sid"] = sid
        return self.api_projects_spiders_cronjobs_run_once_endpoint.call_with_http_info(
            **kwargs
        )
    def api_projects_spiders_cronjobs_update(self, cjid, pid, sid, data, **kwargs):
        """api_projects_spiders_cronjobs_update  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_projects_spiders_cronjobs_update(cjid, pid, sid, data, async_req=True)
        >>> result = thread.get()

        Args:
            cjid (int): A unique integer value identifying this cron job.
            pid (str):
            sid (str):
            data (SpiderCronJobUpdate):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            SpiderCronJobUpdate
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["_request_auths"] = kwargs.get("_request_auths", None)
        kwargs["cjid"] = cjid
        kwargs["pid"] = pid
        kwargs["sid"] = sid
        kwargs["data"] = data
        return self.api_projects_spiders_cronjobs_update_endpoint.call_with_http_info(
            **kwargs
        )
