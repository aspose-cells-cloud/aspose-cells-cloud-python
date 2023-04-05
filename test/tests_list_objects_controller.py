# coding: utf-8

from __future__ import absolute_import

import os
import sys
import unittest
import warnings

ABSPATH = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/..")
sys.path.append(ABSPATH)

from asposecellscloud.rest import ApiException
from asposecellscloud.apis.cells_api import CellsApi
import AuthUtil
from asposecellscloud.models import *
from asposecellscloud.requests import *

global_api = None

class TestListObjectsControllerApi(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        global global_api
        if global_api is None:
           global_api = CellsApi(AuthUtil.GetClientId(),AuthUtil.GetClientSecret(),"v3.0",AuthUtil.GetBaseUrl())
        self.api = global_api

    def tearDown(self):
        pass

    def test_get_worksheet_list_objects(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorksheetListObjectsRequest( remote_name, 'Sheet7',folder= remote_folder,storage_name= '')
        self.api.get_worksheet_list_objects(request)


    def test_get_worksheet_list_object(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorksheetListObjectRequest( remote_name, 'Sheet7', 0,format= 'pdf',folder= remote_folder,storage_name= '')
        self.api.get_worksheet_list_object(request)


    def test_put_worksheet_list_object(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutWorksheetListObjectRequest( remote_name, 'Sheet7',start_row= 1,start_column= 1,end_row= 6,end_column= 6,folder= remote_folder,has_headers= True,display_name= 'true',show_totals= False,storage_name= '')
        self.api.put_worksheet_list_object(request)


    def test_delete_worksheet_list_objects(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  DeleteWorksheetListObjectsRequest( remote_name, 'Sheet7',folder= remote_folder,storage_name= '')
        self.api.delete_worksheet_list_objects(request)


    def test_delete_worksheet_list_object(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  DeleteWorksheetListObjectRequest( remote_name, 'Sheet7', 0,folder= remote_folder,storage_name= '')
        self.api.delete_worksheet_list_object(request)


    def test_post_worksheet_list_object(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        listObject = ListObject(show_header_row= True )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorksheetListObjectRequest( remote_name, 'Sheet7', 0, listObject,folder= remote_folder,storage_name= '')
        self.api.post_worksheet_list_object(request)


    def test_post_worksheet_list_object_convert_to_range(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorksheetListObjectConvertToRangeRequest( remote_name, 'Sheet7', 0,folder= remote_folder,storage_name= '')
        self.api.post_worksheet_list_object_convert_to_range(request)


    def test_post_worksheet_list_object_summarize_with_pivot_table(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        createPivotTableRequestPivotFieldColumns = [
            2
        ]
        createPivotTableRequestPivotFieldData = [
            1
        ]
        createPivotTableRequestPivotFieldRows = [
            0
        ]
        createPivotTableRequest = CreatePivotTableRequest(dest_cell_name= 'C1' ,name= 'testp' ,source_data= '=Sheet2!A1:E8' ,use_same_source= True ,pivot_field_columns= createPivotTableRequestPivotFieldColumns ,pivot_field_data= createPivotTableRequestPivotFieldData ,pivot_field_rows= createPivotTableRequestPivotFieldRows )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorksheetListObjectSummarizeWithPivotTableRequest( remote_name, 'Sheet7', 0, 'Sheet2', createPivotTableRequest,folder= remote_folder,storage_name= '')
        self.api.post_worksheet_list_object_summarize_with_pivot_table(request)


    def test_post_worksheet_list_object_sort_table(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        dataSorter = DataSorter(case_sensitive= True )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorksheetListObjectSortTableRequest( remote_name, 'Sheet7', 0, dataSorter,folder= remote_folder,storage_name= '')
        self.api.post_worksheet_list_object_sort_table(request)


    def test_post_worksheet_list_column(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        listColumn = ListColumn(name= 'test cloumn' )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorksheetListColumnRequest( remote_name, 'Sheet7', 0, 0, listColumn,folder= remote_folder,storage_name= '')
        self.api.post_worksheet_list_column(request)


    def test_post_worksheet_list_columns_total(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        tableTotalRequeststableTotalRequest0 = TableTotalRequest(list_column_index= 1 ,totals_calculation= 'Average' )
        tableTotalRequests = [
            tableTotalRequeststableTotalRequest0
        ]
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorksheetListColumnsTotalRequest( remote_name, 'Sheet7', 0, tableTotalRequests,folder= remote_folder,storage_name= '')
        self.api.post_worksheet_list_columns_total(request)


if __name__ == '__main__':
    unittest.main()