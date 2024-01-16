import os
import sys
from asposecellscloud.apis.cells_api import CellsApi
from asposecellscloud.models import *
from asposecellscloud.requests import *

api  = CellsApi(os.getenv('CellsCloudClientId'),os.getenv('CellsCloudClientSecret'),"v3.0",os.getenv('CellsCloudApiBaseUrl'))
assembly_test_xlsx = 'assemblytest.xlsx'
data_source_xlsx = 'datasource.xlsx'

out_format = 'csv'

mapFiles = { 
    assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
}
 
request =  PostSplitRequest( mapFiles, out_format)
api.post_split(request)
