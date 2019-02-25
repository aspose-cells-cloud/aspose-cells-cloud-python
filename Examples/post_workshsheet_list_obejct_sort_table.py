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
        sheet_name ='Sheet7'
        listObjectIndex = 0   
        dataSorter = DataSorter()
        dataSorter.case_sensitive = True
        folder = "Temp"
        AuthUtil.Ready(name, folder)
        result = self.api.cells_list_objects_post_worksheet_list_object_sort_table(name, sheet_name,listObjectIndex,data_sorter=dataSorter,folder=folder)