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
        filterIndex = 0
        needReCalculate = 'true'
        folder = "Temp"
        pivotFilter = PivotFilter()
        pivotFilter.field_index = 1
        pivotFilter.filter_type = "Count"
        
        filterColumn = FilterColumn(field_index = 0)
        filterColumn.filter_type = "Top10"
        top10filter = Top10Filter(is_percent = False, is_top = True, items = 1)
        filterColumn.top10_filter = top10filter

        autoFilter = AutoFilter()
        autoFilter.filter_columns = [filterColumn]
        pivotFilter.auto_filter = autoFilter

        AuthUtil.Ready(name, folder)
        result = self.api.cells_pivot_tables_put_worksheet_pivot_table_filter(name, sheet_name,pivotTableIndex, filter=pivotFilter, need_re_calculate=needReCalculate,folder=folder)
        result = self.api.cells_pivot_tables_get_worksheet_pivot_table_filter(name, sheet_name,pivotTableIndex, filterIndex, folder=folder)