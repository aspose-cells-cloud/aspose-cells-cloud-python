import os
import sys
from asposecellscloud.apis.cells_api import CellsApi
from asposecellscloud.models import *
from asposecellscloud.requests import *

api  = CellsApi(os.getenv('CellsCloudClientId'),os.getenv('CellsCloudClientSecret'),"v3.0",os.getenv('CellsCloudApiBaseUrl'))
remote_folder = 'TestData/In'

local_name = 'Template.xlsx'
data_xml = 'data.xml'
remote_name = 'Template.xlsx'

importXMLRequestXMLFileSource = DataSource(data_source_type= 'CloudFileSystem' ,data_path= remote_folder + '/data.xml' )
importXMLRequestImportPosition = ImportPosition(sheet_name= 'Sheet1' ,row_index= 3 ,column_index= 4 )
importXMLRequest = ImportXMLRequest(xml_file_source= importXMLRequestXMLFileSource ,import_position= importXMLRequestImportPosition )
mapFiles = { 
    local_name:  local_name             
}
request =  UploadFileRequest( mapFiles, remote_folder + '/' + remote_name,storage_name= '')
api.upload_file(request)
mapFiles = { 
    local_name:  local_name             
}
request =  UploadFileRequest( mapFiles, remote_folder + '/' + remote_name,storage_name= '')
api.upload_file(request)
 
request =  PostWorkbookImportXMLRequest( remote_name, importXMLRequest,folder= remote_folder,storage_name= '')
api.post_workbook_import_xml(request)
