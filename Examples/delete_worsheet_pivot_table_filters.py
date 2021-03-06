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
        name ='TestCase.xlsx'
        sheet_name ='Sheet4'
        pivotTableIndex = 0
        fieldIndex = 0
        needReCalculate = True
        folder = "Temp"
        AuthUtil.Ready(name, folder)
        result = self.api.cells_pivot_tables_delete_worksheet_pivot_table_filters(name, sheet_name,pivotTableIndex,need_re_calculate=needReCalculate, folder=folder)