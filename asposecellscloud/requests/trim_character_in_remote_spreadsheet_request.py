# coding: utf-8
"""
<copyright company="Aspose" file="TrimCharacterInRemoteSpreadsheetRequest.cs">
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

class TrimCharacterInRemoteSpreadsheetRequest(object):

    def __init__(self , name ,worksheet ,range ,trim_content =None ,trim_leading =None ,trim_trailing =None ,trim_space_between_word_to1 =None ,trim_non_breaking_spaces =None ,remove_extra_line_breaks =None ,remove_all_line_breaks =None ,folder =None ,storage_name =None ,region =None ,password =None ):
        self.name = name 
        self.worksheet = worksheet 
        self.range = range 
        self.trim_content = trim_content 
        self.trim_leading = trim_leading 
        self.trim_trailing = trim_trailing 
        self.trim_space_between_word_to1 = trim_space_between_word_to1 
        self.trim_non_breaking_spaces = trim_non_breaking_spaces 
        self.remove_extra_line_breaks = remove_extra_line_breaks 
        self.remove_all_line_breaks = remove_all_line_breaks 
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
            raise ValueError("Missing the required parameter `name` when calling `trim_character_in_remote_spreadsheet`")


        # verify the required parameter 'worksheet' is set
        if self.worksheet is None:
            raise ValueError("Missing the required parameter `worksheet` when calling `trim_character_in_remote_spreadsheet`")


        # verify the required parameter 'range' is set
        if self.range is None:
            raise ValueError("Missing the required parameter `range` when calling `trim_character_in_remote_spreadsheet`")


        collection_formats = {}

        path_params = {}
        if self.name is not None:
            path_params['name'] = self.name
        if self.worksheet is not None:
            path_params['worksheet'] = self.worksheet
        if self.range is not None:
            path_params['range'] = self.range
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
        header_params['x-aspose-client-version'] = '26.8';

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
        resource_path =  "v4.0/cells/{name}/worksheets/{worksheet}/range/{range}/content/trim"
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

