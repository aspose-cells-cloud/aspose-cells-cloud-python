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
instance  = CellsApi(os.getenv('CellsCloudClientId'),os.getenv('CellsCloudClientSecret'))

# 1. Cells Cloud v3.0: Convert table to image
# 1.1. Upload a local Excel file to Cells Cloud Storage.
instance.upload_file( UploadFileRequest(EmployeeSalesSummaryXlsx, "PythonSDK/EmployeeSalesSummary.xlsx"))
# 1.2. Convert table to image
request = GetWorksheetListObjectRequest( name=EmployeeSalesSummaryXlsx,  sheet_name="SalesChartData",
                                                listobjectindex=0, format="svg", folder=RemoteFolder  )
tmp_path = instance.get_worksheet_list_object(request)
# 1.3. Save image to local file.
shutil.move( tmp_path ,"EmployeeSalesSummary_SalesChartData_v30.svg")

# 2. Cells Cloud V4.0: table range to image
# Convert a local Excel file's specified worksheet list object directly to another format file. Set query parameters
instance.convert_table_to_pdf( ConvertTableToPdfRequest( EmployeeSalesSummaryXlsx , "SalesChartData" , "Table1" ) , local_outpath="EmployeeSalesSummary_Sales_Table.pdf")
instance.convert_table_to_image( ConvertTableToImageRequest( EmployeeSalesSummaryXlsx , "SalesChartData" , "Table1" ,"png" ) , local_outpath="EmployeeSalesSummary_Sales_Table.png")
instance.convert_table_to_image( ConvertTableToImageRequest( EmployeeSalesSummaryXlsx , "SalesChartData" , "Table1" ,"svg" ) , local_outpath="EmployeeSalesSummary_Sales_Table.svg")
instance.convert_table_to_json( ConvertTableToJsonRequest( EmployeeSalesSummaryXlsx , "SalesChartData" , "Table1" ) , local_outpath="EmployeeSalesSummary_Sales_Table.json")
instance.convert_table_to_html( ConvertTableToHtmlRequest( EmployeeSalesSummaryXlsx , "SalesChartData" , "Table1" ) , local_outpath="EmployeeSalesSummary_Sales_Table.html")
