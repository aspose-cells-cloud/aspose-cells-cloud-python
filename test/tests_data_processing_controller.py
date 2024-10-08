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

class TestDataProcessingControllerApi(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        global global_api
        if global_api is None:
           global_api = CellsApi(AuthUtil.GetClientId(),AuthUtil.GetClientSecret(),"v3.0",AuthUtil.GetBaseUrl())
        self.api = global_api

    def tearDown(self):
        pass

    def test_post_workbook_data_cleansing(self):
        remote_folder = 'TestData/In'

        local_name = 'BookCsvDuplicateData.csv'
        remote_name = 'BookCsvDuplicateData.csv'

        dataCleansingDataFillDataFillDefaultValue = DataFillValue(default_date= '2024-01-01' ,default_number= 0 ,default_boolean= False )
        dataCleansingDataFill = DataFill(data_fill_default_value= dataCleansingDataFillDataFillDefaultValue )
        dataCleansing = DataCleansing(need_fill_data= True ,data_fill= dataCleansingDataFill )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorkbookDataCleansingRequest( remote_name, dataCleansing,folder= remote_folder,storage_name= '')
        self.api.post_workbook_data_cleansing(request)

    def test_post_workbook_data_deduplication(self):
        remote_folder = 'TestData/In'

        local_name = 'BookCsvDuplicateData.csv'
        remote_name = 'BookCsvDuplicateData.csv'

        deduplicationRegionRanges = [
        ]
        deduplicationRegion = DeduplicationRegion(ranges= deduplicationRegionRanges )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorkbookDataDeduplicationRequest( remote_name, deduplicationRegion,folder= remote_folder,storage_name= '')
        self.api.post_workbook_data_deduplication(request)

    def test_post_workbook_data_fill(self):
        remote_folder = 'TestData/In'

        local_name = 'BookCsvDuplicateData.csv'
        remote_name = 'BookCsvDuplicateData.csv'

        dataFillDataFillDefaultValue = DataFillValue(default_date= '2024-01-01' ,default_number= 0 ,default_boolean= False )
        dataFill = DataFill(data_fill_default_value= dataFillDataFillDefaultValue )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorkbookDataFillRequest( remote_name, dataFill,folder= remote_folder,storage_name= '')
        self.api.post_workbook_data_fill(request)

    def test_post_data_transformation(self):
        remote_folder = 'TestData/In'

        local_name = 'BookTableL2W.xlsx'
        remote_name = 'BookTableL2W.xlsx'

        dataTransformationRequestLoadDataLoadTo = LoadTo(begin_column_index= 2 ,begin_row_index= 3 ,worksheet= 'L2W' )
        dataTransformationRequestLoadDataDataQueryDataItem = DataItem(data_item_type= 'Table' ,value= 'Table1' )
        dataTransformationRequestLoadDataDataQueryDataSource = DataSource(data_source_type= 'CloudFileSystem' ,data_path= 'BookTableL2W.xlsx' )
        dataTransformationRequestLoadDataDataQuery = DataQuery(name= 'DataQuery' ,data_item= dataTransformationRequestLoadDataDataQueryDataItem ,data_source= dataTransformationRequestLoadDataDataQueryDataSource ,data_source_data_type= 'ListObject' )
        dataTransformationRequestLoadData = LoadData(load_to= dataTransformationRequestLoadDataLoadTo ,data_query= dataTransformationRequestLoadDataDataQuery )
        dataTransformationRequestAppliedStepsAppliedStep0AppliedOperateUnpivotColumnNames = [
            '2017',
            '2018',
            '2019'
        ]
        dataTransformationRequestAppliedStepsAppliedStep0AppliedOperate = UnpivotColumn(applied_operate_type= 'UnpivotColumn' ,value_map_name= 'Count' ,column_map_name= 'Date' ,unpivot_column_names= dataTransformationRequestAppliedStepsAppliedStep0AppliedOperateUnpivotColumnNames )
        dataTransformationRequestAppliedStepsAppliedStep0 = AppliedStep(step_name= 'UnpivotColumn' ,applied_operate= dataTransformationRequestAppliedStepsAppliedStep0AppliedOperate )
        dataTransformationRequestAppliedSteps = [
            dataTransformationRequestAppliedStepsAppliedStep0
        ]
        dataTransformationRequest = DataTransformationRequest(load_data= dataTransformationRequestLoadData ,applied_steps= dataTransformationRequestAppliedSteps )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostDataTransformationRequest( dataTransformationRequest)
        self.api.post_data_transformation(request)

if __name__ == '__main__':
    unittest.main()