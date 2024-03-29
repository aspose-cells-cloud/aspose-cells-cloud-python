import os
import sys
from asposecellscloud.apis.cells_api import CellsApi
from asposecellscloud.models import *
from asposecellscloud.requests import *

api  = CellsApi(os.getenv('CellsCloudClientId'),os.getenv('CellsCloudClientSecret'),"v3.0",os.getenv('CellsCloudApiBaseUrl'))
assembly_test_xlsx = 'assemblytest.xlsx'
book1_xlsx = 'Book1.xlsx'

format = 'csv'
object_type = 'workbook'

mapFiles = { 
    assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
}
 
request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
api.post_export(request)
