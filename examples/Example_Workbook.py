import json
import os

from asposecellscloud.apis.cells_api import CellsApi
from asposecellscloud.models import *
from asposecellscloud.requests import *

# Get Cells Cloud SDK instance
# If no environment variables are configured, please obtain the ClientId and ClientSecret from https://dashboard.aspose.cloud/#/applications and replace the following values:
# instance  = CellsApi('YourClientId','YourClientSecret')
instance  = CellsApi(os.getenv('CellsCloudClientId'),os.getenv('CellsCloudClientSecret'))

# Upload a local Excel file to Cells Cloud Storage.
instance.upload_file( UploadFileRequest("EmployeeSalesSummary.Xlsx", "PythonSDK/EmployeeSalesSummary.xlsx"))
#  Get workbook settings of 
response = instance.get_workbook_settings(GetWorkbookSettingsRequest("EmployeeSalesSummary.xlsx",folder = "PythonSDK"))
print(response.settings.build_version)
print(response.settings.author)
print(response.settings)