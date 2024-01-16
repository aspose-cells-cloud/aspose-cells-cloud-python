import os
import sys
from asposecellscloud.apis.cells_api import CellsApi
from asposecellscloud.models import *
from asposecellscloud.requests import *

api  = CellsApi(os.getenv('CellsCloudClientId'),os.getenv('CellsCloudClientSecret'),"v3.0",os.getenv('CellsCloudApiBaseUrl'))
remote_folder = 'TestData/In'

local_name = 'Group.xlsx'
remote_name = 'Group.xlsx'

rangeSortRequestDataSorter = DataSorter(case_sensitive= True )
rangeSortRequestCellArea = Range(column_count= 3 ,first_column= 0 ,first_row= 0 ,row_count= 15 )
rangeSortRequest = RangeSortRequest(data_sorter= rangeSortRequestDataSorter ,cell_area= rangeSortRequestCellArea )
mapFiles = { 
    local_name:  local_name             
}
request =  UploadFileRequest( mapFiles, remote_folder + '/' + remote_name,storage_name= '')
api.upload_file(request)
 
request =  PostWorksheetCellsRangeSortRequest( remote_name, 'book1', rangeSortRequest,folder= remote_folder,storage_name= '')
api.post_worksheet_cells_range_sort(request)
