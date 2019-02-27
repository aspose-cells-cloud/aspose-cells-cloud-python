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
        sheet_name ='Sheet6'       
        picture = None
        upperLeftRow = 1   
        upperLeftColumn = 1   
        lowerRightRow = 10   
        lowerRightColumn = 10   
        picturePath = 'WaterMark.png'        
        folder = "Temp"
        AuthUtil.Ready(name, folder)
        result = self.api.cells_pictures_put_worksheet_add_picture(name, sheet_name, picture=picture, upper_left_row=upperLeftRow,upper_left_column=upperLeftColumn,lower_right_row=lowerRightRow,lower_right_column=lowerRightColumn,picture_path=picturePath, folder=folder)
