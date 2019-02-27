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
        range = Range(column_count=1, column_width = 10.1, first_column = 1, first_row = 1, row_count = 10, row_height=10)
        folder = "Temp"
        AuthUtil.Ready(name, folder)
        result = self.api.cells_ranges_post_worksheet_cells_range_unmerge(name, sheet_name,range=range,folder=folder)