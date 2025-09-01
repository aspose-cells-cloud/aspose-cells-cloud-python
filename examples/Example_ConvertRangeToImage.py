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

# 1. Cells Cloud v3.0: Convert range to image
# 1.1. Upload a local Excel file to Cells Cloud Storage.
instance.upload_file( UploadFileRequest(EmployeeSalesSummaryXlsx, "PythonSDK/EmployeeSalesSummary.xlsx"))
# 1.2. Convert range to image
source_range =  Range(column_count= 11 ,first_column= 1 ,first_row= 25 ,row_count= 11 )
image_options = ImageOrPrintOptions( image_type="svg" )
range_convert_request = RangeConvertRequest(    source=source_range,    image_type="svg",    image_or_print_options=image_options)
request = PostWorksheetCellsRangeToImageRequest( name=EmployeeSalesSummaryXlsx,  sheet_name="Sales",
                                                 range_convert_request=range_convert_request,  folder=RemoteFolder  )
tmp_path = instance.post_worksheet_cells_range_to_image(request)
# 1.3. Save image to local file.
shutil.move( tmp_path ,"EmployeeSalesSummary_Sales_v30.svg")

# 2. Cells Cloud V4.0: Convert range to image
# 2.1. convert range to image
range_convert_request = ConvertRangeToImageRequest( EmployeeSalesSummaryXlsx, 'Sales', "B28:L36", "svg")
instance.convert_range_to_image(range_convert_request ,local_outpath = "EmployeeSalesSummary_Sales_v40.svg" )
