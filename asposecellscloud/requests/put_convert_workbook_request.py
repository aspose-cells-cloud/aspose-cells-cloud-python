# coding: utf-8
"""
<copyright company="Aspose" file="PutConvertWorkbookRequest.cs">
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

class PutConvertWorkbookRequest(object):

    def __init__(self , file ,format =None ,password =None ,out_path =None ,storage_name =None ,check_excel_restriction =None ,stream_format =None ,region =None ,page_wide_fit_on_per_sheet =None ,page_tall_fit_on_per_sheet =None ,sheet_name =None ,page_index =None ):
        self.file = file 
        self.format = format 
        self.password = password 
        self.out_path = out_path 
        self.storage_name = storage_name 
        self.check_excel_restriction = check_excel_restriction 
        self.stream_format = stream_format 
        self.region = region 
        self.page_wide_fit_on_per_sheet = page_wide_fit_on_per_sheet 
        self.page_tall_fit_on_per_sheet = page_tall_fit_on_per_sheet 
        self.sheet_name = sheet_name 
        self.page_index = page_index 
    def create_http_request(self, api_client):

        # verify the required parameter 'file' is set
        if self.file is None:
            raise ValueError("Missing the required parameter `file` when calling `put_convert_workbook`")


        collection_formats = {}

        path_params = {}
        query_params = []
        if self.format is not None:
            query_params.append(('format',self.format ))
        if self.password is not None:
            query_params.append(('password',self.password ))
        if self.out_path is not None:
            query_params.append(('outPath',self.out_path ))
        if self.storage_name is not None:
            query_params.append(('storageName',self.storage_name ))
        if self.check_excel_restriction is not None:
            query_params.append(('checkExcelRestriction',self.check_excel_restriction ))
        if self.stream_format is not None:
            query_params.append(('streamFormat',self.stream_format ))
        if self.region is not None:
            query_params.append(('region',self.region ))
        if self.page_wide_fit_on_per_sheet is not None:
            query_params.append(('pageWideFitOnPerSheet',self.page_wide_fit_on_per_sheet ))
        if self.page_tall_fit_on_per_sheet is not None:
            query_params.append(('pageTallFitOnPerSheet',self.page_tall_fit_on_per_sheet ))
        if self.sheet_name is not None:
            query_params.append(('sheetName',self.sheet_name ))
        if self.page_index is not None:
            query_params.append(('pageIndex',self.page_index ))

        header_params = {}

        form_params = []
        local_var_files = {}
        if self.file is not None:            
            if isinstance(self.file,dict):
                for filename , filecontext in  self.file.items():
                    local_var_files[filename] = filecontext
            else:
                local_var_files['File'] = self.file   

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = api_client.\
            select_header_content_type(['multipart/form-data'])

        # Authentication setting
        auth_settings = []
        resource_path = "/cells/convert"
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

