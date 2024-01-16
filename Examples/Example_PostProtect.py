import os
import sys
from asposecellscloud.apis.cells_api import CellsApi
from asposecellscloud.models import *
from asposecellscloud.requests import *

api  = CellsApi(os.getenv('CellsCloudClientId'),os.getenv('CellsCloudClientSecret'),"v3.0",os.getenv('CellsCloudApiBaseUrl'))
assembly_test_xlsx = 'assemblytest.xlsx'
data_source_xlsx = 'datasource.xlsx'

mapFiles = { 
    assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
}
protectWorkbookRequest = ProtectWorkbookRequest(aways_open_read_only= True ,encrypt_with_password= '123456' )


 
request =  PostProtectRequest( mapFiles, protectWorkbookRequest,password= '123456')
api.post_protect(request)
