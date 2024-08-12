import os
import sys
from asposecellscloud.apis.cells_api import CellsApi
from asposecellscloud.models import *
from asposecellscloud.requests import *

api  = CellsApi(os.getenv('CellsCloudClientId'),os.getenv('CellsCloudClientSecret'),"v3.0",os.getenv('CellsCloudApiBaseUrl'))
remote_folder = 'TestData/In'

local_name = 'BookText.xlsx'
remote_name = 'BookText.xlsx'

addTextOptionsDataSource = DataSource(data_source_type= 'CloudFileSystem' ,data_path= 'BookText.xlsx' )
addTextOptions = AddTextOptions(data_source= addTextOptionsDataSource ,text= 'Aspose.Cells Cloud is an excellent product.' ,worksheet= '202401' ,select_poistion= 'AtTheBeginning' ,skip_empty_cells= True )
mapFiles = { 
    local_name:  local_name             
}
request =  UploadFileRequest( mapFiles, remote_folder + '/' + remote_name,storage_name= '')
api.upload_file(request)
 
request =  PostAddTextContentRequest( addTextOptions)
api.post_add_text_content(request)
