import os
import sys
from asposecellscloud.apis.cells_api import CellsApi
from asposecellscloud.models import *
from asposecellscloud.requests import *

api  = CellsApi(os.getenv('CellsCloudClientId'),os.getenv('CellsCloudClientSecret'),"v3.0",os.getenv('CellsCloudApiBaseUrl'))
remote_folder = 'TestData/In'

local_book1 = 'Book1.xlsx'
remote_book1 = 'Book1.xlsx'
local_my_doc = 'myDocument.xlsx'
remote_my_doc = 'myDocument.xlsx'

batchProtectRequestMatchCondition = MatchConditionRequest(regex_pattern= '(^Book)(.+)(xlsx$)' )
batchProtectRequest = BatchProtectRequest(source_folder= remote_folder ,protection_type= 'All' ,password= '123456' ,out_folder= 'OutResult' ,match_condition= batchProtectRequestMatchCondition )
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
 
request =  PostBatchProtectRequest( batchProtectRequest)
api.post_batch_protect(request)
