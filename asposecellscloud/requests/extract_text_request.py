# coding: utf-8
"""
<copyright company="Aspose" file="ExtractTextRequest.cs">
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

class ExtractTextRequest(object):

    def __init__(self , spreadsheet ,extract_text_type ,out_position_range ,before_text =None ,after_text =None ,before_position =None ,after_position =None ,worksheet =None ,range =None ,out_path =None ,out_storage_name =None ,region =None ,password =None ):
        self.spreadsheet = spreadsheet 
        self.extract_text_type = extract_text_type 
        self.out_position_range = out_position_range 
        self.before_text = before_text 
        self.after_text = after_text 
        self.before_position = before_position 
        self.after_position = after_position 
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
            raise ValueError("Missing the required parameter `spreadsheet` when calling `extract_text`")


        # verify the required parameter 'extract_text_type' is set
        if self.extract_text_type is None:
            raise ValueError("Missing the required parameter `extract_text_type` when calling `extract_text`")


        # verify the required parameter 'out_position_range' is set
        if self.out_position_range is None:
            raise ValueError("Missing the required parameter `out_position_range` when calling `extract_text`")


        collection_formats = {}

        path_params = {}
        query_params = []
        if self.extract_text_type is not None:
            query_params.append(('extractTextType',self.extract_text_type ))
        if self.out_position_range is not None:
            query_params.append(('outPositionRange',self.out_position_range ))
        if self.before_text is not None:
            query_params.append(('beforeText',self.before_text ))
        if self.after_text is not None:
            query_params.append(('afterText',self.after_text ))
        if self.before_position is not None:
            query_params.append(('beforePosition',self.before_position ))
        if self.after_position is not None:
            query_params.append(('afterPosition',self.after_position ))
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
        header_params['x-aspose-client-version'] = '26.1.1';

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
        resource_path =  "v4.0/cells/content/extract/text"
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

