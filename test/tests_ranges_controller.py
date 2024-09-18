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

class TestRangesControllerApi(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        global global_api
        if global_api is None:
           global_api = CellsApi(AuthUtil.GetClientId(),AuthUtil.GetClientSecret(),"v3.0",AuthUtil.GetBaseUrl())
        self.api = global_api

    def tearDown(self):
        pass

    def test_post_worksheet_cells_ranges_copy(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        rangeOperateSource = Range(column_count= 1 ,column_width= 10.0 ,first_row= 1 ,row_count= 10 )
        rangeOperateTarget = Range(column_count= 1 ,column_width= 10.0 ,first_row= 10 ,row_count= 10 )
        rangeOperate = RangeCopyRequest(operate= 'copydata' ,source= rangeOperateSource ,target= rangeOperateTarget )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorksheetCellsRangesCopyRequest( remote_name, 'Sheet1', rangeOperate,folder= remote_folder,storage_name= '')
        self.api.post_worksheet_cells_ranges_copy(request)

    def test_post_worksheet_cells_range_merge(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        range = Range(column_count= 1 ,column_width= 10.0 ,first_row= 1 ,row_count= 10 )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorksheetCellsRangeMergeRequest( remote_name, 'Sheet1', range,folder= remote_folder,storage_name= '')
        self.api.post_worksheet_cells_range_merge(request)

    def test_post_worksheet_cells_range_un_merge(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        range = Range(column_count= 1 ,column_width= 10.0 ,first_row= 1 ,row_count= 10 )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorksheetCellsRangeUnMergeRequest( remote_name, 'Sheet1', range,folder= remote_folder,storage_name= '')
        self.api.post_worksheet_cells_range_un_merge(request)

    def test_post_worksheet_cells_range_style(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        rangeOperateStyleFont = Font(size= 16 )
        rangeOperateStyle = Style(font= rangeOperateStyleFont )
        rangeOperateRange = Range(column_count= 1 ,column_width= 10.0 ,first_row= 1 ,row_count= 10 )
        rangeOperate = RangeSetStyleRequest(style= rangeOperateStyle ,range= rangeOperateRange )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorksheetCellsRangeStyleRequest( remote_name, 'Sheet1', rangeOperate,folder= remote_folder,storage_name= '')
        self.api.post_worksheet_cells_range_style(request)

    def test_get_worksheet_cells_range_value(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorksheetCellsRangeValueRequest( remote_name, 'Sheet1',namerange= 'Name_2',first_row= 0,first_column= 0,row_count= 3,column_count= 2,folder= remote_folder,storage_name= '')
        self.api.get_worksheet_cells_range_value(request)

    def test_post_worksheet_cells_range_value(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        range = Range(column_count= 1 ,column_width= 10.0 ,first_row= 1 ,row_count= 10 )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorksheetCellsRangeValueRequest( remote_name, 'Sheet1', range, '100',is_converted= True,set_style= True,folder= remote_folder,storage_name= '')
        self.api.post_worksheet_cells_range_value(request)

    def test_post_worksheet_cells_range_move_to(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        range = Range(column_count= 1 ,column_width= 10.0 ,first_row= 1 ,row_count= 10 )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorksheetCellsRangeMoveToRequest( remote_name, 'Sheet1', range, 10, 10,folder= remote_folder,storage_name= '')
        self.api.post_worksheet_cells_range_move_to(request)

    def test_post_worksheet_cells_range_outline_border(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        rangeOperateborderColor = Color(r= 48 ,g= 48 ,b= 48 )
        rangeOperateRange = Range(column_count= 1 ,column_width= 10.0 ,first_row= 1 ,row_count= 10 )
        rangeOperate = RangeSetOutlineBorderRequest(border_edge= 'LeftBorder' ,border_style= 'Dotted' ,border_color= rangeOperateborderColor ,range= rangeOperateRange )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorksheetCellsRangeOutlineBorderRequest( remote_name, 'Sheet1', rangeOperate,folder= remote_folder,storage_name= '')
        self.api.post_worksheet_cells_range_outline_border(request)

    def test_post_worksheet_cells_range_column_width(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        range = Range(column_count= 1 ,column_width= 10.0 ,first_row= 1 ,row_count= 10 )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorksheetCellsRangeColumnWidthRequest( remote_name, 'Sheet1', range, 10.7,folder= remote_folder,storage_name= '')
        self.api.post_worksheet_cells_range_column_width(request)

    def test_post_worksheet_cells_range_row_height(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        range = Range(column_count= 1 ,column_width= 10.0 ,first_row= 1 ,row_count= 10 )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorksheetCellsRangeRowHeightRequest( remote_name, 'Sheet1', range, 10.9,folder= remote_folder,storage_name= '')
        self.api.post_worksheet_cells_range_row_height(request)

    def test_put_worksheet_cells_range(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutWorksheetCellsRangeRequest( remote_name, 'Sheet1', 'A1:C6', 'Down',folder= remote_folder,storage_name= '')
        self.api.put_worksheet_cells_range(request)

    def test_delete_worksheet_cells_range(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  DeleteWorksheetCellsRangeRequest( remote_name, 'Sheet1', 'A1:C6', 'Up',folder= remote_folder,storage_name= '')
        self.api.delete_worksheet_cells_range(request)

    def test_post_worksheet_cells_range_sort(self):
        remote_folder = 'TestData/In'

        local_name = 'Group.xlsx'
        remote_name = 'Group.xlsx'

        rangeSortRequestDataSorter = DataSorter(case_sensitive= True )
        rangeSortRequestCellArea = Range(column_count= 3 ,first_column= 0 ,first_row= 0 ,row_count= 15 )
        rangeSortRequest = RangeSortRequest(data_sorter= rangeSortRequestDataSorter ,cell_area= rangeSortRequestCellArea )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorksheetCellsRangeSortRequest( remote_name, 'book1', rangeSortRequest,folder= remote_folder,storage_name= '')
        self.api.post_worksheet_cells_range_sort(request)

if __name__ == '__main__':
    unittest.main()