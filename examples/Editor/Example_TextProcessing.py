import os

from asposecellscloud.apis.cells_api import CellsApi
from asposecellscloud.models import *
from asposecellscloud.requests import *

# If no environment variables are configured, please obtain the ClientId and ClientSecret from https://dashboard.aspose.cloud/#/applications and replace the following values:
# instance  = CellsApi('YourClientId','YourClientSecret')
instance  = CellsApi(os.getenv('CellsCloudClientId'),os.getenv('CellsCloudClientSecret'))
instance.upload_file(  UploadFileRequest( "BookText.xlsx", "PythonSDK/BookText.xlsx"))
worksheet = "HumanResources"
_range ="A1:C12"
trim_text = " "
response = instance.trim_character_in_remote_spreadsheet(
    TrimCharacterInRemoteSpreadsheetRequest( "BookText.xlsx", worksheet, _range, trim_content=',    ', trim_leading = True,folder ="PythonSDK" ))
print(response.status == "OK")

response = instance.update_word_case_in_remote_spreadsheet(
    UpdateWordCaseInRemoteSpreadsheetRequest( "BookText.xlsx", worksheet, _range,  "UpperCase",folder ="PythonSDK" ))
print(response)

