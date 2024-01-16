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
 
request =  PutWorksheetChartRequest( remote_name, 'Sheet4', 'Pie',upper_left_row= 5,upper_left_column= 5,lower_right_row= 10,lower_right_column= 10,area= 'C7:D11',is_vertical= True,title= 'Aspose Chart',folder= remote_folder,storage_name= '')
api.put_worksheet_chart(request)
