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
        cellname = 'A1'     
        row = 1  
        column = 1  
        startColumn = 1  
        endColumn = 1      
        folder = "Temp"
        AuthUtil.Ready(name, folder)
        result = self.api.cells_page_breaks_put_horizontal_page_break(name, sheet_name, cellname=cellname,row=row, column=column ,start_column=startColumn,end_column=endColumn,folder=folder)