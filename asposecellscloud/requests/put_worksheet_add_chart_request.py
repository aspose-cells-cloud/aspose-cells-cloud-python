# coding: utf-8
"""
<copyright company="Aspose" file="PutWorksheetAddChartRequest.cs">
  Copyright (c) 2023 Aspose.Cells Cloud
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

class PutWorksheetAddChartRequest(object):

    def __init__(self , name ,sheet_name ,chart_type =None ,upper_left_row =None ,upper_left_column =None ,lower_right_row =None ,lower_right_column =None ,area =None ,is_vertical =None ,category_data =None ,is_auto_get_serial_name =None ,title =None ,folder =None ,data_labels =None ,data_labels_position =None ,pivot_table_sheet =None ,pivot_table_name =None ,storage_name =None ):
        self.name = name 
        self.sheet_name = sheet_name 
        self.chart_type = chart_type 
        self.upper_left_row = upper_left_row 
        self.upper_left_column = upper_left_column 
        self.lower_right_row = lower_right_row 
        self.lower_right_column = lower_right_column 
        self.area = area 
        self.is_vertical = is_vertical 
        self.category_data = category_data 
        self.is_auto_get_serial_name = is_auto_get_serial_name 
        self.title = title 
        self.folder = folder 
        self.data_labels = data_labels 
        self.data_labels_position = data_labels_position 
        self.pivot_table_sheet = pivot_table_sheet 
        self.pivot_table_name = pivot_table_name 
        self.storage_name = storage_name 
    def create_http_request(self, api_client):

        # verify the required parameter 'name' is set
        if self.name is None:
            raise ValueError("Missing the required parameter `name` when calling `put_worksheet_add_chart`")


        # verify the required parameter 'sheet_name' is set
        if self.sheet_name is None:
            raise ValueError("Missing the required parameter `sheet_name` when calling `put_worksheet_add_chart`")


        # verify the required parameter 'chart_type' is set
        if self.chart_type is None:
            raise ValueError("Missing the required parameter `chart_type` when calling `put_worksheet_add_chart`")


        collection_formats = {}

        path_params = {}
        if self.name is not None:
            path_params['name'] = self.name
        if self.sheet_name is not None:
            path_params['sheetName'] = self.sheet_name
        query_params = []
        if self.chart_type is not None:
            query_params.append(('chartType',self.chart_type ))
        if self.upper_left_row is not None:
            query_params.append(('upperLeftRow',self.upper_left_row ))
        if self.upper_left_column is not None:
            query_params.append(('upperLeftColumn',self.upper_left_column ))
        if self.lower_right_row is not None:
            query_params.append(('lowerRightRow',self.lower_right_row ))
        if self.lower_right_column is not None:
            query_params.append(('lowerRightColumn',self.lower_right_column ))
        if self.area is not None:
            query_params.append(('area',self.area ))
        if self.is_vertical is not None:
            query_params.append(('isVertical',self.is_vertical ))
        if self.category_data is not None:
            query_params.append(('categoryData',self.category_data ))
        if self.is_auto_get_serial_name is not None:
            query_params.append(('isAutoGetSerialName',self.is_auto_get_serial_name ))
        if self.title is not None:
            query_params.append(('title',self.title ))
        if self.folder is not None:
            query_params.append(('folder',self.folder ))
        if self.data_labels is not None:
            query_params.append(('dataLabels',self.data_labels ))
        if self.data_labels_position is not None:
            query_params.append(('dataLabelsPosition',self.data_labels_position ))
        if self.pivot_table_sheet is not None:
            query_params.append(('pivotTableSheet',self.pivot_table_sheet ))
        if self.pivot_table_name is not None:
            query_params.append(('pivotTableName',self.pivot_table_name ))
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
        resource_path = "/cells/{name}/worksheets/{sheetName}/charts"
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

