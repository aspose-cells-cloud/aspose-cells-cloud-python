import os
import sys
from asposecellscloud.apis.cells_api import CellsApi
from asposecellscloud.models import *
from asposecellscloud.requests import *

api  = CellsApi(os.getenv('CellsCloudClientId'),os.getenv('CellsCloudClientSecret'),"v3.0",os.getenv('CellsCloudApiBaseUrl'))
remote_folder = 'TestData/In'

local_name = 'Book1.xlsx'
report_data_xml = 'ReportData.xml'
remote_name = 'Book1.xlsx'

mapFiles = { 
    local_name:  local_name             
}
request =  UploadFileRequest( mapFiles, remote_folder + '/' + remote_name,storage_name= '')
api.upload_file(request)
mapFiles = { 
    local_name:  local_name             
}
request =  UploadFileRequest( mapFiles, remote_folder + '/' + remote_name,storage_name= '')
api.upload_file(request)
 
request =  PutWorkbookCreateRequest( 'PutWorkbookCreate.xlsx',template_file= remote_folder + '/' + remote_name,data_file= remote_folder + '/ReportData.xml',is_write_over= True,folder= remote_folder,storage_name= '',check_excel_restriction= True)
api.put_workbook_create(request)
