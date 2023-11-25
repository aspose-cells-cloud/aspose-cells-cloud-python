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

class TestCellsControllerApi(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        global global_api
        if global_api is None:
           global_api = CellsApi(AuthUtil.GetClientId(),AuthUtil.GetClientSecret(),"v3.0",AuthUtil.GetBaseUrl())
        self.api = global_api

    def tearDown(self):
        pass

    def test_post_clear_contents(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostClearContentsRequest( remote_name, 'Sheet1',range= 'A1:C10',start_row= 1,start_column= 1,end_row= 3,end_column= 3,folder= remote_folder,storage_name= '')
        self.api.post_clear_contents(request)


    def test_post_clear_formats(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostClearFormatsRequest( remote_name, 'Sheet1',range= 'A1:C10',start_row= 1,start_column= 1,end_row= 3,end_column= 3,folder= remote_folder,storage_name= '')
        self.api.post_clear_formats(request)


    def test_post_update_worksheet_range_style(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        styleFont = Font(size= 16 )
        style = Style(font= styleFont )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostUpdateWorksheetRangeStyleRequest( remote_name, 'Sheet1', 'A1:C10', style,folder= remote_folder,storage_name= '')
        self.api.post_update_worksheet_range_style(request)


    def test_post_worksheet_merge(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorksheetMergeRequest( remote_name, 'Sheet1', 1, 1, 4, 4,folder= remote_folder,storage_name= '')
        self.api.post_worksheet_merge(request)


    def test_post_worksheet_unmerge(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorksheetUnmergeRequest( remote_name, 'Sheet1', 1, 1, 4, 4,folder= remote_folder,storage_name= '')
        self.api.post_worksheet_unmerge(request)


    def test_get_worksheet_cells(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorksheetCellsRequest( remote_name, 'Sheet1',offest= 1,count= 10,folder= remote_folder,storage_name= '')
        self.api.get_worksheet_cells(request)


    def test_get_worksheet_cell(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorksheetCellRequest( remote_name, 'Sheet1', 'A1',folder= remote_folder,storage_name= '')
        self.api.get_worksheet_cell(request)


    def test_get_worksheet_cell_style(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorksheetCellStyleRequest( remote_name, 'Sheet1', 'A1',folder= remote_folder,storage_name= '')
        self.api.get_worksheet_cell_style(request)


    def test_post_worksheet_cell_set_value(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorksheetCellSetValueRequest( remote_name, 'Sheet1', 'A1',value= '1',type= 'int',folder= remote_folder,storage_name= '')
        self.api.post_worksheet_cell_set_value(request)


    def test_post_update_worksheet_cell_style(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        styleFont = Font(size= 16 )
        style = Style(font= styleFont )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostUpdateWorksheetCellStyleRequest( remote_name, 'Sheet1', 'A1', style,folder= remote_folder,storage_name= '')
        self.api.post_update_worksheet_cell_style(request)


    def test_post_set_cell_range_value(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostSetCellRangeValueRequest( remote_name, 'Sheet1', 'A1:C10', 'Test', 'string',folder= remote_folder,storage_name= '')
        self.api.post_set_cell_range_value(request)


    def test_post_copy_cell_into_cell(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostCopyCellIntoCellRequest( remote_name, 'C1', 'Sheet1', 'Sheet2',cellname= 'A1',row= 1,column= 1,folder= remote_folder,storage_name= '')
        self.api.post_copy_cell_into_cell(request)


    def test_get_cell_html_string(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetCellHtmlStringRequest( remote_name, 'Sheet1', 'A1',folder= remote_folder,storage_name= '')
        self.api.get_cell_html_string(request)


    def test_post_set_cell_html_string(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostSetCellHtmlStringRequest( remote_name, 'Sheet1', 'A1',folder= remote_folder,storage_name= '')
        self.api.post_set_cell_html_string(request)


    def test_post_cell_calculate(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        options = CalculationOptions(recursive= True ,ignore_error= True )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostCellCalculateRequest( remote_name, 'Sheet1', 'A1',options= options,folder= remote_folder,storage_name= '')
        self.api.post_cell_calculate(request)


    def test_post_cell_characters(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        optionsvalue0Font = Font(is_bold= True ,size= 16 )
        optionsvalue0 = FontSetting(length= 5 ,start_index= 0 ,font= optionsvalue0Font )
        options = [
            optionsvalue0
        ]
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostCellCharactersRequest( remote_name, 'Sheet1', 'E36',options= options,folder= remote_folder,storage_name= '')
        self.api.post_cell_characters(request)


    def test_get_worksheet_columns(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorksheetColumnsRequest(name= remote_name,sheet_name= 'Sheet1',offset= 1,count= 10,folder= remote_folder,storage_name= '')
        self.api.get_worksheet_columns(request)


    def test_post_set_worksheet_column_width(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostSetWorksheetColumnWidthRequest( remote_name, 'Sheet1', 1, 10.9,count= 10,folder= remote_folder,storage_name= '')
        self.api.post_set_worksheet_column_width(request)


    def test_get_worksheet_column(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorksheetColumnRequest( remote_name, 'Sheet1', 1,folder= remote_folder,storage_name= '')
        self.api.get_worksheet_column(request)


    def test_put_insert_worksheet_columns(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutInsertWorksheetColumnsRequest( remote_name, 'Sheet1', 1, 10,update_reference= True,folder= remote_folder,storage_name= '')
        self.api.put_insert_worksheet_columns(request)


    def test_delete_worksheet_columns(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  DeleteWorksheetColumnsRequest( remote_name, 'Sheet1', 1, 10, True,folder= remote_folder,storage_name= '')
        self.api.delete_worksheet_columns(request)


    def test_post_hide_worksheet_columns(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostHideWorksheetColumnsRequest( remote_name, 'Sheet1', 1, 10,folder= remote_folder,storage_name= '')
        self.api.post_hide_worksheet_columns(request)


    def test_post_unhide_worksheet_columns(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostUnhideWorksheetColumnsRequest( remote_name, 'Sheet1', 1, 10,width= 10.9,folder= remote_folder,storage_name= '')
        self.api.post_unhide_worksheet_columns(request)


    def test_post_group_worksheet_columns(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostGroupWorksheetColumnsRequest( remote_name, 'Sheet1', 1, 9,hide= True,folder= remote_folder,storage_name= '')
        self.api.post_group_worksheet_columns(request)


    def test_post_ungroup_worksheet_columns(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostUngroupWorksheetColumnsRequest( remote_name, 'Sheet1', 1, 9,folder= remote_folder,storage_name= '')
        self.api.post_ungroup_worksheet_columns(request)


    def test_post_copy_worksheet_columns(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostCopyWorksheetColumnsRequest( remote_name, 'Sheet1', 1, 19, 8,worksheet= 'Sheet2',folder= remote_folder,storage_name= '')
        self.api.post_copy_worksheet_columns(request)


    def test_post_column_style(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        styleFont = Font(size= 16 )
        style = Style(font= styleFont )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostColumnStyleRequest( remote_name, 'Sheet1', 1, style,folder= remote_folder,storage_name= '')
        self.api.post_column_style(request)


    def test_get_worksheet_rows(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorksheetRowsRequest( remote_name, 'Sheet1',offset= 1,count= 10,folder= remote_folder,storage_name= '')
        self.api.get_worksheet_rows(request)


    def test_get_worksheet_row(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorksheetRowRequest( remote_name, 'Sheet1', 1,folder= remote_folder,storage_name= '')
        self.api.get_worksheet_row(request)


    def test_delete_worksheet_row(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  DeleteWorksheetRowRequest( remote_name, 'Sheet1', 1,folder= remote_folder,storage_name= '')
        self.api.delete_worksheet_row(request)


    def test_delete_worksheet_rows(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  DeleteWorksheetRowsRequest( remote_name, 'Sheet1', 1,total_rows= 10,update_reference= True,folder= remote_folder,storage_name= '')
        self.api.delete_worksheet_rows(request)


    def test_put_insert_worksheet_rows(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutInsertWorksheetRowsRequest( remote_name, 'Sheet1', 1,total_rows= 10,update_reference= True,folder= remote_folder,storage_name= '')
        self.api.put_insert_worksheet_rows(request)


    def test_put_insert_worksheet_row(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutInsertWorksheetRowRequest( remote_name, 'Sheet1', 1,folder= remote_folder,storage_name= '')
        self.api.put_insert_worksheet_row(request)


    def test_post_update_worksheet_row(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostUpdateWorksheetRowRequest( remote_name, 'Sheet1', 1,height= 10.8,count= 9,folder= remote_folder,storage_name= '')
        self.api.post_update_worksheet_row(request)


    def test_post_hide_worksheet_rows(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostHideWorksheetRowsRequest( remote_name, 'Sheet1', 1, 6,folder= remote_folder,storage_name= '')
        self.api.post_hide_worksheet_rows(request)


    def test_post_unhide_worksheet_rows(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostUnhideWorksheetRowsRequest( remote_name, 'Sheet1', 1, 8,height= 10.9,folder= remote_folder,storage_name= '')
        self.api.post_unhide_worksheet_rows(request)


    def test_post_group_worksheet_rows(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostGroupWorksheetRowsRequest( remote_name, 'Sheet1', 1, 9,hide= True,folder= remote_folder,storage_name= '')
        self.api.post_group_worksheet_rows(request)


    def test_post_ungroup_worksheet_rows(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostUngroupWorksheetRowsRequest( remote_name, 'Sheet1', 1, 9,is_all= True,folder= remote_folder,storage_name= '')
        self.api.post_ungroup_worksheet_rows(request)


    def test_post_copy_worksheet_rows(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostCopyWorksheetRowsRequest( remote_name, 'Sheet1', 1, 12, 5,worksheet= 'Sheet2',folder= remote_folder,storage_name= '')
        self.api.post_copy_worksheet_rows(request)


    def test_post_row_style(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        styleFont = Font(size= 16 )
        style = Style(font= styleFont )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostRowStyleRequest( remote_name, 'Sheet1', 1, style,folder= remote_folder,storage_name= '')
        self.api.post_row_style(request)


if __name__ == '__main__':
    unittest.main()