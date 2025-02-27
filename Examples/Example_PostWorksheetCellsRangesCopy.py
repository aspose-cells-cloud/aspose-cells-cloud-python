import os
import sys
from asposecellscloud.apis.cells_api import CellsApi
from asposecellscloud.models import *
from asposecellscloud.requests import *

api  = CellsApi(os.getenv('CellsCloudClientId'),os.getenv('CellsCloudClientSecret'),"v3.0",os.getenv('CellsCloudApiBaseUrl'))
remote_folder = 'TestData/In'

local_name = 'Book1.xlsx'
remote_name = 'Book1.xlsx'

rangeOperateSource = Range(column_count= 3 ,first_column= 8 ,first_row= 3 ,row_count= 2 )
rangeOperateTarget = Range(column_count= 3 ,first_column= 8 ,first_row= 13 ,row_count= 2 )
rangeOperate = RangeCopyRequest(operate= 'copydata' ,source= rangeOperateSource ,target= rangeOperateTarget )
mapFiles = { 
    local_name:  local_name             
}
request =  UploadFileRequest( mapFiles, remote_folder + '/' + remote_name,storage_name= '')
api.upload_file(request)
 
request =  PostWorksheetCellsRangesCopyRequest( remote_name, 'Sheet1', rangeOperate,folder= remote_folder,storage_name= '')
api.post_worksheet_cells_ranges_copy(request)
