# coding: utf-8
"""
<copyright company="Aspose" file="GetWorkbookRequest.cs">
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

class GetWorkbookRequest(object):

    def __init__(self , name ,format =None ,password =None ,is_auto_fit =None ,only_save_table =None ,folder =None ,out_path =None ,storage_name =None ,out_storage_name =None ,check_excel_restriction =None ,region =None ,page_wide_fit_on_per_sheet =None ,page_tall_fit_on_per_sheet =None ,one_page_per_sheet =None ,only_autofit_table =None ,fonts_location =None ):
        self.name = name 
        self.format = format 
        self.password = password 
        self.is_auto_fit = is_auto_fit 
        self.only_save_table = only_save_table 
        self.folder = folder 
        self.out_path = out_path 
        self.storage_name = storage_name 
        self.out_storage_name = out_storage_name 
        self.check_excel_restriction = check_excel_restriction 
        self.region = region 
        self.page_wide_fit_on_per_sheet = page_wide_fit_on_per_sheet 
        self.page_tall_fit_on_per_sheet = page_tall_fit_on_per_sheet 
        self.one_page_per_sheet = one_page_per_sheet 
        self.only_autofit_table = only_autofit_table 
        self.fonts_location = fonts_location         
        self.expand_query_parameters = {}

    def set_expand_query_parameter(self, query_name, query_value):
        self.expand_query_parameters.append(query_name,query_value)
        pass
    def create_http_request(self, api_client):

        # verify the required parameter 'name' is set
        if self.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_workbook`")


        collection_formats = {}

        path_params = {}
        if self.name is not None:
            path_params['name'] = self.name
        query_params = []
        if self.format is not None:
            query_params.append(('format',self.format ))
        if self.password is not None:
            query_params.append(('password',self.password ))
        if self.is_auto_fit is not None:
            query_params.append(('isAutoFit',self.is_auto_fit ))
        if self.only_save_table is not None:
            query_params.append(('onlySaveTable',self.only_save_table ))
        if self.folder is not None:
            query_params.append(('folder',self.folder ))
        if self.out_path is not None:
            query_params.append(('outPath',self.out_path ))
        if self.storage_name is not None:
            query_params.append(('storageName',self.storage_name ))
        if self.out_storage_name is not None:
            query_params.append(('outStorageName',self.out_storage_name ))
        if self.check_excel_restriction is not None:
            query_params.append(('checkExcelRestriction',self.check_excel_restriction ))
        if self.region is not None:
            query_params.append(('region',self.region ))
        if self.page_wide_fit_on_per_sheet is not None:
            query_params.append(('pageWideFitOnPerSheet',self.page_wide_fit_on_per_sheet ))
        if self.page_tall_fit_on_per_sheet is not None:
            query_params.append(('pageTallFitOnPerSheet',self.page_tall_fit_on_per_sheet ))
        if self.one_page_per_sheet is not None:
            query_params.append(('onePagePerSheet',self.one_page_per_sheet ))
        if self.only_autofit_table is not None:
            query_params.append(('onlyAutofitTable',self.only_autofit_table ))
        if self.fonts_location is not None:
            query_params.append(('FontsLocation',self.fonts_location ))
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
        resource_path =  "v3.0/cells/{name}"
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

