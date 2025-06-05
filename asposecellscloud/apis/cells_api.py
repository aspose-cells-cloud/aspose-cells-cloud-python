# coding: utf-8
"""
<copyright company="Aspose" file="CellsApi.cs">
  Copyright (c) 2025 Aspose.Cells Cloud
</copyright>
<summary>
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
 SOFTWARE.
</summary>
"""

from __future__ import absolute_import

import sys
import os
import shutil
import re
import time

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class CellsApi(object):

    def __init__(self,clientid, clientsecret, version='v3.0', base_uri= 'https://api.aspose.cloud', api_client=None):
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
        # self.auth_data = self.o_auth_post("client_credentials", appsid, appkey)
        config = Configuration()
        config.host = self.base_uri +'/' 
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client
        if self.needAuth :            
            self.api_client.set_default_header("Authorization", "Bearer " + self.access_token)
        self.get_access_token_time =  time.time()

    def check_access_token(self):
        if self.needAuth :
            if self.access_token:
                timediff =  time.time() - self.get_access_token_time
                if timediff > 86300 :
                    api_client =  ApiClient(self.base_uri)
                    self.access_token = api_client.get_access_token("client_credentials", self.clientid, self.clientsecret,self.version)
                    self.api_client.set_default_header("Authorization", "Bearer " + self.access_token)
                    self.get_access_token_time =  time.time()

    # <summary>
    # Get Access Token Result: The Cells Cloud Get Token API acts as a proxy service,
    # forwarding user requests to the Aspose Cloud authentication server and returning the resulting access token to the client.
    # </summary>
    # <param name="request">Request. <see cref="PostAccessTokenRequest" /></param>
    def post_access_token(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_access_token_with_http_info(request,**kwargs)
        else:
            (data) = self.post_access_token_with_http_info(request,**kwargs)
            return data

    def post_access_token_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_access_token" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Check the Health Status of Aspose.Cells Cloud Service.
    # </summary>
    # <param name="request">Request. <see cref="GetAsposeCellsCloudStatusRequest" /></param>
    def get_aspose_cells_cloud_status(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_aspose_cells_cloud_status_with_http_info(request,**kwargs)
        else:
            (data) = self.get_aspose_cells_cloud_status_with_http_info(request,**kwargs)
            return data

    def get_aspose_cells_cloud_status_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_aspose_cells_cloud_status" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Check the Health Status of Aspose.Cells Cloud Service.
    # </summary>
    # <param name="request">Request. <see cref="CheckCloudServiceHealthRequest" /></param>
    def check_cloud_service_health(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.check_cloud_service_health_with_http_info(request,**kwargs)
        else:
            (data) = self.check_cloud_service_health_with_http_info(request,**kwargs)
            return data

    def check_cloud_service_health_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method check_cloud_service_health" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Converts a spreadsheet in cloud storage to the specified format.
    # </summary>
    # <param name="request">Request. <see cref="GetWorkbookWithFormatRequest" /></param>
    def get_workbook_with_format(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        response_file = None
        if kwargs.get('callback'):
            response_file = self.get_workbook_with_format_with_http_info(request,**kwargs)
        else:
            (data) = self.get_workbook_with_format_with_http_info(request,**kwargs)
            response_file = data
        if kwargs.get('local_outpath'):
            shutil.move( response_file , kwargs.get('local_outpath'))
            return kwargs.get('local_outpath')
        else:
            return response_file
    def get_workbook_with_format_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('local_outpath')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workbook_with_format" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Converts a spreadsheet on a local drive to the specified format.
    # </summary>
    # <param name="request">Request. <see cref="ConvertWorkbookRequest" /></param>
    def convert_workbook(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        response_file = None
        if kwargs.get('callback'):
            response_file = self.convert_workbook_with_http_info(request,**kwargs)
        else:
            (data) = self.convert_workbook_with_http_info(request,**kwargs)
            response_file = data
        if kwargs.get('local_outpath'):
            shutil.move( response_file , kwargs.get('local_outpath'))
            return kwargs.get('local_outpath')
        else:
            return response_file
    def convert_workbook_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('local_outpath')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method convert_workbook" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Converts a spreadsheet in cloud storage to the specified format.
    # </summary>
    # <param name="request">Request. <see cref="WorkbookSaveAsRequest" /></param>
    def workbook_save_as(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.workbook_save_as_with_http_info(request,**kwargs)
        else:
            (data) = self.workbook_save_as_with_http_info(request,**kwargs)
            return data

    def workbook_save_as_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method workbook_save_as" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Merge local spreadsheet files into a specified format file.
    # </summary>
    # <param name="request">Request. <see cref="MergeFilesRequest" /></param>
    def merge_files(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        response_file = None
        if kwargs.get('callback'):
            response_file = self.merge_files_with_http_info(request,**kwargs)
        else:
            (data) = self.merge_files_with_http_info(request,**kwargs)
            response_file = data
        if kwargs.get('local_outpath'):
            shutil.move( response_file , kwargs.get('local_outpath'))
            return kwargs.get('local_outpath')
        else:
            return response_file
    def merge_files_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('local_outpath')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method merge_files" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Merge spreadsheet files in cloud storage into a specified format file.
    # </summary>
    # <param name="request">Request. <see cref="MergeFilesInRemoteFolderRequest" /></param>
    def merge_files_in_remote_folder(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        response_file = None
        if kwargs.get('callback'):
            response_file = self.merge_files_in_remote_folder_with_http_info(request,**kwargs)
        else:
            (data) = self.merge_files_in_remote_folder_with_http_info(request,**kwargs)
            response_file = data
        if kwargs.get('local_outpath'):
            shutil.move( response_file , kwargs.get('local_outpath'))
            return kwargs.get('local_outpath')
        else:
            return response_file
    def merge_files_in_remote_folder_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('local_outpath')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method merge_files_in_remote_folder" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Split a local spreadsheet into the specified format, multi-file.
    # </summary>
    # <param name="request">Request. <see cref="SplitFileRequest" /></param>
    def split_file(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        response_file = None
        if kwargs.get('callback'):
            response_file = self.split_file_with_http_info(request,**kwargs)
        else:
            (data) = self.split_file_with_http_info(request,**kwargs)
            response_file = data
        if kwargs.get('local_outpath'):
            shutil.move( response_file , kwargs.get('local_outpath'))
            return kwargs.get('local_outpath')
        else:
            return response_file
    def split_file_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('local_outpath')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method split_file" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Split a spreadsheet in cloud storage into the specified format, multi-file.
    # </summary>
    # <param name="request">Request. <see cref="SplitFileInRemoteRequest" /></param>
    def split_file_in_remote(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        response_file = None
        if kwargs.get('callback'):
            response_file = self.split_file_in_remote_with_http_info(request,**kwargs)
        else:
            (data) = self.split_file_in_remote_with_http_info(request,**kwargs)
            response_file = data
        if kwargs.get('local_outpath'):
            shutil.move( response_file , kwargs.get('local_outpath'))
            return kwargs.get('local_outpath')
        else:
            return response_file
    def split_file_in_remote_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('local_outpath')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method split_file_in_remote" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Get an asymmetric public key.
    # </summary>
    # <param name="request">Request. <see cref="GetPublicKeyRequest" /></param>
    def get_public_key(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_public_key_with_http_info(request,**kwargs)
        else:
            (data) = self.get_public_key_with_http_info(request,**kwargs)
            return data

    def get_public_key_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_public_key" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Search text in the local spreadsheet.
    # </summary>
    # <param name="request">Request. <see cref="SearchTextRequest" /></param>
    def search_text(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.search_text_with_http_info(request,**kwargs)
        else:
            (data) = self.search_text_with_http_info(request,**kwargs)
            return data

    def search_text_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_text" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Search text in the remoted spreadsheet.
    # </summary>
    # <param name="request">Request. <see cref="SearchTextInRemoteRequest" /></param>
    def search_text_in_remote(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.search_text_in_remote_with_http_info(request,**kwargs)
        else:
            (data) = self.search_text_in_remote_with_http_info(request,**kwargs)
            return data

    def search_text_in_remote_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_text_in_remote" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Replace text in the local spreadsheet.
    # </summary>
    # <param name="request">Request. <see cref="ReplaceTextRequest" /></param>
    def replace_text(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        response_file = None
        if kwargs.get('callback'):
            response_file = self.replace_text_with_http_info(request,**kwargs)
        else:
            (data) = self.replace_text_with_http_info(request,**kwargs)
            response_file = data
        if kwargs.get('local_outpath'):
            shutil.move( response_file , kwargs.get('local_outpath'))
            return kwargs.get('local_outpath')
        else:
            return response_file
    def replace_text_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('local_outpath')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method replace_text" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Replace text in the remoted spreadsheet.
    # </summary>
    # <param name="request">Request. <see cref="ReplaceTextInRemoteRequest" /></param>
    def replace_text_in_remote(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.replace_text_in_remote_with_http_info(request,**kwargs)
        else:
            (data) = self.replace_text_in_remote_with_http_info(request,**kwargs)
            return data

    def replace_text_in_remote_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method replace_text_in_remote" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Search broken links in the local spreadsheet.
    # </summary>
    # <param name="request">Request. <see cref="SearchBrokenLinksRequest" /></param>
    def search_broken_links(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.search_broken_links_with_http_info(request,**kwargs)
        else:
            (data) = self.search_broken_links_with_http_info(request,**kwargs)
            return data

    def search_broken_links_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_broken_links" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Search broken links in the remoted spreadsheet.
    # </summary>
    # <param name="request">Request. <see cref="SearchBrokenLinksInRemoteRequest" /></param>
    def search_broken_links_in_remote(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.search_broken_links_in_remote_with_http_info(request,**kwargs)
        else:
            (data) = self.search_broken_links_in_remote_with_http_info(request,**kwargs)
            return data

    def search_broken_links_in_remote_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_broken_links_in_remote" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Get the specifications
    # </summary>
    # <param name="request">Request. <see cref="SpecRequest" /></param>
    def spec(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.spec_with_http_info(request,**kwargs)
        else:
            (data) = self.spec_with_http_info(request,**kwargs)
            return data

    def spec_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method spec" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # </summary>
    # <param name="request">Request. <see cref="CodegenSpecRequest" /></param>
    def codegen_spec(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.codegen_spec_with_http_info(request,**kwargs)
        else:
            (data) = self.codegen_spec_with_http_info(request,**kwargs)
            return data

    def codegen_spec_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method codegen_spec" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # </summary>
    # <param name="request">Request. <see cref="DownloadFileRequest" /></param>
    def download_file(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        response_file = None
        if kwargs.get('callback'):
            response_file = self.download_file_with_http_info(request,**kwargs)
        else:
            (data) = self.download_file_with_http_info(request,**kwargs)
            response_file = data
        if kwargs.get('local_outpath'):
            shutil.move( response_file , kwargs.get('local_outpath'))
            return kwargs.get('local_outpath')
        else:
            return response_file
    def download_file_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('local_outpath')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method download_file" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # </summary>
    # <param name="request">Request. <see cref="UploadFileRequest" /></param>
    def upload_file(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.upload_file_with_http_info(request,**kwargs)
        else:
            (data) = self.upload_file_with_http_info(request,**kwargs)
            return data

    def upload_file_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method upload_file" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # </summary>
    # <param name="request">Request. <see cref="CopyFileRequest" /></param>
    def copy_file(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.copy_file_with_http_info(request,**kwargs)
        else:
            (data) = self.copy_file_with_http_info(request,**kwargs)
            return data

    def copy_file_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method copy_file" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # </summary>
    # <param name="request">Request. <see cref="MoveFileRequest" /></param>
    def move_file(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.move_file_with_http_info(request,**kwargs)
        else:
            (data) = self.move_file_with_http_info(request,**kwargs)
            return data

    def move_file_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method move_file" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # </summary>
    # <param name="request">Request. <see cref="DeleteFileRequest" /></param>
    def delete_file(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.delete_file_with_http_info(request,**kwargs)
        else:
            (data) = self.delete_file_with_http_info(request,**kwargs)
            return data

    def delete_file_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_file" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # </summary>
    # <param name="request">Request. <see cref="GetFilesListRequest" /></param>
    def get_files_list(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_files_list_with_http_info(request,**kwargs)
        else:
            (data) = self.get_files_list_with_http_info(request,**kwargs)
            return data

    def get_files_list_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_files_list" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # </summary>
    # <param name="request">Request. <see cref="CreateFolderRequest" /></param>
    def create_folder(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.create_folder_with_http_info(request,**kwargs)
        else:
            (data) = self.create_folder_with_http_info(request,**kwargs)
            return data

    def create_folder_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_folder" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # </summary>
    # <param name="request">Request. <see cref="CopyFolderRequest" /></param>
    def copy_folder(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.copy_folder_with_http_info(request,**kwargs)
        else:
            (data) = self.copy_folder_with_http_info(request,**kwargs)
            return data

    def copy_folder_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method copy_folder" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # </summary>
    # <param name="request">Request. <see cref="MoveFolderRequest" /></param>
    def move_folder(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.move_folder_with_http_info(request,**kwargs)
        else:
            (data) = self.move_folder_with_http_info(request,**kwargs)
            return data

    def move_folder_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method move_folder" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # </summary>
    # <param name="request">Request. <see cref="DeleteFolderRequest" /></param>
    def delete_folder(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.delete_folder_with_http_info(request,**kwargs)
        else:
            (data) = self.delete_folder_with_http_info(request,**kwargs)
            return data

    def delete_folder_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_folder" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # </summary>
    # <param name="request">Request. <see cref="StorageExistsRequest" /></param>
    def storage_exists(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.storage_exists_with_http_info(request,**kwargs)
        else:
            (data) = self.storage_exists_with_http_info(request,**kwargs)
            return data

    def storage_exists_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method storage_exists" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # </summary>
    # <param name="request">Request. <see cref="ObjectExistsRequest" /></param>
    def object_exists(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.object_exists_with_http_info(request,**kwargs)
        else:
            (data) = self.object_exists_with_http_info(request,**kwargs)
            return data

    def object_exists_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method object_exists" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # </summary>
    # <param name="request">Request. <see cref="GetDiscUsageRequest" /></param>
    def get_disc_usage(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_disc_usage_with_http_info(request,**kwargs)
        else:
            (data) = self.get_disc_usage_with_http_info(request,**kwargs)
            return data

    def get_disc_usage_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_disc_usage" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # </summary>
    # <param name="request">Request. <see cref="GetFileVersionsRequest" /></param>
    def get_file_versions(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_file_versions_with_http_info(request,**kwargs)
        else:
            (data) = self.get_file_versions_with_http_info(request,**kwargs)
            return data

    def get_file_versions_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_file_versions" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Perform business analysis of data in Excel files.
    # </summary>
    # <param name="request">Request. <see cref="PostAnalyzeExcelRequest" /></param>
    def post_analyze_excel(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_analyze_excel_with_http_info(request,**kwargs)
        else:
            (data) = self.post_analyze_excel_with_http_info(request,**kwargs)
            return data

    def post_analyze_excel_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_analyze_excel" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Retrieve the description of auto filters from a worksheet.
    # </summary>
    # <param name="request">Request. <see cref="GetWorksheetAutoFilterRequest" /></param>
    def get_worksheet_auto_filter(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_worksheet_auto_filter_with_http_info(request,**kwargs)
        else:
            (data) = self.get_worksheet_auto_filter_with_http_info(request,**kwargs)
            return data

    def get_worksheet_auto_filter_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_worksheet_auto_filter" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Apply a date filter in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PutWorksheetDateFilterRequest" /></param>
    def put_worksheet_date_filter(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.put_worksheet_date_filter_with_http_info(request,**kwargs)
        else:
            (data) = self.put_worksheet_date_filter_with_http_info(request,**kwargs)
            return data

    def put_worksheet_date_filter_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_worksheet_date_filter" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Add a filter for a column in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PutWorksheetFilterRequest" /></param>
    def put_worksheet_filter(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.put_worksheet_filter_with_http_info(request,**kwargs)
        else:
            (data) = self.put_worksheet_filter_with_http_info(request,**kwargs)
            return data

    def put_worksheet_filter_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_worksheet_filter" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Add an icon filter in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PutWorksheetIconFilterRequest" /></param>
    def put_worksheet_icon_filter(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.put_worksheet_icon_filter_with_http_info(request,**kwargs)
        else:
            (data) = self.put_worksheet_icon_filter_with_http_info(request,**kwargs)
            return data

    def put_worksheet_icon_filter_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_worksheet_icon_filter" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Filter a list with custom criteria in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PutWorksheetCustomFilterRequest" /></param>
    def put_worksheet_custom_filter(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.put_worksheet_custom_filter_with_http_info(request,**kwargs)
        else:
            (data) = self.put_worksheet_custom_filter_with_http_info(request,**kwargs)
            return data

    def put_worksheet_custom_filter_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_worksheet_custom_filter" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Add a dynamic filter in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PutWorksheetDynamicFilterRequest" /></param>
    def put_worksheet_dynamic_filter(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.put_worksheet_dynamic_filter_with_http_info(request,**kwargs)
        else:
            (data) = self.put_worksheet_dynamic_filter_with_http_info(request,**kwargs)
            return data

    def put_worksheet_dynamic_filter_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_worksheet_dynamic_filter" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Filter the top 10 items in the list in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PutWorksheetFilterTop10Request" /></param>
    def put_worksheet_filter_top10(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.put_worksheet_filter_top10_with_http_info(request,**kwargs)
        else:
            (data) = self.put_worksheet_filter_top10_with_http_info(request,**kwargs)
            return data

    def put_worksheet_filter_top10_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_worksheet_filter_top10" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Add a color filter in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PutWorksheetColorFilterRequest" /></param>
    def put_worksheet_color_filter(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.put_worksheet_color_filter_with_http_info(request,**kwargs)
        else:
            (data) = self.put_worksheet_color_filter_with_http_info(request,**kwargs)
            return data

    def put_worksheet_color_filter_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_worksheet_color_filter" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Match all blank cells in the list.
    # </summary>
    # <param name="request">Request. <see cref="PostWorksheetMatchBlanksRequest" /></param>
    def post_worksheet_match_blanks(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_worksheet_match_blanks_with_http_info(request,**kwargs)
        else:
            (data) = self.post_worksheet_match_blanks_with_http_info(request,**kwargs)
            return data

    def post_worksheet_match_blanks_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_worksheet_match_blanks" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Match all not blank cells in the list.
    # </summary>
    # <param name="request">Request. <see cref="PostWorksheetMatchNonBlanksRequest" /></param>
    def post_worksheet_match_non_blanks(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_worksheet_match_non_blanks_with_http_info(request,**kwargs)
        else:
            (data) = self.post_worksheet_match_non_blanks_with_http_info(request,**kwargs)
            return data

    def post_worksheet_match_non_blanks_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_worksheet_match_non_blanks" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Refresh auto filters in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PostWorksheetAutoFilterRefreshRequest" /></param>
    def post_worksheet_auto_filter_refresh(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_worksheet_auto_filter_refresh_with_http_info(request,**kwargs)
        else:
            (data) = self.post_worksheet_auto_filter_refresh_with_http_info(request,**kwargs)
            return data

    def post_worksheet_auto_filter_refresh_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_worksheet_auto_filter_refresh" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Remove a date filter in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="DeleteWorksheetDateFilterRequest" /></param>
    def delete_worksheet_date_filter(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.delete_worksheet_date_filter_with_http_info(request,**kwargs)
        else:
            (data) = self.delete_worksheet_date_filter_with_http_info(request,**kwargs)
            return data

    def delete_worksheet_date_filter_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_worksheet_date_filter" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Delete a filter for a column in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="DeleteWorksheetFilterRequest" /></param>
    def delete_worksheet_filter(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.delete_worksheet_filter_with_http_info(request,**kwargs)
        else:
            (data) = self.delete_worksheet_filter_with_http_info(request,**kwargs)
            return data

    def delete_worksheet_filter_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_worksheet_filter" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Get autoshapes description in worksheet.
    # </summary>
    # <param name="request">Request. <see cref="GetWorksheetAutoshapesRequest" /></param>
    def get_worksheet_autoshapes(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_worksheet_autoshapes_with_http_info(request,**kwargs)
        else:
            (data) = self.get_worksheet_autoshapes_with_http_info(request,**kwargs)
            return data

    def get_worksheet_autoshapes_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_worksheet_autoshapes" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Get autoshape description in some format.
    # </summary>
    # <param name="request">Request. <see cref="GetWorksheetAutoshapeWithFormatRequest" /></param>
    def get_worksheet_autoshape_with_format(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        response_file = None
        if kwargs.get('callback'):
            response_file = self.get_worksheet_autoshape_with_format_with_http_info(request,**kwargs)
        else:
            (data) = self.get_worksheet_autoshape_with_format_with_http_info(request,**kwargs)
            response_file = data
        if kwargs.get('local_outpath'):
            shutil.move( response_file , kwargs.get('local_outpath'))
            return kwargs.get('local_outpath')
        else:
            return response_file
    def get_worksheet_autoshape_with_format_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('local_outpath')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_worksheet_autoshape_with_format" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Batch converting files that meet specific matching conditions.
    # </summary>
    # <param name="request">Request. <see cref="PostBatchConvertRequest" /></param>
    def post_batch_convert(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        response_file = None
        if kwargs.get('callback'):
            response_file = self.post_batch_convert_with_http_info(request,**kwargs)
        else:
            (data) = self.post_batch_convert_with_http_info(request,**kwargs)
            response_file = data
        if kwargs.get('local_outpath'):
            shutil.move( response_file , kwargs.get('local_outpath'))
            return kwargs.get('local_outpath')
        else:
            return response_file
    def post_batch_convert_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('local_outpath')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_batch_convert" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Batch protecting files that meet specific matching conditions.
    # </summary>
    # <param name="request">Request. <see cref="PostBatchProtectRequest" /></param>
    def post_batch_protect(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        response_file = None
        if kwargs.get('callback'):
            response_file = self.post_batch_protect_with_http_info(request,**kwargs)
        else:
            (data) = self.post_batch_protect_with_http_info(request,**kwargs)
            response_file = data
        if kwargs.get('local_outpath'):
            shutil.move( response_file , kwargs.get('local_outpath'))
            return kwargs.get('local_outpath')
        else:
            return response_file
    def post_batch_protect_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('local_outpath')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_batch_protect" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Batch locking files that meet specific matching conditions.
    # </summary>
    # <param name="request">Request. <see cref="PostBatchLockRequest" /></param>
    def post_batch_lock(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        response_file = None
        if kwargs.get('callback'):
            response_file = self.post_batch_lock_with_http_info(request,**kwargs)
        else:
            (data) = self.post_batch_lock_with_http_info(request,**kwargs)
            response_file = data
        if kwargs.get('local_outpath'):
            shutil.move( response_file , kwargs.get('local_outpath'))
            return kwargs.get('local_outpath')
        else:
            return response_file
    def post_batch_lock_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('local_outpath')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_batch_lock" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Batch unlocking files that meet specific matching conditions.
    # </summary>
    # <param name="request">Request. <see cref="PostBatchUnlockRequest" /></param>
    def post_batch_unlock(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        response_file = None
        if kwargs.get('callback'):
            response_file = self.post_batch_unlock_with_http_info(request,**kwargs)
        else:
            (data) = self.post_batch_unlock_with_http_info(request,**kwargs)
            response_file = data
        if kwargs.get('local_outpath'):
            shutil.move( response_file , kwargs.get('local_outpath'))
            return kwargs.get('local_outpath')
        else:
            return response_file
    def post_batch_unlock_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('local_outpath')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_batch_unlock" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Batch splitting files that meet specific matching conditions.
    # </summary>
    # <param name="request">Request. <see cref="PostBatchSplitRequest" /></param>
    def post_batch_split(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        response_file = None
        if kwargs.get('callback'):
            response_file = self.post_batch_split_with_http_info(request,**kwargs)
        else:
            (data) = self.post_batch_split_with_http_info(request,**kwargs)
            response_file = data
        if kwargs.get('local_outpath'):
            shutil.move( response_file , kwargs.get('local_outpath'))
            return kwargs.get('local_outpath')
        else:
            return response_file
    def post_batch_split_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('local_outpath')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_batch_split" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Clear cell area contents in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PostClearContentsRequest" /></param>
    def post_clear_contents(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_clear_contents_with_http_info(request,**kwargs)
        else:
            (data) = self.post_clear_contents_with_http_info(request,**kwargs)
            return data

    def post_clear_contents_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_clear_contents" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Clear cell formats in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PostClearFormatsRequest" /></param>
    def post_clear_formats(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_clear_formats_with_http_info(request,**kwargs)
        else:
            (data) = self.post_clear_formats_with_http_info(request,**kwargs)
            return data

    def post_clear_formats_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_clear_formats" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Update cell range styles in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PostUpdateWorksheetRangeStyleRequest" /></param>
    def post_update_worksheet_range_style(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_update_worksheet_range_style_with_http_info(request,**kwargs)
        else:
            (data) = self.post_update_worksheet_range_style_with_http_info(request,**kwargs)
            return data

    def post_update_worksheet_range_style_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_update_worksheet_range_style" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Merge cells in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PostWorksheetMergeRequest" /></param>
    def post_worksheet_merge(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_worksheet_merge_with_http_info(request,**kwargs)
        else:
            (data) = self.post_worksheet_merge_with_http_info(request,**kwargs)
            return data

    def post_worksheet_merge_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_worksheet_merge" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Unmerge cells in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PostWorksheetUnmergeRequest" /></param>
    def post_worksheet_unmerge(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_worksheet_unmerge_with_http_info(request,**kwargs)
        else:
            (data) = self.post_worksheet_unmerge_with_http_info(request,**kwargs)
            return data

    def post_worksheet_unmerge_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_worksheet_unmerge" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Retrieve cell descriptions in a specified format.
    # </summary>
    # <param name="request">Request. <see cref="GetWorksheetCellsRequest" /></param>
    def get_worksheet_cells(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_worksheet_cells_with_http_info(request,**kwargs)
        else:
            (data) = self.get_worksheet_cells_with_http_info(request,**kwargs)
            return data

    def get_worksheet_cells_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_worksheet_cells" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Retrieve cell data using either cell reference or method name in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="GetWorksheetCellRequest" /></param>
    def get_worksheet_cell(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_worksheet_cell_with_http_info(request,**kwargs)
        else:
            (data) = self.get_worksheet_cell_with_http_info(request,**kwargs)
            return data

    def get_worksheet_cell_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_worksheet_cell" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Retrieve cell style descriptions in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="GetWorksheetCellStyleRequest" /></param>
    def get_worksheet_cell_style(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_worksheet_cell_style_with_http_info(request,**kwargs)
        else:
            (data) = self.get_worksheet_cell_style_with_http_info(request,**kwargs)
            return data

    def get_worksheet_cell_style_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_worksheet_cell_style" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Set cell value using cell name in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PostWorksheetCellSetValueRequest" /></param>
    def post_worksheet_cell_set_value(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_worksheet_cell_set_value_with_http_info(request,**kwargs)
        else:
            (data) = self.post_worksheet_cell_set_value_with_http_info(request,**kwargs)
            return data

    def post_worksheet_cell_set_value_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_worksheet_cell_set_value" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Set cell style using cell name in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PostUpdateWorksheetCellStyleRequest" /></param>
    def post_update_worksheet_cell_style(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_update_worksheet_cell_style_with_http_info(request,**kwargs)
        else:
            (data) = self.post_update_worksheet_cell_style_with_http_info(request,**kwargs)
            return data

    def post_update_worksheet_cell_style_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_update_worksheet_cell_style" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Set the value of the range in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PostSetCellRangeValueRequest" /></param>
    def post_set_cell_range_value(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_set_cell_range_value_with_http_info(request,**kwargs)
        else:
            (data) = self.post_set_cell_range_value_with_http_info(request,**kwargs)
            return data

    def post_set_cell_range_value_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_set_cell_range_value" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Copy data from a source cell to a destination cell in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PostCopyCellIntoCellRequest" /></param>
    def post_copy_cell_into_cell(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_copy_cell_into_cell_with_http_info(request,**kwargs)
        else:
            (data) = self.post_copy_cell_into_cell_with_http_info(request,**kwargs)
            return data

    def post_copy_cell_into_cell_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_copy_cell_into_cell" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Retrieve the HTML string containing data and specific formats in this cell.
    # </summary>
    # <param name="request">Request. <see cref="GetCellHtmlStringRequest" /></param>
    def get_cell_html_string(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_cell_html_string_with_http_info(request,**kwargs)
        else:
            (data) = self.get_cell_html_string_with_http_info(request,**kwargs)
            return data

    def get_cell_html_string_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_cell_html_string" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Set the HTML string containing data and specific formats in this cell.
    # </summary>
    # <param name="request">Request. <see cref="PostSetCellHtmlStringRequest" /></param>
    def post_set_cell_html_string(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_set_cell_html_string_with_http_info(request,**kwargs)
        else:
            (data) = self.post_set_cell_html_string_with_http_info(request,**kwargs)
            return data

    def post_set_cell_html_string_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_set_cell_html_string" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Calculate cell formula in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PostCellCalculateRequest" /></param>
    def post_cell_calculate(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_cell_calculate_with_http_info(request,**kwargs)
        else:
            (data) = self.post_cell_calculate_with_http_info(request,**kwargs)
            return data

    def post_cell_calculate_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_cell_calculate" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Set cell characters in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PostCellCharactersRequest" /></param>
    def post_cell_characters(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_cell_characters_with_http_info(request,**kwargs)
        else:
            (data) = self.post_cell_characters_with_http_info(request,**kwargs)
            return data

    def post_cell_characters_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_cell_characters" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Retrieve descriptions of worksheet columns.
    # </summary>
    # <param name="request">Request. <see cref="GetWorksheetColumnsRequest" /></param>
    def get_worksheet_columns(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_worksheet_columns_with_http_info(request,**kwargs)
        else:
            (data) = self.get_worksheet_columns_with_http_info(request,**kwargs)
            return data

    def get_worksheet_columns_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_worksheet_columns" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Set worksheet column width.
    # </summary>
    # <param name="request">Request. <see cref="PostSetWorksheetColumnWidthRequest" /></param>
    def post_set_worksheet_column_width(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_set_worksheet_column_width_with_http_info(request,**kwargs)
        else:
            (data) = self.post_set_worksheet_column_width_with_http_info(request,**kwargs)
            return data

    def post_set_worksheet_column_width_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_set_worksheet_column_width" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Retrieve worksheet column data by column index.
    # </summary>
    # <param name="request">Request. <see cref="GetWorksheetColumnRequest" /></param>
    def get_worksheet_column(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_worksheet_column_with_http_info(request,**kwargs)
        else:
            (data) = self.get_worksheet_column_with_http_info(request,**kwargs)
            return data

    def get_worksheet_column_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_worksheet_column" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Insert worksheet columns in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PutInsertWorksheetColumnsRequest" /></param>
    def put_insert_worksheet_columns(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.put_insert_worksheet_columns_with_http_info(request,**kwargs)
        else:
            (data) = self.put_insert_worksheet_columns_with_http_info(request,**kwargs)
            return data

    def put_insert_worksheet_columns_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_insert_worksheet_columns" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Delete worksheet columns in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="DeleteWorksheetColumnsRequest" /></param>
    def delete_worksheet_columns(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.delete_worksheet_columns_with_http_info(request,**kwargs)
        else:
            (data) = self.delete_worksheet_columns_with_http_info(request,**kwargs)
            return data

    def delete_worksheet_columns_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_worksheet_columns" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Hide worksheet columns in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PostHideWorksheetColumnsRequest" /></param>
    def post_hide_worksheet_columns(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_hide_worksheet_columns_with_http_info(request,**kwargs)
        else:
            (data) = self.post_hide_worksheet_columns_with_http_info(request,**kwargs)
            return data

    def post_hide_worksheet_columns_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_hide_worksheet_columns" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Unhide worksheet columns in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PostUnhideWorksheetColumnsRequest" /></param>
    def post_unhide_worksheet_columns(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_unhide_worksheet_columns_with_http_info(request,**kwargs)
        else:
            (data) = self.post_unhide_worksheet_columns_with_http_info(request,**kwargs)
            return data

    def post_unhide_worksheet_columns_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_unhide_worksheet_columns" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Group worksheet columns in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PostGroupWorksheetColumnsRequest" /></param>
    def post_group_worksheet_columns(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_group_worksheet_columns_with_http_info(request,**kwargs)
        else:
            (data) = self.post_group_worksheet_columns_with_http_info(request,**kwargs)
            return data

    def post_group_worksheet_columns_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_group_worksheet_columns" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Ungroup worksheet columns.
    # </summary>
    # <param name="request">Request. <see cref="PostUngroupWorksheetColumnsRequest" /></param>
    def post_ungroup_worksheet_columns(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_ungroup_worksheet_columns_with_http_info(request,**kwargs)
        else:
            (data) = self.post_ungroup_worksheet_columns_with_http_info(request,**kwargs)
            return data

    def post_ungroup_worksheet_columns_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_ungroup_worksheet_columns" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Copy data from source columns to destination columns in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PostCopyWorksheetColumnsRequest" /></param>
    def post_copy_worksheet_columns(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_copy_worksheet_columns_with_http_info(request,**kwargs)
        else:
            (data) = self.post_copy_worksheet_columns_with_http_info(request,**kwargs)
            return data

    def post_copy_worksheet_columns_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_copy_worksheet_columns" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Set column style in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PostColumnStyleRequest" /></param>
    def post_column_style(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_column_style_with_http_info(request,**kwargs)
        else:
            (data) = self.post_column_style_with_http_info(request,**kwargs)
            return data

    def post_column_style_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_column_style" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Retrieve descriptions of rows in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="GetWorksheetRowsRequest" /></param>
    def get_worksheet_rows(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_worksheet_rows_with_http_info(request,**kwargs)
        else:
            (data) = self.get_worksheet_rows_with_http_info(request,**kwargs)
            return data

    def get_worksheet_rows_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_worksheet_rows" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Retrieve row data by the row's index in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="GetWorksheetRowRequest" /></param>
    def get_worksheet_row(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_worksheet_row_with_http_info(request,**kwargs)
        else:
            (data) = self.get_worksheet_row_with_http_info(request,**kwargs)
            return data

    def get_worksheet_row_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_worksheet_row" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Delete a row in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="DeleteWorksheetRowRequest" /></param>
    def delete_worksheet_row(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.delete_worksheet_row_with_http_info(request,**kwargs)
        else:
            (data) = self.delete_worksheet_row_with_http_info(request,**kwargs)
            return data

    def delete_worksheet_row_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_worksheet_row" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Delete several rows in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="DeleteWorksheetRowsRequest" /></param>
    def delete_worksheet_rows(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.delete_worksheet_rows_with_http_info(request,**kwargs)
        else:
            (data) = self.delete_worksheet_rows_with_http_info(request,**kwargs)
            return data

    def delete_worksheet_rows_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_worksheet_rows" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Insert several new rows in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PutInsertWorksheetRowsRequest" /></param>
    def put_insert_worksheet_rows(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.put_insert_worksheet_rows_with_http_info(request,**kwargs)
        else:
            (data) = self.put_insert_worksheet_rows_with_http_info(request,**kwargs)
            return data

    def put_insert_worksheet_rows_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_insert_worksheet_rows" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Insert a new row in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PutInsertWorksheetRowRequest" /></param>
    def put_insert_worksheet_row(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.put_insert_worksheet_row_with_http_info(request,**kwargs)
        else:
            (data) = self.put_insert_worksheet_row_with_http_info(request,**kwargs)
            return data

    def put_insert_worksheet_row_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_insert_worksheet_row" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Update height of rows in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PostUpdateWorksheetRowRequest" /></param>
    def post_update_worksheet_row(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_update_worksheet_row_with_http_info(request,**kwargs)
        else:
            (data) = self.post_update_worksheet_row_with_http_info(request,**kwargs)
            return data

    def post_update_worksheet_row_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_update_worksheet_row" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Hide rows in worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PostHideWorksheetRowsRequest" /></param>
    def post_hide_worksheet_rows(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_hide_worksheet_rows_with_http_info(request,**kwargs)
        else:
            (data) = self.post_hide_worksheet_rows_with_http_info(request,**kwargs)
            return data

    def post_hide_worksheet_rows_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_hide_worksheet_rows" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Unhide rows in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PostUnhideWorksheetRowsRequest" /></param>
    def post_unhide_worksheet_rows(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_unhide_worksheet_rows_with_http_info(request,**kwargs)
        else:
            (data) = self.post_unhide_worksheet_rows_with_http_info(request,**kwargs)
            return data

    def post_unhide_worksheet_rows_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_unhide_worksheet_rows" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Group rows in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PostGroupWorksheetRowsRequest" /></param>
    def post_group_worksheet_rows(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_group_worksheet_rows_with_http_info(request,**kwargs)
        else:
            (data) = self.post_group_worksheet_rows_with_http_info(request,**kwargs)
            return data

    def post_group_worksheet_rows_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_group_worksheet_rows" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Ungroup rows in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PostUngroupWorksheetRowsRequest" /></param>
    def post_ungroup_worksheet_rows(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_ungroup_worksheet_rows_with_http_info(request,**kwargs)
        else:
            (data) = self.post_ungroup_worksheet_rows_with_http_info(request,**kwargs)
            return data

    def post_ungroup_worksheet_rows_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_ungroup_worksheet_rows" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Copy data and formats from specific entire rows in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PostCopyWorksheetRowsRequest" /></param>
    def post_copy_worksheet_rows(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_copy_worksheet_rows_with_http_info(request,**kwargs)
        else:
            (data) = self.post_copy_worksheet_rows_with_http_info(request,**kwargs)
            return data

    def post_copy_worksheet_rows_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_copy_worksheet_rows" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Apply formats to an entire row in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PostRowStyleRequest" /></param>
    def post_row_style(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_row_style_with_http_info(request,**kwargs)
        else:
            (data) = self.post_row_style_with_http_info(request,**kwargs)
            return data

    def post_row_style_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_row_style" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Retrieve cell descriptions in a specified format.
    # </summary>
    # <param name="request">Request. <see cref="GetCellsCloudServicesHealthCheckRequest" /></param>
    def get_cells_cloud_services_health_check(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_cells_cloud_services_health_check_with_http_info(request,**kwargs)
        else:
            (data) = self.get_cells_cloud_services_health_check_with_http_info(request,**kwargs)
            return data

    def get_cells_cloud_services_health_check_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_cells_cloud_services_health_check" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Aspose.Cells Cloud service health status check.
    # </summary>
    # <param name="request">Request. <see cref="GetCellsCloudServiceStatusRequest" /></param>
    def get_cells_cloud_service_status(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_cells_cloud_service_status_with_http_info(request,**kwargs)
        else:
            (data) = self.get_cells_cloud_service_status_with_http_info(request,**kwargs)
            return data

    def get_cells_cloud_service_status_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_cells_cloud_service_status" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Retrieve chart area description in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="GetChartAreaRequest" /></param>
    def get_chart_area(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_chart_area_with_http_info(request,**kwargs)
        else:
            (data) = self.get_chart_area_with_http_info(request,**kwargs)
            return data

    def get_chart_area_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_chart_area" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Retrieve chart area fill format description in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="GetChartAreaFillFormatRequest" /></param>
    def get_chart_area_fill_format(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_chart_area_fill_format_with_http_info(request,**kwargs)
        else:
            (data) = self.get_chart_area_fill_format_with_http_info(request,**kwargs)
            return data

    def get_chart_area_fill_format_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_chart_area_fill_format" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Retrieve chart area border description.
    # </summary>
    # <param name="request">Request. <see cref="GetChartAreaBorderRequest" /></param>
    def get_chart_area_border(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_chart_area_border_with_http_info(request,**kwargs)
        else:
            (data) = self.get_chart_area_border_with_http_info(request,**kwargs)
            return data

    def get_chart_area_border_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_chart_area_border" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Retrieve descriptions of charts in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="GetWorksheetChartsRequest" /></param>
    def get_worksheet_charts(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_worksheet_charts_with_http_info(request,**kwargs)
        else:
            (data) = self.get_worksheet_charts_with_http_info(request,**kwargs)
            return data

    def get_worksheet_charts_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_worksheet_charts" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Retrieve the chart in a specified format.
    # </summary>
    # <param name="request">Request. <see cref="GetWorksheetChartRequest" /></param>
    def get_worksheet_chart(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        response_file = None
        if kwargs.get('callback'):
            response_file = self.get_worksheet_chart_with_http_info(request,**kwargs)
        else:
            (data) = self.get_worksheet_chart_with_http_info(request,**kwargs)
            response_file = data
        if kwargs.get('local_outpath'):
            shutil.move( response_file , kwargs.get('local_outpath'))
            return kwargs.get('local_outpath')
        else:
            return response_file
    def get_worksheet_chart_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('local_outpath')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_worksheet_chart" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Add a new chart in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PutWorksheetChartRequest" /></param>
    def put_worksheet_chart(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.put_worksheet_chart_with_http_info(request,**kwargs)
        else:
            (data) = self.put_worksheet_chart_with_http_info(request,**kwargs)
            return data

    def put_worksheet_chart_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_worksheet_chart" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Delete a chart by index in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="DeleteWorksheetChartRequest" /></param>
    def delete_worksheet_chart(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.delete_worksheet_chart_with_http_info(request,**kwargs)
        else:
            (data) = self.delete_worksheet_chart_with_http_info(request,**kwargs)
            return data

    def delete_worksheet_chart_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_worksheet_chart" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Update chart properties in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PostWorksheetChartRequest" /></param>
    def post_worksheet_chart(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_worksheet_chart_with_http_info(request,**kwargs)
        else:
            (data) = self.post_worksheet_chart_with_http_info(request,**kwargs)
            return data

    def post_worksheet_chart_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_worksheet_chart" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Retrieve chart legend description in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="GetWorksheetChartLegendRequest" /></param>
    def get_worksheet_chart_legend(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_worksheet_chart_legend_with_http_info(request,**kwargs)
        else:
            (data) = self.get_worksheet_chart_legend_with_http_info(request,**kwargs)
            return data

    def get_worksheet_chart_legend_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_worksheet_chart_legend" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Update chart legend in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PostWorksheetChartLegendRequest" /></param>
    def post_worksheet_chart_legend(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_worksheet_chart_legend_with_http_info(request,**kwargs)
        else:
            (data) = self.post_worksheet_chart_legend_with_http_info(request,**kwargs)
            return data

    def post_worksheet_chart_legend_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_worksheet_chart_legend" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Show chart legend in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PutWorksheetChartLegendRequest" /></param>
    def put_worksheet_chart_legend(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.put_worksheet_chart_legend_with_http_info(request,**kwargs)
        else:
            (data) = self.put_worksheet_chart_legend_with_http_info(request,**kwargs)
            return data

    def put_worksheet_chart_legend_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_worksheet_chart_legend" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Hides chart legend in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="DeleteWorksheetChartLegendRequest" /></param>
    def delete_worksheet_chart_legend(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.delete_worksheet_chart_legend_with_http_info(request,**kwargs)
        else:
            (data) = self.delete_worksheet_chart_legend_with_http_info(request,**kwargs)
            return data

    def delete_worksheet_chart_legend_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_worksheet_chart_legend" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Clear the charts in the worksheets.
    # </summary>
    # <param name="request">Request. <see cref="DeleteWorksheetChartsRequest" /></param>
    def delete_worksheet_charts(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.delete_worksheet_charts_with_http_info(request,**kwargs)
        else:
            (data) = self.delete_worksheet_charts_with_http_info(request,**kwargs)
            return data

    def delete_worksheet_charts_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_worksheet_charts" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Retrieve chart title description in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="GetWorksheetChartTitleRequest" /></param>
    def get_worksheet_chart_title(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_worksheet_chart_title_with_http_info(request,**kwargs)
        else:
            (data) = self.get_worksheet_chart_title_with_http_info(request,**kwargs)
            return data

    def get_worksheet_chart_title_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_worksheet_chart_title" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Update chart title in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PostWorksheetChartTitleRequest" /></param>
    def post_worksheet_chart_title(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_worksheet_chart_title_with_http_info(request,**kwargs)
        else:
            (data) = self.post_worksheet_chart_title_with_http_info(request,**kwargs)
            return data

    def post_worksheet_chart_title_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_worksheet_chart_title" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Set chart title in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PutWorksheetChartTitleRequest" /></param>
    def put_worksheet_chart_title(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.put_worksheet_chart_title_with_http_info(request,**kwargs)
        else:
            (data) = self.put_worksheet_chart_title_with_http_info(request,**kwargs)
            return data

    def put_worksheet_chart_title_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_worksheet_chart_title" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Hide chart title in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="DeleteWorksheetChartTitleRequest" /></param>
    def delete_worksheet_chart_title(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.delete_worksheet_chart_title_with_http_info(request,**kwargs)
        else:
            (data) = self.delete_worksheet_chart_title_with_http_info(request,**kwargs)
            return data

    def delete_worksheet_chart_title_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_worksheet_chart_title" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Retrieve descriptions of chart seriesaxis in the chart.
    # </summary>
    # <param name="request">Request. <see cref="GetChartSeriesAxisRequest" /></param>
    def get_chart_series_axis(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_chart_series_axis_with_http_info(request,**kwargs)
        else:
            (data) = self.get_chart_series_axis_with_http_info(request,**kwargs)
            return data

    def get_chart_series_axis_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_chart_series_axis" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Retrieve descriptions of chart series axis in the chart.
    # </summary>
    # <param name="request">Request. <see cref="GetChartCategoryAxisRequest" /></param>
    def get_chart_category_axis(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_chart_category_axis_with_http_info(request,**kwargs)
        else:
            (data) = self.get_chart_category_axis_with_http_info(request,**kwargs)
            return data

    def get_chart_category_axis_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_chart_category_axis" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Retrieve chart value axis in the chart.
    # </summary>
    # <param name="request">Request. <see cref="GetChartValueAxisRequest" /></param>
    def get_chart_value_axis(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_chart_value_axis_with_http_info(request,**kwargs)
        else:
            (data) = self.get_chart_value_axis_with_http_info(request,**kwargs)
            return data

    def get_chart_value_axis_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_chart_value_axis" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Retrieve chart second category axis in the chart
    # </summary>
    # <param name="request">Request. <see cref="GetChartSecondCategoryAxisRequest" /></param>
    def get_chart_second_category_axis(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_chart_second_category_axis_with_http_info(request,**kwargs)
        else:
            (data) = self.get_chart_second_category_axis_with_http_info(request,**kwargs)
            return data

    def get_chart_second_category_axis_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_chart_second_category_axis" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Retrieve chart second value axis in the chart.
    # </summary>
    # <param name="request">Request. <see cref="GetChartSecondValueAxisRequest" /></param>
    def get_chart_second_value_axis(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_chart_second_value_axis_with_http_info(request,**kwargs)
        else:
            (data) = self.get_chart_second_value_axis_with_http_info(request,**kwargs)
            return data

    def get_chart_second_value_axis_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_chart_second_value_axis" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Update chart series axis in the chart.
    # </summary>
    # <param name="request">Request. <see cref="PostChartSeriesAxisRequest" /></param>
    def post_chart_series_axis(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_chart_series_axis_with_http_info(request,**kwargs)
        else:
            (data) = self.post_chart_series_axis_with_http_info(request,**kwargs)
            return data

    def post_chart_series_axis_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_chart_series_axis" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Update chart category axis in the chart.
    # </summary>
    # <param name="request">Request. <see cref="PostChartCategoryAxisRequest" /></param>
    def post_chart_category_axis(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_chart_category_axis_with_http_info(request,**kwargs)
        else:
            (data) = self.post_chart_category_axis_with_http_info(request,**kwargs)
            return data

    def post_chart_category_axis_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_chart_category_axis" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Update chart value axis in the chart.
    # </summary>
    # <param name="request">Request. <see cref="PostChartValueAxisRequest" /></param>
    def post_chart_value_axis(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_chart_value_axis_with_http_info(request,**kwargs)
        else:
            (data) = self.post_chart_value_axis_with_http_info(request,**kwargs)
            return data

    def post_chart_value_axis_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_chart_value_axis" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Update chart sencond category axis in the chart.
    # </summary>
    # <param name="request">Request. <see cref="PostChartSecondCategoryAxisRequest" /></param>
    def post_chart_second_category_axis(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_chart_second_category_axis_with_http_info(request,**kwargs)
        else:
            (data) = self.post_chart_second_category_axis_with_http_info(request,**kwargs)
            return data

    def post_chart_second_category_axis_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_chart_second_category_axis" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Update chart sencond value axis in the chart.
    # </summary>
    # <param name="request">Request. <see cref="PostChartSecondValueAxisRequest" /></param>
    def post_chart_second_value_axis(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_chart_second_value_axis_with_http_info(request,**kwargs)
        else:
            (data) = self.post_chart_second_value_axis_with_http_info(request,**kwargs)
            return data

    def post_chart_second_value_axis_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_chart_second_value_axis" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Retrieve descriptions of conditional formattings in a worksheet.
    # </summary>
    # <param name="request">Request. <see cref="GetWorksheetConditionalFormattingsRequest" /></param>
    def get_worksheet_conditional_formattings(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_worksheet_conditional_formattings_with_http_info(request,**kwargs)
        else:
            (data) = self.get_worksheet_conditional_formattings_with_http_info(request,**kwargs)
            return data

    def get_worksheet_conditional_formattings_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_worksheet_conditional_formattings" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Retrieve conditional formatting descriptions in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="GetWorksheetConditionalFormattingRequest" /></param>
    def get_worksheet_conditional_formatting(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_worksheet_conditional_formatting_with_http_info(request,**kwargs)
        else:
            (data) = self.get_worksheet_conditional_formatting_with_http_info(request,**kwargs)
            return data

    def get_worksheet_conditional_formatting_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_worksheet_conditional_formatting" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Add conditional formatting in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PutWorksheetConditionalFormattingRequest" /></param>
    def put_worksheet_conditional_formatting(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.put_worksheet_conditional_formatting_with_http_info(request,**kwargs)
        else:
            (data) = self.put_worksheet_conditional_formatting_with_http_info(request,**kwargs)
            return data

    def put_worksheet_conditional_formatting_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_worksheet_conditional_formatting" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Add a format condition in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PutWorksheetFormatConditionRequest" /></param>
    def put_worksheet_format_condition(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.put_worksheet_format_condition_with_http_info(request,**kwargs)
        else:
            (data) = self.put_worksheet_format_condition_with_http_info(request,**kwargs)
            return data

    def put_worksheet_format_condition_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_worksheet_format_condition" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Add a cell area for the format condition in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PutWorksheetFormatConditionAreaRequest" /></param>
    def put_worksheet_format_condition_area(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.put_worksheet_format_condition_area_with_http_info(request,**kwargs)
        else:
            (data) = self.put_worksheet_format_condition_area_with_http_info(request,**kwargs)
            return data

    def put_worksheet_format_condition_area_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_worksheet_format_condition_area" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Add a condition for the format condition in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PutWorksheetFormatConditionConditionRequest" /></param>
    def put_worksheet_format_condition_condition(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.put_worksheet_format_condition_condition_with_http_info(request,**kwargs)
        else:
            (data) = self.put_worksheet_format_condition_condition_with_http_info(request,**kwargs)
            return data

    def put_worksheet_format_condition_condition_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_worksheet_format_condition_condition" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Clear all conditional formattings in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="DeleteWorksheetConditionalFormattingsRequest" /></param>
    def delete_worksheet_conditional_formattings(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.delete_worksheet_conditional_formattings_with_http_info(request,**kwargs)
        else:
            (data) = self.delete_worksheet_conditional_formattings_with_http_info(request,**kwargs)
            return data

    def delete_worksheet_conditional_formattings_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_worksheet_conditional_formattings" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Remove a conditional formatting.
    # </summary>
    # <param name="request">Request. <see cref="DeleteWorksheetConditionalFormattingRequest" /></param>
    def delete_worksheet_conditional_formatting(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.delete_worksheet_conditional_formatting_with_http_info(request,**kwargs)
        else:
            (data) = self.delete_worksheet_conditional_formatting_with_http_info(request,**kwargs)
            return data

    def delete_worksheet_conditional_formatting_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_worksheet_conditional_formatting" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Remove cell area from conditional formatting.
    # </summary>
    # <param name="request">Request. <see cref="DeleteWorksheetConditionalFormattingAreaRequest" /></param>
    def delete_worksheet_conditional_formatting_area(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.delete_worksheet_conditional_formatting_area_with_http_info(request,**kwargs)
        else:
            (data) = self.delete_worksheet_conditional_formatting_area_with_http_info(request,**kwargs)
            return data

    def delete_worksheet_conditional_formatting_area_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_worksheet_conditional_formatting_area" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Retrieve workbooks in various formats.
    # </summary>
    # <param name="request">Request. <see cref="GetWorkbookRequest" /></param>
    def get_workbook(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        response_file = None
        if kwargs.get('callback'):
            response_file = self.get_workbook_with_http_info(request,**kwargs)
        else:
            (data) = self.get_workbook_with_http_info(request,**kwargs)
            response_file = data
        if kwargs.get('local_outpath'):
            shutil.move( response_file , kwargs.get('local_outpath'))
            return kwargs.get('local_outpath')
        else:
            return response_file
    def get_workbook_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('local_outpath')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workbook" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Convert the workbook from the requested content into files in different formats.
    # </summary>
    # <param name="request">Request. <see cref="PutConvertWorkbookRequest" /></param>
    def put_convert_workbook(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        response_file = None
        if kwargs.get('callback'):
            response_file = self.put_convert_workbook_with_http_info(request,**kwargs)
        else:
            (data) = self.put_convert_workbook_with_http_info(request,**kwargs)
            response_file = data
        if kwargs.get('local_outpath'):
            shutil.move( response_file , kwargs.get('local_outpath'))
            return kwargs.get('local_outpath')
        else:
            return response_file
    def put_convert_workbook_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('local_outpath')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_convert_workbook" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Save an Excel file in various formats.
    # </summary>
    # <param name="request">Request. <see cref="PostWorkbookSaveAsRequest" /></param>
    def post_workbook_save_as(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_workbook_save_as_with_http_info(request,**kwargs)
        else:
            (data) = self.post_workbook_save_as_with_http_info(request,**kwargs)
            return data

    def post_workbook_save_as_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workbook_save_as" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Convert Excel file to PDF files.
    # </summary>
    # <param name="request">Request. <see cref="PostConvertWorkbookToPDFRequest" /></param>
    def post_convert_workbook_to_pdf(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_convert_workbook_to_pdf_with_http_info(request,**kwargs)
        else:
            (data) = self.post_convert_workbook_to_pdf_with_http_info(request,**kwargs)
            return data

    def post_convert_workbook_to_pdf_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_convert_workbook_to_pdf" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Convert Excel file to PNG files.
    # </summary>
    # <param name="request">Request. <see cref="PostConvertWorkbookToPNGRequest" /></param>
    def post_convert_workbook_to_png(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_convert_workbook_to_png_with_http_info(request,**kwargs)
        else:
            (data) = self.post_convert_workbook_to_png_with_http_info(request,**kwargs)
            return data

    def post_convert_workbook_to_png_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_convert_workbook_to_png" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Convert Excel file to Docx files.
    # </summary>
    # <param name="request">Request. <see cref="PostConvertWorkbookToDocxRequest" /></param>
    def post_convert_workbook_to_docx(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_convert_workbook_to_docx_with_http_info(request,**kwargs)
        else:
            (data) = self.post_convert_workbook_to_docx_with_http_info(request,**kwargs)
            return data

    def post_convert_workbook_to_docx_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_convert_workbook_to_docx" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Convert Excel file to Pptx files.
    # </summary>
    # <param name="request">Request. <see cref="PostConvertWorkbookToPptxRequest" /></param>
    def post_convert_workbook_to_pptx(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_convert_workbook_to_pptx_with_http_info(request,**kwargs)
        else:
            (data) = self.post_convert_workbook_to_pptx_with_http_info(request,**kwargs)
            return data

    def post_convert_workbook_to_pptx_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_convert_workbook_to_pptx" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Convert Excel file to HTML files.
    # </summary>
    # <param name="request">Request. <see cref="PostConvertWorkbookToHtmlRequest" /></param>
    def post_convert_workbook_to_html(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_convert_workbook_to_html_with_http_info(request,**kwargs)
        else:
            (data) = self.post_convert_workbook_to_html_with_http_info(request,**kwargs)
            return data

    def post_convert_workbook_to_html_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_convert_workbook_to_html" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Convert Excel file to Markdown files.
    # </summary>
    # <param name="request">Request. <see cref="PostConvertWorkbookToMarkdownRequest" /></param>
    def post_convert_workbook_to_markdown(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_convert_workbook_to_markdown_with_http_info(request,**kwargs)
        else:
            (data) = self.post_convert_workbook_to_markdown_with_http_info(request,**kwargs)
            return data

    def post_convert_workbook_to_markdown_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_convert_workbook_to_markdown" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Convert Excel file to Json files.
    # </summary>
    # <param name="request">Request. <see cref="PostConvertWorkbookToJsonRequest" /></param>
    def post_convert_workbook_to_json(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_convert_workbook_to_json_with_http_info(request,**kwargs)
        else:
            (data) = self.post_convert_workbook_to_json_with_http_info(request,**kwargs)
            return data

    def post_convert_workbook_to_json_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_convert_workbook_to_json" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Convert Excel file to SQL Script files.
    # </summary>
    # <param name="request">Request. <see cref="PostConvertWorkbookToSQLRequest" /></param>
    def post_convert_workbook_to_sql(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_convert_workbook_to_sql_with_http_info(request,**kwargs)
        else:
            (data) = self.post_convert_workbook_to_sql_with_http_info(request,**kwargs)
            return data

    def post_convert_workbook_to_sql_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_convert_workbook_to_sql" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Convert Excel file to Csv files.
    # </summary>
    # <param name="request">Request. <see cref="PostConvertWorkbookToCSVRequest" /></param>
    def post_convert_workbook_to_csv(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_convert_workbook_to_csv_with_http_info(request,**kwargs)
        else:
            (data) = self.post_convert_workbook_to_csv_with_http_info(request,**kwargs)
            return data

    def post_convert_workbook_to_csv_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_convert_workbook_to_csv" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # </summary>
    # <param name="request">Request. <see cref="PostConvertWorksheetToImageRequest" /></param>
    def post_convert_worksheet_to_image(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_convert_worksheet_to_image_with_http_info(request,**kwargs)
        else:
            (data) = self.post_convert_worksheet_to_image_with_http_info(request,**kwargs)
            return data

    def post_convert_worksheet_to_image_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_convert_worksheet_to_image" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # </summary>
    # <param name="request">Request. <see cref="PostConvertWorkbookRequest" /></param>
    def post_convert_workbook(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_convert_workbook_with_http_info(request,**kwargs)
        else:
            (data) = self.post_convert_workbook_with_http_info(request,**kwargs)
            return data

    def post_convert_workbook_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_convert_workbook" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Export Excel internal elements or the workbook itself to various format files.
    # </summary>
    # <param name="request">Request. <see cref="CheckWrokbookExternalReferenceRequest" /></param>
    def check_wrokbook_external_reference(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.check_wrokbook_external_reference_with_http_info(request,**kwargs)
        else:
            (data) = self.check_wrokbook_external_reference_with_http_info(request,**kwargs)
            return data

    def check_wrokbook_external_reference_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method check_wrokbook_external_reference" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # </summary>
    # <param name="request">Request. <see cref="CheckWorkbookFormulaErrorsRequest" /></param>
    def check_workbook_formula_errors(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.check_workbook_formula_errors_with_http_info(request,**kwargs)
        else:
            (data) = self.check_workbook_formula_errors_with_http_info(request,**kwargs)
            return data

    def check_workbook_formula_errors_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method check_workbook_formula_errors" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Export Excel internal elements or the workbook itself to various format files.
    # </summary>
    # <param name="request">Request. <see cref="PostExportRequest" /></param>
    def post_export(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_export_with_http_info(request,**kwargs)
        else:
            (data) = self.post_export_with_http_info(request,**kwargs)
            return data

    def post_export_with_http_info(self, request, **kwargs):
        all_params = []
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

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Export XML data from an Excel file.
    # When there are XML Maps in an Excel file, export XML data. When there is no XML map in the Excel file, convert the Excel file to an XML file.
    # </summary>
    # <param name="request">Request. <see cref="PostWorkbookExportXMLRequest" /></param>
    def post_workbook_export_xml(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        response_file = None
        if kwargs.get('callback'):
            response_file = self.post_workbook_export_xml_with_http_info(request,**kwargs)
        else:
            (data) = self.post_workbook_export_xml_with_http_info(request,**kwargs)
            response_file = data
        if kwargs.get('local_outpath'):
            shutil.move( response_file , kwargs.get('local_outpath'))
            return kwargs.get('local_outpath')
        else:
            return response_file
    def post_workbook_export_xml_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('local_outpath')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workbook_export_xml" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Import a JSON data file into the workbook. The JSON data file can either be a cloud file or data from an HTTP URI.
    # </summary>
    # <param name="request">Request. <see cref="PostWorkbookImportJsonRequest" /></param>
    def post_workbook_import_json(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        response_file = None
        if kwargs.get('callback'):
            response_file = self.post_workbook_import_json_with_http_info(request,**kwargs)
        else:
            (data) = self.post_workbook_import_json_with_http_info(request,**kwargs)
            response_file = data
        if kwargs.get('local_outpath'):
            shutil.move( response_file , kwargs.get('local_outpath'))
            return kwargs.get('local_outpath')
        else:
            return response_file
    def post_workbook_import_json_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('local_outpath')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workbook_import_json" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Import an XML data file into an Excel file. The XML data file can either be a cloud file or data from an HTTP URI.
    # </summary>
    # <param name="request">Request. <see cref="PostWorkbookImportXMLRequest" /></param>
    def post_workbook_import_xml(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        response_file = None
        if kwargs.get('callback'):
            response_file = self.post_workbook_import_xml_with_http_info(request,**kwargs)
        else:
            (data) = self.post_workbook_import_xml_with_http_info(request,**kwargs)
            response_file = data
        if kwargs.get('local_outpath'):
            shutil.move( response_file , kwargs.get('local_outpath'))
            return kwargs.get('local_outpath')
        else:
            return response_file
    def post_workbook_import_xml_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('local_outpath')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workbook_import_xml" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Import data into the Excel file.
    # </summary>
    # <param name="request">Request. <see cref="PostImportDataRequest" /></param>
    def post_import_data(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_import_data_with_http_info(request,**kwargs)
        else:
            (data) = self.post_import_data_with_http_info(request,**kwargs)
            return data

    def post_import_data_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_import_data" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Data cleaning of spreadsheet files is a data management process used to identify, correct, and remove errors, incompleteness, duplicates, or inaccuracies in tables and ranges.
    # </summary>
    # <param name="request">Request. <see cref="PostWorkbookDataCleansingRequest" /></param>
    def post_workbook_data_cleansing(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_workbook_data_cleansing_with_http_info(request,**kwargs)
        else:
            (data) = self.post_workbook_data_cleansing_with_http_info(request,**kwargs)
            return data

    def post_workbook_data_cleansing_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workbook_data_cleansing" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Data cleansing of spreadsheet files is a data management process used to identify, correct, and remove errors, incompleteness, duplicates, or inaccuracies in tables and ranges.
    # </summary>
    # <param name="request">Request. <see cref="PostDataCleansingRequest" /></param>
    def post_data_cleansing(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_data_cleansing_with_http_info(request,**kwargs)
        else:
            (data) = self.post_data_cleansing_with_http_info(request,**kwargs)
            return data

    def post_data_cleansing_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_data_cleansing" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Data deduplication of spreadsheet files is mainly used to eliminate duplicate data in tables and ranges.
    # </summary>
    # <param name="request">Request. <see cref="PostWorkbookDataDeduplicationRequest" /></param>
    def post_workbook_data_deduplication(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_workbook_data_deduplication_with_http_info(request,**kwargs)
        else:
            (data) = self.post_workbook_data_deduplication_with_http_info(request,**kwargs)
            return data

    def post_workbook_data_deduplication_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workbook_data_deduplication" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Data deduplication of spreadsheet files is mainly used to eliminate duplicate data in tables and ranges.
    # </summary>
    # <param name="request">Request. <see cref="PostDataDeduplicationRequest" /></param>
    def post_data_deduplication(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_data_deduplication_with_http_info(request,**kwargs)
        else:
            (data) = self.post_data_deduplication_with_http_info(request,**kwargs)
            return data

    def post_data_deduplication_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_data_deduplication" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Data filling for spreadsheet files is primarily used to fill empty data in tables and ranges.
    # </summary>
    # <param name="request">Request. <see cref="PostWorkbookDataFillRequest" /></param>
    def post_workbook_data_fill(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_workbook_data_fill_with_http_info(request,**kwargs)
        else:
            (data) = self.post_workbook_data_fill_with_http_info(request,**kwargs)
            return data

    def post_workbook_data_fill_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workbook_data_fill" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Data filling for spreadsheet files is primarily used to fill empty data in tables and ranges.
    # </summary>
    # <param name="request">Request. <see cref="PostDataFillRequest" /></param>
    def post_data_fill(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_data_fill_with_http_info(request,**kwargs)
        else:
            (data) = self.post_data_fill_with_http_info(request,**kwargs)
            return data

    def post_data_fill_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_data_fill" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Deleting incomplete rows of spreadsheet files is mainly used to eliminate incomplete rows in tables and ranges.
    # </summary>
    # <param name="request">Request. <see cref="PostDeleteIncompleteRowsRequest" /></param>
    def post_delete_incomplete_rows(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_delete_incomplete_rows_with_http_info(request,**kwargs)
        else:
            (data) = self.post_delete_incomplete_rows_with_http_info(request,**kwargs)
            return data

    def post_delete_incomplete_rows_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_delete_incomplete_rows" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Transform spreadsheet data is mainly used to pivot columns, unpivot columns.
    # </summary>
    # <param name="request">Request. <see cref="PostDataTransformationRequest" /></param>
    def post_data_transformation(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_data_transformation_with_http_info(request,**kwargs)
        else:
            (data) = self.post_data_transformation_with_http_info(request,**kwargs)
            return data

    def post_data_transformation_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_data_transformation" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Retrieve descriptions of hyperlinks in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="GetWorksheetHyperlinksRequest" /></param>
    def get_worksheet_hyperlinks(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_worksheet_hyperlinks_with_http_info(request,**kwargs)
        else:
            (data) = self.get_worksheet_hyperlinks_with_http_info(request,**kwargs)
            return data

    def get_worksheet_hyperlinks_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_worksheet_hyperlinks" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Retrieve hyperlink description by index in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="GetWorksheetHyperlinkRequest" /></param>
    def get_worksheet_hyperlink(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_worksheet_hyperlink_with_http_info(request,**kwargs)
        else:
            (data) = self.get_worksheet_hyperlink_with_http_info(request,**kwargs)
            return data

    def get_worksheet_hyperlink_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_worksheet_hyperlink" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Delete hyperlink by index in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="DeleteWorksheetHyperlinkRequest" /></param>
    def delete_worksheet_hyperlink(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.delete_worksheet_hyperlink_with_http_info(request,**kwargs)
        else:
            (data) = self.delete_worksheet_hyperlink_with_http_info(request,**kwargs)
            return data

    def delete_worksheet_hyperlink_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_worksheet_hyperlink" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Update hyperlink by index in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PostWorksheetHyperlinkRequest" /></param>
    def post_worksheet_hyperlink(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_worksheet_hyperlink_with_http_info(request,**kwargs)
        else:
            (data) = self.post_worksheet_hyperlink_with_http_info(request,**kwargs)
            return data

    def post_worksheet_hyperlink_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_worksheet_hyperlink" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Add hyperlink in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PutWorksheetHyperlinkRequest" /></param>
    def put_worksheet_hyperlink(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.put_worksheet_hyperlink_with_http_info(request,**kwargs)
        else:
            (data) = self.put_worksheet_hyperlink_with_http_info(request,**kwargs)
            return data

    def put_worksheet_hyperlink_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_worksheet_hyperlink" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Delete all hyperlinks in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="DeleteWorksheetHyperlinksRequest" /></param>
    def delete_worksheet_hyperlinks(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.delete_worksheet_hyperlinks_with_http_info(request,**kwargs)
        else:
            (data) = self.delete_worksheet_hyperlinks_with_http_info(request,**kwargs)
            return data

    def delete_worksheet_hyperlinks_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_worksheet_hyperlinks" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Assemble data files with template files to generate files in various formats.
    # </summary>
    # <param name="request">Request. <see cref="PostAssembleRequest" /></param>
    def post_assemble(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_assemble_with_http_info(request,**kwargs)
        else:
            (data) = self.post_assemble_with_http_info(request,**kwargs)
            return data

    def post_assemble_with_http_info(self, request, **kwargs):
        all_params = []
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

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Compress files and generate target files in various formats, supported file formats are include Xls, Xlsx, Xlsm, Xlsb, Ods and more.
    # </summary>
    # <param name="request">Request. <see cref="PostCompressRequest" /></param>
    def post_compress(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_compress_with_http_info(request,**kwargs)
        else:
            (data) = self.post_compress_with_http_info(request,**kwargs)
            return data

    def post_compress_with_http_info(self, request, **kwargs):
        all_params = []
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

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Merge cells in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PostMergeRequest" /></param>
    def post_merge(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_merge_with_http_info(request,**kwargs)
        else:
            (data) = self.post_merge_with_http_info(request,**kwargs)
            return data

    def post_merge_with_http_info(self, request, **kwargs):
        all_params = []
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

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Split Excel spreadsheet files based on worksheets and create output files in various formats.
    # </summary>
    # <param name="request">Request. <see cref="PostSplitRequest" /></param>
    def post_split(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_split_with_http_info(request,**kwargs)
        else:
            (data) = self.post_split_with_http_info(request,**kwargs)
            return data

    def post_split_with_http_info(self, request, **kwargs):
        all_params = []
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

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Search for specified text within Excel files.
    # </summary>
    # <param name="request">Request. <see cref="PostSearchRequest" /></param>
    def post_search(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_search_with_http_info(request,**kwargs)
        else:
            (data) = self.post_search_with_http_info(request,**kwargs)
            return data

    def post_search_with_http_info(self, request, **kwargs):
        all_params = []
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

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Replace specified text with new text in Excel files.
    # </summary>
    # <param name="request">Request. <see cref="PostReplaceRequest" /></param>
    def post_replace(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_replace_with_http_info(request,**kwargs)
        else:
            (data) = self.post_replace_with_http_info(request,**kwargs)
            return data

    def post_replace_with_http_info(self, request, **kwargs):
        all_params = []
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

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Import data into an Excel file and generate output files in various formats.
    # </summary>
    # <param name="request">Request. <see cref="PostImportRequest" /></param>
    def post_import(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_import_with_http_info(request,**kwargs)
        else:
            (data) = self.post_import_with_http_info(request,**kwargs)
            return data

    def post_import_with_http_info(self, request, **kwargs):
        all_params = []
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

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Add Text Watermark to Excel files and generate output files in various formats.
    # </summary>
    # <param name="request">Request. <see cref="PostWatermarkRequest" /></param>
    def post_watermark(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_watermark_with_http_info(request,**kwargs)
        else:
            (data) = self.post_watermark_with_http_info(request,**kwargs)
            return data

    def post_watermark_with_http_info(self, request, **kwargs):
        all_params = []
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

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Clear internal elements in Excel files and generate output files in various formats.
    # </summary>
    # <param name="request">Request. <see cref="PostClearObjectsRequest" /></param>
    def post_clear_objects(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_clear_objects_with_http_info(request,**kwargs)
        else:
            (data) = self.post_clear_objects_with_http_info(request,**kwargs)
            return data

    def post_clear_objects_with_http_info(self, request, **kwargs):
        all_params = []
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

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Reverse rows or columns in Excel files and create output files in various formats.
    # </summary>
    # <param name="request">Request. <see cref="PostReverseRequest" /></param>
    def post_reverse(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_reverse_with_http_info(request,**kwargs)
        else:
            (data) = self.post_reverse_with_http_info(request,**kwargs)
            return data

    def post_reverse_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_reverse" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Repair abnormal files and generate files in various formats.
    # </summary>
    # <param name="request">Request. <see cref="PostRepairRequest" /></param>
    def post_repair(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_repair_with_http_info(request,**kwargs)
        else:
            (data) = self.post_repair_with_http_info(request,**kwargs)
            return data

    def post_repair_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_repair" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Rotate rows, columns, or other objects in Excel files and save them in various formats.
    # </summary>
    # <param name="request">Request. <see cref="PostRotateRequest" /></param>
    def post_rotate(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_rotate_with_http_info(request,**kwargs)
        else:
            (data) = self.post_rotate_with_http_info(request,**kwargs)
            return data

    def post_rotate_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_rotate" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Update document properties in Excel file, and save them is various formats.
    # </summary>
    # <param name="request">Request. <see cref="PostMetadataRequest" /></param>
    def post_metadata(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_metadata_with_http_info(request,**kwargs)
        else:
            (data) = self.post_metadata_with_http_info(request,**kwargs)
            return data

    def post_metadata_with_http_info(self, request, **kwargs):
        all_params = []
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

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Get cells document properties.
    # </summary>
    # <param name="request">Request. <see cref="GetMetadataRequest" /></param>
    def get_metadata(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_metadata_with_http_info(request,**kwargs)
        else:
            (data) = self.get_metadata_with_http_info(request,**kwargs)
            return data

    def get_metadata_with_http_info(self, request, **kwargs):
        all_params = []
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

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Delete cells document properties in Excel file, and save them is various formats.
    # </summary>
    # <param name="request">Request. <see cref="DeleteMetadataRequest" /></param>
    def delete_metadata(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.delete_metadata_with_http_info(request,**kwargs)
        else:
            (data) = self.delete_metadata_with_http_info(request,**kwargs)
            return data

    def delete_metadata_with_http_info(self, request, **kwargs):
        all_params = []
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

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Retrieve descriptions of ListObjects in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="GetWorksheetListObjectsRequest" /></param>
    def get_worksheet_list_objects(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_worksheet_list_objects_with_http_info(request,**kwargs)
        else:
            (data) = self.get_worksheet_list_objects_with_http_info(request,**kwargs)
            return data

    def get_worksheet_list_objects_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_worksheet_list_objects" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Retrieve list object description by index in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="GetWorksheetListObjectRequest" /></param>
    def get_worksheet_list_object(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        response_file = None
        if kwargs.get('callback'):
            response_file = self.get_worksheet_list_object_with_http_info(request,**kwargs)
        else:
            (data) = self.get_worksheet_list_object_with_http_info(request,**kwargs)
            response_file = data
        if kwargs.get('local_outpath'):
            shutil.move( response_file , kwargs.get('local_outpath'))
            return kwargs.get('local_outpath')
        else:
            return response_file
    def get_worksheet_list_object_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('local_outpath')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_worksheet_list_object" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Add a ListObject in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PutWorksheetListObjectRequest" /></param>
    def put_worksheet_list_object(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.put_worksheet_list_object_with_http_info(request,**kwargs)
        else:
            (data) = self.put_worksheet_list_object_with_http_info(request,**kwargs)
            return data

    def put_worksheet_list_object_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_worksheet_list_object" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Delete ListObjects in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="DeleteWorksheetListObjectsRequest" /></param>
    def delete_worksheet_list_objects(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.delete_worksheet_list_objects_with_http_info(request,**kwargs)
        else:
            (data) = self.delete_worksheet_list_objects_with_http_info(request,**kwargs)
            return data

    def delete_worksheet_list_objects_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_worksheet_list_objects" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Delete list object by index in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="DeleteWorksheetListObjectRequest" /></param>
    def delete_worksheet_list_object(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.delete_worksheet_list_object_with_http_info(request,**kwargs)
        else:
            (data) = self.delete_worksheet_list_object_with_http_info(request,**kwargs)
            return data

    def delete_worksheet_list_object_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_worksheet_list_object" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Update list object by index in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PostWorksheetListObjectRequest" /></param>
    def post_worksheet_list_object(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_worksheet_list_object_with_http_info(request,**kwargs)
        else:
            (data) = self.post_worksheet_list_object_with_http_info(request,**kwargs)
            return data

    def post_worksheet_list_object_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_worksheet_list_object" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Convert list object to range in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PostWorksheetListObjectConvertToRangeRequest" /></param>
    def post_worksheet_list_object_convert_to_range(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_worksheet_list_object_convert_to_range_with_http_info(request,**kwargs)
        else:
            (data) = self.post_worksheet_list_object_convert_to_range_with_http_info(request,**kwargs)
            return data

    def post_worksheet_list_object_convert_to_range_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_worksheet_list_object_convert_to_range" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Create a pivot table with a list object in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PostWorksheetListObjectSummarizeWithPivotTableRequest" /></param>
    def post_worksheet_list_object_summarize_with_pivot_table(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_worksheet_list_object_summarize_with_pivot_table_with_http_info(request,**kwargs)
        else:
            (data) = self.post_worksheet_list_object_summarize_with_pivot_table_with_http_info(request,**kwargs)
            return data

    def post_worksheet_list_object_summarize_with_pivot_table_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_worksheet_list_object_summarize_with_pivot_table" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Sort list object in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PostWorksheetListObjectSortTableRequest" /></param>
    def post_worksheet_list_object_sort_table(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_worksheet_list_object_sort_table_with_http_info(request,**kwargs)
        else:
            (data) = self.post_worksheet_list_object_sort_table_with_http_info(request,**kwargs)
            return data

    def post_worksheet_list_object_sort_table_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_worksheet_list_object_sort_table" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Remove duplicates in list object.
    # </summary>
    # <param name="request">Request. <see cref="PostWorksheetListObjectRemoveDuplicatesRequest" /></param>
    def post_worksheet_list_object_remove_duplicates(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_worksheet_list_object_remove_duplicates_with_http_info(request,**kwargs)
        else:
            (data) = self.post_worksheet_list_object_remove_duplicates_with_http_info(request,**kwargs)
            return data

    def post_worksheet_list_object_remove_duplicates_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_worksheet_list_object_remove_duplicates" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Insert slicer for list object.
    # </summary>
    # <param name="request">Request. <see cref="PostWorksheetListObjectInsertSlicerRequest" /></param>
    def post_worksheet_list_object_insert_slicer(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_worksheet_list_object_insert_slicer_with_http_info(request,**kwargs)
        else:
            (data) = self.post_worksheet_list_object_insert_slicer_with_http_info(request,**kwargs)
            return data

    def post_worksheet_list_object_insert_slicer_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_worksheet_list_object_insert_slicer" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Update list column in list object.
    # </summary>
    # <param name="request">Request. <see cref="PostWorksheetListColumnRequest" /></param>
    def post_worksheet_list_column(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_worksheet_list_column_with_http_info(request,**kwargs)
        else:
            (data) = self.post_worksheet_list_column_with_http_info(request,**kwargs)
            return data

    def post_worksheet_list_column_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_worksheet_list_column" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Update total of list columns in the table.
    # </summary>
    # <param name="request">Request. <see cref="PostWorksheetListColumnsTotalRequest" /></param>
    def post_worksheet_list_columns_total(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_worksheet_list_columns_total_with_http_info(request,**kwargs)
        else:
            (data) = self.post_worksheet_list_columns_total_with_http_info(request,**kwargs)
            return data

    def post_worksheet_list_columns_total_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_worksheet_list_columns_total" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Retrieve descriptions of OLE objects in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="GetWorksheetOleObjectsRequest" /></param>
    def get_worksheet_ole_objects(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_worksheet_ole_objects_with_http_info(request,**kwargs)
        else:
            (data) = self.get_worksheet_ole_objects_with_http_info(request,**kwargs)
            return data

    def get_worksheet_ole_objects_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_worksheet_ole_objects" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Retrieve the OLE object in a specified format in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="GetWorksheetOleObjectRequest" /></param>
    def get_worksheet_ole_object(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        response_file = None
        if kwargs.get('callback'):
            response_file = self.get_worksheet_ole_object_with_http_info(request,**kwargs)
        else:
            (data) = self.get_worksheet_ole_object_with_http_info(request,**kwargs)
            response_file = data
        if kwargs.get('local_outpath'):
            shutil.move( response_file , kwargs.get('local_outpath'))
            return kwargs.get('local_outpath')
        else:
            return response_file
    def get_worksheet_ole_object_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('local_outpath')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_worksheet_ole_object" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Delete all OLE objects in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="DeleteWorksheetOleObjectsRequest" /></param>
    def delete_worksheet_ole_objects(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.delete_worksheet_ole_objects_with_http_info(request,**kwargs)
        else:
            (data) = self.delete_worksheet_ole_objects_with_http_info(request,**kwargs)
            return data

    def delete_worksheet_ole_objects_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_worksheet_ole_objects" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Delete an OLE object in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="DeleteWorksheetOleObjectRequest" /></param>
    def delete_worksheet_ole_object(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.delete_worksheet_ole_object_with_http_info(request,**kwargs)
        else:
            (data) = self.delete_worksheet_ole_object_with_http_info(request,**kwargs)
            return data

    def delete_worksheet_ole_object_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_worksheet_ole_object" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Update an OLE object in worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PostUpdateWorksheetOleObjectRequest" /></param>
    def post_update_worksheet_ole_object(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_update_worksheet_ole_object_with_http_info(request,**kwargs)
        else:
            (data) = self.post_update_worksheet_ole_object_with_http_info(request,**kwargs)
            return data

    def post_update_worksheet_ole_object_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_update_worksheet_ole_object" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Add an OLE object in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PutWorksheetOleObjectRequest" /></param>
    def put_worksheet_ole_object(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.put_worksheet_ole_object_with_http_info(request,**kwargs)
        else:
            (data) = self.put_worksheet_ole_object_with_http_info(request,**kwargs)
            return data

    def put_worksheet_ole_object_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_worksheet_ole_object" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Retrieve descriptions of vertical page breaks in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="GetVerticalPageBreaksRequest" /></param>
    def get_vertical_page_breaks(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_vertical_page_breaks_with_http_info(request,**kwargs)
        else:
            (data) = self.get_vertical_page_breaks_with_http_info(request,**kwargs)
            return data

    def get_vertical_page_breaks_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_vertical_page_breaks" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Retrieve descriptions of horizontal page breaks in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="GetHorizontalPageBreaksRequest" /></param>
    def get_horizontal_page_breaks(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_horizontal_page_breaks_with_http_info(request,**kwargs)
        else:
            (data) = self.get_horizontal_page_breaks_with_http_info(request,**kwargs)
            return data

    def get_horizontal_page_breaks_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_horizontal_page_breaks" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Retrieve a vertical page break description in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="GetVerticalPageBreakRequest" /></param>
    def get_vertical_page_break(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_vertical_page_break_with_http_info(request,**kwargs)
        else:
            (data) = self.get_vertical_page_break_with_http_info(request,**kwargs)
            return data

    def get_vertical_page_break_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_vertical_page_break" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Retrieve a horizontal page break descripton in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="GetHorizontalPageBreakRequest" /></param>
    def get_horizontal_page_break(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_horizontal_page_break_with_http_info(request,**kwargs)
        else:
            (data) = self.get_horizontal_page_break_with_http_info(request,**kwargs)
            return data

    def get_horizontal_page_break_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_horizontal_page_break" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Add a vertical page break in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PutVerticalPageBreakRequest" /></param>
    def put_vertical_page_break(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.put_vertical_page_break_with_http_info(request,**kwargs)
        else:
            (data) = self.put_vertical_page_break_with_http_info(request,**kwargs)
            return data

    def put_vertical_page_break_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_vertical_page_break" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Add a horizontal page breaks in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PutHorizontalPageBreakRequest" /></param>
    def put_horizontal_page_break(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.put_horizontal_page_break_with_http_info(request,**kwargs)
        else:
            (data) = self.put_horizontal_page_break_with_http_info(request,**kwargs)
            return data

    def put_horizontal_page_break_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_horizontal_page_break" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Delete vertical page breaks in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="DeleteVerticalPageBreaksRequest" /></param>
    def delete_vertical_page_breaks(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.delete_vertical_page_breaks_with_http_info(request,**kwargs)
        else:
            (data) = self.delete_vertical_page_breaks_with_http_info(request,**kwargs)
            return data

    def delete_vertical_page_breaks_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_vertical_page_breaks" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Delete horizontal page breaks in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="DeleteHorizontalPageBreaksRequest" /></param>
    def delete_horizontal_page_breaks(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.delete_horizontal_page_breaks_with_http_info(request,**kwargs)
        else:
            (data) = self.delete_horizontal_page_breaks_with_http_info(request,**kwargs)
            return data

    def delete_horizontal_page_breaks_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_horizontal_page_breaks" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Delete a vertical page break in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="DeleteVerticalPageBreakRequest" /></param>
    def delete_vertical_page_break(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.delete_vertical_page_break_with_http_info(request,**kwargs)
        else:
            (data) = self.delete_vertical_page_break_with_http_info(request,**kwargs)
            return data

    def delete_vertical_page_break_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_vertical_page_break" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Delete a horizontal page break in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="DeleteHorizontalPageBreakRequest" /></param>
    def delete_horizontal_page_break(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.delete_horizontal_page_break_with_http_info(request,**kwargs)
        else:
            (data) = self.delete_horizontal_page_break_with_http_info(request,**kwargs)
            return data

    def delete_horizontal_page_break_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_horizontal_page_break" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Retrieve page setup description in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="GetPageSetupRequest" /></param>
    def get_page_setup(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_page_setup_with_http_info(request,**kwargs)
        else:
            (data) = self.get_page_setup_with_http_info(request,**kwargs)
            return data

    def get_page_setup_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_page_setup" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Update page setup in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PostPageSetupRequest" /></param>
    def post_page_setup(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_page_setup_with_http_info(request,**kwargs)
        else:
            (data) = self.post_page_setup_with_http_info(request,**kwargs)
            return data

    def post_page_setup_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_page_setup" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Clear header and footer in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="DeleteHeaderFooterRequest" /></param>
    def delete_header_footer(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.delete_header_footer_with_http_info(request,**kwargs)
        else:
            (data) = self.delete_header_footer_with_http_info(request,**kwargs)
            return data

    def delete_header_footer_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_header_footer" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Retrieve page header description in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="GetHeaderRequest" /></param>
    def get_header(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_header_with_http_info(request,**kwargs)
        else:
            (data) = self.get_header_with_http_info(request,**kwargs)
            return data

    def get_header_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_header" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Update page header in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PostHeaderRequest" /></param>
    def post_header(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_header_with_http_info(request,**kwargs)
        else:
            (data) = self.post_header_with_http_info(request,**kwargs)
            return data

    def post_header_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_header" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Retrieve page footer description in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="GetFooterRequest" /></param>
    def get_footer(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_footer_with_http_info(request,**kwargs)
        else:
            (data) = self.get_footer_with_http_info(request,**kwargs)
            return data

    def get_footer_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_footer" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Update page footer in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PostFooterRequest" /></param>
    def post_footer(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_footer_with_http_info(request,**kwargs)
        else:
            (data) = self.post_footer_with_http_info(request,**kwargs)
            return data

    def post_footer_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_footer" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Set the scale at which the page will fit wide when printed on the sheet.
    # </summary>
    # <param name="request">Request. <see cref="PostFitWideToPagesRequest" /></param>
    def post_fit_wide_to_pages(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_fit_wide_to_pages_with_http_info(request,**kwargs)
        else:
            (data) = self.post_fit_wide_to_pages_with_http_info(request,**kwargs)
            return data

    def post_fit_wide_to_pages_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_fit_wide_to_pages" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Set the scale at which the page will fit tall when printed on the sheet.
    # </summary>
    # <param name="request">Request. <see cref="PostFitTallToPagesRequest" /></param>
    def post_fit_tall_to_pages(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_fit_tall_to_pages_with_http_info(request,**kwargs)
        else:
            (data) = self.post_fit_tall_to_pages_with_http_info(request,**kwargs)
            return data

    def post_fit_tall_to_pages_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_fit_tall_to_pages" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Retrieve descriptions of pictures in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="GetWorksheetPicturesRequest" /></param>
    def get_worksheet_pictures(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_worksheet_pictures_with_http_info(request,**kwargs)
        else:
            (data) = self.get_worksheet_pictures_with_http_info(request,**kwargs)
            return data

    def get_worksheet_pictures_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_worksheet_pictures" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Retrieve a picture by number in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="GetWorksheetPictureWithFormatRequest" /></param>
    def get_worksheet_picture_with_format(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        response_file = None
        if kwargs.get('callback'):
            response_file = self.get_worksheet_picture_with_format_with_http_info(request,**kwargs)
        else:
            (data) = self.get_worksheet_picture_with_format_with_http_info(request,**kwargs)
            response_file = data
        if kwargs.get('local_outpath'):
            shutil.move( response_file , kwargs.get('local_outpath'))
            return kwargs.get('local_outpath')
        else:
            return response_file
    def get_worksheet_picture_with_format_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('local_outpath')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_worksheet_picture_with_format" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Add a new picture in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PutWorksheetAddPictureRequest" /></param>
    def put_worksheet_add_picture(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.put_worksheet_add_picture_with_http_info(request,**kwargs)
        else:
            (data) = self.put_worksheet_add_picture_with_http_info(request,**kwargs)
            return data

    def put_worksheet_add_picture_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_worksheet_add_picture" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # add new picture in the cells.
    # </summary>
    # <param name="request">Request. <see cref="AddPictureInCellRequest" /></param>
    def add_picture_in_cell(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.add_picture_in_cell_with_http_info(request,**kwargs)
        else:
            (data) = self.add_picture_in_cell_with_http_info(request,**kwargs)
            return data

    def add_picture_in_cell_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_picture_in_cell" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Update a picture by index in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PostWorksheetPictureRequest" /></param>
    def post_worksheet_picture(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_worksheet_picture_with_http_info(request,**kwargs)
        else:
            (data) = self.post_worksheet_picture_with_http_info(request,**kwargs)
            return data

    def post_worksheet_picture_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_worksheet_picture" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Delete a picture object by index in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="DeleteWorksheetPictureRequest" /></param>
    def delete_worksheet_picture(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.delete_worksheet_picture_with_http_info(request,**kwargs)
        else:
            (data) = self.delete_worksheet_picture_with_http_info(request,**kwargs)
            return data

    def delete_worksheet_picture_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_worksheet_picture" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Delete all pictures in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="DeleteWorksheetPicturesRequest" /></param>
    def delete_worksheet_pictures(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.delete_worksheet_pictures_with_http_info(request,**kwargs)
        else:
            (data) = self.delete_worksheet_pictures_with_http_info(request,**kwargs)
            return data

    def delete_worksheet_pictures_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_worksheet_pictures" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Retrieve descriptions of pivottables  in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="GetWorksheetPivotTablesRequest" /></param>
    def get_worksheet_pivot_tables(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_worksheet_pivot_tables_with_http_info(request,**kwargs)
        else:
            (data) = self.get_worksheet_pivot_tables_with_http_info(request,**kwargs)
            return data

    def get_worksheet_pivot_tables_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_worksheet_pivot_tables" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Retrieve PivotTable information by index in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="GetWorksheetPivotTableRequest" /></param>
    def get_worksheet_pivot_table(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_worksheet_pivot_table_with_http_info(request,**kwargs)
        else:
            (data) = self.get_worksheet_pivot_table_with_http_info(request,**kwargs)
            return data

    def get_worksheet_pivot_table_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_worksheet_pivot_table" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Retrieve descriptions of pivot fields in the PivotTable.
    # </summary>
    # <param name="request">Request. <see cref="GetPivotTableFieldRequest" /></param>
    def get_pivot_table_field(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_pivot_table_field_with_http_info(request,**kwargs)
        else:
            (data) = self.get_pivot_table_field_with_http_info(request,**kwargs)
            return data

    def get_pivot_table_field_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_pivot_table_field" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Gets PivotTable filters in worksheet.
    # </summary>
    # <param name="request">Request. <see cref="GetWorksheetPivotTableFiltersRequest" /></param>
    def get_worksheet_pivot_table_filters(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_worksheet_pivot_table_filters_with_http_info(request,**kwargs)
        else:
            (data) = self.get_worksheet_pivot_table_filters_with_http_info(request,**kwargs)
            return data

    def get_worksheet_pivot_table_filters_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_worksheet_pivot_table_filters" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Retrieve PivotTable filters in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="GetWorksheetPivotTableFilterRequest" /></param>
    def get_worksheet_pivot_table_filter(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_worksheet_pivot_table_filter_with_http_info(request,**kwargs)
        else:
            (data) = self.get_worksheet_pivot_table_filter_with_http_info(request,**kwargs)
            return data

    def get_worksheet_pivot_table_filter_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_worksheet_pivot_table_filter" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Add a PivotTable in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PutWorksheetPivotTableRequest" /></param>
    def put_worksheet_pivot_table(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.put_worksheet_pivot_table_with_http_info(request,**kwargs)
        else:
            (data) = self.put_worksheet_pivot_table_with_http_info(request,**kwargs)
            return data

    def put_worksheet_pivot_table_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_worksheet_pivot_table" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Add a pivot field in the PivotTable.
    # </summary>
    # <param name="request">Request. <see cref="PutPivotTableFieldRequest" /></param>
    def put_pivot_table_field(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.put_pivot_table_field_with_http_info(request,**kwargs)
        else:
            (data) = self.put_pivot_table_field_with_http_info(request,**kwargs)
            return data

    def put_pivot_table_field_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_pivot_table_field" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Add a pivot filter to the PivotTable.
    # </summary>
    # <param name="request">Request. <see cref="PutWorksheetPivotTableFilterRequest" /></param>
    def put_worksheet_pivot_table_filter(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.put_worksheet_pivot_table_filter_with_http_info(request,**kwargs)
        else:
            (data) = self.put_worksheet_pivot_table_filter_with_http_info(request,**kwargs)
            return data

    def put_worksheet_pivot_table_filter_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_worksheet_pivot_table_filter" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Hide a pivot field item in the PivotTable.
    # </summary>
    # <param name="request">Request. <see cref="PostPivotTableFieldHideItemRequest" /></param>
    def post_pivot_table_field_hide_item(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_pivot_table_field_hide_item_with_http_info(request,**kwargs)
        else:
            (data) = self.post_pivot_table_field_hide_item_with_http_info(request,**kwargs)
            return data

    def post_pivot_table_field_hide_item_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_pivot_table_field_hide_item" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Move a pivot field in the PivotTable.
    # </summary>
    # <param name="request">Request. <see cref="PostPivotTableFieldMoveToRequest" /></param>
    def post_pivot_table_field_move_to(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_pivot_table_field_move_to_with_http_info(request,**kwargs)
        else:
            (data) = self.post_pivot_table_field_move_to_with_http_info(request,**kwargs)
            return data

    def post_pivot_table_field_move_to_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_pivot_table_field_move_to" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Update cell style in the PivotTable.
    # </summary>
    # <param name="request">Request. <see cref="PostPivotTableCellStyleRequest" /></param>
    def post_pivot_table_cell_style(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_pivot_table_cell_style_with_http_info(request,**kwargs)
        else:
            (data) = self.post_pivot_table_cell_style_with_http_info(request,**kwargs)
            return data

    def post_pivot_table_cell_style_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_pivot_table_cell_style" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Update style in the PivotTable.
    # </summary>
    # <param name="request">Request. <see cref="PostPivotTableStyleRequest" /></param>
    def post_pivot_table_style(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_pivot_table_style_with_http_info(request,**kwargs)
        else:
            (data) = self.post_pivot_table_style_with_http_info(request,**kwargs)
            return data

    def post_pivot_table_style_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_pivot_table_style" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Update pivot fields in the PivotTable.
    # </summary>
    # <param name="request">Request. <see cref="PostPivotTableUpdatePivotFieldsRequest" /></param>
    def post_pivot_table_update_pivot_fields(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_pivot_table_update_pivot_fields_with_http_info(request,**kwargs)
        else:
            (data) = self.post_pivot_table_update_pivot_fields_with_http_info(request,**kwargs)
            return data

    def post_pivot_table_update_pivot_fields_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_pivot_table_update_pivot_fields" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Update pivot field in the PivotTable.
    # </summary>
    # <param name="request">Request. <see cref="PostPivotTableUpdatePivotFieldRequest" /></param>
    def post_pivot_table_update_pivot_field(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_pivot_table_update_pivot_field_with_http_info(request,**kwargs)
        else:
            (data) = self.post_pivot_table_update_pivot_field_with_http_info(request,**kwargs)
            return data

    def post_pivot_table_update_pivot_field_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_pivot_table_update_pivot_field" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Calculate pivottable's data to cells.
    # </summary>
    # <param name="request">Request. <see cref="PostWorksheetPivotTableCalculateRequest" /></param>
    def post_worksheet_pivot_table_calculate(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_worksheet_pivot_table_calculate_with_http_info(request,**kwargs)
        else:
            (data) = self.post_worksheet_pivot_table_calculate_with_http_info(request,**kwargs)
            return data

    def post_worksheet_pivot_table_calculate_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_worksheet_pivot_table_calculate" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Move PivotTable in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PostWorksheetPivotTableMoveRequest" /></param>
    def post_worksheet_pivot_table_move(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_worksheet_pivot_table_move_with_http_info(request,**kwargs)
        else:
            (data) = self.post_worksheet_pivot_table_move_with_http_info(request,**kwargs)
            return data

    def post_worksheet_pivot_table_move_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_worksheet_pivot_table_move" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Delete PivotTables in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="DeleteWorksheetPivotTablesRequest" /></param>
    def delete_worksheet_pivot_tables(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.delete_worksheet_pivot_tables_with_http_info(request,**kwargs)
        else:
            (data) = self.delete_worksheet_pivot_tables_with_http_info(request,**kwargs)
            return data

    def delete_worksheet_pivot_tables_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_worksheet_pivot_tables" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Delete PivotTable by index in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="DeleteWorksheetPivotTableRequest" /></param>
    def delete_worksheet_pivot_table(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.delete_worksheet_pivot_table_with_http_info(request,**kwargs)
        else:
            (data) = self.delete_worksheet_pivot_table_with_http_info(request,**kwargs)
            return data

    def delete_worksheet_pivot_table_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_worksheet_pivot_table" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Delete a pivot field in the PivotTable.
    # </summary>
    # <param name="request">Request. <see cref="DeletePivotTableFieldRequest" /></param>
    def delete_pivot_table_field(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.delete_pivot_table_field_with_http_info(request,**kwargs)
        else:
            (data) = self.delete_pivot_table_field_with_http_info(request,**kwargs)
            return data

    def delete_pivot_table_field_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_pivot_table_field" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Delete all pivot filters in the PivotTable.
    # </summary>
    # <param name="request">Request. <see cref="DeleteWorksheetPivotTableFiltersRequest" /></param>
    def delete_worksheet_pivot_table_filters(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.delete_worksheet_pivot_table_filters_with_http_info(request,**kwargs)
        else:
            (data) = self.delete_worksheet_pivot_table_filters_with_http_info(request,**kwargs)
            return data

    def delete_worksheet_pivot_table_filters_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_worksheet_pivot_table_filters" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Delete a pivot filter in the PivotTable.
    # </summary>
    # <param name="request">Request. <see cref="DeleteWorksheetPivotTableFilterRequest" /></param>
    def delete_worksheet_pivot_table_filter(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.delete_worksheet_pivot_table_filter_with_http_info(request,**kwargs)
        else:
            (data) = self.delete_worksheet_pivot_table_filter_with_http_info(request,**kwargs)
            return data

    def delete_worksheet_pivot_table_filter_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_worksheet_pivot_table_filter" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Retrieve descriptions of Excel file properties.
    # </summary>
    # <param name="request">Request. <see cref="GetDocumentPropertiesRequest" /></param>
    def get_document_properties(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_document_properties_with_http_info(request,**kwargs)
        else:
            (data) = self.get_document_properties_with_http_info(request,**kwargs)
            return data

    def get_document_properties_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_document_properties" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Set or add an Excel property.
    # </summary>
    # <param name="request">Request. <see cref="PutDocumentPropertyRequest" /></param>
    def put_document_property(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.put_document_property_with_http_info(request,**kwargs)
        else:
            (data) = self.put_document_property_with_http_info(request,**kwargs)
            return data

    def put_document_property_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_document_property" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Get Excel property by name.
    # </summary>
    # <param name="request">Request. <see cref="GetDocumentPropertyRequest" /></param>
    def get_document_property(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_document_property_with_http_info(request,**kwargs)
        else:
            (data) = self.get_document_property_with_http_info(request,**kwargs)
            return data

    def get_document_property_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_document_property" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Delete an Excel property.
    # </summary>
    # <param name="request">Request. <see cref="DeleteDocumentPropertyRequest" /></param>
    def delete_document_property(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.delete_document_property_with_http_info(request,**kwargs)
        else:
            (data) = self.delete_document_property_with_http_info(request,**kwargs)
            return data

    def delete_document_property_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_document_property" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Delete all custom document properties and reset built-in ones.
    # </summary>
    # <param name="request">Request. <see cref="DeleteDocumentPropertiesRequest" /></param>
    def delete_document_properties(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.delete_document_properties_with_http_info(request,**kwargs)
        else:
            (data) = self.delete_document_properties_with_http_info(request,**kwargs)
            return data

    def delete_document_properties_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_document_properties" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Excel file digital signature.
    # </summary>
    # <param name="request">Request. <see cref="PostDigitalSignatureRequest" /></param>
    def post_digital_signature(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_digital_signature_with_http_info(request,**kwargs)
        else:
            (data) = self.post_digital_signature_with_http_info(request,**kwargs)
            return data

    def post_digital_signature_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_digital_signature" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Excel Encryption.
    # </summary>
    # <param name="request">Request. <see cref="PostEncryptWorkbookRequest" /></param>
    def post_encrypt_workbook(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_encrypt_workbook_with_http_info(request,**kwargs)
        else:
            (data) = self.post_encrypt_workbook_with_http_info(request,**kwargs)
            return data

    def post_encrypt_workbook_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_encrypt_workbook" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Excel files decryption.
    # </summary>
    # <param name="request">Request. <see cref="DeleteDecryptWorkbookRequest" /></param>
    def delete_decrypt_workbook(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.delete_decrypt_workbook_with_http_info(request,**kwargs)
        else:
            (data) = self.delete_decrypt_workbook_with_http_info(request,**kwargs)
            return data

    def delete_decrypt_workbook_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_decrypt_workbook" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Excel protection.
    # </summary>
    # <param name="request">Request. <see cref="PostProtectWorkbookRequest" /></param>
    def post_protect_workbook(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_protect_workbook_with_http_info(request,**kwargs)
        else:
            (data) = self.post_protect_workbook_with_http_info(request,**kwargs)
            return data

    def post_protect_workbook_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_protect_workbook" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Excel unprotection.
    # </summary>
    # <param name="request">Request. <see cref="DeleteUnProtectWorkbookRequest" /></param>
    def delete_un_protect_workbook(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.delete_un_protect_workbook_with_http_info(request,**kwargs)
        else:
            (data) = self.delete_un_protect_workbook_with_http_info(request,**kwargs)
            return data

    def delete_un_protect_workbook_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_un_protect_workbook" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Excel file write protection.
    # </summary>
    # <param name="request">Request. <see cref="PutDocumentProtectFromChangesRequest" /></param>
    def put_document_protect_from_changes(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.put_document_protect_from_changes_with_http_info(request,**kwargs)
        else:
            (data) = self.put_document_protect_from_changes_with_http_info(request,**kwargs)
            return data

    def put_document_protect_from_changes_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_document_protect_from_changes" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Excel file cancel write protection.
    # </summary>
    # <param name="request">Request. <see cref="DeleteDocumentUnProtectFromChangesRequest" /></param>
    def delete_document_un_protect_from_changes(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.delete_document_un_protect_from_changes_with_http_info(request,**kwargs)
        else:
            (data) = self.delete_document_un_protect_from_changes_with_http_info(request,**kwargs)
            return data

    def delete_document_un_protect_from_changes_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_document_un_protect_from_changes" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Unlock Excel files.
    # </summary>
    # <param name="request">Request. <see cref="PostUnlockRequest" /></param>
    def post_unlock(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_unlock_with_http_info(request,**kwargs)
        else:
            (data) = self.post_unlock_with_http_info(request,**kwargs)
            return data

    def post_unlock_with_http_info(self, request, **kwargs):
        all_params = []
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

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Lock Excel files.
    # </summary>
    # <param name="request">Request. <see cref="PostLockRequest" /></param>
    def post_lock(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_lock_with_http_info(request,**kwargs)
        else:
            (data) = self.post_lock_with_http_info(request,**kwargs)
            return data

    def post_lock_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_lock" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Excel files encryption.
    # </summary>
    # <param name="request">Request. <see cref="PostProtectRequest" /></param>
    def post_protect(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_protect_with_http_info(request,**kwargs)
        else:
            (data) = self.post_protect_with_http_info(request,**kwargs)
            return data

    def post_protect_with_http_info(self, request, **kwargs):
        all_params = []
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

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Copy content from the source range to the destination range in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PostWorksheetCellsRangesCopyRequest" /></param>
    def post_worksheet_cells_ranges_copy(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_worksheet_cells_ranges_copy_with_http_info(request,**kwargs)
        else:
            (data) = self.post_worksheet_cells_ranges_copy_with_http_info(request,**kwargs)
            return data

    def post_worksheet_cells_ranges_copy_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_worksheet_cells_ranges_copy" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Merge a range of cells into a single cell.
    # </summary>
    # <param name="request">Request. <see cref="PostWorksheetCellsRangeMergeRequest" /></param>
    def post_worksheet_cells_range_merge(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_worksheet_cells_range_merge_with_http_info(request,**kwargs)
        else:
            (data) = self.post_worksheet_cells_range_merge_with_http_info(request,**kwargs)
            return data

    def post_worksheet_cells_range_merge_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_worksheet_cells_range_merge" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Unmerge merged cells within this range.
    # </summary>
    # <param name="request">Request. <see cref="PostWorksheetCellsRangeUnMergeRequest" /></param>
    def post_worksheet_cells_range_un_merge(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_worksheet_cells_range_un_merge_with_http_info(request,**kwargs)
        else:
            (data) = self.post_worksheet_cells_range_un_merge_with_http_info(request,**kwargs)
            return data

    def post_worksheet_cells_range_un_merge_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_worksheet_cells_range_un_merge" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Set the style for the specified range.
    # </summary>
    # <param name="request">Request. <see cref="PostWorksheetCellsRangeStyleRequest" /></param>
    def post_worksheet_cells_range_style(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_worksheet_cells_range_style_with_http_info(request,**kwargs)
        else:
            (data) = self.post_worksheet_cells_range_style_with_http_info(request,**kwargs)
            return data

    def post_worksheet_cells_range_style_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_worksheet_cells_range_style" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Retrieve the values of cells within the specified range.
    # </summary>
    # <param name="request">Request. <see cref="GetWorksheetCellsRangeValueRequest" /></param>
    def get_worksheet_cells_range_value(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_worksheet_cells_range_value_with_http_info(request,**kwargs)
        else:
            (data) = self.get_worksheet_cells_range_value_with_http_info(request,**kwargs)
            return data

    def get_worksheet_cells_range_value_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_worksheet_cells_range_value" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Assign a value to the range; if necessary, the value will be converted to another data type, and the cell's number format will be reset.
    # </summary>
    # <param name="request">Request. <see cref="PostWorksheetCellsRangeValueRequest" /></param>
    def post_worksheet_cells_range_value(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_worksheet_cells_range_value_with_http_info(request,**kwargs)
        else:
            (data) = self.post_worksheet_cells_range_value_with_http_info(request,**kwargs)
            return data

    def post_worksheet_cells_range_value_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_worksheet_cells_range_value" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Move the current range to the destination range.
    # </summary>
    # <param name="request">Request. <see cref="PostWorksheetCellsRangeMoveToRequest" /></param>
    def post_worksheet_cells_range_move_to(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_worksheet_cells_range_move_to_with_http_info(request,**kwargs)
        else:
            (data) = self.post_worksheet_cells_range_move_to_with_http_info(request,**kwargs)
            return data

    def post_worksheet_cells_range_move_to_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_worksheet_cells_range_move_to" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Perform data sorting around a range of cells.
    # </summary>
    # <param name="request">Request. <see cref="PostWorksheetCellsRangeSortRequest" /></param>
    def post_worksheet_cells_range_sort(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_worksheet_cells_range_sort_with_http_info(request,**kwargs)
        else:
            (data) = self.post_worksheet_cells_range_sort_with_http_info(request,**kwargs)
            return data

    def post_worksheet_cells_range_sort_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_worksheet_cells_range_sort" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Apply an outline border around a range of cells.
    # </summary>
    # <param name="request">Request. <see cref="PostWorksheetCellsRangeOutlineBorderRequest" /></param>
    def post_worksheet_cells_range_outline_border(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_worksheet_cells_range_outline_border_with_http_info(request,**kwargs)
        else:
            (data) = self.post_worksheet_cells_range_outline_border_with_http_info(request,**kwargs)
            return data

    def post_worksheet_cells_range_outline_border_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_worksheet_cells_range_outline_border" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Set the column width of the specified range.
    # </summary>
    # <param name="request">Request. <see cref="PostWorksheetCellsRangeColumnWidthRequest" /></param>
    def post_worksheet_cells_range_column_width(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_worksheet_cells_range_column_width_with_http_info(request,**kwargs)
        else:
            (data) = self.post_worksheet_cells_range_column_width_with_http_info(request,**kwargs)
            return data

    def post_worksheet_cells_range_column_width_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_worksheet_cells_range_column_width" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Sets row height of range.
    # </summary>
    # <param name="request">Request. <see cref="PostWorksheetCellsRangeRowHeightRequest" /></param>
    def post_worksheet_cells_range_row_height(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_worksheet_cells_range_row_height_with_http_info(request,**kwargs)
        else:
            (data) = self.post_worksheet_cells_range_row_height_with_http_info(request,**kwargs)
            return data

    def post_worksheet_cells_range_row_height_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_worksheet_cells_range_row_height" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # </summary>
    # <param name="request">Request. <see cref="PostWorksheetCellsRangeToImageRequest" /></param>
    def post_worksheet_cells_range_to_image(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        response_file = None
        if kwargs.get('callback'):
            response_file = self.post_worksheet_cells_range_to_image_with_http_info(request,**kwargs)
        else:
            (data) = self.post_worksheet_cells_range_to_image_with_http_info(request,**kwargs)
            response_file = data
        if kwargs.get('local_outpath'):
            shutil.move( response_file , kwargs.get('local_outpath'))
            return kwargs.get('local_outpath')
        else:
            return response_file
    def post_worksheet_cells_range_to_image_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('local_outpath')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_worksheet_cells_range_to_image" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Insert a range of cells and shift existing cells based on the specified shift option.
    # </summary>
    # <param name="request">Request. <see cref="PutWorksheetCellsRangeRequest" /></param>
    def put_worksheet_cells_range(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.put_worksheet_cells_range_with_http_info(request,**kwargs)
        else:
            (data) = self.put_worksheet_cells_range_with_http_info(request,**kwargs)
            return data

    def put_worksheet_cells_range_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_worksheet_cells_range" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Delete a range of cells and shift existing cells based on the specified shift option.
    # </summary>
    # <param name="request">Request. <see cref="DeleteWorksheetCellsRangeRequest" /></param>
    def delete_worksheet_cells_range(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.delete_worksheet_cells_range_with_http_info(request,**kwargs)
        else:
            (data) = self.delete_worksheet_cells_range_with_http_info(request,**kwargs)
            return data

    def delete_worksheet_cells_range_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_worksheet_cells_range" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Retrieve descriptions of shapes in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="GetWorksheetShapesRequest" /></param>
    def get_worksheet_shapes(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_worksheet_shapes_with_http_info(request,**kwargs)
        else:
            (data) = self.get_worksheet_shapes_with_http_info(request,**kwargs)
            return data

    def get_worksheet_shapes_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_worksheet_shapes" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Retrieve description of shape in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="GetWorksheetShapeRequest" /></param>
    def get_worksheet_shape(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_worksheet_shape_with_http_info(request,**kwargs)
        else:
            (data) = self.get_worksheet_shape_with_http_info(request,**kwargs)
            return data

    def get_worksheet_shape_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_worksheet_shape" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Add a shape in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PutWorksheetShapeRequest" /></param>
    def put_worksheet_shape(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.put_worksheet_shape_with_http_info(request,**kwargs)
        else:
            (data) = self.put_worksheet_shape_with_http_info(request,**kwargs)
            return data

    def put_worksheet_shape_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_worksheet_shape" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Delete all shapes in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="DeleteWorksheetShapesRequest" /></param>
    def delete_worksheet_shapes(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.delete_worksheet_shapes_with_http_info(request,**kwargs)
        else:
            (data) = self.delete_worksheet_shapes_with_http_info(request,**kwargs)
            return data

    def delete_worksheet_shapes_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_worksheet_shapes" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Delete a shape in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="DeleteWorksheetShapeRequest" /></param>
    def delete_worksheet_shape(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.delete_worksheet_shape_with_http_info(request,**kwargs)
        else:
            (data) = self.delete_worksheet_shape_with_http_info(request,**kwargs)
            return data

    def delete_worksheet_shape_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_worksheet_shape" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Update a shape in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PostWorksheetShapeRequest" /></param>
    def post_worksheet_shape(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_worksheet_shape_with_http_info(request,**kwargs)
        else:
            (data) = self.post_worksheet_shape_with_http_info(request,**kwargs)
            return data

    def post_worksheet_shape_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_worksheet_shape" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Group shapes in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PostWorksheetGroupShapeRequest" /></param>
    def post_worksheet_group_shape(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_worksheet_group_shape_with_http_info(request,**kwargs)
        else:
            (data) = self.post_worksheet_group_shape_with_http_info(request,**kwargs)
            return data

    def post_worksheet_group_shape_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_worksheet_group_shape" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Ungroup shapes in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PostWorksheetUngroupShapeRequest" /></param>
    def post_worksheet_ungroup_shape(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_worksheet_ungroup_shape_with_http_info(request,**kwargs)
        else:
            (data) = self.post_worksheet_ungroup_shape_with_http_info(request,**kwargs)
            return data

    def post_worksheet_ungroup_shape_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_worksheet_ungroup_shape" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Retrieve descriptions of sparkline groups in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="GetWorksheetSparklineGroupsRequest" /></param>
    def get_worksheet_sparkline_groups(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_worksheet_sparkline_groups_with_http_info(request,**kwargs)
        else:
            (data) = self.get_worksheet_sparkline_groups_with_http_info(request,**kwargs)
            return data

    def get_worksheet_sparkline_groups_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_worksheet_sparkline_groups" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Retrieve description of a sparkline group in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="GetWorksheetSparklineGroupRequest" /></param>
    def get_worksheet_sparkline_group(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_worksheet_sparkline_group_with_http_info(request,**kwargs)
        else:
            (data) = self.get_worksheet_sparkline_group_with_http_info(request,**kwargs)
            return data

    def get_worksheet_sparkline_group_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_worksheet_sparkline_group" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Delete sparkline groups in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="DeleteWorksheetSparklineGroupsRequest" /></param>
    def delete_worksheet_sparkline_groups(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.delete_worksheet_sparkline_groups_with_http_info(request,**kwargs)
        else:
            (data) = self.delete_worksheet_sparkline_groups_with_http_info(request,**kwargs)
            return data

    def delete_worksheet_sparkline_groups_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_worksheet_sparkline_groups" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Delete a sparkline group in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="DeleteWorksheetSparklineGroupRequest" /></param>
    def delete_worksheet_sparkline_group(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.delete_worksheet_sparkline_group_with_http_info(request,**kwargs)
        else:
            (data) = self.delete_worksheet_sparkline_group_with_http_info(request,**kwargs)
            return data

    def delete_worksheet_sparkline_group_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_worksheet_sparkline_group" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Add a sparkline group in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PutWorksheetSparklineGroupRequest" /></param>
    def put_worksheet_sparkline_group(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.put_worksheet_sparkline_group_with_http_info(request,**kwargs)
        else:
            (data) = self.put_worksheet_sparkline_group_with_http_info(request,**kwargs)
            return data

    def put_worksheet_sparkline_group_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_worksheet_sparkline_group" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Update a sparkline group in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PostWorksheetSparklineGroupRequest" /></param>
    def post_worksheet_sparkline_group(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_worksheet_sparkline_group_with_http_info(request,**kwargs)
        else:
            (data) = self.post_worksheet_sparkline_group_with_http_info(request,**kwargs)
            return data

    def post_worksheet_sparkline_group_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_worksheet_sparkline_group" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # </summary>
    # <param name="request">Request. <see cref="PostCharacterCountRequest" /></param>
    def post_character_count(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_character_count_with_http_info(request,**kwargs)
        else:
            (data) = self.post_character_count_with_http_info(request,**kwargs)
            return data

    def post_character_count_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_character_count" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # </summary>
    # <param name="request">Request. <see cref="PostWordsCountRequest" /></param>
    def post_words_count(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_words_count_with_http_info(request,**kwargs)
        else:
            (data) = self.post_words_count_with_http_info(request,**kwargs)
            return data

    def post_words_count_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_words_count" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # </summary>
    # <param name="request">Request. <see cref="PostSpecifyWordsCountRequest" /></param>
    def post_specify_words_count(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_specify_words_count_with_http_info(request,**kwargs)
        else:
            (data) = self.post_specify_words_count_with_http_info(request,**kwargs)
            return data

    def post_specify_words_count_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_specify_words_count" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Run tasks.
    # </summary>
    # <param name="request">Request. <see cref="PostRunTaskRequest" /></param>
    def post_run_task(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        response_file = None
        if kwargs.get('callback'):
            response_file = self.post_run_task_with_http_info(request,**kwargs)
        else:
            (data) = self.post_run_task_with_http_info(request,**kwargs)
            response_file = data
        if kwargs.get('local_outpath'):
            shutil.move( response_file , kwargs.get('local_outpath'))
            return kwargs.get('local_outpath')
        else:
            return response_file
    def post_run_task_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('local_outpath')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_run_task" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Adds text content to a workbook at specified positions within cells based on provided options using ASP.NET Core Web API.
    # </summary>
    # <param name="request">Request. <see cref="PostAddTextContentRequest" /></param>
    def post_add_text_content(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_add_text_content_with_http_info(request,**kwargs)
        else:
            (data) = self.post_add_text_content_with_http_info(request,**kwargs)
            return data

    def post_add_text_content_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_add_text_content" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # </summary>
    # <param name="request">Request. <see cref="PostTrimContentRequest" /></param>
    def post_trim_content(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_trim_content_with_http_info(request,**kwargs)
        else:
            (data) = self.post_trim_content_with_http_info(request,**kwargs)
            return data

    def post_trim_content_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_trim_content" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # </summary>
    # <param name="request">Request. <see cref="PostUpdateWordCaseRequest" /></param>
    def post_update_word_case(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_update_word_case_with_http_info(request,**kwargs)
        else:
            (data) = self.post_update_word_case_with_http_info(request,**kwargs)
            return data

    def post_update_word_case_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_update_word_case" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # </summary>
    # <param name="request">Request. <see cref="PostRemoveCharactersRequest" /></param>
    def post_remove_characters(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_remove_characters_with_http_info(request,**kwargs)
        else:
            (data) = self.post_remove_characters_with_http_info(request,**kwargs)
            return data

    def post_remove_characters_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_remove_characters" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # </summary>
    # <param name="request">Request. <see cref="PostConvertTextRequest" /></param>
    def post_convert_text(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_convert_text_with_http_info(request,**kwargs)
        else:
            (data) = self.post_convert_text_with_http_info(request,**kwargs)
            return data

    def post_convert_text_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_convert_text" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # </summary>
    # <param name="request">Request. <see cref="PostRemoveDuplicatesRequest" /></param>
    def post_remove_duplicates(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_remove_duplicates_with_http_info(request,**kwargs)
        else:
            (data) = self.post_remove_duplicates_with_http_info(request,**kwargs)
            return data

    def post_remove_duplicates_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_remove_duplicates" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # </summary>
    # <param name="request">Request. <see cref="PostExtractTextRequest" /></param>
    def post_extract_text(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_extract_text_with_http_info(request,**kwargs)
        else:
            (data) = self.post_extract_text_with_http_info(request,**kwargs)
            return data

    def post_extract_text_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_extract_text" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # </summary>
    # <param name="request">Request. <see cref="PostSplitTextRequest" /></param>
    def post_split_text(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_split_text_with_http_info(request,**kwargs)
        else:
            (data) = self.post_split_text_with_http_info(request,**kwargs)
            return data

    def post_split_text_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_split_text" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Retrieve the description of the default style for the workbook .
    # </summary>
    # <param name="request">Request. <see cref="GetWorkbookDefaultStyleRequest" /></param>
    def get_workbook_default_style(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_workbook_default_style_with_http_info(request,**kwargs)
        else:
            (data) = self.get_workbook_default_style_with_http_info(request,**kwargs)
            return data

    def get_workbook_default_style_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workbook_default_style" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Retrieve text items in the workbook.
    # </summary>
    # <param name="request">Request. <see cref="GetWorkbookTextItemsRequest" /></param>
    def get_workbook_text_items(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_workbook_text_items_with_http_info(request,**kwargs)
        else:
            (data) = self.get_workbook_text_items_with_http_info(request,**kwargs)
            return data

    def get_workbook_text_items_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workbook_text_items" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Retrieve named ranges in the workbook.
    # </summary>
    # <param name="request">Request. <see cref="GetWorkbookNamesRequest" /></param>
    def get_workbook_names(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_workbook_names_with_http_info(request,**kwargs)
        else:
            (data) = self.get_workbook_names_with_http_info(request,**kwargs)
            return data

    def get_workbook_names_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workbook_names" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Define a new name in the workbook.
    # </summary>
    # <param name="request">Request. <see cref="PutWorkbookNameRequest" /></param>
    def put_workbook_name(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.put_workbook_name_with_http_info(request,**kwargs)
        else:
            (data) = self.put_workbook_name_with_http_info(request,**kwargs)
            return data

    def put_workbook_name_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_workbook_name" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Retrieve description of a named range in the workbook.
    # </summary>
    # <param name="request">Request. <see cref="GetWorkbookNameRequest" /></param>
    def get_workbook_name(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_workbook_name_with_http_info(request,**kwargs)
        else:
            (data) = self.get_workbook_name_with_http_info(request,**kwargs)
            return data

    def get_workbook_name_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workbook_name" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Update a named range in the workbook.
    # </summary>
    # <param name="request">Request. <see cref="PostWorkbookNameRequest" /></param>
    def post_workbook_name(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_workbook_name_with_http_info(request,**kwargs)
        else:
            (data) = self.post_workbook_name_with_http_info(request,**kwargs)
            return data

    def post_workbook_name_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workbook_name" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Retrieve the value of a named range in the workbook.
    # </summary>
    # <param name="request">Request. <see cref="GetWorkbookNameValueRequest" /></param>
    def get_workbook_name_value(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_workbook_name_value_with_http_info(request,**kwargs)
        else:
            (data) = self.get_workbook_name_value_with_http_info(request,**kwargs)
            return data

    def get_workbook_name_value_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workbook_name_value" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Delete all named ranges in the workbook.
    # </summary>
    # <param name="request">Request. <see cref="DeleteWorkbookNamesRequest" /></param>
    def delete_workbook_names(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.delete_workbook_names_with_http_info(request,**kwargs)
        else:
            (data) = self.delete_workbook_names_with_http_info(request,**kwargs)
            return data

    def delete_workbook_names_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_workbook_names" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Delete a named range in the workbook.
    # </summary>
    # <param name="request">Request. <see cref="DeleteWorkbookNameRequest" /></param>
    def delete_workbook_name(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.delete_workbook_name_with_http_info(request,**kwargs)
        else:
            (data) = self.delete_workbook_name_with_http_info(request,**kwargs)
            return data

    def delete_workbook_name_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_workbook_name" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Merge a workbook into the existing workbook.
    # </summary>
    # <param name="request">Request. <see cref="PostWorkbooksMergeRequest" /></param>
    def post_workbooks_merge(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_workbooks_merge_with_http_info(request,**kwargs)
        else:
            (data) = self.post_workbooks_merge_with_http_info(request,**kwargs)
            return data

    def post_workbooks_merge_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workbooks_merge" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Search for text in the workbook.
    # </summary>
    # <param name="request">Request. <see cref="PostWorkbooksTextSearchRequest" /></param>
    def post_workbooks_text_search(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_workbooks_text_search_with_http_info(request,**kwargs)
        else:
            (data) = self.post_workbooks_text_search_with_http_info(request,**kwargs)
            return data

    def post_workbooks_text_search_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workbooks_text_search" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Replace text in the workbook.
    # </summary>
    # <param name="request">Request. <see cref="PostWorkbookTextReplaceRequest" /></param>
    def post_workbook_text_replace(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_workbook_text_replace_with_http_info(request,**kwargs)
        else:
            (data) = self.post_workbook_text_replace_with_http_info(request,**kwargs)
            return data

    def post_workbook_text_replace_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workbook_text_replace" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Smart marker processing.
    # </summary>
    # <param name="request">Request. <see cref="PostWorkbookGetSmartMarkerResultRequest" /></param>
    def post_workbook_get_smart_marker_result(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        response_file = None
        if kwargs.get('callback'):
            response_file = self.post_workbook_get_smart_marker_result_with_http_info(request,**kwargs)
        else:
            (data) = self.post_workbook_get_smart_marker_result_with_http_info(request,**kwargs)
            response_file = data
        if kwargs.get('local_outpath'):
            shutil.move( response_file , kwargs.get('local_outpath'))
            return kwargs.get('local_outpath')
        else:
            return response_file
    def post_workbook_get_smart_marker_result_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('local_outpath')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workbook_get_smart_marker_result" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Create a new workbook using different methods.
    # </summary>
    # <param name="request">Request. <see cref="PutWorkbookCreateRequest" /></param>
    def put_workbook_create(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.put_workbook_create_with_http_info(request,**kwargs)
        else:
            (data) = self.put_workbook_create_with_http_info(request,**kwargs)
            return data

    def put_workbook_create_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_workbook_create" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Split the workbook with a specific format.
    # </summary>
    # <param name="request">Request. <see cref="PostWorkbookSplitRequest" /></param>
    def post_workbook_split(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_workbook_split_with_http_info(request,**kwargs)
        else:
            (data) = self.post_workbook_split_with_http_info(request,**kwargs)
            return data

    def post_workbook_split_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workbook_split" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Calculate all formulas in the workbook.
    # </summary>
    # <param name="request">Request. <see cref="PostWorkbookCalculateFormulaRequest" /></param>
    def post_workbook_calculate_formula(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_workbook_calculate_formula_with_http_info(request,**kwargs)
        else:
            (data) = self.post_workbook_calculate_formula_with_http_info(request,**kwargs)
            return data

    def post_workbook_calculate_formula_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workbook_calculate_formula" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Autofit rows in the workbook.
    # </summary>
    # <param name="request">Request. <see cref="PostAutofitWorkbookRowsRequest" /></param>
    def post_autofit_workbook_rows(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_autofit_workbook_rows_with_http_info(request,**kwargs)
        else:
            (data) = self.post_autofit_workbook_rows_with_http_info(request,**kwargs)
            return data

    def post_autofit_workbook_rows_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_autofit_workbook_rows" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Autofit columns in the workbook.
    # </summary>
    # <param name="request">Request. <see cref="PostAutofitWorkbookColumnsRequest" /></param>
    def post_autofit_workbook_columns(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_autofit_workbook_columns_with_http_info(request,**kwargs)
        else:
            (data) = self.post_autofit_workbook_columns_with_http_info(request,**kwargs)
            return data

    def post_autofit_workbook_columns_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_autofit_workbook_columns" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Retrieve descriptions of workbook settings.
    # </summary>
    # <param name="request">Request. <see cref="GetWorkbookSettingsRequest" /></param>
    def get_workbook_settings(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_workbook_settings_with_http_info(request,**kwargs)
        else:
            (data) = self.get_workbook_settings_with_http_info(request,**kwargs)
            return data

    def get_workbook_settings_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workbook_settings" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Update setting in the workbook.
    # </summary>
    # <param name="request">Request. <see cref="PostWorkbookSettingsRequest" /></param>
    def post_workbook_settings(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_workbook_settings_with_http_info(request,**kwargs)
        else:
            (data) = self.post_workbook_settings_with_http_info(request,**kwargs)
            return data

    def post_workbook_settings_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workbook_settings" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Set background in the workbook.
    # </summary>
    # <param name="request">Request. <see cref="PutWorkbookBackgroundRequest" /></param>
    def put_workbook_background(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.put_workbook_background_with_http_info(request,**kwargs)
        else:
            (data) = self.put_workbook_background_with_http_info(request,**kwargs)
            return data

    def put_workbook_background_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_workbook_background" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Delete background in the workbook.
    # </summary>
    # <param name="request">Request. <see cref="DeleteWorkbookBackgroundRequest" /></param>
    def delete_workbook_background(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.delete_workbook_background_with_http_info(request,**kwargs)
        else:
            (data) = self.delete_workbook_background_with_http_info(request,**kwargs)
            return data

    def delete_workbook_background_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_workbook_background" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Set water marker in the workbook.
    # </summary>
    # <param name="request">Request. <see cref="PutWorkbookWaterMarkerRequest" /></param>
    def put_workbook_water_marker(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.put_workbook_water_marker_with_http_info(request,**kwargs)
        else:
            (data) = self.put_workbook_water_marker_with_http_info(request,**kwargs)
            return data

    def put_workbook_water_marker_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_workbook_water_marker" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Get page count in the workbook.
    # </summary>
    # <param name="request">Request. <see cref="GetPageCountRequest" /></param>
    def get_page_count(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_page_count_with_http_info(request,**kwargs)
        else:
            (data) = self.get_page_count_with_http_info(request,**kwargs)
            return data

    def get_page_count_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_page_count" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Get all style in the workbook.
    # </summary>
    # <param name="request">Request. <see cref="GetAllStylesRequest" /></param>
    def get_all_styles(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_all_styles_with_http_info(request,**kwargs)
        else:
            (data) = self.get_all_styles_with_http_info(request,**kwargs)
            return data

    def get_all_styles_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_styles" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Retrieve the description of worksheets from a workbook.
    # </summary>
    # <param name="request">Request. <see cref="GetWorksheetsRequest" /></param>
    def get_worksheets(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_worksheets_with_http_info(request,**kwargs)
        else:
            (data) = self.get_worksheets_with_http_info(request,**kwargs)
            return data

    def get_worksheets_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_worksheets" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Retrieve the worksheet in a specified format from the workbook.
    # </summary>
    # <param name="request">Request. <see cref="GetWorksheetWithFormatRequest" /></param>
    def get_worksheet_with_format(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        response_file = None
        if kwargs.get('callback'):
            response_file = self.get_worksheet_with_format_with_http_info(request,**kwargs)
        else:
            (data) = self.get_worksheet_with_format_with_http_info(request,**kwargs)
            response_file = data
        if kwargs.get('local_outpath'):
            shutil.move( response_file , kwargs.get('local_outpath'))
            return kwargs.get('local_outpath')
        else:
            return response_file
    def get_worksheet_with_format_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('local_outpath')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_worksheet_with_format" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Change worksheet visibility in the workbook.
    # </summary>
    # <param name="request">Request. <see cref="PutChangeVisibilityWorksheetRequest" /></param>
    def put_change_visibility_worksheet(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.put_change_visibility_worksheet_with_http_info(request,**kwargs)
        else:
            (data) = self.put_change_visibility_worksheet_with_http_info(request,**kwargs)
            return data

    def put_change_visibility_worksheet_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_change_visibility_worksheet" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Set active worksheet index in the workbook.
    # </summary>
    # <param name="request">Request. <see cref="PutActiveWorksheetRequest" /></param>
    def put_active_worksheet(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.put_active_worksheet_with_http_info(request,**kwargs)
        else:
            (data) = self.put_active_worksheet_with_http_info(request,**kwargs)
            return data

    def put_active_worksheet_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_active_worksheet" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Insert a new worksheet in the workbook.
    # </summary>
    # <param name="request">Request. <see cref="PutInsertNewWorksheetRequest" /></param>
    def put_insert_new_worksheet(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.put_insert_new_worksheet_with_http_info(request,**kwargs)
        else:
            (data) = self.put_insert_new_worksheet_with_http_info(request,**kwargs)
            return data

    def put_insert_new_worksheet_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_insert_new_worksheet" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Add a new worksheet in the workbook.
    # </summary>
    # <param name="request">Request. <see cref="PutAddNewWorksheetRequest" /></param>
    def put_add_new_worksheet(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.put_add_new_worksheet_with_http_info(request,**kwargs)
        else:
            (data) = self.put_add_new_worksheet_with_http_info(request,**kwargs)
            return data

    def put_add_new_worksheet_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_add_new_worksheet" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Delete a worksheet in the workbook.
    # </summary>
    # <param name="request">Request. <see cref="DeleteWorksheetRequest" /></param>
    def delete_worksheet(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.delete_worksheet_with_http_info(request,**kwargs)
        else:
            (data) = self.delete_worksheet_with_http_info(request,**kwargs)
            return data

    def delete_worksheet_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_worksheet" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Delete matched worksheets in the workbook.
    # </summary>
    # <param name="request">Request. <see cref="DeleteWorksheetsRequest" /></param>
    def delete_worksheets(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.delete_worksheets_with_http_info(request,**kwargs)
        else:
            (data) = self.delete_worksheets_with_http_info(request,**kwargs)
            return data

    def delete_worksheets_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_worksheets" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Move worksheet in the workbook.
    # </summary>
    # <param name="request">Request. <see cref="PostMoveWorksheetRequest" /></param>
    def post_move_worksheet(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_move_worksheet_with_http_info(request,**kwargs)
        else:
            (data) = self.post_move_worksheet_with_http_info(request,**kwargs)
            return data

    def post_move_worksheet_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_move_worksheet" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Protect worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PutProtectWorksheetRequest" /></param>
    def put_protect_worksheet(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.put_protect_worksheet_with_http_info(request,**kwargs)
        else:
            (data) = self.put_protect_worksheet_with_http_info(request,**kwargs)
            return data

    def put_protect_worksheet_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_protect_worksheet" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Unprotect worksheet.
    # </summary>
    # <param name="request">Request. <see cref="DeleteUnprotectWorksheetRequest" /></param>
    def delete_unprotect_worksheet(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.delete_unprotect_worksheet_with_http_info(request,**kwargs)
        else:
            (data) = self.delete_unprotect_worksheet_with_http_info(request,**kwargs)
            return data

    def delete_unprotect_worksheet_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_unprotect_worksheet" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Retrieve text items in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="GetWorksheetTextItemsRequest" /></param>
    def get_worksheet_text_items(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_worksheet_text_items_with_http_info(request,**kwargs)
        else:
            (data) = self.get_worksheet_text_items_with_http_info(request,**kwargs)
            return data

    def get_worksheet_text_items_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_worksheet_text_items" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Retrieve the description of comments in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="GetWorksheetCommentsRequest" /></param>
    def get_worksheet_comments(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_worksheet_comments_with_http_info(request,**kwargs)
        else:
            (data) = self.get_worksheet_comments_with_http_info(request,**kwargs)
            return data

    def get_worksheet_comments_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_worksheet_comments" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Retrieve the description of comment in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="GetWorksheetCommentRequest" /></param>
    def get_worksheet_comment(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_worksheet_comment_with_http_info(request,**kwargs)
        else:
            (data) = self.get_worksheet_comment_with_http_info(request,**kwargs)
            return data

    def get_worksheet_comment_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_worksheet_comment" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Add cell comment in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PutWorksheetCommentRequest" /></param>
    def put_worksheet_comment(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.put_worksheet_comment_with_http_info(request,**kwargs)
        else:
            (data) = self.put_worksheet_comment_with_http_info(request,**kwargs)
            return data

    def put_worksheet_comment_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_worksheet_comment" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Update cell comment in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PostWorksheetCommentRequest" /></param>
    def post_worksheet_comment(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_worksheet_comment_with_http_info(request,**kwargs)
        else:
            (data) = self.post_worksheet_comment_with_http_info(request,**kwargs)
            return data

    def post_worksheet_comment_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_worksheet_comment" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Delete cell comment in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="DeleteWorksheetCommentRequest" /></param>
    def delete_worksheet_comment(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.delete_worksheet_comment_with_http_info(request,**kwargs)
        else:
            (data) = self.delete_worksheet_comment_with_http_info(request,**kwargs)
            return data

    def delete_worksheet_comment_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_worksheet_comment" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Delete all comments in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="DeleteWorksheetCommentsRequest" /></param>
    def delete_worksheet_comments(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.delete_worksheet_comments_with_http_info(request,**kwargs)
        else:
            (data) = self.delete_worksheet_comments_with_http_info(request,**kwargs)
            return data

    def delete_worksheet_comments_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_worksheet_comments" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Get worksheet merged cells.
    # </summary>
    # <param name="request">Request. <see cref="GetWorksheetMergedCellsRequest" /></param>
    def get_worksheet_merged_cells(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_worksheet_merged_cells_with_http_info(request,**kwargs)
        else:
            (data) = self.get_worksheet_merged_cells_with_http_info(request,**kwargs)
            return data

    def get_worksheet_merged_cells_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_worksheet_merged_cells" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Retrieve description of a merged cell by its index in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="GetWorksheetMergedCellRequest" /></param>
    def get_worksheet_merged_cell(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_worksheet_merged_cell_with_http_info(request,**kwargs)
        else:
            (data) = self.get_worksheet_merged_cell_with_http_info(request,**kwargs)
            return data

    def get_worksheet_merged_cell_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_worksheet_merged_cell" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Calculate formula in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="GetWorksheetCalculateFormulaRequest" /></param>
    def get_worksheet_calculate_formula(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_worksheet_calculate_formula_with_http_info(request,**kwargs)
        else:
            (data) = self.get_worksheet_calculate_formula_with_http_info(request,**kwargs)
            return data

    def get_worksheet_calculate_formula_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_worksheet_calculate_formula" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Calculate formula in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PostWorksheetCalculateFormulaRequest" /></param>
    def post_worksheet_calculate_formula(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_worksheet_calculate_formula_with_http_info(request,**kwargs)
        else:
            (data) = self.post_worksheet_calculate_formula_with_http_info(request,**kwargs)
            return data

    def post_worksheet_calculate_formula_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_worksheet_calculate_formula" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Search for text in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PostWorksheetTextSearchRequest" /></param>
    def post_worksheet_text_search(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_worksheet_text_search_with_http_info(request,**kwargs)
        else:
            (data) = self.post_worksheet_text_search_with_http_info(request,**kwargs)
            return data

    def post_worksheet_text_search_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_worksheet_text_search" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Replace old text with new text in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PostWorksheetTextReplaceRequest" /></param>
    def post_worksheet_text_replace(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_worksheet_text_replace_with_http_info(request,**kwargs)
        else:
            (data) = self.post_worksheet_text_replace_with_http_info(request,**kwargs)
            return data

    def post_worksheet_text_replace_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_worksheet_text_replace" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Sort a range in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PostWorksheetRangeSortRequest" /></param>
    def post_worksheet_range_sort(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_worksheet_range_sort_with_http_info(request,**kwargs)
        else:
            (data) = self.post_worksheet_range_sort_with_http_info(request,**kwargs)
            return data

    def post_worksheet_range_sort_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_worksheet_range_sort" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Autofit a row in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PostAutofitWorksheetRowRequest" /></param>
    def post_autofit_worksheet_row(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_autofit_worksheet_row_with_http_info(request,**kwargs)
        else:
            (data) = self.post_autofit_worksheet_row_with_http_info(request,**kwargs)
            return data

    def post_autofit_worksheet_row_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_autofit_worksheet_row" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Autofit rows in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PostAutofitWorksheetRowsRequest" /></param>
    def post_autofit_worksheet_rows(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_autofit_worksheet_rows_with_http_info(request,**kwargs)
        else:
            (data) = self.post_autofit_worksheet_rows_with_http_info(request,**kwargs)
            return data

    def post_autofit_worksheet_rows_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_autofit_worksheet_rows" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Autofit columns in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PostAutofitWorksheetColumnsRequest" /></param>
    def post_autofit_worksheet_columns(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_autofit_worksheet_columns_with_http_info(request,**kwargs)
        else:
            (data) = self.post_autofit_worksheet_columns_with_http_info(request,**kwargs)
            return data

    def post_autofit_worksheet_columns_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_autofit_worksheet_columns" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Set background image in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PutWorksheetBackgroundRequest" /></param>
    def put_worksheet_background(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.put_worksheet_background_with_http_info(request,**kwargs)
        else:
            (data) = self.put_worksheet_background_with_http_info(request,**kwargs)
            return data

    def put_worksheet_background_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_worksheet_background" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Delete background image in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="DeleteWorksheetBackgroundRequest" /></param>
    def delete_worksheet_background(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.delete_worksheet_background_with_http_info(request,**kwargs)
        else:
            (data) = self.delete_worksheet_background_with_http_info(request,**kwargs)
            return data

    def delete_worksheet_background_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_worksheet_background" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Set freeze panes in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PutWorksheetFreezePanesRequest" /></param>
    def put_worksheet_freeze_panes(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.put_worksheet_freeze_panes_with_http_info(request,**kwargs)
        else:
            (data) = self.put_worksheet_freeze_panes_with_http_info(request,**kwargs)
            return data

    def put_worksheet_freeze_panes_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_worksheet_freeze_panes" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Unfreeze panes in worksheet.
    # </summary>
    # <param name="request">Request. <see cref="DeleteWorksheetFreezePanesRequest" /></param>
    def delete_worksheet_freeze_panes(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.delete_worksheet_freeze_panes_with_http_info(request,**kwargs)
        else:
            (data) = self.delete_worksheet_freeze_panes_with_http_info(request,**kwargs)
            return data

    def delete_worksheet_freeze_panes_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_worksheet_freeze_panes" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Copy contents and formats from another worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PostCopyWorksheetRequest" /></param>
    def post_copy_worksheet(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_copy_worksheet_with_http_info(request,**kwargs)
        else:
            (data) = self.post_copy_worksheet_with_http_info(request,**kwargs)
            return data

    def post_copy_worksheet_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_copy_worksheet" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Rename worksheet in the workbook.
    # </summary>
    # <param name="request">Request. <see cref="PostRenameWorksheetRequest" /></param>
    def post_rename_worksheet(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_rename_worksheet_with_http_info(request,**kwargs)
        else:
            (data) = self.post_rename_worksheet_with_http_info(request,**kwargs)
            return data

    def post_rename_worksheet_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_rename_worksheet" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Update worksheet properties in the workbook.
    # </summary>
    # <param name="request">Request. <see cref="PostUpdateWorksheetPropertyRequest" /></param>
    def post_update_worksheet_property(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_update_worksheet_property_with_http_info(request,**kwargs)
        else:
            (data) = self.post_update_worksheet_property_with_http_info(request,**kwargs)
            return data

    def post_update_worksheet_property_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_update_worksheet_property" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Retrieve descriptions of ranges in the worksheets.
    # </summary>
    # <param name="request">Request. <see cref="GetNamedRangesRequest" /></param>
    def get_named_ranges(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_named_ranges_with_http_info(request,**kwargs)
        else:
            (data) = self.get_named_ranges_with_http_info(request,**kwargs)
            return data

    def get_named_ranges_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_named_ranges" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Retrieve values in range.
    # </summary>
    # <param name="request">Request. <see cref="GetNamedRangeValueRequest" /></param>
    def get_named_range_value(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_named_range_value_with_http_info(request,**kwargs)
        else:
            (data) = self.get_named_range_value_with_http_info(request,**kwargs)
            return data

    def get_named_range_value_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_named_range_value" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Update the scaling percentage in the worksheet. It should be between 10 and 400.
    # </summary>
    # <param name="request">Request. <see cref="PostUpdateWorksheetZoomRequest" /></param>
    def post_update_worksheet_zoom(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_update_worksheet_zoom_with_http_info(request,**kwargs)
        else:
            (data) = self.post_update_worksheet_zoom_with_http_info(request,**kwargs)
            return data

    def post_update_worksheet_zoom_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_update_worksheet_zoom" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Get page count in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="GetWorksheetPageCountRequest" /></param>
    def get_worksheet_page_count(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_worksheet_page_count_with_http_info(request,**kwargs)
        else:
            (data) = self.get_worksheet_page_count_with_http_info(request,**kwargs)
            return data

    def get_worksheet_page_count_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_worksheet_page_count" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Retrieve descriptions of validations in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="GetWorksheetValidationsRequest" /></param>
    def get_worksheet_validations(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_worksheet_validations_with_http_info(request,**kwargs)
        else:
            (data) = self.get_worksheet_validations_with_http_info(request,**kwargs)
            return data

    def get_worksheet_validations_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_worksheet_validations" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Retrieve a validation by its index in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="GetWorksheetValidationRequest" /></param>
    def get_worksheet_validation(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.get_worksheet_validation_with_http_info(request,**kwargs)
        else:
            (data) = self.get_worksheet_validation_with_http_info(request,**kwargs)
            return data

    def get_worksheet_validation_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_worksheet_validation" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Add a validation at index in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PutWorksheetValidationRequest" /></param>
    def put_worksheet_validation(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.put_worksheet_validation_with_http_info(request,**kwargs)
        else:
            (data) = self.put_worksheet_validation_with_http_info(request,**kwargs)
            return data

    def put_worksheet_validation_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_worksheet_validation" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Update a validation by index in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="PostWorksheetValidationRequest" /></param>
    def post_worksheet_validation(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.post_worksheet_validation_with_http_info(request,**kwargs)
        else:
            (data) = self.post_worksheet_validation_with_http_info(request,**kwargs)
            return data

    def post_worksheet_validation_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_worksheet_validation" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Delete a validation by index in worksheet.
    # </summary>
    # <param name="request">Request. <see cref="DeleteWorksheetValidationRequest" /></param>
    def delete_worksheet_validation(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.delete_worksheet_validation_with_http_info(request,**kwargs)
        else:
            (data) = self.delete_worksheet_validation_with_http_info(request,**kwargs)
            return data

    def delete_worksheet_validation_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_worksheet_validation" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    # <summary>
    # Delete all validations in the worksheet.
    # </summary>
    # <param name="request">Request. <see cref="DeleteWorksheetValidationsRequest" /></param>
    def delete_worksheet_validations(self, request, **kwargs):

        kwargs['_return_http_data_only'] = True
        self.check_access_token()
        if kwargs.get('callback'):
            return self.delete_worksheet_validations_with_http_info(request,**kwargs)
        else:
            (data) = self.delete_worksheet_validations_with_http_info(request,**kwargs)
            return data

    def delete_worksheet_validations_with_http_info(self, request, **kwargs):
        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_worksheet_validations" % key
                )
            params[key] = val
        del params['kwargs'] 

        http_params = request.create_http_request(self.api_client)
        return self.api_client.call_api(http_params['path'], http_params['method'],
                                        None,
                                        http_params['query_params'],
                                        http_params['header_params'],
                                        body=http_params['body'],
                                        post_params=http_params['form_params'],
                                        files=http_params['files'],
                                        response_type=http_params['response_type'],
                                        auth_settings=http_params['auth_settings'],
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=http_params['collection_formats'])



    