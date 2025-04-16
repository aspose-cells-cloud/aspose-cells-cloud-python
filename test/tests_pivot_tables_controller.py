# coding: utf-8

from __future__ import absolute_import

import os
import sys
import unittest
import warnings
import time

ABSPATH = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/..")
sys.path.append(ABSPATH)

from asposecellscloud.rest import ApiException
from asposecellscloud.apis.cells_api import CellsApi
import AuthUtil
from asposecellscloud.models import *
from asposecellscloud.requests import *

global_api = None

class TestPivotTablesControllerApi(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        global global_api
        if global_api is None:
           global_api = CellsApi(AuthUtil.GetClientId(),AuthUtil.GetClientSecret(),"v3.0",AuthUtil.GetBaseUrl())
        self.api = global_api

    def tearDown(self):
        pass

    def test_get_worksheet_pivot_tables(self):
        remote_folder = 'TestData/In'

        local_name = 'TestCase.xlsx'
        remote_name = 'TestCase.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorksheetPivotTablesRequest( remote_name, 'Sheet4',folder= remote_folder,storage_name= '')
        self.api.get_worksheet_pivot_tables(request)

    def test_get_worksheet_pivot_table(self):
        remote_folder = 'TestData/In'

        local_name = 'TestCase.xlsx'
        remote_name = 'TestCase.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorksheetPivotTableRequest( remote_name, 'Sheet4', 0,folder= remote_folder,storage_name= '')
        self.api.get_worksheet_pivot_table(request)

    def test_get_pivot_table_field(self):
        remote_folder = 'TestData/In'

        local_name = 'TestCase.xlsx'
        remote_name = 'TestCase.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetPivotTableFieldRequest( remote_name, 'Sheet4', 0, 0, 'Row',folder= remote_folder,storage_name= '')
        self.api.get_pivot_table_field(request)

    def test_get_worksheet_pivot_table_filters(self):
        remote_folder = 'TestData/In'

        local_name = 'TestCase.xlsx'
        remote_name = 'TestCase.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorksheetPivotTableFiltersRequest( remote_name, 'Sheet4', 0,folder= remote_folder,storage_name= '')
        self.api.get_worksheet_pivot_table_filters(request)

    def test_get_worksheet_pivot_table_filter(self):
        remote_folder = 'TestData/In'

        local_name = 'TestCase.xlsx'
        remote_name = 'TestCase.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorksheetPivotTableFilterRequest( remote_name, 'Sheet3', 0, 0,folder= remote_folder,storage_name= '')
        self.api.get_worksheet_pivot_table_filter(request)

    def test_put_worksheet_pivot_table(self):
        remote_folder = 'TestData/In'

        local_name = 'TestCase.xlsx'
        remote_name = 'TestCase.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutWorksheetPivotTableRequest( remote_name, 'Sheet4',folder= remote_folder,source_data= '=Sheet1!C6:E13',dest_cell_name= 'C1',table_name= 'TestPivot',use_same_source= True,storage_name= '')
        self.api.put_worksheet_pivot_table(request)

    def test_put_pivot_table_field(self):
        remote_folder = 'TestData/In'

        local_name = 'TestCase.xlsx'
        remote_name = 'TestCase.xlsx'

        pivotTableFieldRequestData = [
            0
        ]
        pivotTableFieldRequest = PivotTableFieldRequest(data= pivotTableFieldRequestData )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutPivotTableFieldRequest( remote_name, 'Sheet4', 0, 'Row', pivotTableFieldRequest,need_re_calculate= True,folder= remote_folder,storage_name= '')
        self.api.put_pivot_table_field(request)

    def test_put_worksheet_pivot_table_filter(self):
        remote_folder = 'TestData/In'

        local_name = 'TestCase.xlsx'
        remote_name = 'TestCase.xlsx'

        filter = PivotFilter(field_index= 0 ,filter_type= 'Count' )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutWorksheetPivotTableFilterRequest( remote_name, 'Sheet4', 0, filter,need_re_calculate= True,folder= remote_folder,storage_name= '')
        self.api.put_worksheet_pivot_table_filter(request)

    def test_post_pivot_table_field_hide_item(self):
        remote_folder = 'TestData/In'

        local_name = 'TestCase.xlsx'
        remote_name = 'TestCase.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostPivotTableFieldHideItemRequest( remote_name, 'Sheet4', 0, 'Row', 0, 1, True,need_re_calculate= True,folder= remote_folder,storage_name= '')
        self.api.post_pivot_table_field_hide_item(request)

    def test_post_pivot_table_field_move_to(self):
        remote_folder = 'TestData/In'

        local_name = 'TestCase.xlsx'
        remote_name = 'TestCase.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostPivotTableFieldMoveToRequest( remote_name, 'Sheet4', 0, 0, 'Row', 'Column',folder= remote_folder,storage_name= '')
        self.api.post_pivot_table_field_move_to(request)

    def test_post_pivot_table_cell_style(self):
        remote_folder = 'TestData/In'

        local_name = 'TestCase.xlsx'
        remote_name = 'TestCase.xlsx'

        styleFont = Font(size= 16 )
        style = Style(font= styleFont )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostPivotTableCellStyleRequest( remote_name, 'Sheet4', 0, 1, 1, style,need_re_calculate= True,folder= remote_folder,storage_name= '')
        self.api.post_pivot_table_cell_style(request)

    def test_post_pivot_table_style(self):
        remote_folder = 'TestData/In'

        local_name = 'TestCase.xlsx'
        remote_name = 'TestCase.xlsx'

        styleFont = Font(size= 16 )
        style = Style(font= styleFont )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostPivotTableStyleRequest( remote_name, 'Sheet4', 0, style,need_re_calculate= True,folder= remote_folder,storage_name= '')
        self.api.post_pivot_table_style(request)

    def test_post_pivot_table_update_pivot_fields(self):
        remote_folder = 'TestData/In'

        local_name = 'TestCase.xlsx'
        remote_name = 'TestCase.xlsx'

        pivotField = PivotField(show_compact= True )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostPivotTableUpdatePivotFieldsRequest( remote_name, 'Sheet4', 0, 'Row', pivotField,need_re_calculate= True,folder= remote_folder,storage_name= '')
        self.api.post_pivot_table_update_pivot_fields(request)

    def test_post_pivot_table_update_pivot_field(self):
        remote_folder = 'TestData/In'

        local_name = 'TestCase.xlsx'
        remote_name = 'TestCase.xlsx'

        pivotField = PivotField(show_compact= True )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostPivotTableUpdatePivotFieldRequest( remote_name, 'Sheet4', 0, 0, 'Row', pivotField,need_re_calculate= True,folder= remote_folder,storage_name= '')
        self.api.post_pivot_table_update_pivot_field(request)

    def test_post_worksheet_pivot_table_calculate(self):
        remote_folder = 'TestData/In'

        local_name = 'TestCase.xlsx'
        remote_name = 'TestCase.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorksheetPivotTableCalculateRequest( remote_name, 'Sheet4', 0,folder= remote_folder,storage_name= '')
        self.api.post_worksheet_pivot_table_calculate(request)

    def test_post_worksheet_pivot_table_move(self):
        remote_folder = 'TestData/In'

        local_name = 'TestCase.xlsx'
        remote_name = 'TestCase.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorksheetPivotTableMoveRequest( remote_name, 'Sheet4', 0,row= 1,column= 1,dest_cell_name= 'C10',folder= remote_folder,storage_name= '')
        self.api.post_worksheet_pivot_table_move(request)

    def test_delete_worksheet_pivot_tables(self):
        remote_folder = 'TestData/In'

        local_name = 'TestCase.xlsx'
        remote_name = 'TestCase.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  DeleteWorksheetPivotTablesRequest( remote_name, 'Sheet4',folder= remote_folder,storage_name= '')
        self.api.delete_worksheet_pivot_tables(request)

    def test_delete_worksheet_pivot_table(self):
        remote_folder = 'TestData/In'

        local_name = 'TestCase.xlsx'
        remote_name = 'TestCase.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  DeleteWorksheetPivotTableRequest( remote_name, 'Sheet4', 0,folder= remote_folder,storage_name= '')
        self.api.delete_worksheet_pivot_table(request)

    def test_delete_pivot_table_field(self):
        remote_folder = 'TestData/In'

        local_name = 'TestCase.xlsx'
        remote_name = 'TestCase.xlsx'

        pivotTableFieldRequestData = [
            0
        ]
        pivotTableFieldRequest = PivotTableFieldRequest(data= pivotTableFieldRequestData )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  DeletePivotTableFieldRequest( remote_name, 'Sheet4', 0, 'Row', pivotTableFieldRequest,folder= remote_folder,storage_name= '')
        self.api.delete_pivot_table_field(request)

    def test_delete_worksheet_pivot_table_filters(self):
        remote_folder = 'TestData/In'

        local_name = 'TestCase.xlsx'
        remote_name = 'TestCase.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  DeleteWorksheetPivotTableFiltersRequest( remote_name, 'Sheet3', 0,need_re_calculate= True,folder= remote_folder,storage_name= '')
        self.api.delete_worksheet_pivot_table_filters(request)

    def test_delete_worksheet_pivot_table_filter(self):
        remote_folder = 'TestData/In'

        local_name = 'TestCase.xlsx'
        remote_name = 'TestCase.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  DeleteWorksheetPivotTableFilterRequest( remote_name, 'Sheet3', 0, 0,need_re_calculate= True,folder= remote_folder,storage_name= '')
        self.api.delete_worksheet_pivot_table_filter(request)

if __name__ == '__main__':
    unittest.main()