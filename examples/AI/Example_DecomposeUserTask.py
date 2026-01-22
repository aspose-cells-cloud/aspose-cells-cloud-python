import os
import shutil

from asposecellscloud.apis.cells_api import CellsApi
from asposecellscloud.requests import  DecomposeUserTaskRequest

EmployeeSalesSummaryXlsx = "EmployeeSalesSummary.xlsx"
RemoteFolder = "PythonSDK"
# Get Cells Cloud SDK instance
# If no environment variables are configured, please obtain the ClientId and ClientSecret from https://dashboard.aspose.cloud/#/applications and replace the following values:
# instance  = CellsApi('YourClientId','YourClientSecret')
instance  = CellsApi(os.getenv('CellsCloudClientId'),os.getenv('CellsCloudClientSecret'))

instance.decompose_user_task( DecomposeUserTaskRequest("Develop a web API for a task-splitting feature on the existing system." )   ,local_outpath = "DecomposeUserTask.xlsx" )
