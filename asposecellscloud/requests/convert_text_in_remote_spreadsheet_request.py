# coding: utf-8
"""
<copyright company="Aspose" file="ConvertTextInRemoteSpreadsheetRequest.cs">
  Copyright (c) 2026 Aspose.Cells Cloud
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

import json
import os

from six import iteritems
from asposecellscloud import *
from asposecellscloud.models import *
from asposecellscloud.requests import *
from six.moves.urllib.parse import quote

class ConvertTextInRemoteSpreadsheetRequest(object):

    def __init__(self , name ,worksheet ,range ,convert_text_type ,source_characters =None ,target_characters =None ,folder =None ,storage_name =None ,region =None ,password =None ):
        self.name = name 
        self.worksheet = worksheet 
        self.range = range 
        self.convert_text_type = convert_text_type 
        self.source_characters = source_characters 
        self.target_characters = target_characters 
        self.folder = folder 
        self.storage_name = storage_name 
        self.region = region 
        self.password = password         
        self.expand_query_parameters = {}

    def set_expand_query_parameter(self, query_name, query_value):
        self.expand_query_parameters.append(query_name,query_value)
        pass
    def create_http_request(self, api_client):

        # verify the required parameter 'name' is set
        if self.name is None:
            raise ValueError("Missing the required parameter `name` when calling `convert_text_in_remote_spreadsheet`")


        # verify the required parameter 'worksheet' is set
        if self.worksheet is None:
            raise ValueError("Missing the required parameter `worksheet` when calling `convert_text_in_remote_spreadsheet`")


        # verify the required parameter 'range' is set
        if self.range is None:
            raise ValueError("Missing the required parameter `range` when calling `convert_text_in_remote_spreadsheet`")


        # verify the required parameter 'convert_text_type' is set
        if self.convert_text_type is None:
            raise ValueError("Missing the required parameter `convert_text_type` when calling `convert_text_in_remote_spreadsheet`")


        collection_formats = {}

        path_params = {}
        if self.name is not None:
            path_params['name'] = self.name
        if self.worksheet is not None:
            path_params['worksheet'] = self.worksheet
        if self.range is not None:
            path_params['range'] = self.range
        query_params = []
        if self.convert_text_type is not None:
            query_params.append(('convertTextType',self.convert_text_type ))
        if self.source_characters is not None:
            query_params.append(('sourceCharacters',self.source_characters ))
        if self.target_characters is not None:
            query_params.append(('targetCharacters',self.target_characters ))
        if self.folder is not None:
            query_params.append(('folder',self.folder ))
        if self.storage_name is not None:
            query_params.append(('storageName',self.storage_name ))
        if self.region is not None:
            query_params.append(('region',self.region ))
        if self.password is not None:
            query_params.append(('password',self.password ))
        if self.expand_query_parameters is not None:
            for key, value in self.expand_query_parameters.items():
                query_params.append(key,value)

        header_params = {}
        header_params['x-aspose-client'] = 'python sdk';
        header_params['x-aspose-client-version'] = '26.6.4';

        form_params = []
        local_var_files = {}
        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = api_client.\
            select_header_content_type(['application/json'])


        # Authentication setting
        auth_settings = []
        resource_path =  "v4.0/cells/{name}/worksheets/{worksheet}/range/{range}/content/convert/text"
        # path parameters
        if path_params:
            path_params = api_client.sanitize_for_serialization(path_params)
            path_params = api_client.parameters_to_tuples(path_params, collection_formats)
            for k, v in path_params:
                # specified safe chars, encode everything
                resource_path = resource_path.replace('{%s}' % k, quote(str(v), safe='/'))
        return {
                "method": "PUT",
                "path":resource_path,
                "query_params": query_params,
                "header_params": header_params,
                "form_params": form_params,
                "files":local_var_files,
                "auth_settings":auth_settings,
                "body": body_params,
                "collection_formats": collection_formats,
                "response_type": 'CellsCloudResponse'  
        }

