# coding: utf-8
"""
<copyright company="Aspose" file="PostWorksheetCellsRangeMoveToRequest.cs">
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

class PostWorksheetCellsRangeMoveToRequest(object):

    def __init__(self , name ,sheet_name ,range ,dest_row ,dest_column ,folder =None ,storage_name =None ):
        self.name = name 
        self.sheet_name = sheet_name 
        self.range = range 
        self.dest_row = dest_row 
        self.dest_column = dest_column 
        self.folder = folder 
        self.storage_name = storage_name 
    def create_http_request(self, api_client):

        # verify the required parameter 'name' is set
        if self.name is None:
            raise ValueError("Missing the required parameter `name` when calling `post_worksheet_cells_range_move_to`")


        # verify the required parameter 'sheet_name' is set
        if self.sheet_name is None:
            raise ValueError("Missing the required parameter `sheet_name` when calling `post_worksheet_cells_range_move_to`")


        # verify the required parameter 'range' is set
        if self.range is None:
            raise ValueError("Missing the required parameter `range` when calling `post_worksheet_cells_range_move_to`")


        # verify the required parameter 'dest_row' is set
        if self.dest_row is None:
            raise ValueError("Missing the required parameter `dest_row` when calling `post_worksheet_cells_range_move_to`")


        # verify the required parameter 'dest_column' is set
        if self.dest_column is None:
            raise ValueError("Missing the required parameter `dest_column` when calling `post_worksheet_cells_range_move_to`")


        collection_formats = {}

        path_params = {}
        if self.name is not None:
            path_params['name'] = self.name
        if self.sheet_name is not None:
            path_params['sheetName'] = self.sheet_name
        query_params = []
        if self.dest_row is not None:
            query_params.append(('destRow',self.dest_row ))
        if self.dest_column is not None:
            query_params.append(('destColumn',self.dest_column ))
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

        if self.range is not None:
             body_params =self.range 

        # Authentication setting
        auth_settings = []
        resource_path =  "v3.0/cells/{name}/worksheets/{sheetName}/ranges/moveto"
        # path parameters
        if path_params:
            path_params = api_client.sanitize_for_serialization(path_params)
            path_params = api_client.parameters_to_tuples(path_params, collection_formats)
            for k, v in path_params:
                # specified safe chars, encode everything
                resource_path = resource_path.replace('{%s}' % k, quote(str(v), safe='/'))
        return {
                "method": "POST",
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

