# coding: utf-8
"""
<copyright company="Aspose" file="AuthUtilpy.cs">
  Copyright (c) 2023 Aspose.Cells Cloud
</copyright>
<summary>
 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:

 The above copyright notice and this permission notice shall be included in all
 copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 SOFTWARE.
</summary>
"""
import os
import sys

ABSPATH = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/..")
sys.path.append(ABSPATH)

import asposecellscloud
from asposecellscloud.rest import ApiException
from asposecellscloud.apis.cells_api import CellsApi
from asposecellscloud.api_client import ApiClient
from asposecellscloud.requests.upload_file_request import UploadFileRequest

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
    path = folder 
    fullfilename = "TestData/" + filename
    uploadFileRequest = UploadFileRequest(fullfilename,path,storage_name=storage)
    response = api.upload_file(uploadFileRequest)
    return response

