# coding: utf-8
"""
<copyright company="Aspose" file="SplitTextRequest.cs">
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

class SplitTextRequest(object):

    def __init__(self , spreadsheet ,delimiters ,keep_delimiters_in_resulting_cells =None ,keep_delimiters_position =None ,how_to_split =None ,out_position_range =None ,worksheet =None ,range =None ,out_path =None ,out_storage_name =None ,region =None ,password =None ):
        self.spreadsheet = spreadsheet 
        self.delimiters = delimiters 
        self.keep_delimiters_in_resulting_cells = keep_delimiters_in_resulting_cells 
        self.keep_delimiters_position = keep_delimiters_position 
        self.how_to_split = how_to_split 
        self.out_position_range = out_position_range 
        self.worksheet = worksheet 
        self.range = range 
        self.out_path = out_path 
        self.out_storage_name = out_storage_name 
        self.region = region 
        self.password = password         
        self.expand_query_parameters = {}

    def set_expand_query_parameter(self, query_name, query_value):
        self.expand_query_parameters.append(query_name,query_value)
        pass
    def create_http_request(self, api_client):

        # verify the required parameter 'spreadsheet' is set
        if self.spreadsheet is None:
            raise ValueError("Missing the required parameter `spreadsheet` when calling `split_text`")


        # verify the required parameter 'delimiters' is set
        if self.delimiters is None:
            raise ValueError("Missing the required parameter `delimiters` when calling `split_text`")


        collection_formats = {}

        path_params = {}
        query_params = []
        if self.delimiters is not None:
            query_params.append(('delimiters',self.delimiters ))
        if self.keep_delimiters_in_resulting_cells is not None:
            query_params.append(('keepDelimitersInResultingCells',self.keep_delimiters_in_resulting_cells ))
        if self.keep_delimiters_position is not None:
            query_params.append(('keepDelimitersPosition',self.keep_delimiters_position ))
        if self.how_to_split is not None:
            query_params.append(('HowToSplit',self.how_to_split ))
        if self.out_position_range is not None:
            query_params.append(('outPositionRange',self.out_position_range ))
        if self.worksheet is not None:
            query_params.append(('worksheet',self.worksheet ))
        if self.range is not None:
            query_params.append(('range',self.range ))
        if self.out_path is not None:
            query_params.append(('outPath',self.out_path ))
        if self.out_storage_name is not None:
            query_params.append(('outStorageName',self.out_storage_name ))
        if self.region is not None:
            query_params.append(('region',self.region ))
        if self.password is not None:
            query_params.append(('password',self.password ))
        if self.expand_query_parameters is not None:
            for key, value in self.expand_query_parameters.items():
                query_params.append(key,value)

        header_params = {}
        header_params['x-aspose-client'] = 'python sdk';
        header_params['x-aspose-client-version'] = '26.1';

        form_params = []
        local_var_files = {}
        if self.spreadsheet is not None:            
            if isinstance(self.spreadsheet,dict):
                for filename , filecontext in  self.spreadsheet.items():
                    local_var_files[filename] = filecontext
            else:
                if isinstance(self.spreadsheet,bytes):
                    local_var_files['File'] = self.spreadsheet
                else:
                    local_var_files[os.path.basename( self.spreadsheet)] = self.spreadsheet   

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = api_client.\
            select_header_content_type(['multipart/form-data'])

        # Authentication setting
        auth_settings = []
        resource_path =  "v4.0/cells/content/split/text"
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
                "response_type": 'file'  
        }

