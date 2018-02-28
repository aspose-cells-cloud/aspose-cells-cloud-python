# asposecellscloud.CellsListObjectsApi

All URIs are relative to *https://api.aspose.cloud/v1.1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cells_list_objects_delete_worksheet_list_object**](CellsListObjectsApi.md#cells_list_objects_delete_worksheet_list_object) | **DELETE** /cells/{name}/worksheets/{sheetName}/listobjects/{listObjectIndex} | Delete worksheet list object by index
[**cells_list_objects_delete_worksheet_list_objects**](CellsListObjectsApi.md#cells_list_objects_delete_worksheet_list_objects) | **DELETE** /cells/{name}/worksheets/{sheetName}/listobjects | Delete worksheet list objects
[**cells_list_objects_get_worksheet_list_object**](CellsListObjectsApi.md#cells_list_objects_get_worksheet_list_object) | **GET** /cells/{name}/worksheets/{sheetName}/listobjects/{listobjectindex} | Get worksheet list object info by index.
[**cells_list_objects_get_worksheet_list_objects**](CellsListObjectsApi.md#cells_list_objects_get_worksheet_list_objects) | **GET** /cells/{name}/worksheets/{sheetName}/listobjects | Get worksheet listobjects info.
[**cells_list_objects_post_worksheet_list_object**](CellsListObjectsApi.md#cells_list_objects_post_worksheet_list_object) | **POST** /cells/{name}/worksheets/{sheetName}/listobjects/{listObjectIndex} | Update  list object 
[**cells_list_objects_post_worksheet_list_object_convert_to_range**](CellsListObjectsApi.md#cells_list_objects_post_worksheet_list_object_convert_to_range) | **POST** /cells/{name}/worksheets/{sheetName}/listobjects/{listObjectIndex}/ConvertToRange | 
[**cells_list_objects_post_worksheet_list_object_sort_table**](CellsListObjectsApi.md#cells_list_objects_post_worksheet_list_object_sort_table) | **POST** /cells/{name}/worksheets/{sheetName}/listobjects/{listObjectIndex}/sort | 
[**cells_list_objects_post_worksheet_list_object_summarize_with_pivot_table**](CellsListObjectsApi.md#cells_list_objects_post_worksheet_list_object_summarize_with_pivot_table) | **POST** /cells/{name}/worksheets/{sheetName}/listobjects/{listObjectIndex}/SummarizeWithPivotTable | 
[**cells_list_objects_put_worksheet_list_object**](CellsListObjectsApi.md#cells_list_objects_put_worksheet_list_object) | **PUT** /cells/{name}/worksheets/{sheetName}/listobjects | Add a list object into worksheet.


# **cells_list_objects_delete_worksheet_list_object**
> SaaSposeResponse cells_list_objects_delete_worksheet_list_object(name, sheet_name, list_object_index, folder=folder)

Delete worksheet list object by index

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsListObjectsApi()
name = 'name_example' # str | Document name.
sheet_name = 'sheet_name_example' # str | The worksheet name.
list_object_index = 56 # int | List object index
folder = 'folder_example' # str | Document's folder. (optional)

try: 
    # Delete worksheet list object by index
    api_response = api_instance.cells_list_objects_delete_worksheet_list_object(name, sheet_name, list_object_index, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsListObjectsApi->cells_list_objects_delete_worksheet_list_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document name. | 
 **sheet_name** | **str**| The worksheet name. | 
 **list_object_index** | **int**| List object index | 
 **folder** | **str**| Document&#39;s folder. | [optional] 

### Return type

[**SaaSposeResponse**](SaaSposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_list_objects_delete_worksheet_list_objects**
> SaaSposeResponse cells_list_objects_delete_worksheet_list_objects(name, sheet_name, folder=folder)

Delete worksheet list objects

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsListObjectsApi()
name = 'name_example' # str | Document name.
sheet_name = 'sheet_name_example' # str | The worksheet name.
folder = 'folder_example' # str | Document's folder. (optional)

try: 
    # Delete worksheet list objects
    api_response = api_instance.cells_list_objects_delete_worksheet_list_objects(name, sheet_name, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsListObjectsApi->cells_list_objects_delete_worksheet_list_objects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document name. | 
 **sheet_name** | **str**| The worksheet name. | 
 **folder** | **str**| Document&#39;s folder. | [optional] 

### Return type

[**SaaSposeResponse**](SaaSposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_list_objects_get_worksheet_list_object**
> ListObjectResponse cells_list_objects_get_worksheet_list_object(name, sheet_name, listobjectindex, folder=folder)

Get worksheet list object info by index.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsListObjectsApi()
name = 'name_example' # str | Document name.
sheet_name = 'sheet_name_example' # str | The worksheet name.
listobjectindex = 56 # int | list object index.
folder = 'folder_example' # str | Document's folder. (optional)

try: 
    # Get worksheet list object info by index.
    api_response = api_instance.cells_list_objects_get_worksheet_list_object(name, sheet_name, listobjectindex, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsListObjectsApi->cells_list_objects_get_worksheet_list_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document name. | 
 **sheet_name** | **str**| The worksheet name. | 
 **listobjectindex** | **int**| list object index. | 
 **folder** | **str**| Document&#39;s folder. | [optional] 

### Return type

[**ListObjectResponse**](ListObjectResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_list_objects_get_worksheet_list_objects**
> ListObjectsResponse cells_list_objects_get_worksheet_list_objects(name, sheet_name, folder=folder)

Get worksheet listobjects info.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsListObjectsApi()
name = 'name_example' # str | Document name.
sheet_name = 'sheet_name_example' # str | The worksheet name.
folder = 'folder_example' # str | Document's folder. (optional)

try: 
    # Get worksheet listobjects info.
    api_response = api_instance.cells_list_objects_get_worksheet_list_objects(name, sheet_name, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsListObjectsApi->cells_list_objects_get_worksheet_list_objects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document name. | 
 **sheet_name** | **str**| The worksheet name. | 
 **folder** | **str**| Document&#39;s folder. | [optional] 

### Return type

[**ListObjectsResponse**](ListObjectsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_list_objects_post_worksheet_list_object**
> SaaSposeResponse cells_list_objects_post_worksheet_list_object(name, sheet_name, list_object_index, list_object=list_object, folder=folder)

Update  list object 

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsListObjectsApi()
name = 'name_example' # str | Document name.
sheet_name = 'sheet_name_example' # str | The worksheet name.
list_object_index = 56 # int | list Object index
list_object = asposecellscloud.ListObject() # ListObject | listObject dto in request body. (optional)
folder = 'folder_example' # str | Document's folder. (optional)

try: 
    # Update  list object 
    api_response = api_instance.cells_list_objects_post_worksheet_list_object(name, sheet_name, list_object_index, list_object=list_object, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsListObjectsApi->cells_list_objects_post_worksheet_list_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document name. | 
 **sheet_name** | **str**| The worksheet name. | 
 **list_object_index** | **int**| list Object index | 
 **list_object** | [**ListObject**](ListObject.md)| listObject dto in request body. | [optional] 
 **folder** | **str**| Document&#39;s folder. | [optional] 

### Return type

[**SaaSposeResponse**](SaaSposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_list_objects_post_worksheet_list_object_convert_to_range**
> SaaSposeResponse cells_list_objects_post_worksheet_list_object_convert_to_range(name, sheet_name, list_object_index, folder=folder)



### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsListObjectsApi()
name = 'name_example' # str | 
sheet_name = 'sheet_name_example' # str | 
list_object_index = 56 # int | 
folder = 'folder_example' # str |  (optional)

try: 
    api_response = api_instance.cells_list_objects_post_worksheet_list_object_convert_to_range(name, sheet_name, list_object_index, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsListObjectsApi->cells_list_objects_post_worksheet_list_object_convert_to_range: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **sheet_name** | **str**|  | 
 **list_object_index** | **int**|  | 
 **folder** | **str**|  | [optional] 

### Return type

[**SaaSposeResponse**](SaaSposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_list_objects_post_worksheet_list_object_sort_table**
> SaaSposeResponse cells_list_objects_post_worksheet_list_object_sort_table(name, sheet_name, list_object_index, data_sorter=data_sorter, folder=folder)



### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsListObjectsApi()
name = 'name_example' # str | 
sheet_name = 'sheet_name_example' # str | 
list_object_index = 56 # int | 
data_sorter = asposecellscloud.DataSorter() # DataSorter |  (optional)
folder = 'folder_example' # str |  (optional)

try: 
    api_response = api_instance.cells_list_objects_post_worksheet_list_object_sort_table(name, sheet_name, list_object_index, data_sorter=data_sorter, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsListObjectsApi->cells_list_objects_post_worksheet_list_object_sort_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **sheet_name** | **str**|  | 
 **list_object_index** | **int**|  | 
 **data_sorter** | [**DataSorter**](DataSorter.md)|  | [optional] 
 **folder** | **str**|  | [optional] 

### Return type

[**SaaSposeResponse**](SaaSposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_list_objects_post_worksheet_list_object_summarize_with_pivot_table**
> SaaSposeResponse cells_list_objects_post_worksheet_list_object_summarize_with_pivot_table(name, sheet_name, list_object_index, destsheet_name, request=request, folder=folder)



### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsListObjectsApi()
name = 'name_example' # str | 
sheet_name = 'sheet_name_example' # str | 
list_object_index = 56 # int | 
destsheet_name = 'destsheet_name_example' # str | 
request = asposecellscloud.CreatePivotTableRequest() # CreatePivotTableRequest |  (optional)
folder = 'folder_example' # str |  (optional)

try: 
    api_response = api_instance.cells_list_objects_post_worksheet_list_object_summarize_with_pivot_table(name, sheet_name, list_object_index, destsheet_name, request=request, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsListObjectsApi->cells_list_objects_post_worksheet_list_object_summarize_with_pivot_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **sheet_name** | **str**|  | 
 **list_object_index** | **int**|  | 
 **destsheet_name** | **str**|  | 
 **request** | [**CreatePivotTableRequest**](CreatePivotTableRequest.md)|  | [optional] 
 **folder** | **str**|  | [optional] 

### Return type

[**SaaSposeResponse**](SaaSposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_list_objects_put_worksheet_list_object**
> ListObjectResponse cells_list_objects_put_worksheet_list_object(name, sheet_name, start_row, start_column, end_row, end_column, folder=folder, has_headers=has_headers)

Add a list object into worksheet.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsListObjectsApi()
name = 'name_example' # str | Document name.
sheet_name = 'sheet_name_example' # str | The worksheet name.
start_row = 56 # int | The start row of the list range.
start_column = 56 # int | The start row of the list range.
end_row = 56 # int | The start row of the list range.
end_column = 56 # int | The start row of the list range.
folder = 'folder_example' # str | Document's folder. (optional)
has_headers = true # bool | Whether the range has headers. (optional) (default to true)

try: 
    # Add a list object into worksheet.
    api_response = api_instance.cells_list_objects_put_worksheet_list_object(name, sheet_name, start_row, start_column, end_row, end_column, folder=folder, has_headers=has_headers)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsListObjectsApi->cells_list_objects_put_worksheet_list_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document name. | 
 **sheet_name** | **str**| The worksheet name. | 
 **start_row** | **int**| The start row of the list range. | 
 **start_column** | **int**| The start row of the list range. | 
 **end_row** | **int**| The start row of the list range. | 
 **end_column** | **int**| The start row of the list range. | 
 **folder** | **str**| Document&#39;s folder. | [optional] 
 **has_headers** | **bool**| Whether the range has headers. | [optional] [default to true]

### Return type

[**ListObjectResponse**](ListObjectResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

