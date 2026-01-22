import os
import sys

from asposecellscloud.apis.cells_api import CellsApi
from asposecellscloud.models import *
from asposecellscloud.requests import *

# If no environment variables are configured, please obtain the ClientId and ClientSecret from https://dashboard.aspose.cloud/#/applications and replace the following values:
# instance  = CellsApi('YourClientId','YourClientSecret')
instance  = CellsApi(os.getenv('CellsCloudClientId'),os.getenv('CellsCloudClientSecret'))

remote_folder = 'SDKPython'
CompanySalesXlsx = 'CompanySales.xlsx'
EmployeeSalesSummaryXlsx = 'EmployeeSalesSummary.xlsx'
response = instance.object_exists(ObjectExistsRequest( 'SDKPython'))
if not response.exists :
    instance.create_folder( CreateFolderRequest('SDKPython') )
    print('Created SDKPython Folder.')
response = instance.object_exists(ObjectExistsRequest( 'SDKPython/CompanySales.xlsx'))
if  not response.exists :
    instance.upload_file(  UploadFileRequest( CompanySalesXlsx, remote_folder + '/' + CompanySalesXlsx))
    print('Uploaded CompanySales.xlsx.')
    instance.create_folder( CreateFolderRequest( 'SDKPython/CellsCloud'))
    response = instance.object_exists( ObjectExistsRequest('SDKPython/CellsCloud'))
    if  response.exists :
        instance.move_folder( MoveFolderRequest( 'SDKPython/CellsCloud','SDKPython/CellsCloud2'))
        print('Moved folder.')
    instance.copy_file( CopyFileRequest( 'SDKPython/CompanySales.xlsx','SDKPython/CellsCloud/CompanySales.xlsx'))
    print('Copy CompanySales.xlsx exists.')
    instance.upload_file(UploadFileRequest(EmployeeSalesSummaryXlsx, 'SDKPython/CellsCloud2/' + EmployeeSalesSummaryXlsx))
    instance.copy_folder(CopyFolderRequest('SDKPython/CellsCloud2','SDKPython/CellsCloud'  ))
    print('Copy folder.')
    fileLists = instance.get_files_list(GetFilesListRequest('SDKPython/CellsCloud'))
    print('Get files from folder.')
    for storageFile in fileLists.value:
        print(storageFile.name)
    instance.delete_folder( DeleteFolderRequest( 'SDKPython/CellsCloud2' , recursive=True))
    print('Deleted Folder.')
    instance.delete_folder(DeleteFolderRequest('SDKPython/CellsCloud', recursive=True))
else :
    print('CompanySales.xlsx exists.')

instance.delete_file(  DeleteFileRequest(remote_folder +'/'+ CompanySalesXlsx ))
print('Delete CompanySales.xlsx.')