import os
import shutil
import base64
from asposecellscloud.apis.cells_api import CellsApi
from asposecellscloud.models import *
from asposecellscloud.requests import *


EmployeeSalesSummaryXlsx = "EmployeeSalesSummary.xlsx"
CompanySalesXlsx = "CompanySales.xlsx"
RemoteFolder = "PythonSDK"
RemoteOutputFolder = "PythonSDKOutput"
# Get Cells Cloud SDK instance
instance  = CellsApi(os.getenv('CellsCloudClientId'),os.getenv('CellsCloudClientSecret'))

instance.upload_file(  UploadFileRequest( CompanySalesXlsx, RemoteFolder + '/' + CompanySalesXlsx))
instance.upload_file(  UploadFileRequest( EmployeeSalesSummaryXlsx, RemoteFolder + '/' + EmployeeSalesSummaryXlsx))

# batch convert matched Xlsx files to PDF format files
instance.post_batch_convert( PostBatchConvertRequest( batch_convert_request= BatchConvertRequest( source_folder= RemoteFolder , format="Pdf" , out_folder=RemoteOutputFolder , match_condition=  MatchConditionRequest( regex_pattern= 'xlsx' ))))

# batch split matched Xlsx files to PDF format files
instance.post_batch_split( PostBatchSplitRequest(  batch_split_request= BatchSplitRequest( source_folder= RemoteFolder , format="png" , out_folder=RemoteOutputFolder , match_condition=  MatchConditionRequest( regex_pattern= 'xlsx' ))))
