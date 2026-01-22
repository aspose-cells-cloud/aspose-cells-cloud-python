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

# Upload a local Excel file to Cells Cloud Storage.
instance.upload_file( UploadFileRequest(EmployeeSalesSummaryXlsx, "PythonSDK/EmployeeSalesSummary.xlsx"))
# Convert an Excel file of Cells Cloud to another format file.
# response = instance.get_workbook( GetWorkbookRequest(EmployeeSalesSummaryXlsx , format='pdf' , folder=RemoteFolder)  )
# shutil.move( response ,"EmployeeSalesSummary2.pdf")
#  Now, Export a cloud Excel file to another format file directly, and directly save to local file.
instance.export_spreadsheet_as_format( ExportSpreadsheetAsFormatRequest( EmployeeSalesSummaryXlsx,"csv" ,folder= "PythonSDK"  ) , local_outpath="EmployeeSalesSummary.csv" )
instance.export_worksheet_as_format( ExportWorksheetAsFormatRequest( EmployeeSalesSummaryXlsx,"Sales", "pdf" ,folder= "PythonSDK"  ) , local_outpath="EmployeeSalesSummary2.pdf" )

# Convert a worksheet of a local Excel file to another format file directly. Set query parameters : print_headings, one_page_per_sheet
#response = instance.get_worksheet_with_format( GetWorksheetWithFormatRequest(EmployeeSalesSummaryXlsx, "Sales", folder ="PythonSDK",  format="png", print_headings=True , one_page_per_sheet= False )  )
#shutil.move( response ,"EmployeeSalesSummary_Sales.png")
# Convert a worksheet of a local Excel file to another format file directly, and save as local file.
instance.convert_worksheet_to_image( ConvertWorksheetToImageRequest( EmployeeSalesSummaryXlsx,"Sales", format="png") , local_outpath="EmployeeSalesSummary_Sales.png")

# Convert a local Excel file's specified worksheet page index directly to another format file. Set query parameters : print_headings, one_page_per_sheet
response = instance.get_worksheet_with_format( GetWorksheetWithFormatRequest(EmployeeSalesSummaryXlsx, "Sales", folder ="PythonSDK",  format="png", page_index= 1 , print_headings=True , one_page_per_sheet= False )  )
shutil.move( response ,"EmployeeSalesSummary_Sales_PageIndex.png")
