import base64
import os
import shutil

from asposecellscloud.apis.cells_api import CellsApi
from asposecellscloud.models import *
from asposecellscloud.requests import *

EmployeeSalesSummaryXlsx = "EmployeeSalesSummary.xlsx"
RemoteFolder = "PythonSDK"
# Get Cells Cloud SDK instance
# If no environment variables are configured, please obtain the ClientId and ClientSecret from https://dashboard.aspose.cloud/#/applications and replace the following values:
# instance  = CellsApi('YourClientId','YourClientSecret')
instance  = CellsApi(os.getenv('CellsCloudTestClientId'),os.getenv('CellsCloudTestClientSecret'))

# Upload a local Excel file to Cells Cloud Storage.
instance.upload_file( UploadFileRequest(EmployeeSalesSummaryXlsx, "PythonSDK/EmployeeSalesSummary.xlsx"))

#Save an Excel file of Cells Cloud as another format file of Cells Cloud.
instance.save_spreadsheet_as( SaveSpreadsheetAsRequest ( EmployeeSalesSummaryXlsx,"pdf" ,folder= RemoteFolder ) )
instance.download_file( DownloadFileRequest("PythonSDK/EmployeeSalesSummary.pdf") , local_outpath="EmployeeSalesSummary3.pdf")
