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
        name ='myDocument.xlsx'
        sheet_name ='Sheet3'
        chartType = 'Pie'  
        upperLeftRow = 5  
        upperLeftColumn = 5 
        lowerRightRow = 10 
        lowerRightColumn = 10 
        area =  "C7:D11" 
        isVertical = True  
        categoryData = None  
        isAutoGetSerialName = None  
        title = None  
        folder = "Temp"
        AuthUtil.Ready(name, folder)
        result = self.api.cells_charts_put_worksheet_add_chart(name, sheet_name, chartType , upper_left_row=upperLeftRow , upper_left_column=upperLeftColumn, lower_right_row=lowerRightRow, lower_right_column=lowerRightColumn, area=area, is_vertical=isVertical, category_data=categoryData,is_auto_get_serial_name=isAutoGetSerialName,title=title, folder=folder)