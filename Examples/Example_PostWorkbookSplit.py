import os
import sys
from asposecellscloud.apis.cells_api import CellsApi
from asposecellscloud.models import *
from asposecellscloud.requests import *

api  = CellsApi(os.getenv('CellsCloudClientId'),os.getenv('CellsCloudClientSecret'),"v3.0",os.getenv('CellsCloudApiBaseUrl'))
remote_folder = 'TestData/In'

local_name = 'Book1.xlsx'
remote_name = 'Book1.xlsx'

mapFiles = { 
    local_name:  local_name             
}
request =  UploadFileRequest( mapFiles, remote_folder + '/' + remote_name,storage_name= '')
api.upload_file(request)
 
request =  PostWorkbookSplitRequest( remote_name,format= 'png',out_folder= 'OutResult',_from= 1,to= 5,horizontal_resolution= 96,vertical_resolution= 96,split_name_rule= 'sheetname',folder= remote_folder,storage_name= '',out_storage_name= '')
api.post_workbook_split(request)
