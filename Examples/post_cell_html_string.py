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
        sheet_name ='Sheet1'
        cellName = 'C1' 
        folder = "Temp"
        AuthUtil.Ready(name, folder)
        self.api.cells_post_set_cell_html_string(name, sheet_name, cellName,folder=folder)