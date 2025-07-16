# coding: utf-8
"""
<copyright company="Aspose" file="GetWorksheetWithFormatRequest.cs">
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

class GetWorksheetWithFormatRequest(object):

    def __init__(self , name ,sheet_name ,format =None ,vertical_resolution =None ,horizontal_resolution =None ,area =None ,page_index =None ,one_page_per_sheet =None ,print_headings =None ,folder =None ,storage_name =None ):
        self.name = name 
        self.sheet_name = sheet_name 
        self.format = format 
        self.vertical_resolution = vertical_resolution 
        self.horizontal_resolution = horizontal_resolution 
        self.area = area 
        self.page_index = page_index 
        self.one_page_per_sheet = one_page_per_sheet 
        self.print_headings = print_headings 
        self.folder = folder 
        self.storage_name = storage_name 
    def create_http_request(self, api_client):

        # verify the required parameter 'name' is set
        if self.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_worksheet_with_format`")


        # verify the required parameter 'sheet_name' is set
        if self.sheet_name is None:
            raise ValueError("Missing the required parameter `sheet_name` when calling `get_worksheet_with_format`")


        collection_formats = {}

        path_params = {}
        if self.name is not None:
            path_params['name'] = self.name
        if self.sheet_name is not None:
            path_params['sheetName'] = self.sheet_name
        query_params = []
        if self.format is not None:
            query_params.append(('format',self.format ))
        if self.vertical_resolution is not None:
            query_params.append(('verticalResolution',self.vertical_resolution ))
        if self.horizontal_resolution is not None:
            query_params.append(('horizontalResolution',self.horizontal_resolution ))
        if self.area is not None:
            query_params.append(('area',self.area ))
        if self.page_index is not None:
            query_params.append(('pageIndex',self.page_index ))
        if self.one_page_per_sheet is not None:
            query_params.append(('onePagePerSheet',self.one_page_per_sheet ))
        if self.print_headings is not None:
            query_params.append(('printHeadings',self.print_headings ))
        if self.folder is not None:
            query_params.append(('folder',self.folder ))
        if self.storage_name is not None:
            query_params.append(('storageName',self.storage_name ))

        header_params = {}
        header_params['x-aspose-client'] = 'python sdk';
        header_params['x-aspose-client-version'] = '25.7';

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
        resource_path =  "v3.0/cells/{name}/worksheets/{sheetName}"
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

