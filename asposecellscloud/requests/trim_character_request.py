# coding: utf-8
"""
<copyright company="Aspose" file="TrimCharacterRequest.cs">
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

class TrimCharacterRequest(object):

    def __init__(self , spreadsheet ,trim_content =None ,trim_leading =None ,trim_trailing =None ,trim_space_between_word_to1 =None ,trim_non_breaking_spaces =None ,remove_extra_line_breaks =None ,remove_all_line_breaks =None ,worksheet =None ,range =None ,out_path =None ,out_storage_name =None ,region =None ,password =None ):
        self.spreadsheet = spreadsheet 
        self.trim_content = trim_content 
        self.trim_leading = trim_leading 
        self.trim_trailing = trim_trailing 
        self.trim_space_between_word_to1 = trim_space_between_word_to1 
        self.trim_non_breaking_spaces = trim_non_breaking_spaces 
        self.remove_extra_line_breaks = remove_extra_line_breaks 
        self.remove_all_line_breaks = remove_all_line_breaks 
        self.worksheet = worksheet 
        self.range = range 
        self.out_path = out_path 
        self.out_storage_name = out_storage_name 
        self.region = region 
        self.password = password 
    def create_http_request(self, api_client):

        # verify the required parameter 'spreadsheet' is set
        if self.spreadsheet is None:
            raise ValueError("Missing the required parameter `spreadsheet` when calling `trim_character`")


        collection_formats = {}

        path_params = {}
        query_params = []
        if self.trim_content is not None:
            query_params.append(('trimContent',self.trim_content ))
        if self.trim_leading is not None:
            query_params.append(('trimLeading',self.trim_leading ))
        if self.trim_trailing is not None:
            query_params.append(('trimTrailing',self.trim_trailing ))
        if self.trim_space_between_word_to1 is not None:
            query_params.append(('trimSpaceBetweenWordTo1',self.trim_space_between_word_to1 ))
        if self.trim_non_breaking_spaces is not None:
            query_params.append(('trimNonBreakingSpaces',self.trim_non_breaking_spaces ))
        if self.remove_extra_line_breaks is not None:
            query_params.append(('removeExtraLineBreaks',self.remove_extra_line_breaks ))
        if self.remove_all_line_breaks is not None:
            query_params.append(('removeAllLineBreaks',self.remove_all_line_breaks ))
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

        header_params = {}
        header_params['x-aspose-client'] = 'python sdk';
        header_params['x-aspose-client-version'] = '25.10';

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
        resource_path =  "v4.0/cells/content/trim"
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

