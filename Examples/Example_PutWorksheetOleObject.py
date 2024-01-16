import os
import sys
from asposecellscloud.apis.cells_api import CellsApi
from asposecellscloud.models import *
from asposecellscloud.requests import *

api  = CellsApi(os.getenv('CellsCloudClientId'),os.getenv('CellsCloudClientSecret'),"v3.0",os.getenv('CellsCloudApiBaseUrl'))
remote_folder = 'TestData/In'

local_name = 'Book1.xlsx'
ole_doc = 'OLEDoc.docx'
word_jpg = 'word.jpg'
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
mapFiles = { 
    local_name:  local_name             
}
request =  UploadFileRequest( mapFiles, remote_folder + '/' + remote_name,storage_name= '')
api.upload_file(request)
 
request =  PutWorksheetOleObjectRequest( remote_name, 'Sheet6',upper_left_row= 1,upper_left_column= 1,height= 100,width= 80,ole_file= 'OLEDoc.docx',image_file= 'word.jpg',folder= remote_folder,storage_name= '')
api.put_worksheet_ole_object(request)
