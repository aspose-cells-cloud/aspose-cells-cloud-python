# coding: utf-8

"""
Copyright (c) 2021 Aspose.Cells Cloud
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all 
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
"""


from __future__ import absolute_import

import sys
import os
import re
import time
import warnings

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class LiteCellsApi(object):

    def __init__(self,clientid, clientsecret, version='v3.0', base_uri= 'https://api.aspose.cloud', api_client=None):
        warnings.warn("LiteCellsApi is deprecated", DeprecationWarning)
        self.clientid = clientid
        self.clientsecret = clientsecret
        self.version = version 
        if base_uri[-1] == '/' :
            self.base_uri = base_uri[0:len(base_uri)-1]
        else:
            self.base_uri = base_uri
        
        if not clientid or not clientsecret  : 
            self.needAuth = False
        else:
            self.needAuth = True

        self.api_client =  ApiClient(base_uri)
        if self.needAuth :
            self.access_token = self.api_client.get_access_token("client_credentials", clientid, clientsecret,version)
        
        config = Configuration()
        config.host = self.base_uri +'/' + self.version
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client
        if self.needAuth :            
            self.api_client.set_default_header("Authorization", "Bearer " + self.access_token)
        self.get_access_token_time =  time.process_time()
        

    def check_access_token(self):
        warnings.warn("LiteCellsApi is deprecated", DeprecationWarning)
        if self.needAuth :
            if self.access_token:
                timediff =  time.process_time() - self.get_access_token_time
                if timediff > 86300 :
                    api_client =  ApiClient(self.base_uri)
                    self.access_token = api_client.get_access_token("client_credentials", self.clientid, self.clientsecret,self.version)
                    self.api_client.set_default_header("Authorization", "Bearer " + self.access_token)
                    self.get_access_token_time =  time.process_time()

    def delete_metadata(self, file, **kwargs):
        """
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_metadata(file, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param file file: File to upload (required)
        :param str type:
        :return: FilesResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.delete_metadata_with_http_info(file, **kwargs)
        else:
            (data) = self.delete_metadata_with_http_info(file, **kwargs)
            return data

    def delete_metadata_with_http_info(self, file, **kwargs):
        """
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_metadata_with_http_info(file, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param file file: File to upload (required)
        :param str type:
        :return: FilesResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['file', 'type']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_metadata" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file' is set
        if ('file' not in params) or (params['file'] is None):
            raise ValueError("Missing the required parameter `file` when calling `delete_metadata`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'type' in params:
            query_params.append(('type', params['type']))

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'file' in params:
            
            if isinstance(params['file'],dict):
                for filename , filecontext in  params['file'].items():
                    local_var_files[filename] = filecontext
            else:
                local_var_files['File'] = params['file']            


        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['multipart/form-data'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/cells/metadata/delete', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='FilesResult',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_metadata(self, file, **kwargs):
        """
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_metadata(file, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param file file: File to upload (required)
        :param str type:
        :return: list[CellsDocumentProperty]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_metadata_with_http_info(file, **kwargs)
        else:
            (data) = self.get_metadata_with_http_info(file, **kwargs)
            return data

    def get_metadata_with_http_info(self, file, **kwargs):
        """
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_metadata_with_http_info(file, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param file file: File to upload (required)
        :param str type:
        :return: list[CellsDocumentProperty]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['file', 'type']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_metadata" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file' is set
        if ('file' not in params) or (params['file'] is None):
            raise ValueError("Missing the required parameter `file` when calling `get_metadata`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'type' in params:
            query_params.append(('type', params['type']))

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'file' in params:
            
            if isinstance(params['file'],dict):
                for filename , filecontext in  params['file'].items():
                    local_var_files[filename] = filecontext
            else:
                local_var_files['File'] = params['file']            


        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['multipart/form-data'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/cells/metadata/get', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[CellsDocumentProperty]',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def post_assemble(self, file, datasource, **kwargs):
        """
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_assemble(file, datasource, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param file file: File to upload (required)
        :param str datasource: (required)
        :param str format:
        :return: FilesResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_assemble_with_http_info(file, datasource, **kwargs)
        else:
            (data) = self.post_assemble_with_http_info(file, datasource, **kwargs)
            return data

    def post_assemble_with_http_info(self, file, datasource, **kwargs):
        """
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_assemble_with_http_info(file, datasource, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param file file: File to upload (required)
        :param str datasource: (required)
        :param str format:
        :return: FilesResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['file', 'datasource', 'format']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_assemble" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file' is set
        if ('file' not in params) or (params['file'] is None):
            raise ValueError("Missing the required parameter `file` when calling `post_assemble`")
        # verify the required parameter 'datasource' is set
        if ('datasource' not in params) or (params['datasource'] is None):
            raise ValueError("Missing the required parameter `datasource` when calling `post_assemble`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'datasource' in params:
            query_params.append(('datasource', params['datasource']))
        if 'format' in params:
            query_params.append(('format', params['format']))

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'file' in params:
            
            if isinstance(params['file'],dict):
                for filename , filecontext in  params['file'].items():
                    local_var_files[filename] = filecontext
            else:
                local_var_files['File'] = params['file']            


        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['multipart/form-data'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/cells/assemble', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='FilesResult',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def post_clear_objects(self, file, objecttype, **kwargs):
        """
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_clear_objects(file, objecttype, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param file file: File to upload (required)
        :param str objecttype: (required)
        :return: FilesResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_clear_objects_with_http_info(file, objecttype, **kwargs)
        else:
            (data) = self.post_clear_objects_with_http_info(file, objecttype, **kwargs)
            return data

    def post_clear_objects_with_http_info(self, file, objecttype, **kwargs):
        """
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_clear_objects_with_http_info(file, objecttype, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param file file: File to upload (required)
        :param str objecttype: (required)
        :return: FilesResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['file', 'objecttype']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_clear_objects" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file' is set
        if ('file' not in params) or (params['file'] is None):
            raise ValueError("Missing the required parameter `file` when calling `post_clear_objects`")
        # verify the required parameter 'objecttype' is set
        if ('objecttype' not in params) or (params['objecttype'] is None):
            raise ValueError("Missing the required parameter `objecttype` when calling `post_clear_objects`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'objecttype' in params:
            query_params.append(('objecttype', params['objecttype']))

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'file' in params:
            
            if isinstance(params['file'],dict):
                for filename , filecontext in  params['file'].items():
                    local_var_files[filename] = filecontext
            else:
                local_var_files['File'] = params['file']            


        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['multipart/form-data'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/cells/clearobjects', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='FilesResult',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def post_export(self, file, object_type, format, **kwargs):
        """
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_export(file, object_type, format, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param file file: File to upload (required)
        :param str object_type: (required)
        :param str format: (required)
        :return: FilesResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_export_with_http_info(file, object_type, format, **kwargs)
        else:
            (data) = self.post_export_with_http_info(file, object_type, format, **kwargs)
            return data

    def post_export_with_http_info(self, file, object_type, format, **kwargs):
        """
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_export_with_http_info(file, object_type, format, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param file file: File to upload (required)
        :param str object_type: (required)
        :param str format: (required)
        :return: FilesResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['file', 'object_type', 'format']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_export" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file' is set
        if ('file' not in params) or (params['file'] is None):
            raise ValueError("Missing the required parameter `file` when calling `post_export`")
        # verify the required parameter 'object_type' is set
        if ('object_type' not in params) or (params['object_type'] is None):
            raise ValueError("Missing the required parameter `object_type` when calling `post_export`")
        # verify the required parameter 'format' is set
        if ('format' not in params) or (params['format'] is None):
            raise ValueError("Missing the required parameter `format` when calling `post_export`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'object_type' in params:
            query_params.append(('objectType', params['object_type']))
        if 'format' in params:
            query_params.append(('format', params['format']))

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'file' in params:
            
            if isinstance(params['file'],dict):
                for filename , filecontext in  params['file'].items():
                    local_var_files[filename] = filecontext
            else:
                local_var_files['File'] = params['file']            


        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['multipart/form-data'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/cells/export', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='FilesResult',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def post_import(self, file, import_data, **kwargs):
        """
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_import(file, import_data, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param file file: File to upload (required)
        :param ImportOption import_data: (required)
        :return: FilesResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_import_with_http_info(file, import_data, **kwargs)
        else:
            (data) = self.post_import_with_http_info(file, import_data, **kwargs)
            return data

    def post_import_with_http_info(self, file, import_data, **kwargs):
        """
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_import_with_http_info(file, import_data, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param file file: File to upload (required)
        :param ImportOption import_data: (required)
        :return: FilesResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['file', 'import_data']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_import" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file' is set
        if ('file' not in params) or (params['file'] is None):
            raise ValueError("Missing the required parameter `file` when calling `post_import`")
        # verify the required parameter 'import_data' is set
        if ('import_data' not in params) or (params['import_data'] is None):
            raise ValueError("Missing the required parameter `import_data` when calling `post_import`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'file' in params:
            
            if isinstance(params['file'],dict):
                for filename , filecontext in  params['file'].items():
                    local_var_files[filename] = filecontext
            else:
                local_var_files['file'] = params['file']            


        body_params = None
        if 'import_data' in params:
            body_params = params['import_data']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['multipart/form-data'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/cells/import', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='FilesResult',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
                                        
    def post_merge(self, file, **kwargs):
        """
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_merge(file, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param file file: File to upload (required)
        :param str format:
        :param bool merge_to_one_sheet:
        :return: FileInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_merge_with_http_info(file, **kwargs)
        else:
            (data) = self.post_merge_with_http_info(file, **kwargs)
            return data

    def post_merge_with_http_info(self, file, **kwargs):
        """
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_merge_with_http_info(file, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param file file: File to upload (required)
        :param str format:
        :param bool merge_to_one_sheet:
        :return: FileInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['file', 'format', 'merge_to_one_sheet']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_merge" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file' is set
        if ('file' not in params) or (params['file'] is None):
            raise ValueError("Missing the required parameter `file` when calling `post_merge`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'format' in params:
            query_params.append(('format', params['format']))
        if 'merge_to_one_sheet' in params:
            query_params.append(('mergeToOneSheet', params['merge_to_one_sheet']))

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'file' in params:
            
            if isinstance(params['file'],dict):
                for filename , filecontext in  params['file'].items():
                    local_var_files[filename] = filecontext
            else:
                local_var_files['File'] = params['file']            


        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['multipart/form-data'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/cells/merge', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='FileInfo',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def post_metadata(self, file, document_properties, **kwargs):
        """
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_metadata(file, document_properties, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param file file: File to upload (required)
        :param CellsDocumentProperty document_properties: Cells document property. (required)
        :return: FilesResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_metadata_with_http_info(file, document_properties, **kwargs)
        else:
            (data) = self.post_metadata_with_http_info(file, document_properties, **kwargs)
            return data

    def post_metadata_with_http_info(self, file, document_properties, **kwargs):
        """
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_metadata_with_http_info(file, document_properties, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param file file: File to upload (required)
        :param CellsDocumentProperty document_properties: Cells document property. (required)
        :return: FilesResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['file', 'document_properties']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_metadata" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file' is set
        if ('file' not in params) or (params['file'] is None):
            raise ValueError("Missing the required parameter `file` when calling `post_metadata`")
        # verify the required parameter 'document_properties' is set
        if ('document_properties' not in params) or (params['document_properties'] is None):
            raise ValueError("Missing the required parameter `document_properties` when calling `post_metadata`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'file' in params:
            
            if isinstance(params['file'],dict):
                for filename , filecontext in  params['file'].items():
                    local_var_files[filename] = filecontext
            else:
                local_var_files['File'] = params['file']            


        body_params = None
        if 'document_properties' in params:
            # form_params['documentproperties'] = tuple(['documentproperties', self.api_client.sanitize_for_serialization( params['document_properties']), 'application/json'])
            form_params.append(tuple(["documentproperties", tuple(["documentproperties",repr(self.api_client.sanitize_for_serialization( params['document_properties'])) , ""])]))            
                       
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['multipart/form-data'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['multipart/form-data'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/cells/metadata/update', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='FilesResult',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def post_protect(self, file, password, **kwargs):
        """
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_protect(file, password, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param file file: File to upload (required)
        :param str password: (required)
        :return: FilesResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_protect_with_http_info(file, password, **kwargs)
        else:
            (data) = self.post_protect_with_http_info(file, password, **kwargs)
            return data

    def post_protect_with_http_info(self, file, password, **kwargs):
        """
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_protect_with_http_info(file, password, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param file file: File to upload (required)
        :param str password: (required)
        :return: FilesResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['file', 'password']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_protect" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file' is set
        if ('file' not in params) or (params['file'] is None):
            raise ValueError("Missing the required parameter `file` when calling `post_protect`")
        # verify the required parameter 'password' is set
        if ('password' not in params) or (params['password'] is None):
            raise ValueError("Missing the required parameter `password` when calling `post_protect`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'password' in params:
            query_params.append(('password', params['password']))

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'file' in params:
            
            if isinstance(params['file'],dict):
                for filename , filecontext in  params['file'].items():
                    local_var_files[filename] = filecontext
            else:
                local_var_files['File'] = params['file']            


        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['multipart/form-data'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/cells/protect', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='FilesResult',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def post_search(self, file, text, **kwargs):
        """
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_search(file, text, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param file file: File to upload (required)
        :param str text: (required)
        :param str password:
        :param str sheetname:
        :return: list[TextItem]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_search_with_http_info(file, text, **kwargs)
        else:
            (data) = self.post_search_with_http_info(file, text, **kwargs)
            return data

    def post_search_with_http_info(self, file, text, **kwargs):
        """
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_search_with_http_info(file, text, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param file file: File to upload (required)
        :param str text: (required)
        :param str password:
        :param str sheetname:
        :return: list[TextItem]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['file', 'text', 'password', 'sheetname']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_search" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file' is set
        if ('file' not in params) or (params['file'] is None):
            raise ValueError("Missing the required parameter `file` when calling `post_search`")
        # verify the required parameter 'text' is set
        if ('text' not in params) or (params['text'] is None):
            raise ValueError("Missing the required parameter `text` when calling `post_search`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'text' in params:
            query_params.append(('text', params['text']))
        if 'password' in params:
            query_params.append(('password', params['password']))
        if 'sheetname' in params:
            query_params.append(('sheetname', params['sheetname']))


        header_params = {}

        form_params = []
        local_var_files = {}
        if 'file' in params:
            
            if isinstance(params['file'],dict):
                for filename , filecontext in  params['file'].items():
                    local_var_files[filename] = filecontext
            else:
                local_var_files['File'] = params['file']            


        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['multipart/form-data'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/cells/search', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[TextItem]',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def post_split(self, file, format, **kwargs):
        """
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_split(file, format, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param file file: File to upload (required)
        :param str format: (required)
        :param str password:
        :param int _from:
        :param int to:
        :return: FilesResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_split_with_http_info(file, format, **kwargs)
        else:
            (data) = self.post_split_with_http_info(file, format, **kwargs)
            return data

    def post_split_with_http_info(self, file, format, **kwargs):
        """
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_split_with_http_info(file, format, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param file file: File to upload (required)
        :param str format: (required)
        :param str password:
        :param int _from:
        :param int to:
        :return: FilesResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['file', 'format', 'password', '_from', 'to']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_split" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file' is set
        if ('file' not in params) or (params['file'] is None):
            raise ValueError("Missing the required parameter `file` when calling `post_split`")
        # verify the required parameter 'format' is set
        if ('format' not in params) or (params['format'] is None):
            raise ValueError("Missing the required parameter `format` when calling `post_split`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'format' in params:
            query_params.append(('format', params['format']))
        if 'password' in params:
            query_params.append(('password', params['password']))
        if '_from' in params:
            query_params.append(('from', params['_from']))
        if 'to' in params:
            query_params.append(('to', params['to']))

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'file' in params:
            
            if isinstance(params['file'],dict):
                for filename , filecontext in  params['file'].items():
                    local_var_files[filename] = filecontext
            else:
                local_var_files['File'] = params['file']            


        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['multipart/form-data'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/cells/split', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='FilesResult',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def post_unlock(self, file, password, **kwargs):
        """
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_unlock(file, password, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param file file: File to upload (required)
        :param str password: (required)
        :return: FilesResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_unlock_with_http_info(file, password, **kwargs)
        else:
            (data) = self.post_unlock_with_http_info(file, password, **kwargs)
            return data

    def post_unlock_with_http_info(self, file, password, **kwargs):
        """
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_unlock_with_http_info(file, password, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param file file: File to upload (required)
        :param str password: (required)
        :return: FilesResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['file', 'password']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_unlock" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file' is set
        if ('file' not in params) or (params['file'] is None):
            raise ValueError("Missing the required parameter `file` when calling `post_unlock`")
        # verify the required parameter 'password' is set
        if ('password' not in params) or (params['password'] is None):
            raise ValueError("Missing the required parameter `password` when calling `post_unlock`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'password' in params:
            query_params.append(('password', params['password']))

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'file' in params:
            
            if isinstance(params['file'],dict):
                for filename , filecontext in  params['file'].items():
                    local_var_files[filename] = filecontext
            else:
                local_var_files['File'] = params['file']            


        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['multipart/form-data'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/cells/unlock', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='FilesResult',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def post_watermark(self, file, text, color, **kwargs):
        """
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_watermark(file, text, color, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param file file: File to upload (required)
        :param str text: (required)
        :param str color: (required)
        :return: FilesResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_watermark_with_http_info(file, text, color, **kwargs)
        else:
            (data) = self.post_watermark_with_http_info(file, text, color, **kwargs)
            return data

    def post_watermark_with_http_info(self, file, text, color, **kwargs):
        """
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_watermark_with_http_info(file, text, color, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param file file: File to upload (required)
        :param str text: (required)
        :param str color: (required)
        :return: FilesResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['file', 'text', 'color']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_watermark" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file' is set
        if ('file' not in params) or (params['file'] is None):
            raise ValueError("Missing the required parameter `file` when calling `post_watermark`")
        # verify the required parameter 'text' is set
        if ('text' not in params) or (params['text'] is None):
            raise ValueError("Missing the required parameter `text` when calling `post_watermark`")
        # verify the required parameter 'color' is set
        if ('color' not in params) or (params['color'] is None):
            raise ValueError("Missing the required parameter `color` when calling `post_watermark`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'text' in params:
            query_params.append(('text', params['text']))
        if 'color' in params:
            query_params.append(('color', params['color']))

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'file' in params:
            
            if isinstance(params['file'],dict):
                for filename , filecontext in  params['file'].items():
                    local_var_files[filename] = filecontext
            else:
                local_var_files['File'] = params['file']            


        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['multipart/form-data'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/cells/watermark', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='FilesResult',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def post_compress(self, file, compress_level,  **kwargs):
        """
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_compress(file, compress_level, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param file file: File to upload (required)
        :param int compress_level: (required)
        :return: FilesResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_compress_with_http_info(file, compress_level, **kwargs)
        else:
            (data) = self.post_compress_with_http_info(file, compress_level, **kwargs)
            return data

    def post_compress_with_http_info(self, file, compress_level, **kwargs):
        """
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_compress_with_http_info(file, compress_level, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param file file: File to upload (required)
        :param int compress_level: (required)
        :return: FilesResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['file', 'compress_level']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_compress" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file' is set
        if ('file' not in params) or (params['file'] is None):
            raise ValueError("Missing the required parameter `file` when calling `post_compress`")
        # verify the required parameter 'compress_level' is set
        if ('compress_level' not in params) or (params['compress_level'] is None):
            raise ValueError("Missing the required parameter `compress_level` when calling `post_compress`")
        


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'compress_level' in params:
            query_params.append(('compressLevel', params['compress_level']))
        

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'file' in params:
            
            if isinstance(params['file'],dict):
                for filename , filecontext in  params['file'].items():
                    local_var_files[filename] = filecontext
            else:
                local_var_files['File'] = params['file']            


        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['multipart/form-data'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/cells/compress', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='FilesResult',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def post_replace(self, file, text, newtext, **kwargs):
        """
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_replace(file, text, color, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param file file: File to upload (required)
        :param str text: (required)
        :param str newtext: (required)
        :param str password: (optional)
        :param str sheet_name: (optional)
        :return: FilesResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_replace_with_http_info(file, text, newtext, **kwargs)
        else:
            (data) = self.post_replace_with_http_info(file, text, newtext, **kwargs)
            return data

    def post_replace_with_http_info(self, file, text, newtext, **kwargs):
        """
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_replace_with_http_info(file, text, newtext, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param file file: File to upload (required)
        :param str text: (required)
        :param str newtext: (required)
        :param str password: (optional)
        :param str sheet_name: (optional)
        :return: FilesResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['file', 'text', 'newtext','password','sheet_name']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_replace" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file' is set
        if ('file' not in params) or (params['file'] is None):
            raise ValueError("Missing the required parameter `file` when calling `post_replace`")
        # verify the required parameter 'text' is set
        if ('text' not in params) or (params['text'] is None):
            raise ValueError("Missing the required parameter `text` when calling `post_replace`")
        # verify the required parameter 'newtext' is set
        if ('newtext' not in params) or (params['newtext'] is None):
            raise ValueError("Missing the required parameter `newtext` when calling `post_replace`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'text' in params:
            query_params.append(('text', params['text']))
        if 'newtext' in params:
            query_params.append(('newtext', params['newtext']))
        if 'password' in params:
            query_params.append(('password', params['password']))
        if 'sheet_name' in params:
            query_params.append(('sheetname', params['sheet_name']))


        header_params = {}

        form_params = []
        local_var_files = {}
        if 'file' in params:
            
            if isinstance(params['file'],dict):
                for filename , filecontext in  params['file'].items():
                    local_var_files[filename] = filecontext
            else:
                local_var_files['File'] = params['file']            


        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['multipart/form-data'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/cells/replace', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='FilesResult',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def post_reverse(self, file, rotate_type, format, **kwargs):
        """
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_reverse(file, text, color, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param file file: File to upload (required)
        :param str rotate_type: (required)
        :param str format: (required)
        :return: FilesResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_reverse_with_http_info(file, rotate_type, format, **kwargs)
        else:
            (data) = self.post_reverse_with_http_info(file, rotate_type, format, **kwargs)
            return data

    def post_reverse_with_http_info(self, file, rotate_type, format, **kwargs):
        """
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_reverse_with_http_info(file, rotateType, format, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param file file: File to upload (required)
        :param str rotateType: (required)
        :param str format: (required)
        :return: FilesResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['file', 'rotate_type', 'format']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_replace" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file' is set
        if ('file' not in params) or (params['file'] is None):
            raise ValueError("Missing the required parameter `file` when calling `post_reverse`")
        # verify the required parameter 'rotateType' is set
        if ('rotate_type' not in params) or (params['rotate_type'] is None):
            raise ValueError("Missing the required parameter `text` when calling `post_reverse`")
        # verify the required parameter 'format' is set
        if ('format' not in params) or (params['format'] is None):
            raise ValueError("Missing the required parameter `newtext` when calling `post_reverse`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'format' in params:
            query_params.append(('format', params['format']))
        if 'rotate_type' in params:
            query_params.append(('rotateType', params['rotate_type']))


        header_params = {}

        form_params = []
        local_var_files = {}
        if 'file' in params:
            
            if isinstance(params['file'],dict):
                for filename , filecontext in  params['file'].items():
                    local_var_files[filename] = filecontext
            else:
                local_var_files['File'] = params['file']            


        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['multipart/form-data'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/cells/reverse', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='FilesResult',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
