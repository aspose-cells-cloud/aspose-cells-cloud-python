import os
import shutil
import base64
from asposecellscloud.apis.cells_api import CellsApi
from asposecellscloud.models import *
from asposecellscloud.requests import *


EmployeeSalesSummaryXlsx = "EmployeeSalesSummary.xlsx"
RemoteFolder = "PythonSDK"
# Get Cells Cloud SDK instance
instance  = CellsApi(os.getenv('CellsCloudClientId'),os.getenv('CellsCloudClientSecret'))

# Upload a local Excel file to Cells Cloud Storage.
instance.upload_file( UploadFileRequest(EmployeeSalesSummaryXlsx, "PythonSDK/EmployeeSalesSummary.xlsx"))

request =  GetWorksheetChartRequest( EmployeeSalesSummaryXlsx, 'Sales', 0,format= 'png',folder= 'PythonSDK',storage_name= '')
tmp_path = instance.get_worksheet_chart(request)
shutil.move( tmp_path ,"EmployeeSalesSummary_Sales.png")