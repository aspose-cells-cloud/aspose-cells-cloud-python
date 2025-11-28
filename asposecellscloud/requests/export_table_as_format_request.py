# coding: utf-8
"""
<copyright company="Aspose" file="ExportTableAsFormatRequest.cs">
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

import json
import os

from six import iteritems
from asposecellscloud import *
from asposecellscloud.models import *
from asposecellscloud.requests import *
from six.moves.urllib.parse import quote

class ExportTableAsFormatRequest(object):

    def __init__(self , name ,worksheet ,table_name ,format ,folder =None ,storage_name =None ,out_path =None ,out_storage_name =None ,fonts_location =None ,region =None ,password =None ):
        self.name = name 
        self.worksheet = worksheet 
        self.table_name = table_name 
        self.format = format 
        self.folder = folder 
        self.storage_name = storage_name 
        self.out_path = out_path 
        self.out_storage_name = out_storage_name 
        self.fonts_location = fonts_location 
        self.region = region 
        self.password = password         
        self.expand_query_parameters = {}

    def set_expand_query_parameter(self, query_name, query_value):
        self.expand_query_parameters.append(query_name,query_value)
        pass
    def create_http_request(self, api_client):

        # verify the required parameter 'name' is set
        if self.name is None:
            raise ValueError("Missing the required parameter `name` when calling `export_table_as_format`")


        # verify the required parameter 'worksheet' is set
        if self.worksheet is None:
            raise ValueError("Missing the required parameter `worksheet` when calling `export_table_as_format`")


        # verify the required parameter 'table_name' is set
        if self.table_name is None:
            raise ValueError("Missing the required parameter `table_name` when calling `export_table_as_format`")


        # verify the required parameter 'format' is set
        if self.format is None:
            raise ValueError("Missing the required parameter `format` when calling `export_table_as_format`")


        collection_formats = {}

        path_params = {}
        if self.name is not None:
            path_params['name'] = self.name
        if self.worksheet is not None:
            path_params['worksheet'] = self.worksheet
        if self.table_name is not None:
            path_params['tableName'] = self.table_name
        query_params = []
        if self.format is not None:
            query_params.append(('format',self.format ))
        if self.folder is not None:
            query_params.append(('folder',self.folder ))
        if self.storage_name is not None:
            query_params.append(('storageName',self.storage_name ))
        if self.out_path is not None:
            query_params.append(('outPath',self.out_path ))
        if self.out_storage_name is not None:
            query_params.append(('outStorageName',self.out_storage_name ))
        if self.fonts_location is not None:
            query_params.append(('fontsLocation',self.fonts_location ))
        if self.region is not None:
            query_params.append(('region',self.region ))
        if self.password is not None:
            query_params.append(('password',self.password ))
        if self.expand_query_parameters is not None:
            for key, value in self.expand_query_parameters.items():
                query_params.append(key,value)

        header_params = {}
        header_params['x-aspose-client'] = 'python sdk';
        header_params['x-aspose-client-version'] = '25.11';

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
        resource_path =  "v4.0/cells/{name}/worksheets/{worksheet}/tables/{tableName}"
        # path parameters
        if path_params:
            path_params = api_client.sanitize_for_serialization(path_params)
            path_params = api_client.parameters_to_tuples(path_params, collection_formats)
            for k, v in path_params:
                # specified safe chars, encode everything
                resource_path = resource_path.replace('{%s}' % k, quote(str(v), safe='/'))
        return {
                "method": "GET",
                "path":resource_path,
                "query_params": query_params,
                "header_params": header_params,
                "form_params": form_params,
                "files":local_var_files,
                "auth_settings":auth_settings,
                "body": body_params,
                "collection_formats": collection_formats,
                "response_type": 'file'  
        }

