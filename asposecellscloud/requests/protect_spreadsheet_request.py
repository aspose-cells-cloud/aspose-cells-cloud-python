# coding: utf-8
"""
<copyright company="Aspose" file="ProtectSpreadsheetRequest.cs">
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

class ProtectSpreadsheetRequest(object):

    def __init__(self , spreadsheet ,password ,modify_password ,out_path =None ,out_storage_name =None ,regoin =None ):
        self.spreadsheet = spreadsheet 
        self.password = password 
        self.modify_password = modify_password 
        self.out_path = out_path 
        self.out_storage_name = out_storage_name 
        self.regoin = regoin 
    def create_http_request(self, api_client):

        # verify the required parameter 'spreadsheet' is set
        if self.spreadsheet is None:
            raise ValueError("Missing the required parameter `spreadsheet` when calling `protect_spreadsheet`")


        # verify the required parameter 'password' is set
        if self.password is None:
            raise ValueError("Missing the required parameter `password` when calling `protect_spreadsheet`")


        # verify the required parameter 'modify_password' is set
        if self.modify_password is None:
            raise ValueError("Missing the required parameter `modify_password` when calling `protect_spreadsheet`")


        collection_formats = {}

        path_params = {}
        query_params = []
        if self.password is not None:
            query_params.append(('password',self.password ))
        if self.modify_password is not None:
            query_params.append(('modifyPassword',self.modify_password ))
        if self.out_path is not None:
            query_params.append(('outPath',self.out_path ))
        if self.out_storage_name is not None:
            query_params.append(('outStorageName',self.out_storage_name ))
        if self.regoin is not None:
            query_params.append(('regoin',self.regoin ))

        header_params = {}
        header_params['x-aspose-client'] = 'python sdk';
        header_params['x-aspose-client-version'] = '25.8';

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
        resource_path =  "v4.0/cells/protection/spreadsheet"
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

