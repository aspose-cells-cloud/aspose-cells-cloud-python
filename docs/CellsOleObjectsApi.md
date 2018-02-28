# asposecellscloud.CellsOleObjectsApi

All URIs are relative to *https://api.aspose.cloud/v1.1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cells_ole_objects_delete_worksheet_ole_object**](CellsOleObjectsApi.md#cells_ole_objects_delete_worksheet_ole_object) | **DELETE** /cells/{name}/worksheets/{sheetName}/oleobjects/{oleObjectIndex} | Delete OLE object.
[**cells_ole_objects_delete_worksheet_ole_objects**](CellsOleObjectsApi.md#cells_ole_objects_delete_worksheet_ole_objects) | **DELETE** /cells/{name}/worksheets/{sheetName}/oleobjects | Delete all OLE objects.
[**cells_ole_objects_get_worksheet_ole_object**](CellsOleObjectsApi.md#cells_ole_objects_get_worksheet_ole_object) | **GET** /cells/{name}/worksheets/{sheetName}/oleobjects/{objectNumber} | Get OLE object info.
[**cells_ole_objects_get_worksheet_ole_objects**](CellsOleObjectsApi.md#cells_ole_objects_get_worksheet_ole_objects) | **GET** /cells/{name}/worksheets/{sheetName}/oleobjects | Get worksheet OLE objects info.
[**cells_ole_objects_post_update_worksheet_ole_object**](CellsOleObjectsApi.md#cells_ole_objects_post_update_worksheet_ole_object) | **POST** /cells/{name}/worksheets/{sheetName}/oleobjects/{oleObjectIndex} | Update OLE object.
[**cells_ole_objects_put_worksheet_ole_object**](CellsOleObjectsApi.md#cells_ole_objects_put_worksheet_ole_object) | **PUT** /cells/{name}/worksheets/{sheetName}/oleobjects | Add OLE object


# **cells_ole_objects_delete_worksheet_ole_object**
> SaaSposeResponse cells_ole_objects_delete_worksheet_ole_object(name, sheet_name, ole_object_index, folder=folder)

Delete OLE object.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsOleObjectsApi()
name = 'name_example' # str | The workbook name.
sheet_name = 'sheet_name_example' # str | The worsheet name.
ole_object_index = 56 # int | Ole object index
folder = 'folder_example' # str | The workbook folder. (optional)

try: 
    # Delete OLE object.
    api_response = api_instance.cells_ole_objects_delete_worksheet_ole_object(name, sheet_name, ole_object_index, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsOleObjectsApi->cells_ole_objects_delete_worksheet_ole_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The workbook name. | 
 **sheet_name** | **str**| The worsheet name. | 
 **ole_object_index** | **int**| Ole object index | 
 **folder** | **str**| The workbook folder. | [optional] 

### Return type

[**SaaSposeResponse**](SaaSposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_ole_objects_delete_worksheet_ole_objects**
> SaaSposeResponse cells_ole_objects_delete_worksheet_ole_objects(name, sheet_name, folder=folder)

Delete all OLE objects.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsOleObjectsApi()
name = 'name_example' # str | The workbook name.
sheet_name = 'sheet_name_example' # str | The worsheet name.
folder = 'folder_example' # str | The workbook folder. (optional)

try: 
    # Delete all OLE objects.
    api_response = api_instance.cells_ole_objects_delete_worksheet_ole_objects(name, sheet_name, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsOleObjectsApi->cells_ole_objects_delete_worksheet_ole_objects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The workbook name. | 
 **sheet_name** | **str**| The worsheet name. | 
 **folder** | **str**| The workbook folder. | [optional] 

### Return type

[**SaaSposeResponse**](SaaSposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_ole_objects_get_worksheet_ole_object**
> file cells_ole_objects_get_worksheet_ole_object(name, sheet_name, object_number, folder=folder)

Get OLE object info.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsOleObjectsApi()
name = 'name_example' # str | Document name.
sheet_name = 'sheet_name_example' # str | Worksheet name.
object_number = 56 # int | The object number.
folder = 'folder_example' # str | The document folder. (optional)

try: 
    # Get OLE object info.
    api_response = api_instance.cells_ole_objects_get_worksheet_ole_object(name, sheet_name, object_number, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsOleObjectsApi->cells_ole_objects_get_worksheet_ole_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document name. | 
 **sheet_name** | **str**| Worksheet name. | 
 **object_number** | **int**| The object number. | 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_ole_objects_get_worksheet_ole_objects**
> OleObjectsResponse cells_ole_objects_get_worksheet_ole_objects(name, sheet_name, folder=folder)

Get worksheet OLE objects info.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsOleObjectsApi()
name = 'name_example' # str | Document name.
sheet_name = 'sheet_name_example' # str | The worksheet name.
folder = 'folder_example' # str | Document's folder. (optional)

try: 
    # Get worksheet OLE objects info.
    api_response = api_instance.cells_ole_objects_get_worksheet_ole_objects(name, sheet_name, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsOleObjectsApi->cells_ole_objects_get_worksheet_ole_objects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document name. | 
 **sheet_name** | **str**| The worksheet name. | 
 **folder** | **str**| Document&#39;s folder. | [optional] 

### Return type

[**OleObjectsResponse**](OleObjectsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_ole_objects_post_update_worksheet_ole_object**
> SaaSposeResponse cells_ole_objects_post_update_worksheet_ole_object(name, sheet_name, ole_object_index, ole=ole, folder=folder)

Update OLE object.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsOleObjectsApi()
name = 'name_example' # str | The workbook name.
sheet_name = 'sheet_name_example' # str | The worsheet name.
ole_object_index = 56 # int | Ole object index
ole = asposecellscloud.OleObject() # OleObject | Ole Object (optional)
folder = 'folder_example' # str | The workbook folder. (optional)

try: 
    # Update OLE object.
    api_response = api_instance.cells_ole_objects_post_update_worksheet_ole_object(name, sheet_name, ole_object_index, ole=ole, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsOleObjectsApi->cells_ole_objects_post_update_worksheet_ole_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The workbook name. | 
 **sheet_name** | **str**| The worsheet name. | 
 **ole_object_index** | **int**| Ole object index | 
 **ole** | [**OleObject**](OleObject.md)| Ole Object | [optional] 
 **folder** | **str**| The workbook folder. | [optional] 

### Return type

[**SaaSposeResponse**](SaaSposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_ole_objects_put_worksheet_ole_object**
> OleObjectResponse cells_ole_objects_put_worksheet_ole_object(name, sheet_name, ole_object=ole_object, upper_left_row=upper_left_row, upper_left_column=upper_left_column, height=height, width=width, ole_file=ole_file, image_file=image_file, folder=folder)

Add OLE object

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsOleObjectsApi()
name = 'name_example' # str | The workbook name.
sheet_name = 'sheet_name_example' # str | The worsheet name.
ole_object = asposecellscloud.OleObject() # OleObject | Ole Object (optional)
upper_left_row = 0 # int | Upper left row index (optional) (default to 0)
upper_left_column = 0 # int | Upper left column index (optional) (default to 0)
height = 0 # int | Height of oleObject, in unit of pixel (optional) (default to 0)
width = 0 # int | Width of oleObject, in unit of pixel (optional) (default to 0)
ole_file = 'ole_file_example' # str | OLE filename (optional)
image_file = 'image_file_example' # str | Image filename (optional)
folder = 'folder_example' # str | The workbook folder. (optional)

try: 
    # Add OLE object
    api_response = api_instance.cells_ole_objects_put_worksheet_ole_object(name, sheet_name, ole_object=ole_object, upper_left_row=upper_left_row, upper_left_column=upper_left_column, height=height, width=width, ole_file=ole_file, image_file=image_file, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsOleObjectsApi->cells_ole_objects_put_worksheet_ole_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The workbook name. | 
 **sheet_name** | **str**| The worsheet name. | 
 **ole_object** | [**OleObject**](OleObject.md)| Ole Object | [optional] 
 **upper_left_row** | **int**| Upper left row index | [optional] [default to 0]
 **upper_left_column** | **int**| Upper left column index | [optional] [default to 0]
 **height** | **int**| Height of oleObject, in unit of pixel | [optional] [default to 0]
 **width** | **int**| Width of oleObject, in unit of pixel | [optional] [default to 0]
 **ole_file** | **str**| OLE filename | [optional] 
 **image_file** | **str**| Image filename | [optional] 
 **folder** | **str**| The workbook folder. | [optional] 

### Return type

[**OleObjectResponse**](OleObjectResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

