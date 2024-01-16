import os
import sys
from asposecellscloud.apis.cells_api import CellsApi
from asposecellscloud.models import *
from asposecellscloud.requests import *

api  = CellsApi(os.getenv('CellsCloudClientId'),os.getenv('CellsCloudClientSecret'),"v3.0",os.getenv('CellsCloudApiBaseUrl'))
remote_folder = 'TestData/In'

local_name = 'Book1.xlsx'
remote_name = 'Book1.xlsx'

createPivotTableRequestPivotFieldColumns = [
    2
]
createPivotTableRequestPivotFieldData = [
    1
]
createPivotTableRequestPivotFieldRows = [
    0
]
createPivotTableRequest = CreatePivotTableRequest(dest_cell_name= 'C1' ,name= 'testp' ,source_data= '=Sheet2!A1:E8' ,use_same_source= True ,pivot_field_columns= createPivotTableRequestPivotFieldColumns ,pivot_field_data= createPivotTableRequestPivotFieldData ,pivot_field_rows= createPivotTableRequestPivotFieldRows )
mapFiles = { 
    local_name:  local_name             
}
request =  UploadFileRequest( mapFiles, remote_folder + '/' + remote_name,storage_name= '')
api.upload_file(request)
 
request =  PostWorksheetListObjectSummarizeWithPivotTableRequest( remote_name, 'Sheet7', 0, 'Sheet2', createPivotTableRequest,folder= remote_folder,storage_name= '')
api.post_worksheet_list_object_summarize_with_pivot_table(request)
