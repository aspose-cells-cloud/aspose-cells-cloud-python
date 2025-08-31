import base64
import os

from asposecellscloud.apis.cells_api import CellsApi
from asposecellscloud.models import *
from asposecellscloud.requests import *

instance  = CellsApi(os.getenv('CellsCloudTestClientId'),os.getenv('CellsCloudTestClientSecret'))

instance.upload_file(  UploadFileRequest( "BookText.xlsx", "PythonSDK/BookText.xlsx"))

trimContentOptions = TrimContentOptions( 
     data_source= DataSource(data_path="PythonSDK/BookText.xlsx", data_source_type="CloudFileSystem" ), 
     remove_all_line_breaks = True, 
     remove_extra_line_breaks= True, 
     remove_extra_spaces= True,
     trim_leading= True,
     trim_trailing= True,
     trim_content= ' ',
     trim_space_between_word_to1= True,
     trim_non_breaking_spaces= True,     
     scope_options = ScopeOptions( scope= "Workbook")
)

response = instance.post_trim_content(PostTrimContentRequest( trimContentOptions))
decoded_data = base64.b64decode(response.file_content)
with open("BookText_1.xlsx", "wb") as file:
     file.write(decoded_data)


trimContentOptions.scope_options.scope =  'Worksheet'
trimContentOptions.scope_options.scope_items = [ScopeItem( worksheet='SDKs')]
response = instance.post_trim_content( PostTrimContentRequest(trimContentOptions))

decoded_data = base64.b64decode(response.file_content)

with open("BookText_2.xlsx", "wb") as file:
     file.write(decoded_data)

trimContentOptions.scope_options.scope =  'SelectionOlny'
trimContentOptions.scope_options.scope_items[0].worksheet = 'SDKs'
trimContentOptions.scope_options.scope_items[0].ranges = ["B2:B2","B4:B4"]
response = instance.post_trim_content( PostTrimContentRequest(trimContentOptions))

decoded_data = base64.b64decode(response.file_content)

with open("BookText_3.xlsx", "wb") as file:
     file.write(decoded_data)

wordCaseOptions = WordCaseOptions( 
     data_source= DataSource(data_path="PythonSDK/BookText.xlsx", data_source_type="CloudFileSystem" ), 
     word_case_type= "ProperCase",
     scope_options = ScopeOptions( scope= "EntireWorkbook")
)

response = instance.post_trim_content(PostTrimContentRequest( trimContentOptions))
decoded_data = base64.b64decode(response.file_content)
with open("BookText_4.xlsx", "wb") as file:
     file.write(decoded_data)
