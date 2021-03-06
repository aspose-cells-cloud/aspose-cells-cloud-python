import os
import sys

ABSPATH = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/..")
sys.path.append(ABSPATH)
import asposecellscloud
from asposecellscloud.rest import ApiException
from asposecellscloud.apis.cells_api import CellsApi
import AuthUtil
from asposecellscloud.models import CalculationOptions
from asposecellscloud.models import FontSetting
from asposecellscloud.models import Font
from asposecellscloud.models import Style


api_client = AuthUtil.GetApiClient()
api = asposecellscloud.apis.cells_api.CellsApi(api_client)
        name ='Book1.xlsx'
        sheet_name ='Sheet6'
        oleObjectIndex = 0  
        ole = OleObject()  
        ole.left = 10
        ole.right = 10
        ole.height = 90
        ole.width = 78
        folder = "Temp"
        AuthUtil.Ready(name, folder)
        result = self.api.cells_ole_objects_post_update_worksheet_ole_object(name, sheet_name,oleObjectIndex,ole=ole,folder=folder)