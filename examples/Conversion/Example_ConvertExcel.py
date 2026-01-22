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

# 3.0 method: Convert a local Excel file to another format file directly.
#response = instance.put_convert_workbook(PutConvertWorkbookRequest( EmployeeSalesSummaryXlsx, 'pdf'))
#shutil.move( response ,"EmployeeSalesSummary1.pdf")
#  Now, Convert a local Excel file to another format file directly, and directly save to local file.
instance.convert_spreadsheet(ConvertSpreadsheetRequest( 'EmployeeSalesSummary.xlsx', 'pdf') , local_outpath = "EmployeeSalesSummary.pdf")

#Save an Excel file of Cells Cloud as another format file of Cells Cloud.
#instance.post_workbook_save_as( PostWorkbookSaveAsRequest( EmployeeSalesSummaryXlsx ,newfilename= "PythonSDK/EmployeeSalesSummary.pdf" ,folder=RemoteFolder   ))
instance.save_spreadsheet_as( SaveSpreadsheetAsRequest ( EmployeeSalesSummaryXlsx,"pdf" ,folder= RemoteFolder ) )
instance.download_file( DownloadFileRequest("PythonSDK/EmployeeSalesSummary.pdf") , local_outpath="EmployeeSalesSummary3.pdf")


# Convert a local Excel file to pdf file directly. The return value is a file info object, which includes of file name, file content(base64string), and file size.
response = instance.post_convert_workbook_to_pdf( PostConvertWorkbookToPDFRequest( EmployeeSalesSummaryXlsx))
filedata = base64.b64decode(response.file_content)
with open("EmployeeSalesSummary.pdf", "wb") as file:
    file.write(filedata)

# Convert a local Excel file to pdf file directly. The return value is a file info object, which includes of file name, file content(base64string), and file size.
response = instance.post_convert_workbook_to_json( PostConvertWorkbookToJsonRequest( EmployeeSalesSummaryXlsx))
filedata = base64.b64decode(response.file_content)
with open("EmployeeSalesSummary.json", "wb") as file:
    file.write(filedata)

# Convert a local Excel file to docx file directly. The return value is a file info object, which includes of file name, file content(base64string), and file size.
response = instance.post_convert_workbook_to_docx( PostConvertWorkbookToDocxRequest( EmployeeSalesSummaryXlsx))
filedata = base64.b64decode(response.file_content)
with open("EmployeeSalesSummary.docx", "wb") as file:
    file.write(filedata)

# Convert a local Excel file to png file directly. The return value is a file info object, which includes of file name, file content(base64string), and file size.
response = instance.post_convert_workbook_to_png( PostConvertWorkbookToPNGRequest( EmployeeSalesSummaryXlsx))
filedata = base64.b64decode(response.file_content)
with open("EmployeeSalesSummary.png", "wb") as file:
    file.write(filedata)

# Convert a local Excel file to pptx file directly. The return value is a file info object, which includes of file name, file content(base64string), and file size.
response = instance.post_convert_workbook_to_pptx(PostConvertWorkbookToPptxRequest(EmployeeSalesSummaryXlsx))
filedata = base64.b64decode(response.file_content)
with open("EmployeeSalesSummary.pptx", "wb") as file:
    file.write(filedata)

# Convert a local Excel file to html file directly. The return value is a file info object, which includes of file name, file content(base64string), and file size.
response = instance.post_convert_workbook_to_html(PostConvertWorkbookToHtmlRequest(EmployeeSalesSummaryXlsx))
filedata = base64.b64decode(response.file_content)
with open("EmployeeSalesSummary.html", "wb") as file:
    file.write(filedata)

# Advanced Conversion allows you to flexibly set page parameters and save parameters
dataSource = DataSource( data_source_type = 'CloudFileSystem' , data_path = RemoteFolder +'/' +EmployeeSalesSummaryXlsx  )
saveOptions = PdfSaveOptions( save_format ='pdf' , one_page_per_sheet = True )
convertWorkbookOptions = ConvertWorkbookOptions( data_source=  dataSource  , convert_format = 'Pdf' ,save_options= saveOptions )
response = instance.post_convert_workbook( PostConvertWorkbookRequest(  convert_workbook_options=convertWorkbookOptions )  )
filedata = base64.b64decode(response.file_content)
with open("EmployeeSalesSummary3.pdf", "wb") as file:
    file.write(filedata)
