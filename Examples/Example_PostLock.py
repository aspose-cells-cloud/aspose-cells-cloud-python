import os
import sys
from asposecellscloud.apis.cells_api import CellsApi
from asposecellscloud.models import *
from asposecellscloud.requests import *

api  = CellsApi(os.getenv('CellsCloudClientId'),os.getenv('CellsCloudClientSecret'),"v3.0",os.getenv('CellsCloudApiBaseUrl'))
needlock_xlsx = 'needlock.xlsx'

mapFiles = { 
    needlock_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +needlock_xlsx             
}
 
request =  PostLockRequest( mapFiles, '123456')
api.post_lock(request)
