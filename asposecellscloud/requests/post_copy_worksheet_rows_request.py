# coding: utf-8
"""
<copyright company="Aspose" file="PostCopyWorksheetRowsRequest.cs">
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

class PostCopyWorksheetRowsRequest(object):

    def __init__(self , name ,sheet_name ,source_row_index ,destination_row_index ,row_number ,worksheet =None ,folder =None ,storage_name =None ):
        self.name = name 
        self.sheet_name = sheet_name 
        self.source_row_index = source_row_index 
        self.destination_row_index = destination_row_index 
        self.row_number = row_number 
        self.worksheet = worksheet 
        self.folder = folder 
        self.storage_name = storage_name         
        self.expand_query_parameters = {}

    def set_expand_query_parameter(self, query_name, query_value):
        self.expand_query_parameters.append(query_name,query_value)
        pass
    def create_http_request(self, api_client):

        # verify the required parameter 'name' is set
        if self.name is None:
            raise ValueError("Missing the required parameter `name` when calling `post_copy_worksheet_rows`")


        # verify the required parameter 'sheet_name' is set
        if self.sheet_name is None:
            raise ValueError("Missing the required parameter `sheet_name` when calling `post_copy_worksheet_rows`")


        # verify the required parameter 'source_row_index' is set
        if self.source_row_index is None:
            raise ValueError("Missing the required parameter `source_row_index` when calling `post_copy_worksheet_rows`")


        # verify the required parameter 'destination_row_index' is set
        if self.destination_row_index is None:
            raise ValueError("Missing the required parameter `destination_row_index` when calling `post_copy_worksheet_rows`")


        # verify the required parameter 'row_number' is set
        if self.row_number is None:
            raise ValueError("Missing the required parameter `row_number` when calling `post_copy_worksheet_rows`")


        collection_formats = {}

        path_params = {}
        if self.name is not None:
            path_params['name'] = self.name
        if self.sheet_name is not None:
            path_params['sheetName'] = self.sheet_name
        query_params = []
        if self.source_row_index is not None:
            query_params.append(('sourceRowIndex',self.source_row_index ))
        if self.destination_row_index is not None:
            query_params.append(('destinationRowIndex',self.destination_row_index ))
        if self.row_number is not None:
            query_params.append(('rowNumber',self.row_number ))
        if self.worksheet is not None:
            query_params.append(('worksheet',self.worksheet ))
        if self.folder is not None:
            query_params.append(('folder',self.folder ))
        if self.storage_name is not None:
            query_params.append(('storageName',self.storage_name ))
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
        resource_path =  "v3.0/cells/{name}/worksheets/{sheetName}/cells/rows/copy"
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

