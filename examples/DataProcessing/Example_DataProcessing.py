import base64
import os
import shutil

from asposecellscloud.apis.cells_api import CellsApi
from asposecellscloud.models import *
from asposecellscloud.requests import *

EmployeeSalesSummaryXlsx = "EmployeeSalesSummary.xlsx"
CompanySalesXlsx = "CompanySales.xlsx"
RemoteFolder = "PythonSDK"
RemoteOutputFolder = "PythonSDKOutput"
# Get Cells Cloud SDK instance
# If no environment variables are configured, please obtain the ClientId and ClientSecret from https://dashboard.aspose.cloud/#/applications and replace the following values:
# instance  = CellsApi('YourClientId','YourClientSecret')
instance  = CellsApi(os.getenv('CellsCloudClientId'),os.getenv('CellsCloudClientSecret'))

instance.upload_file(  UploadFileRequest( CompanySalesXlsx, RemoteFolder + '/' + CompanySalesXlsx))
instance.upload_file(  UploadFileRequest( EmployeeSalesSummaryXlsx, RemoteFolder + '/' + EmployeeSalesSummaryXlsx))

instance.post_batch_split( PostBatchSplitRequest(  batch_split_request= BatchSplitRequest( source_folder= RemoteFolder , format="png" , out_folder=RemoteOutputFolder , match_condition=  MatchConditionRequest( regex_pattern= 'xlsx' ))))
