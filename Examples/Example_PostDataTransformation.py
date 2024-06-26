import os
import sys
from asposecellscloud.apis.cells_api import CellsApi
from asposecellscloud.models import *
from asposecellscloud.requests import *

api  = CellsApi(os.getenv('CellsCloudClientId'),os.getenv('CellsCloudClientSecret'),"v3.0",os.getenv('CellsCloudApiBaseUrl'))
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
mapFiles = { 
    local_name:  local_name             
}
request =  UploadFileRequest( mapFiles, remote_folder + '/' + remote_name,storage_name= '')
api.upload_file(request)
 
request =  PostDataTransformationRequest( dataTransformationRequest)
api.post_data_transformation(request)
