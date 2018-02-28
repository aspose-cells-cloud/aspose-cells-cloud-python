# asposecellscloud.CellsAutoshapesApi

All URIs are relative to *https://api.aspose.cloud/v1.1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cells_autoshapes_get_worksheet_autoshape**](CellsAutoshapesApi.md#cells_autoshapes_get_worksheet_autoshape) | **GET** /cells/{name}/worksheets/{sheetName}/autoshapes/{autoshapeNumber} | Get autoshape info.
[**cells_autoshapes_get_worksheet_autoshapes**](CellsAutoshapesApi.md#cells_autoshapes_get_worksheet_autoshapes) | **GET** /cells/{name}/worksheets/{sheetName}/autoshapes | Get worksheet autoshapes info.


# **cells_autoshapes_get_worksheet_autoshape**
> file cells_autoshapes_get_worksheet_autoshape(name, sheet_name, autoshape_number, folder=folder)

Get autoshape info.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsAutoshapesApi()
name = 'name_example' # str | Document name.
sheet_name = 'sheet_name_example' # str | Worksheet name.
autoshape_number = 56 # int | The autoshape number.
folder = 'folder_example' # str | The document folder. (optional)

try: 
    # Get autoshape info.
    api_response = api_instance.cells_autoshapes_get_worksheet_autoshape(name, sheet_name, autoshape_number, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsAutoshapesApi->cells_autoshapes_get_worksheet_autoshape: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document name. | 
 **sheet_name** | **str**| Worksheet name. | 
 **autoshape_number** | **int**| The autoshape number. | 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_autoshapes_get_worksheet_autoshapes**
> AutoShapesResponse cells_autoshapes_get_worksheet_autoshapes(name, sheet_name, folder=folder)

Get worksheet autoshapes info.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsAutoshapesApi()
name = 'name_example' # str | Document name.
sheet_name = 'sheet_name_example' # str | The worksheet name.
folder = 'folder_example' # str | Document's folder. (optional)

try: 
    # Get worksheet autoshapes info.
    api_response = api_instance.cells_autoshapes_get_worksheet_autoshapes(name, sheet_name, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsAutoshapesApi->cells_autoshapes_get_worksheet_autoshapes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document name. | 
 **sheet_name** | **str**| The worksheet name. | 
 **folder** | **str**| Document&#39;s folder. | [optional] 

### Return type

[**AutoShapesResponse**](AutoShapesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

