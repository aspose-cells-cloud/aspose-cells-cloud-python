import os
import sys
from asposecellscloud.apis.cells_api import CellsApi
from asposecellscloud.models import *
from asposecellscloud.requests import *

api  = CellsApi(os.getenv('CellsCloudClientId'),os.getenv('CellsCloudClientSecret'),"v3.0",os.getenv('CellsCloudApiBaseUrl'))
book1_xlsx = 'Book1.xlsx'
data_source_xlsx = 'datasource.xlsx'

objecttype = 'chart'

mapFiles = { 
    book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
}
 
request =  PostClearObjectsRequest( mapFiles, objecttype)
api.post_clear_objects(request)
