# asposecellscloud.OAuthApi

All URIs are relative to *https://api.aspose.cloud/v1.1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**o_auth_post**](OAuthApi.md#o_auth_post) | **POST** /oauth2/token | Get Access token


# **o_auth_post**
> AccessTokenResponse o_auth_post(grant_type, client_id, client_secret)

Get Access token

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.OAuthApi()
grant_type = 'grant_type_example' # str | Grant Type
client_id = 'client_id_example' # str | App SID
client_secret = 'client_secret_example' # str | App Key

try: 
    # Get Access token
    api_response = api_instance.o_auth_post(grant_type, client_id, client_secret)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OAuthApi->o_auth_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grant_type** | **str**| Grant Type | 
 **client_id** | **str**| App SID | 
 **client_secret** | **str**| App Key | 

### Return type

[**AccessTokenResponse**](AccessTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

