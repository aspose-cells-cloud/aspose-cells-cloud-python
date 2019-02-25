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
        rangeOperate = RangeCopyRequest()
        rangeOperate.operate = "copydata"
        pasteOptions = PasteOptions()
        pasteOptions.only_visible_cells = True
        rangeOperate.paste_options = pasteOptions
        range = Range(column_count=1, column_width = 10.1, first_column = 1, first_row = 1, row_count = 10, row_height=10)
        range2 = Range(column_count=1, column_width = 10.1, first_column = 10, first_row = 10, row_count = 10, row_height=10)
        rangeOperate.source = range
        rangeOperate.target = range2
        folder = "Temp"
        AuthUtil.Ready(name, folder)
        result = self.api.cells_ranges_post_worksheet_cells_ranges(name, sheet_name, range_operate=rangeOperate,folder=folder)