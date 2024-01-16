import os
import sys
from asposecellscloud.apis.cells_api import CellsApi
from asposecellscloud.models import *
from asposecellscloud.requests import *

api  = CellsApi(os.getenv('CellsCloudClientId'),os.getenv('CellsCloudClientSecret'),"v3.0",os.getenv('CellsCloudApiBaseUrl'))
need_unlock_xlsx = 'needUnlock.xlsx'

mapFiles = { 
    need_unlock_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +need_unlock_xlsx             
}
 
request =  PostUnlockRequest( mapFiles, '123456')
api.post_unlock(request)
