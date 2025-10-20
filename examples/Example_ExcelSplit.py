import base64
import os
import zipfile

from asposecellscloud.apis.cells_api import CellsApi
from asposecellscloud.models import *
from asposecellscloud.requests import *

EmployeeSalesSummaryXlsx = "EmployeeSalesSummary.xlsx"
CompanySalesXlsx = "CompanySales.xlsx"
# Get Cells Cloud SDK instance
# If no environment variables are configured, please obtain the ClientId and ClientSecret from https://dashboard.aspose.cloud/#/applications and replace the following values:
# instance  = CellsApi('YourClientId','YourClientSecret')
instance  = CellsApi(os.getenv('CellsCloudClientId'),os.getenv('CellsCloudClientSecret'))
instance.split_spreadsheet(SplitSpreadsheetRequest(EmployeeSalesSummaryXlsx),local_outpath ="split.zip")
with zipfile.ZipFile("split.zip",'r') as zip_ref:
    zip_ref.extractall(".")