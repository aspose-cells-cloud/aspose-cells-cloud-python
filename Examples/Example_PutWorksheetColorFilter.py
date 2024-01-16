import os
import sys
from asposecellscloud.apis.cells_api import CellsApi
from asposecellscloud.models import *
from asposecellscloud.requests import *

api  = CellsApi(os.getenv('CellsCloudClientId'),os.getenv('CellsCloudClientSecret'),"v3.0",os.getenv('CellsCloudApiBaseUrl'))
remote_folder = 'TestData/In'

local_name = 'Book1.xlsx'
remote_name = 'Book1.xlsx'

colorFilterForegroundColorColor = Color(r= 48 ,g= 48 ,b= 48 )
colorFilterForegroundColor = CellsColor(type= 'Automatic' ,color= colorFilterForegroundColorColor )
colorFilter = ColorFilterRequest(pattern= 'Solid' ,foreground_color= colorFilterForegroundColor )
mapFiles = { 
    local_name:  local_name             
}
request =  UploadFileRequest( mapFiles, remote_folder + '/' + remote_name,storage_name= '')
api.upload_file(request)
 
request =  PutWorksheetColorFilterRequest( remote_name, 'Sheet1', 'A1:B1', 0, colorFilter,match_blanks= True,refresh= True,folder= remote_folder,storage_name= '')
api.put_worksheet_color_filter(request)
