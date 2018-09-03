# asposecellscloud.CellsSaveAsApi

All URIs are relative to *https://api.aspose.cloud/v1.1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cells_save_as_post_document_save_as**](CellsSaveAsApi.md#cells_save_as_post_document_save_as) | **POST** /cells/{name}/SaveAs | Convert document and save result to storage.


# **cells_save_as_post_document_save_as**
> SaveResponse cells_save_as_post_document_save_as(name, save_options=save_options, newfilename=newfilename, is_auto_fit_rows=is_auto_fit_rows, is_auto_fit_columns=is_auto_fit_columns, folder=folder, storage=storage)

Convert document and save result to storage.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsSaveAsApi()
name = 'name_example' # str | The document name.
save_options = asposecellscloud.SaveOptions() # SaveOptions | Save options. (optional)
newfilename = 'newfilename_example' # str | The new file name. (optional)
is_auto_fit_rows = false # bool | Autofit rows. (optional) (default to false)
is_auto_fit_columns = false # bool | Autofit columns. (optional) (default to false)
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Convert document and save result to storage.
    api_response = api_instance.cells_save_as_post_document_save_as(name, save_options=save_options, newfilename=newfilename, is_auto_fit_rows=is_auto_fit_rows, is_auto_fit_columns=is_auto_fit_columns, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsSaveAsApi->cells_save_as_post_document_save_as: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **save_options** | [**SaveOptions**](SaveOptions.md)| Save options. | [optional] 
 **newfilename** | **str**| The new file name. | [optional] 
 **is_auto_fit_rows** | **bool**| Autofit rows. | [optional] [default to false]
 **is_auto_fit_columns** | **bool**| Autofit columns. | [optional] [default to false]
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**SaveResponse**](SaveResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

