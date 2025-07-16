# coding: utf-8
"""
<copyright company="Aspose" file="PostWorkbookImportXMLRequest.cs">
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

class PostWorkbookImportXMLRequest(object):

    def __init__(self , name ,import_xml_request ,password =None ,folder =None ,storage_name =None ,out_path =None ,out_storage_name =None ,check_excel_restriction =None ,region =None ):
        self.name = name 
        self.import_xml_request = import_xml_request 
        self.password = password 
        self.folder = folder 
        self.storage_name = storage_name 
        self.out_path = out_path 
        self.out_storage_name = out_storage_name 
        self.check_excel_restriction = check_excel_restriction 
        self.region = region 
    def create_http_request(self, api_client):

        # verify the required parameter 'name' is set
        if self.name is None:
            raise ValueError("Missing the required parameter `name` when calling `post_workbook_import_xml`")


        # verify the required parameter 'import_xml_request' is set
        if self.import_xml_request is None:
            raise ValueError("Missing the required parameter `import_xml_request` when calling `post_workbook_import_xml`")


        collection_formats = {}

        path_params = {}
        if self.name is not None:
            path_params['name'] = self.name
        query_params = []
        if self.password is not None:
            query_params.append(('password',self.password ))
        if self.folder is not None:
            query_params.append(('folder',self.folder ))
        if self.storage_name is not None:
            query_params.append(('storageName',self.storage_name ))
        if self.out_path is not None:
            query_params.append(('outPath',self.out_path ))
        if self.out_storage_name is not None:
            query_params.append(('outStorageName',self.out_storage_name ))
        if self.check_excel_restriction is not None:
            query_params.append(('checkExcelRestriction',self.check_excel_restriction ))
        if self.region is not None:
            query_params.append(('region',self.region ))

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

        if self.import_xml_request is not None:
             body_params =self.import_xml_request 

        # Authentication setting
        auth_settings = []
        resource_path =  "v3.0/cells/{name}/importxml"
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
                "response_type": 'file'  
        }

