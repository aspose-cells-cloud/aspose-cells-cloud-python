import os
import shutil
import base64
from asposecellscloud.apis.cells_api import CellsApi
from asposecellscloud.models import *
from asposecellscloud.requests import *


EmployeeSalesSummaryXlsx = "EmployeeSalesSummary.xlsx"
RemoteFolder = "PythonSDK"
# Get Cells Cloud SDK instance
instance  = CellsApi(os.getenv('CellsCloudClientId'),os.getenv('CellsCloudClientSecret'))

# Convert a local Excel file to another format file directly.
response = instance.put_convert_workbook(PutConvertWorkbookRequest( EmployeeSalesSummaryXlsx, 'pdf'))
shutil.move( response ,"EmployeeSalesSummary1.pdf")

# Upload a local Excel file to Cells Cloud Storage.
instance.upload_file( UploadFileRequest(EmployeeSalesSummaryXlsx, "PythonSDK/EmployeeSalesSummary.xlsx"))

source_range =  Range(column_count= 11 ,first_column= 1 ,first_row= 25 ,row_count= 11 )
image_options = ImageOrPrintOptions( image_type="svg" )
range_convert_request = RangeConvertRequest(    source=source_range,    image_type="svg",    image_or_print_options=image_options)
request = PostWorksheetCellsRangeToImageRequest( name=EmployeeSalesSummaryXlsx,  sheet_name="Sales",
                                                 range_convert_request=range_convert_request,  folder=RemoteFolder  )
tmp_path = instance.post_worksheet_cells_range_to_image(request)
shutil.move( tmp_path ,"EmployeeSalesSummary_Sales.svg")