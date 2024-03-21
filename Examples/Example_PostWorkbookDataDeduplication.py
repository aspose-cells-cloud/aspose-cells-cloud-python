import os
import sys
from asposecellscloud.apis.cells_api import CellsApi
from asposecellscloud.models import *
from asposecellscloud.requests import *

api  = CellsApi(os.getenv('CellsCloudClientId'),os.getenv('CellsCloudClientSecret'),"v3.0",os.getenv('CellsCloudApiBaseUrl'))
remote_folder = 'TestData/In'

local_name = 'BookCsvDuplicateData.csv'
remote_name = 'BookCsvDuplicateData.csv'

deduplicationRegion = DeduplicationRegion()
mapFiles = { 
    local_name:  local_name             
}
request =  UploadFileRequest( mapFiles, remote_folder + '/' + remote_name,storage_name= '')
api.upload_file(request)
 
request =  PostWorkbookDataDeduplicationRequest( remote_name, deduplicationRegion,folder= remote_folder,storage_name= '')
api.post_workbook_data_deduplication(request)
