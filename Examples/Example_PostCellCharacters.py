import os
import sys
from asposecellscloud.apis.cells_api import CellsApi
from asposecellscloud.models import *
from asposecellscloud.requests import *

api  = CellsApi(os.getenv('CellsCloudClientId'),os.getenv('CellsCloudClientSecret'),"v3.0",os.getenv('CellsCloudApiBaseUrl'))
remote_folder = 'TestData/In'

local_name = 'Book1.xlsx'
remote_name = 'Book1.xlsx'

optionsvalue0Font = Font(is_bold= True ,size= 16 )
optionsvalue0 = FontSetting(length= 5 ,start_index= 0 ,font= optionsvalue0Font )
options = [
    optionsvalue0
]
mapFiles = { 
    local_name:  local_name             
}
request =  UploadFileRequest( mapFiles, remote_folder + '/' + remote_name,storage_name= '')
api.upload_file(request)
 
request =  PostCellCharactersRequest( remote_name, 'Sheet1', 'E36',options= options,folder= remote_folder,storage_name= '')
api.post_cell_characters(request)
