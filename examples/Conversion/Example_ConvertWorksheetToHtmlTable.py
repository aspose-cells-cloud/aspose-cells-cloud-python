import json
import os

from asposecellscloud.apis.cells_api import CellsApi
from asposecellscloud.models import *
from asposecellscloud.requests import *

# Get Cells Cloud SDK instance
# If no environment variables are configured, please obtain the ClientId and ClientSecret from https://dashboard.aspose.cloud/#/applications and replace the following values:
# instance  = CellsApi('YourClientId','YourClientSecret')
instance  = CellsApi(os.getenv('CellsCloudClientId'),os.getenv('CellsCloudClientSecret'))

# How to get all worksheet names from spreadsheet.
# Upload a local Excel file to Cells Cloud Storage.
instance.upload_file( UploadFileRequest("EmployeeSalesSummary.Xlsx", "PythonSDK/EmployeeSalesSummary.xlsx"))
# Get worksheet collection description with workbook
response = instance.get_worksheets( GetWorksheetsRequest ("EmployeeSalesSummary.xlsx",folder = "PythonSDK") )
# json data about worksheet collection description.
for link in response.worksheets.worksheet_list:
    # print worksheet name
    print (link.link.href[1:])
    # convert worksheet to HTML table.
    response = instance.convert_worksheet_to_html_table( ConvertWorksheetToHtmlTableRequest( "EmployeeSalesSummary.xlsx", link.link.href[1:])  )
    with open(response, "r", encoding="utf-8") as f:
        content = f.read()
        with open(f"EmployeeSalesSummaryToHtmlTable_{link.link.href[1:]}.html", "w") as file:
            file.write(content)
