import os
import sys
from asposecellscloud.apis.cells_api import CellsApi
from asposecellscloud.models import *
from asposecellscloud.requests import *

api  = CellsApi(os.getenv('CellsCloudClientId'),os.getenv('CellsCloudClientSecret'),"v3.0",os.getenv('CellsCloudApiBaseUrl'))
book1_xlsx = 'Book1.xlsx'

out_format = 'csv'

mapFiles = { 
    book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
}
 
request =  PostSplitRequest( mapFiles, out_format)
api.post_split(request)
