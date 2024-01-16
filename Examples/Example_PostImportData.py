import os
import sys
from asposecellscloud.apis.cells_api import CellsApi
from asposecellscloud.models import *
from asposecellscloud.requests import *

api  = CellsApi(os.getenv('CellsCloudClientId'),os.getenv('CellsCloudClientSecret'),"v3.0",os.getenv('CellsCloudApiBaseUrl'))
remote_folder = 'TestData/In'

local_name = 'Book1.xlsx'
remote_name = 'Book1.xlsx'

importOptionData = [
    1,
    2,
    3,
    4
]
importOption = ImportIntArrayOption(destination_worksheet= 'Sheet1' ,first_column= 1 ,first_row= 3 ,import_data_type= 'IntArray' ,is_insert= True ,is_vertical= True ,data= importOptionData )
mapFiles = { 
    local_name:  local_name             
}
request =  UploadFileRequest( mapFiles, remote_folder + '/' + remote_name,storage_name= '')
api.upload_file(request)
 
request =  PostImportDataRequest( remote_name,import_option= importOption,folder= remote_folder,storage_name= '')
api.post_import_data(request)
