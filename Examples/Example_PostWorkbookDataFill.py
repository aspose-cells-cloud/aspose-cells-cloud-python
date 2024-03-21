import os
import sys
from asposecellscloud.apis.cells_api import CellsApi
from asposecellscloud.models import *
from asposecellscloud.requests import *

api  = CellsApi(os.getenv('CellsCloudClientId'),os.getenv('CellsCloudClientSecret'),"v3.0",os.getenv('CellsCloudApiBaseUrl'))
remote_folder = 'TestData/In'

local_name = 'BookCsvDuplicateData.csv'
remote_name = 'BookCsvDuplicateData.csv'

dataFillDataFillDefaultValue = DataFillValue(default_date= '2024-01-01' ,default_number= 0 ,default_boolean= False )
dataFill = DataFill(data_fill_default_value= dataFillDataFillDefaultValue )
mapFiles = { 
    local_name:  local_name             
}
request =  UploadFileRequest( mapFiles, remote_folder + '/' + remote_name,storage_name= '')
api.upload_file(request)
 
request =  PostWorkbookDataFillRequest( remote_name, dataFill,folder= remote_folder,storage_name= '')
api.post_workbook_data_fill(request)
