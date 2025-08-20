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

# 3.0 method: Convert a local Excel file to another format file directly.
#response = instance.put_convert_workbook(PutConvertWorkbookRequest( EmployeeSalesSummaryXlsx, 'pdf'))
#shutil.move( response ,"EmployeeSalesSummary1.pdf")
#  Now, Convert a local Excel file to another format file directly, and directly save to local file.
instance.convert_spreadsheet(ConvertSpreadsheetRequest( 'EmployeeSalesSummary.xlsx', 'pdf') , local_outpath = "EmployeeSalesSummary.pdf")

# Upload a local Excel file to Cells Cloud Storage.
instance.upload_file( UploadFileRequest(EmployeeSalesSummaryXlsx, "PythonSDK/EmployeeSalesSummary.xlsx"))
# Convert an Excel file of Cells Cloud to another format file.
# response = instance.get_workbook( GetWorkbookRequest(EmployeeSalesSummaryXlsx , format='pdf' , folder=RemoteFolder)  )
# shutil.move( response ,"EmployeeSalesSummary2.pdf")
#  Now, Export a cloud Excel file to another format file directly, and directly save to local file.
instance.export_Spreadsheet_as_format( ExportSpreadsheetAsFormatRequest( EmployeeSalesSummaryXlsx,"csv" ,folder= "PythonSDK"  ) , local_outpath="EmployeeSalesSummary.csv" )
instance.export_worksheet_as_format( ExportWorksheetAsFormatRequest( EmployeeSalesSummaryXlsx,"Sales", "pdf" ,folder= "PythonSDK"  ) , local_outpath="EmployeeSalesSummary2.pdf" )

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

# Convert a worksheet of a local Excel file to another format file directly. Set query parameters : print_headings, one_page_per_sheet
#response = instance.get_worksheet_with_format( GetWorksheetWithFormatRequest(EmployeeSalesSummaryXlsx, "Sales", folder ="PythonSDK",  format="png", print_headings=True , one_page_per_sheet= False )  )
#shutil.move( response ,"EmployeeSalesSummary_Sales.png")
# Convert a worksheet of a local Excel file to another format file directly, and save as local file.
instance.convert_worksheet_to_image( ConvertWorksheetToImageRequest( EmployeeSalesSummaryXlsx,"Sales", format="png") , local_outpath="EmployeeSalesSummary_Sales.png")

# Convert a local Excel file's specified worksheet page index directly to another format file. Set query parameters : print_headings, one_page_per_sheet
response = instance.get_worksheet_with_format( GetWorksheetWithFormatRequest(EmployeeSalesSummaryXlsx, "Sales", folder ="PythonSDK",  format="png", page_index= 1 , print_headings=True , one_page_per_sheet= False )  )
shutil.move( response ,"EmployeeSalesSummary_Sales_PageIndex.png")

# Convert a local Excel file's specified worksheet list object directly to another format file. Set query parameters 
instance.convert_table_to_pdf( ConvertTableToPdfRequest( EmployeeSalesSummaryXlsx , "Sales" , "Table1" ) , local_outpath="EmployeeSalesSummary_Sales_Table.pdf")
instance.convert_table_to_image( ConvertTableToImageRequest( EmployeeSalesSummaryXlsx , "Sales" , "Table1" ,"png" ) , local_outpath="EmployeeSalesSummary_Sales_Table.png")
instance.convert_table_to_image( ConvertTableToImageRequest( EmployeeSalesSummaryXlsx , "Sales" , "Table1" ,"svg" ) , local_outpath="EmployeeSalesSummary_Sales_Table.svg")
instance.convert_table_to_json( ConvertTableToJsonRequest( EmployeeSalesSummaryXlsx , "Sales" , "Table1" ) , local_outpath="EmployeeSalesSummary_Sales_Table.json")
instance.convert_table_to_html( ConvertTableToHtmlRequest( EmployeeSalesSummaryXlsx , "Sales" , "Table1" ) , local_outpath="EmployeeSalesSummary_Sales_Table.html")


# Convert a local Excel file's specified worksheet cells area directly to another format file. Set query parameters : print_headings, one_page_per_sheet
# response = instance.get_worksheet_with_format( GetWorksheetWithFormatRequest(EmployeeSalesSummaryXlsx, "Sales", folder ="PythonSDK",  format="png", area="B5:L36" ,print_headings=True , one_page_per_sheet= False )  )
# shutil.move( response ,"EmployeeSalesSummary_Sales_area.png")
instance.convert_range_to_pdf( ConvertRangeToPdfRequest( EmployeeSalesSummaryXlsx , "Sales" , "B5:L36" ) , local_outpath="EmployeeSalesSummary_Sales_area.pdf")
instance.convert_range_to_image( ConvertRangeToImageRequest( EmployeeSalesSummaryXlsx , "Sales" , "B5:L36" ,"png" ) , local_outpath="EmployeeSalesSummary_Sales_area.png")
instance.convert_range_to_image( ConvertRangeToImageRequest( EmployeeSalesSummaryXlsx , "Sales" , "B5:L36" ,"svg" ) , local_outpath="EmployeeSalesSummary_Sales_area.svg")
instance.convert_range_to_json( ConvertRangeToJsonRequest( EmployeeSalesSummaryXlsx , "Sales" , "B5:L36" ) , local_outpath="EmployeeSalesSummary_Sales_area.json")
instance.convert_range_to_html( ConvertRangeToHtmlRequest( EmployeeSalesSummaryXlsx , "Sales" , "B5:L36" ) , local_outpath="EmployeeSalesSummary_Sales_area.html")

# Advanced Conversion allows you to flexibly set page parameters and save parameters
dataSource = DataSource( data_source_type = 'CloudFileSystem' , data_path = RemoteFolder +'/' +EmployeeSalesSummaryXlsx  )
saveOptions = PdfSaveOptions( save_format ='pdf' , one_page_per_sheet = True )
convertWorkbookOptions = ConvertWorkbookOptions( data_source=  dataSource  , convert_format = 'Pdf' ,save_options= saveOptions )
response = instance.post_convert_workbook( PostConvertWorkbookRequest(  convert_workbook_options=convertWorkbookOptions )  )
filedata = base64.b64decode(response.file_content)
with open("EmployeeSalesSummary3.pdf", "wb") as file:
    file.write(filedata)
