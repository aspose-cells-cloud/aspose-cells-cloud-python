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
# cells_cloud  = CellsApi('YourClientId','YourClientSecret')
cells_cloud  = CellsApi(os.getenv('CellsCloudTestClientId'),os.getenv('CellsCloudTestClientSecret'))

# Create blank spreadsheet
cells_cloud.create_spreadsheet( CreateSpreadsheetRequest( format="xlsb"),local_outpath ="blank_spreadsheet.xlsb" )
# Create template spreadsheet
cells_cloud.create_spreadsheet( CreateSpreadsheetRequest( format="xlsb" , template="SalesDataComparisonXLSX"),local_outpath ="SalesDataComparison.xlsb" )
# Add worksheet into spreadsheet
cells_cloud.add_worksheet_to_spreadsheet( 
    AddWorksheetToSpreadsheetRequest( spreadsheet= EmployeeSalesSummaryXlsx ,position=0,sheet_name= "NewSalesData"  ),
    local_outpath = "EmployeeSalesSummary_AddNewSalesData.xlsx"  )
# Worksheet rename
cells_cloud.rename_worksheet_in_spreadsheet( 
    RenameWorksheetInSpreadsheetRequest(spreadsheet="EmployeeSalesSummary_AddNewSalesData.xlsx" , source_name="NewSalesData" ,target_name="2025SalesData" ),
    local_outpath = "EmployeeSalesSummary_RenameNewSalesData.xlsx"  )
# Move worksheet position.
cells_cloud.move_worksheet_in_spreadsheet( 
    MoveWorksheetInSpreadsheetRequest(spreadsheet="EmployeeSalesSummary_RenameNewSalesData.xlsx", worksheet="2025SalesData", position=2),
    local_outpath = "EmployeeSalesSummary_MoveNewSalesData.xlsx")
#Deletge worksheet.
cells_cloud.delete_worksheet_from_spreadsheet( 
    DeleteWorksheetFromSpreadsheetRequest(spreadsheet= "EmployeeSalesSummary_RenameNewSalesData.xlsx"  , sheet_name="2025SalesData" ),
    local_outpath = "EmployeeSalesSummary_DeleteNewSalesData.xlsx" ) 
