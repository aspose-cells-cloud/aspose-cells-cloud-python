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

class TestWorksheetControllerApi(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        global global_api
        if global_api is None:
           global_api = CellsApi(AuthUtil.GetClientId(),AuthUtil.GetClientSecret(),"v3.0",AuthUtil.GetBaseUrl())
        self.api = global_api

    def tearDown(self):
        pass

    def test_get_worksheets(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorksheetsRequest( remote_name,folder= remote_folder,storage_name= '')
        self.api.get_worksheets(request)


    def test_get_worksheet_with_format(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorksheetWithFormatRequest( remote_name, 'Sheet1',format= 'png',page_index= 0,folder= remote_folder,storage_name= '')
        self.api.get_worksheet_with_format(request)


    def test_put_change_visibility_worksheet(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutChangeVisibilityWorksheetRequest( remote_name, 'Sheet1', True,folder= remote_folder,storage_name= '')
        self.api.put_change_visibility_worksheet(request)


    def test_put_active_worksheet(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutActiveWorksheetRequest( remote_name, 'Sheet1',folder= remote_folder,storage_name= '')
        self.api.put_active_worksheet(request)


    def test_put_insert_new_worksheet(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutInsertNewWorksheetRequest( remote_name, 'Sheet1', 1, 'VB',newsheetname= 'VBASheet',folder= remote_folder,storage_name= '')
        self.api.put_insert_new_worksheet(request)


    def test_put_add_new_worksheet(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutAddNewWorksheetRequest( remote_name, 'Sheet1',position= 0,sheettype= 'VB',folder= remote_folder,storage_name= '')
        self.api.put_add_new_worksheet(request)


    def test_delete_worksheet(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  DeleteWorksheetRequest( remote_name, 'Sheet1',folder= remote_folder,storage_name= '')
        self.api.delete_worksheet(request)


    def test_delete_worksheets(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        matchCondition = MatchConditionRequest(regex_pattern= '{*}' )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  DeleteWorksheetsRequest( remote_name,match_condition= matchCondition,folder= remote_folder,storage_name= '')
        self.api.delete_worksheets(request)


    def test_post_move_worksheet(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        moving = WorksheetMovingRequest(destination_worksheet= 'Sheet4' ,position= 'After' )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostMoveWorksheetRequest( remote_name, 'Sheet1', moving,folder= remote_folder,storage_name= '')
        self.api.post_move_worksheet(request)


    def test_put_protect_worksheet(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        protectParameter = ProtectSheetParameter(protection_type= 'ALL' ,password= '123' )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutProtectWorksheetRequest( remote_name, 'Sheet1', protectParameter,folder= remote_folder,storage_name= '')
        self.api.put_protect_worksheet(request)


    def test_delete_unprotect_worksheet(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        protectParameter = ProtectSheetParameter(protection_type= 'ALL' ,password= '123' )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  DeleteUnprotectWorksheetRequest( remote_name, 'Sheet1', protectParameter,folder= remote_folder,storage_name= '')
        self.api.delete_unprotect_worksheet(request)


    def test_get_worksheet_text_items(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorksheetTextItemsRequest( remote_name, 'Sheet1',folder= remote_folder,storage_name= '')
        self.api.get_worksheet_text_items(request)


    def test_get_worksheet_comments(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorksheetCommentsRequest( remote_name, 'Sheet1',folder= remote_folder,storage_name= '')
        self.api.get_worksheet_comments(request)


    def test_get_worksheet_comment(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorksheetCommentRequest( remote_name, 'Sheet1', 'B3',folder= remote_folder,storage_name= '')
        self.api.get_worksheet_comment(request)


    def test_put_worksheet_comment(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        comment = Comment(author= 'aspose cells developer' ,note= 'aspose cells cloud api add comment.' )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutWorksheetCommentRequest( remote_name, 'Sheet1', 'C1', comment,folder= remote_folder,storage_name= '')
        self.api.put_worksheet_comment(request)


    def test_post_worksheet_comment(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        comment = Comment(author= 'aspose cells developer' ,note= 'aspose cells cloud api update comment.' )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorksheetCommentRequest( remote_name, 'Sheet1', 'B3', comment,folder= remote_folder,storage_name= '')
        self.api.post_worksheet_comment(request)


    def test_delete_worksheet_comment(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  DeleteWorksheetCommentRequest( remote_name, 'Sheet1', 'B3',folder= remote_folder,storage_name= '')
        self.api.delete_worksheet_comment(request)


    def test_delete_worksheet_comments(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  DeleteWorksheetCommentsRequest( remote_name, 'Sheet1',folder= remote_folder,storage_name= '')
        self.api.delete_worksheet_comments(request)


    def test_get_worksheet_merged_cells(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorksheetMergedCellsRequest( remote_name, 'Sheet1',folder= remote_folder,storage_name= '')
        self.api.get_worksheet_merged_cells(request)


    def test_get_worksheet_merged_cell(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorksheetMergedCellRequest( remote_name, 'Sheet1', 0,folder= remote_folder,storage_name= '')
        self.api.get_worksheet_merged_cell(request)


    def test_get_worksheet_calculate_formula(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorksheetCalculateFormulaRequest( remote_name, 'Sheet1', '=NOW()',folder= remote_folder,storage_name= '')
        self.api.get_worksheet_calculate_formula(request)


    def test_post_worksheet_calculate_formula(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorksheetCalculateFormulaRequest( remote_name, 'Sheet1', '=NOW()',folder= remote_folder,storage_name= '')
        self.api.post_worksheet_calculate_formula(request)


    def test_post_worksheet_text_search(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorksheetTextSearchRequest( remote_name, 'Sheet1', '123',folder= remote_folder,storage_name= '')
        self.api.post_worksheet_text_search(request)


    def test_post_worsheet_text_replace(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorsheetTextReplaceRequest( remote_name, 'Sheet1', '123', '456',folder= remote_folder,storage_name= '')
        self.api.post_worsheet_text_replace(request)


    def test_post_worksheet_range_sort(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        dataSorter = DataSorter(case_sensitive= True )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorksheetRangeSortRequest( remote_name, 'Sheet1', 'A1:C10', dataSorter,folder= remote_folder,storage_name= '')
        self.api.post_worksheet_range_sort(request)


    def test_post_autofit_worksheet_row(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostAutofitWorksheetRowRequest( remote_name, 'Sheet1', 1, 1, 8,folder= remote_folder,storage_name= '')
        self.api.post_autofit_worksheet_row(request)


    def test_post_autofit_worksheet_rows(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostAutofitWorksheetRowsRequest( remote_name, 'Sheet1',start_row= 1,end_row= 9,only_auto= True,folder= remote_folder,storage_name= '')
        self.api.post_autofit_worksheet_rows(request)


    def test_post_autofit_worksheet_columns(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostAutofitWorksheetColumnsRequest( remote_name, 'Sheet1',start_column= 1,end_column= 9,only_auto= True,folder= remote_folder,storage_name= '')
        self.api.post_autofit_worksheet_columns(request)


    def test_put_worksheet_background(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        water_mark_png = 'WaterMark.png'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
        result = AuthUtil.Ready(self.api, water_mark_png, remote_folder + '/WaterMark.png' ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutWorksheetBackgroundRequest( remote_name, 'Sheet1',pic_path= remote_folder + '/WaterMark.png',folder= remote_folder,storage_name= '')
        self.api.put_worksheet_background(request)


    def test_delete_worksheet_background(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  DeleteWorksheetBackgroundRequest( remote_name, 'Sheet1',folder= remote_folder,storage_name= '')
        self.api.delete_worksheet_background(request)


    def test_put_worksheet_freeze_panes(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutWorksheetFreezePanesRequest( remote_name, 'Sheet1', 1, 1, 4, 5,folder= remote_folder,storage_name= '')
        self.api.put_worksheet_freeze_panes(request)


    def test_delete_worksheet_freeze_panes(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  DeleteWorksheetFreezePanesRequest( remote_name, 'Sheet1', 1, 1, 4, 5,folder= remote_folder,storage_name= '')
        self.api.delete_worksheet_freeze_panes(request)


    def test_post_copy_worksheet(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        options = CopyOptions(column_character_width= True )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostCopyWorksheetRequest( remote_name, 'Sheet15', 'Sheet6', options,source_workbook= '',source_folder= '',folder= remote_folder,storage_name= '')
        self.api.post_copy_worksheet(request)


    def test_post_rename_worksheet(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostRenameWorksheetRequest( remote_name, 'Sheet5', 'Sheet55',folder= remote_folder,storage_name= '')
        self.api.post_rename_worksheet(request)


    def test_post_update_worksheet_property(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        sheet = Worksheet(name= 'sheet65' ,is_gridlines_visible= True )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostUpdateWorksheetPropertyRequest( remote_name, 'Sheet5', sheet,folder= remote_folder,storage_name= '')
        self.api.post_update_worksheet_property(request)


    def test_get_named_ranges(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetNamedRangesRequest( remote_name,folder= remote_folder,storage_name= '')
        self.api.get_named_ranges(request)


    def test_get_named_range_value(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetNamedRangeValueRequest( remote_name, 'Name_2',folder= remote_folder,storage_name= '')
        self.api.get_named_range_value(request)


    def test_post_update_worksheet_zoom(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostUpdateWorksheetZoomRequest( remote_name, 'Sheet1', 90,folder= remote_folder,storage_name= '')
        self.api.post_update_worksheet_zoom(request)


    def test_get_worksheet_page_count(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorksheetPageCountRequest( remote_name, 'Sheet1',folder= remote_folder,storage_name= '')
        self.api.get_worksheet_page_count(request)


if __name__ == '__main__':
    unittest.main()