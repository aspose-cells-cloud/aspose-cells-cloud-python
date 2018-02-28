# asposecellscloud.CellsTaskApi

All URIs are relative to *https://api.aspose.cloud/v1.1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cells_task_post_run_task**](CellsTaskApi.md#cells_task_post_run_task) | **POST** /cells/task/runtask | Run tasks  


# **cells_task_post_run_task**
> file cells_task_post_run_task(task_data)

Run tasks  

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsTaskApi()
task_data = asposecellscloud.TaskData() # TaskData | 

try: 
    # Run tasks  
    api_response = api_instance.cells_task_post_run_task(task_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsTaskApi->cells_task_post_run_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_data** | [**TaskData**](TaskData.md)|  | 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

