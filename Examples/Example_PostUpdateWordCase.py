import os
import sys
from asposecellscloud.apis.cells_api import CellsApi
from asposecellscloud.models import *
from asposecellscloud.requests import *

api  = CellsApi(os.getenv('CellsCloudClientId'),os.getenv('CellsCloudClientSecret'),"v3.0",os.getenv('CellsCloudApiBaseUrl'))
remote_folder = 'TestData/In'

local_name = 'BookText.xlsx'
remote_name = 'BookText.xlsx'

wordCaseOptionsDataSource = DataSource(data_source_type= 'CloudFileSystem' ,data_path= 'BookText.xlsx' )
wordCaseOptionsScopeOptions = ScopeOptions(scope= 'EntireWorkbook' )
wordCaseOptions = WordCaseOptions(data_source= wordCaseOptionsDataSource ,word_case_type= 'None' ,scope_options= wordCaseOptionsScopeOptions )
mapFiles = { 
    local_name:  local_name             
}
request =  UploadFileRequest( mapFiles, remote_folder + '/' + remote_name,storage_name= '')
api.upload_file(request)
 
request =  PostUpdateWordCaseRequest( wordCaseOptions)
api.post_update_word_case(request)
