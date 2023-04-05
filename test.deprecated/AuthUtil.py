# coding: utf-8

import os
import sys

ABSPATH = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/..")
sys.path.append(ABSPATH)

import asposecellscloud
from asposecellscloud.rest import ApiException
from asposecellscloud.apis.cells_api import CellsApi
from asposecellscloud.api_client import ApiClient


grantType = "client_credentials"
clientId = os.getenv('CellsCloudTestClientId')
clientSecret = os.getenv('CellsCloudTestClientSecret')
def GetBaseUrl():
    return os.getenv('CellsCloudTestApiBaseUrl')
def GetClientId():
    return clientId
def GetClientSecret():
    return clientSecret
def GetAccessToken():
    client = ApiClient(GetBaseUrl())
    api = asposecellscloud.apis.cells_api.CellsApi(client)
    data = api.o_auth_post(grantType, clientId, clientSecret)
    return data.access_token
def GetAppUrl():
    appurl = GetBaseUrl()
    if not appurl.endswith('/'):
        appurl.append('/')
    appurl.append('v3.0')    
    return appurl 
def IsDockerSDK():
    return True
    
api_client = None

def GetApiClient():
    global api_client
    if api_client == None:
        api_client = ApiClient(GetAppUrl())
        api_client.set_default_header("Authorization", "Bearer " + GetAccessToken())
    return api_client


def Ready(api, filename, folder, storage=None): 
    path = folder + '/' + filename
    fullfilename = "TestData/" + filename
    if storage == None:
        response = api.upload_file(path, fullfilename)
    else:
        response = api.upload_file(path, fullfilename, storage_name=storage)
    return response

