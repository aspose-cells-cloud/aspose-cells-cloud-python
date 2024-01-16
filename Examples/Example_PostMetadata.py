import os
import sys
from asposecellscloud.apis.cells_api import CellsApi
from asposecellscloud.models import *
from asposecellscloud.requests import *

api  = CellsApi(os.getenv('CellsCloudClientId'),os.getenv('CellsCloudClientSecret'),"v3.0",os.getenv('CellsCloudApiBaseUrl'))
book1_xlsx = 'Book1.xlsx'

mapFiles = { 
    book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
}
cellsDocumentscellsDocument0 = CellsDocumentProperty(name= 'Author' ,value= 'roy.wang' )
cellsDocuments = [
    cellsDocumentscellsDocument0
]

 
request =  PostMetadataRequest( mapFiles, cellsDocuments)
api.post_metadata(request)
