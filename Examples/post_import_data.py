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

        name ='Book1.xlsx'       
        folder = "Temp"
        data = ImportIntArrayOption()
        data.destination_worksheet = 'Sheet1'
        data.first_column = 1
        data.first_row = 3
        data.import_data_type = 'IntArray'
        data.is_vertical = True
        data.data = [1, 2, 3, 4]
        AuthUtil.Ready(name, folder)
        result = self.api.cells_workbook_post_import_data(name, importdata=data,  folder=folder)