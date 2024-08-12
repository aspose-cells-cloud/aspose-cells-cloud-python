import os
import sys
from asposecellscloud.apis.cells_api import CellsApi
from asposecellscloud.models import *
from asposecellscloud.requests import *

api  = CellsApi(os.getenv('CellsCloudClientId'),os.getenv('CellsCloudClientSecret'),"v3.0",os.getenv('CellsCloudApiBaseUrl'))
remote_folder = 'TestData/In'

local_name = 'BookText.xlsx'
remote_name = 'BookText.xlsx'

trimContentOptionsDataSource = DataSource(data_source_type= 'CloudFileSystem' ,data_path= 'BookText.xlsx' )
trimContentOptionsScopeOptions = ScopeOptions(scope= 'EntireWorkbook' )
trimContentOptions = TrimContentOptions(data_source= trimContentOptionsDataSource ,trim_leading= True ,trim_trailing= True ,trim_space_between_word_to1= True ,remove_all_line_breaks= True ,scope_options= trimContentOptionsScopeOptions )
mapFiles = { 
    local_name:  local_name             
}
request =  UploadFileRequest( mapFiles, remote_folder + '/' + remote_name,storage_name= '')
api.upload_file(request)
 
request =  PostTrimContentRequest( trimContentOptions)
api.post_trim_content(request)
