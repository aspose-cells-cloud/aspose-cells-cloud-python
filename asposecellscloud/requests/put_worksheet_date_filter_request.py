# coding: utf-8
"""
<copyright company="Aspose" file="PutWorksheetDateFilterRequest.cs">
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

class PutWorksheetDateFilterRequest(object):

    def __init__(self , name ,sheet_name ,range =None ,field_index =None ,date_time_grouping_type =None ,year =None ,month =None ,day =None ,hour =None ,minute =None ,second =None ,match_blanks =None ,refresh =None ,folder =None ,storage_name =None ):
        self.name = name 
        self.sheet_name = sheet_name 
        self.range = range 
        self.field_index = field_index 
        self.date_time_grouping_type = date_time_grouping_type 
        self.year = year 
        self.month = month 
        self.day = day 
        self.hour = hour 
        self.minute = minute 
        self.second = second 
        self.match_blanks = match_blanks 
        self.refresh = refresh 
        self.folder = folder 
        self.storage_name = storage_name 
    def create_http_request(self, api_client):

        # verify the required parameter 'name' is set
        if self.name is None:
            raise ValueError("Missing the required parameter `name` when calling `put_worksheet_date_filter`")


        # verify the required parameter 'sheet_name' is set
        if self.sheet_name is None:
            raise ValueError("Missing the required parameter `sheet_name` when calling `put_worksheet_date_filter`")


        # verify the required parameter 'range' is set
        if self.range is None:
            raise ValueError("Missing the required parameter `range` when calling `put_worksheet_date_filter`")


        # verify the required parameter 'field_index' is set
        if self.field_index is None:
            raise ValueError("Missing the required parameter `field_index` when calling `put_worksheet_date_filter`")


        # verify the required parameter 'date_time_grouping_type' is set
        if self.date_time_grouping_type is None:
            raise ValueError("Missing the required parameter `date_time_grouping_type` when calling `put_worksheet_date_filter`")


        collection_formats = {}

        path_params = {}
        if self.name is not None:
            path_params['name'] = self.name
        if self.sheet_name is not None:
            path_params['sheetName'] = self.sheet_name
        query_params = []
        if self.range is not None:
            query_params.append(('range',self.range ))
        if self.field_index is not None:
            query_params.append(('fieldIndex',self.field_index ))
        if self.date_time_grouping_type is not None:
            query_params.append(('dateTimeGroupingType',self.date_time_grouping_type ))
        if self.year is not None:
            query_params.append(('year',self.year ))
        if self.month is not None:
            query_params.append(('month',self.month ))
        if self.day is not None:
            query_params.append(('day',self.day ))
        if self.hour is not None:
            query_params.append(('hour',self.hour ))
        if self.minute is not None:
            query_params.append(('minute',self.minute ))
        if self.second is not None:
            query_params.append(('second',self.second ))
        if self.match_blanks is not None:
            query_params.append(('matchBlanks',self.match_blanks ))
        if self.refresh is not None:
            query_params.append(('refresh',self.refresh ))
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
        resource_path = "/cells/{name}/worksheets/{sheetName}/autoFilter/dateFilter"
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

