import os
import sys
from asposecellscloud.apis.cells_api import CellsApi
from asposecellscloud.models import *
from asposecellscloud.requests import *

api  = CellsApi(os.getenv('CellsCloudClientId'),os.getenv('CellsCloudClientSecret'),"v3.0",os.getenv('CellsCloudApiBaseUrl'))
remote_folder = 'TestData/In'

local_name = 'TestCase.xlsx'
remote_name = 'TestCase.xlsx'

mapFiles = { 
    local_name:  local_name             
}
request =  UploadFileRequest( mapFiles, remote_folder + '/' + remote_name,storage_name= '')
api.upload_file(request)
 
request =  PutWorksheetPivotTableRequest( remote_name, 'Sheet4',folder= remote_folder,source_data= '=Sheet1!C6:E13',dest_cell_name= 'C1',table_name= 'TestPivot',use_same_source= True,storage_name= '')
api.put_worksheet_pivot_table(request)