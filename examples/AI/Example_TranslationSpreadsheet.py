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
#china
instance.translation_spreadsheet(TranslationSpreadsheetRequest( EmployeeSalesSummaryXlsx,target_language="zh" ) ,local_outpath = "EmployeeSalesSummary_zh.xlsx" )

#
instance.convert_spreadsheet( ConvertSpreadsheetRequest(EmployeeSalesSummaryXlsx, "ods" ), local_outpath = "EmployeeSalesSummary.ods" )
instance.translation_spreadsheet(TranslationSpreadsheetRequest( "EmployeeSalesSummary.ods",target_language="zh" ) ,local_outpath = "EmployeeSalesSummary_zh_2.ods" )

