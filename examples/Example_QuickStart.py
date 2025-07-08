import os

from asposecellscloud.apis.cells_api import CellsApi
from asposecellscloud.models import *
from asposecellscloud.requests import *

# CellsCloudClientId ='....'  # get from https://dashboard.aspose.cloud/#/applications
# CellsCloudClientSecret='....'  # get from https://dashboard.aspose.cloud/#/applications
# instance  = CellsApi(CellsCloudClientId,CellsCloudClientSecret)
instance  = CellsApi(os.getenv('CellsCloudClientId'),os.getenv('CellsCloudClientSecret'))
response = instance.convert_spreadsheet(ConvertSpreadsheetRequest( 'EmployeeSalesSummary.xlsx', 'pdf') , local_outpath = "EmployeeSalesSummary.pdf")
