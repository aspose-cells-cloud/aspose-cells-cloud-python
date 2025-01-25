# coding: utf-8
"""
<copyright company="Aspose" file="PostCopyCellIntoCellRequest.cs">
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

from six import iteritems
from asposecellscloud import *
from asposecellscloud.models import *
from asposecellscloud.requests import *
from six.moves.urllib.parse import quote

class PostCopyCellIntoCellRequest(object):

    def __init__(self , name ,dest_cell_name ,sheet_name ,worksheet =None ,cellname =None ,row =None ,column =None ,folder =None ,storage_name =None ):
        self.name = name 
        self.dest_cell_name = dest_cell_name 
        self.sheet_name = sheet_name 
        self.worksheet = worksheet 
        self.cellname = cellname 
        self.row = row 
        self.column = column 
        self.folder = folder 
        self.storage_name = storage_name 
    def create_http_request(self, api_client):

        # verify the required parameter 'name' is set
        if self.name is None:
            raise ValueError("Missing the required parameter `name` when calling `post_copy_cell_into_cell`")


        # verify the required parameter 'dest_cell_name' is set
        if self.dest_cell_name is None:
            raise ValueError("Missing the required parameter `dest_cell_name` when calling `post_copy_cell_into_cell`")


        # verify the required parameter 'sheet_name' is set
        if self.sheet_name is None:
            raise ValueError("Missing the required parameter `sheet_name` when calling `post_copy_cell_into_cell`")


        # verify the required parameter 'worksheet' is set
        if self.worksheet is None:
            raise ValueError("Missing the required parameter `worksheet` when calling `post_copy_cell_into_cell`")


        collection_formats = {}

        path_params = {}
        if self.name is not None:
            path_params['name'] = self.name
        if self.dest_cell_name is not None:
            path_params['destCellName'] = self.dest_cell_name
        if self.sheet_name is not None:
            path_params['sheetName'] = self.sheet_name
        query_params = []
        if self.worksheet is not None:
            query_params.append(('worksheet',self.worksheet ))
        if self.cellname is not None:
            query_params.append(('cellname',self.cellname ))
        if self.row is not None:
            query_params.append(('row',self.row ))
        if self.column is not None:
            query_params.append(('column',self.column ))
        if self.folder is not None:
            query_params.append(('folder',self.folder ))
        if self.storage_name is not None:
            query_params.append(('storageName',self.storage_name ))

        header_params = {}

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
        resource_path = "/cells/{name}/worksheets/{sheetName}/cells/{destCellName}/copy"
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

