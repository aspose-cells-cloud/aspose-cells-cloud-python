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
        folder = "Temp"
        format = "png"
        _from = 1
        to = 3
        horizontalResolution = 100
        verticalResolution = 90
        AuthUtil.Ready(name, folder)
        result = self.api.cells_workbook_post_workbook_split(name, format=format, _from=_from, to=to, horizontal_resolution=horizontalResolution, vertical_resolution=verticalResolution,  folder=folder)