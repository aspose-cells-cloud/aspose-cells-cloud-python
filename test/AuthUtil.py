# coding: utf-8

import os
import sys

ABSPATH = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/..")
sys.path.append(ABSPATH)

import asposecellscloud
from asposecellscloud.rest import ApiException
from asposecellscloud.apis.o_auth_api import OAuthApi
from asposecellscloud.api_client import ApiClient
import asposestoragecloud

grantType = "client_credentials"
clientId = "66164C51-693E-4904-A121-545961673EC1"
clientSecret = "536e76768419db9585afdd37bb5f7533"

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


def Ready(filename, folder, storage=None):
    storage_apiClient = asposestoragecloud.ApiClient(clientSecret, clientId)
    storageApi = asposestoragecloud.StorageApi(storage_apiClient)
  
    path = folder + '/' + filename
    fullfilename = os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" + filename
    with open(fullfilename, 'rb') as file_object:
        contents = file_object.read()
        response = None
        if storage == None:
            response = storageApi.put_create(path, contents)
        else:    
            response = storageApi.put_create(path, contents, storage=storage)
        if response['Status'] == "OK":
            return True

    return False
