# coding: utf-8

import os
import sys

ABSPATH = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/..")
sys.path.append(ABSPATH)

import asposecellscloud
from asposecellscloud.rest import ApiException
from asposecellscloud.apis.o_auth_api import OAuthApi
from asposecellscloud.api_client import ApiClient

PY2 = sys.version_info[0] == 2
if PY2:
    import asposestoragecloud
    from asposestoragecloud.StorageApi import StorageApi
    from asposestoragecloud.ApiClient import ApiClient as StorageApiClient
    from asposestoragecloud.ApiClient import ApiException
    from asposestoragecloud.models import FileExistResponse
else:
    import asposestoragecloud
    from asposestoragecloud.StorageApi3 import StorageApi3 as StorageApi
    from asposestoragecloud.ApiClient3 import ApiClient3 as StorageApiClient
    from asposestoragecloud.ApiClient3 import ApiException
    from asposestoragecloud.models import FileExistResponse

grantType = "client_credentials"
clientId = "your clientId"
clientSecret = "your clientSecret"

def GetAccessToken():
    client = ApiClient('https://api.aspose.cloud/')
    api = asposecellscloud.apis.o_auth_api.OAuthApi(client)
    data = api.o_auth_post(grantType, clientId, clientSecret)
    return data.access_token

api_client = None

def GetApiClient():
    global api_client
    if api_client == None:
        api_client = ApiClient('https://api.aspose.cloud/v1.1')
        api_client.set_default_header("Authorization", "Bearer " + GetAccessToken())
    return api_client


def Ready(filename, folder):
    storage_apiClient = StorageApiClient(clientSecret, clientId)
    storageApi = StorageApi(storage_apiClient)
  
    path = folder + '/' + filename
    fullfilename = os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" + filename
    response = storageApi.PutCreate(path, fullfilename)

    if response.Status == "OK":
        return True
    return False
