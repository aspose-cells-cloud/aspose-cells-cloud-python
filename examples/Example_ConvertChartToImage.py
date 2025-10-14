import os
import shutil

from asposecellscloud.apis.cells_api import CellsApi
from asposecellscloud.requests import (ConvertChartToImageRequest,
                                       GetWorksheetChartRequest,
                                       UploadFileRequest)

EmployeeSalesSummaryXlsx = "EmployeeSalesSummary.xlsx"
RemoteFolder = "PythonSDK"
# Get Cells Cloud SDK instance
# If no environment variables are configured, please obtain the ClientId and ClientSecret from https://dashboard.aspose.cloud/#/applications and replace the following values:
# instance  = CellsApi('YourClientId','YourClientSecret')
instance  = CellsApi(os.getenv('CellsCloudClientId'),os.getenv('CellsCloudClientSecret'))
# Cloud file processing
# 1. Cells Cloud V3.0: Convert chart to image 
# 1.1. Upload a local Excel file to Cells Cloud Storage.
instance.upload_file( UploadFileRequest(EmployeeSalesSummaryXlsx, "PythonSDK/EmployeeSalesSummary.xlsx"))
# 1.2 Get chart image from Excel worksheet.
request =  GetWorksheetChartRequest( EmployeeSalesSummaryXlsx, 'Sales', 0,format= 'png',folder= 'PythonSDK',storage_name= '')
tmp_path = instance.get_worksheet_chart(request)
# 1.3 Save chart image to local file.
shutil.move( tmp_path ,"EmployeeSalesSummary_Sales_v30.png")
# Local file processing
# 2. Cells Cloud V3.0: Convert chart to image 
convertChartToImageRequest = ConvertChartToImageRequest( EmployeeSalesSummaryXlsx, 'Sales', 0,format= 'png')
instance.convert_chart_to_image(convertChartToImageRequest ,local_outpath = "EmployeeSalesSummary_Sales_v40.png" )
