import os
import sys
from asposecellscloud.apis.cells_api import CellsApi
from asposecellscloud.models import *
from asposecellscloud.requests import *

api  = CellsApi(os.getenv('CellsCloudClientId'),os.getenv('CellsCloudClientSecret'),"v3.0",os.getenv('CellsCloudApiBaseUrl'))
remote_folder = 'TestData/In'

local_name = 'Book1.xlsx'
remote_name = 'Book1.xlsx'

rangeOperateborderColor = Color(r= 48 ,g= 48 ,b= 48 )
rangeOperateRange = Range(column_count= 1 ,column_width= 10.0 ,first_row= 1 ,row_count= 10 )
rangeOperate = RangeSetOutlineBorderRequest(border_edge= 'LeftBorder' ,border_style= 'Dotted' ,border_color= rangeOperateborderColor ,range= rangeOperateRange )
mapFiles = { 
    local_name:  local_name             
}
request =  UploadFileRequest( mapFiles, remote_folder + '/' + remote_name,storage_name= '')
api.upload_file(request)
 
request =  PostWorksheetCellsRangeOutlineBorderRequest( remote_name, 'Sheet1', rangeOperate,folder= remote_folder,storage_name= '')
api.post_worksheet_cells_range_outline_border(request)
