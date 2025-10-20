import base64
import os

from asposecellscloud.apis.cells_api import CellsApi
from asposecellscloud.models import *
from asposecellscloud.requests import *

# If no environment variables are configured, please obtain the ClientId and ClientSecret from https://dashboard.aspose.cloud/#/applications and replace the following values:
# instance  = CellsApi('YourClientId','YourClientSecret')
instance  = CellsApi(os.getenv('CellsCloudClientId'),os.getenv('CellsCloudClientSecret'))
# Remove all blank columns of BookText.xlsx, save as TempBookText.xlsx
instance.remove_spreadsheet_blank_columns(RemoveSpreadsheetBlankColumnsRequest("BookText.xlsx"),local_outpath = "TempBookText.xlsx")
# Remove all blank rows of TmpBookText.xlsx, save it.
instance.remove_spreadsheet_blank_rows(RemoveSpreadsheetBlankRowsRequest("TempBookText.xlsx"),local_outpath = "TempBookText.xlsx")
# Remove all blank worksheets of TempBookText.xlsx, save it.
instance.remove_spreadsheet_blank_worksheets(RemoveSpreadsheetBlankWorksheetsRequest("TempBookText.xlsx"),local_outpath = "TempBookText.xlsx")
# Remove all duplicates of TempBookText.xlsx, save it.
instance.remove_duplicates(RemoveDuplicatesRequest("TempBookText.xlsx"),local_outpath = "TempBookText.xlsx")
