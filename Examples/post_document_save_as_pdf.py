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
        saveOptions = PdfSaveOptions()
        saveOptions.OnePagePerSheet = True
        saveOptions.SaveFormat = "pdf"
        newfilename = "newbook.pdf"
        isAutoFitRows= True
        isAutoFitColumns= True
        folder = "Temp"
        AuthUtil.Ready(name, folder)
        result = self.api.cells_save_as_post_document_save_as(name, save_options=saveOptions, newfilename=newfilename,is_auto_fit_rows=isAutoFitRows, is_auto_fit_columns=isAutoFitColumns,folder=folder)