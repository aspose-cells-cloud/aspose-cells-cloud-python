# coding: utf-8

import os
import sys

ABSPATH = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/..")
sys.path.append(ABSPATH)

import asposecellscloud
from asposecellscloud.rest import ApiException
from asposecellscloud.apis.cells_api import CellsApi
from asposecellscloud.api_client import ApiClient
import asposestoragecloud

grantType = "client_credentials"
clientId = "66164C51-693E-4904-A121-545961673EC1"
clientSecret = "536e76768419db9585afdd37bb5f7533"
def GetAPPSID():
    return clientId
def GetAPPKey():
    return clientSecret
def GetAccessToken():
    client = ApiClient('https://api.aspose.cloud')
    api = asposecellscloud.apis.cells_api.CellsApi(client)
    data = api.o_auth_post(grantType, clientId, clientSecret)
    return data.access_token

api_client = None

def GetApiClient():
    global api_client
    if api_client == None:
        api_client = ApiClient('https://api.aspose.cloud/v3.0')
        api_client.set_default_header("Authorization", "Bearer " + GetAccessToken())
    return api_client


def Ready(api, filename, folder, storage=None):

  
    path = folder + '/' + filename
    fullfilename = "D:/Projects/Aspose/Aspose.Cloud/Aspose.Cells.Cloud.SDK/src/TestData/" + filename
    response = api.upload_file(path, fullfilename)
    # with open(fullfilename, 'rb') as file_object:
    #     contents = file_object.read()
    # response = None
    # if storage == None:
    #     response = api.upload_file(path, fullfilename)
    # else:    
    #     response = api.upload_file(path, fullfilename, storage)
    #     if response['Status'] == "OK":
    #         return True
    
    # return False
