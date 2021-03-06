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
        hyperlinkIndex = 0         
        folder = "Temp"
        hyperlink = Hyperlink()
        hyperlink.address = 'http://wwww.aspose.com'
        AuthUtil.Ready(name, folder)
        result = self.api.cells_hypelinks_post_worksheet_hyperlink(name, sheet_name, hyperlinkIndex , hyperlink = hyperlink , folder=folder)