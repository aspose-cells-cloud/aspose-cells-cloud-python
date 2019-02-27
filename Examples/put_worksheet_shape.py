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
        drawingType= "button"  
        upperLeftRow=1 
        upperLeftColumn= 1 
        top=10
        left= 10
        width= 100 
        height= 90 
        folder = "Temp"
        AuthUtil.Ready(name, folder)
        result = self.api.cells_shapes_put_worksheet_shape(name, sheet_name, drawingType,upperLeftRow,upperLeftColumn, top, left, width, height,folder=folder)