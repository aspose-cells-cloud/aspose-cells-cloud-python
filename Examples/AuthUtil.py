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
clientId = os.getenv('CellsCloudTestClientId')
clientSecret =  os.getenv('CellsCloudTestClientSecret')

def GetAccessToken():
    client = ApiClient(os.getenv('CellsCloudTestApiBaseUrl'))
    api = asposecellscloud.apis.o_auth_api.OAuthApi(client)
    data = api.o_auth_post(grantType, clientId, clientSecret)
    return data.access_token

api_client = None

def GetApiClient():
    global api_client
    if api_client == None:
        api_client = ApiClient(os.getenv('CellsCloudTestApiBaseUrl')+'/v1.1')
        api_client.set_default_header("Authorization", "Bearer " + GetAccessToken())
    return api_client    