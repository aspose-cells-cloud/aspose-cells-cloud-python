import os
import sys
from asposecellscloud.apis.cells_api import CellsApi
from asposecellscloud.models import *
from asposecellscloud.requests import *

api  = CellsApi(os.getenv('CellsCloudClientId'),os.getenv('CellsCloudClientSecret'),"v3.0",os.getenv('CellsCloudApiBaseUrl'))
data_source_xlsx = 'datasource.xlsx'

compress_level = 50

mapFiles = { 
    data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
}
 
request =  PostCompressRequest( mapFiles,compress_level= compress_level)
api.post_compress(request)
