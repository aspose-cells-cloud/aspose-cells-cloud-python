import os

from asposecellscloud.apis.cells_api import CellsApi
from asposecellscloud.requests import  *

# How to translate an entire Excel file to the specified language?
EmployeeSalesSummaryXlsx = "EmployeeSalesSummary.xlsx"
# Get Cells Cloud SDK instance
# If no environment variables are configured, please obtain the ClientId and ClientSecret from https://dashboard.aspose.cloud/#/applications and replace the following values:
# instance  = CellsApi('YourClientId','YourClientSecret')
instance  = CellsApi(os.getenv('CellsCloudClientId'),os.getenv('CellsCloudClientSecret'))
# Translate Excel files accurately into the specified language.
instance.convert_spreadsheet( ConvertSpreadsheetRequest(EmployeeSalesSummaryXlsx, "txt" ), local_outpath = "EmployeeSalesSummary.txt" )

instance.translation_spreadsheet(TranslationSpreadsheetRequest( "EmployeeSalesSummary.txt",target_language="zh" ) ,local_outpath = "EmployeeSalesSummary_zh.xlsx" )
