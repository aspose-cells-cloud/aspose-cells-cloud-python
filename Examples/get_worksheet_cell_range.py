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
        folder = "Temp"
        AuthUtil.Ready(name, folder)
        firstRow = 0
        firstColumn = 0
        rowCount = 3
        columnCount = 2
        response = self.api.cells_ranges_get_worksheet_cells_range_value(name, sheet_name, first_row=firstRow, first_column=firstColumn, row_count=rowCount, column_count=columnCount, folder=folder)
        assert(len(response.cells_list) > 0)

        range_name = "A1:B3"
        response = self.api.cells_ranges_get_worksheet_cells_range_value(name, sheet_name, namerange=range_name, folder=folder)
        assert(len(response.cells_list) > 0)

        range_name = "Name_2"
        response = self.api.cells_ranges_get_worksheet_cells_range_value(name, sheet_name, namerange=range_name, folder=folder