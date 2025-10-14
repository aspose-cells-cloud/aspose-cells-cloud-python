# coding: utf-8
"""
<copyright company="Aspose" file="PutWorksheetFormatConditionConditionRequest.cs">
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

class PutWorksheetFormatConditionConditionRequest(object):

    def __init__(self , name ,sheet_name ,index ,type ,operator_type ,formula1 ,formula2 ,folder =None ,storage_name =None ):
        self.name = name 
        self.sheet_name = sheet_name 
        self.index = index 
        self.type = type 
        self.operator_type = operator_type 
        self.formula1 = formula1 
        self.formula2 = formula2 
        self.folder = folder 
        self.storage_name = storage_name 
    def create_http_request(self, api_client):

        # verify the required parameter 'name' is set
        if self.name is None:
            raise ValueError("Missing the required parameter `name` when calling `put_worksheet_format_condition_condition`")


        # verify the required parameter 'sheet_name' is set
        if self.sheet_name is None:
            raise ValueError("Missing the required parameter `sheet_name` when calling `put_worksheet_format_condition_condition`")


        # verify the required parameter 'index' is set
        if self.index is None:
            raise ValueError("Missing the required parameter `index` when calling `put_worksheet_format_condition_condition`")


        # verify the required parameter 'type' is set
        if self.type is None:
            raise ValueError("Missing the required parameter `type` when calling `put_worksheet_format_condition_condition`")


        # verify the required parameter 'operator_type' is set
        if self.operator_type is None:
            raise ValueError("Missing the required parameter `operator_type` when calling `put_worksheet_format_condition_condition`")


        # verify the required parameter 'formula1' is set
        if self.formula1 is None:
            raise ValueError("Missing the required parameter `formula1` when calling `put_worksheet_format_condition_condition`")


        # verify the required parameter 'formula2' is set
        if self.formula2 is None:
            raise ValueError("Missing the required parameter `formula2` when calling `put_worksheet_format_condition_condition`")


        collection_formats = {}

        path_params = {}
        if self.name is not None:
            path_params['name'] = self.name
        if self.sheet_name is not None:
            path_params['sheetName'] = self.sheet_name
        if self.index is not None:
            path_params['index'] = self.index
        query_params = []
        if self.type is not None:
            query_params.append(('type',self.type ))
        if self.operator_type is not None:
            query_params.append(('operatorType',self.operator_type ))
        if self.formula1 is not None:
            query_params.append(('formula1',self.formula1 ))
        if self.formula2 is not None:
            query_params.append(('formula2',self.formula2 ))
        if self.folder is not None:
            query_params.append(('folder',self.folder ))
        if self.storage_name is not None:
            query_params.append(('storageName',self.storage_name ))

        header_params = {}
        header_params['x-aspose-client'] = 'python sdk';
        header_params['x-aspose-client-version'] = '25.10';

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
        resource_path =  "v3.0/cells/{name}/worksheets/{sheetName}/conditionalFormattings/{index}/condition"
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

