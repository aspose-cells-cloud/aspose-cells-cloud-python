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
        request = CreatePivotTableRequest(use_same_source=True)
        request.name = "TestPivot"
        request.dest_cell_name = "C1"
        request.source_data = "Sheet1!C6:E13"
        sourceData = "Sheet1!C6:E13"
        destCellName = "C1"
        tableName = "TestPivot"
        useSameSource = 'true'
        folder = "Temp"
        AuthUtil.Ready(name, folder)
        result = self.api.cells_pivot_tables_put_worksheet_pivot_table(name, sheet_name, request=None, folder=folder,source_data=sourceData,dest_cell_name=destCellName,table_name=tableName,use_same_source=useSameSource)