import os
import sys
from asposecellscloud.apis.cells_api import CellsApi
from asposecellscloud.models import *
from asposecellscloud.requests import *

api  = CellsApi(os.getenv('CellsCloudClientId'),os.getenv('CellsCloudClientSecret'),"v3.0",os.getenv('CellsCloudApiBaseUrl'))
data_source_xlsx = 'datasource.xlsx'

mapFiles = { 
    data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
}
 
request =  PostReplaceRequest( mapFiles, '12', 'newtext')
api.post_replace(request)
