import os
import shutil
import base64
from asposecellscloud.apis.cells_api import CellsApi
from asposecellscloud.models import *
from asposecellscloud.requests import *

bookFormulaXlsx = "BookFormula.xlsx"
remoteFolder = "PythonSDK"
def file_to_base64(file_path):
    with open(file_path, 'rb') as file:
        file_content = file.read()
    return base64.b64encode(file_content).decode('utf-8')

instance  = CellsApi(os.getenv('CellsCloudClientId'),os.getenv('CellsCloudClientSecret'))

# 1 Check the formula error for an online Excel file in the Cells Cloud Storage.

instance.upload_file(  UploadFileRequest( bookFormulaXlsx, remoteFolder + '/' + bookFormulaXlsx))
dataSource =  DataSource( data_source_type='CloudFileSystem' ,data_path= remoteFolder + '/' + bookFormulaXlsx )
formulaErrorOptions = CheckFormulaErrorOptions ( data_source = dataSource  )
checkWorkbookFormulaErrorsRequest = CheckWorkbookFormulaErrorsRequest( formula_error_options = formulaErrorOptions )
response = instance.check_workbook_formula_errors( checkWorkbookFormulaErrorsRequest )
print(response)

# 1 Check the formula error for a local Excel file.

fileInfo = FileInfo( filename= bookFormulaXlsx, file_content= file_to_base64(bookFormulaXlsx))
response = instance.check_workbook_formula_errors( CheckWorkbookFormulaErrorsRequest( formula_error_options = CheckFormulaErrorOptions(file_info= fileInfo )) )
print(response)

# 1 Check the formula error for a local Excel file.

fileInfo = FileInfo( filename= bookFormulaXlsx, file_content= file_to_base64(bookFormulaXlsx))
response = instance.check_workbook_formula_errors( CheckWorkbookFormulaErrorsRequest( formula_error_options = CheckFormulaErrorOptions(file_info= fileInfo )) )
print(response)





