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
        sheet_name ='Sheet1'
        fieldIndex = 0  
        criteria ="Day"       
        folder = "Temp"
        AuthUtil.Ready(name, folder)
        result = self.api.cells_auto_filter_delete_worksheet_filter(name, sheet_name,fieldIndex, criteria=criteria,folder=folder)
