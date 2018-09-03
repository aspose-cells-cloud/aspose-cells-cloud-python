# asposecellscloud.CellsShapesApi

All URIs are relative to *https://api.aspose.cloud/v1.1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cells_shapes_delete_worksheet_shape**](CellsShapesApi.md#cells_shapes_delete_worksheet_shape) | **DELETE** /cells/{name}/worksheets/{sheetName}/shapes/{shapeindex} | Delete a shape in worksheet
[**cells_shapes_delete_worksheet_shapes**](CellsShapesApi.md#cells_shapes_delete_worksheet_shapes) | **DELETE** /cells/{name}/worksheets/{sheetName}/shapes | delete all shapes in worksheet
[**cells_shapes_get_worksheet_shape**](CellsShapesApi.md#cells_shapes_get_worksheet_shape) | **GET** /cells/{name}/worksheets/{sheetName}/shapes/{shapeindex} | Get worksheet shape
[**cells_shapes_get_worksheet_shapes**](CellsShapesApi.md#cells_shapes_get_worksheet_shapes) | **GET** /cells/{name}/worksheets/{sheetName}/shapes | Get worksheet shapes 
[**cells_shapes_post_worksheet_shape**](CellsShapesApi.md#cells_shapes_post_worksheet_shape) | **POST** /cells/{name}/worksheets/{sheetName}/shapes/{shapeindex} | Update a shape in worksheet
[**cells_shapes_put_worksheet_shape**](CellsShapesApi.md#cells_shapes_put_worksheet_shape) | **PUT** /cells/{name}/worksheets/{sheetName}/shapes | Add shape in worksheet


# **cells_shapes_delete_worksheet_shape**
> SaaSposeResponse cells_shapes_delete_worksheet_shape(name, sheet_name, shapeindex, folder=folder, storage=storage)

Delete a shape in worksheet

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsShapesApi()
name = 'name_example' # str | document name.
sheet_name = 'sheet_name_example' # str | worksheet name.
shapeindex = 56 # int | shape index in worksheet shapes.
folder = 'folder_example' # str | Document's folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Delete a shape in worksheet
    api_response = api_instance.cells_shapes_delete_worksheet_shape(name, sheet_name, shapeindex, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsShapesApi->cells_shapes_delete_worksheet_shape: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| document name. | 
 **sheet_name** | **str**| worksheet name. | 
 **shapeindex** | **int**| shape index in worksheet shapes. | 
 **folder** | **str**| Document&#39;s folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**SaaSposeResponse**](SaaSposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_shapes_delete_worksheet_shapes**
> SaaSposeResponse cells_shapes_delete_worksheet_shapes(name, sheet_name, folder=folder, storage=storage)

delete all shapes in worksheet

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsShapesApi()
name = 'name_example' # str | document name.
sheet_name = 'sheet_name_example' # str | worksheet name.
folder = 'folder_example' # str | Document's folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # delete all shapes in worksheet
    api_response = api_instance.cells_shapes_delete_worksheet_shapes(name, sheet_name, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsShapesApi->cells_shapes_delete_worksheet_shapes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| document name. | 
 **sheet_name** | **str**| worksheet name. | 
 **folder** | **str**| Document&#39;s folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**SaaSposeResponse**](SaaSposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_shapes_get_worksheet_shape**
> ShapeResponse cells_shapes_get_worksheet_shape(name, sheet_name, shapeindex, folder=folder, storage=storage)

Get worksheet shape

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsShapesApi()
name = 'name_example' # str | document name.
sheet_name = 'sheet_name_example' # str | worksheet name.
shapeindex = 56 # int | shape index in worksheet shapes.
folder = 'folder_example' # str | Document's folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Get worksheet shape
    api_response = api_instance.cells_shapes_get_worksheet_shape(name, sheet_name, shapeindex, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsShapesApi->cells_shapes_get_worksheet_shape: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| document name. | 
 **sheet_name** | **str**| worksheet name. | 
 **shapeindex** | **int**| shape index in worksheet shapes. | 
 **folder** | **str**| Document&#39;s folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**ShapeResponse**](ShapeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_shapes_get_worksheet_shapes**
> ShapesResponse cells_shapes_get_worksheet_shapes(name, sheet_name, folder=folder, storage=storage)

Get worksheet shapes 

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsShapesApi()
name = 'name_example' # str | document name.
sheet_name = 'sheet_name_example' # str | worksheet name.
folder = 'folder_example' # str | Document's folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Get worksheet shapes 
    api_response = api_instance.cells_shapes_get_worksheet_shapes(name, sheet_name, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsShapesApi->cells_shapes_get_worksheet_shapes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| document name. | 
 **sheet_name** | **str**| worksheet name. | 
 **folder** | **str**| Document&#39;s folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**ShapesResponse**](ShapesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_shapes_post_worksheet_shape**
> SaaSposeResponse cells_shapes_post_worksheet_shape(name, sheet_name, shapeindex, dto=dto, folder=folder, storage=storage)

Update a shape in worksheet

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsShapesApi()
name = 'name_example' # str | document name.
sheet_name = 'sheet_name_example' # str | worksheet name.
shapeindex = 56 # int | shape index in worksheet shapes.
dto = asposecellscloud.Shape() # Shape |  (optional)
folder = 'folder_example' # str | Document's folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Update a shape in worksheet
    api_response = api_instance.cells_shapes_post_worksheet_shape(name, sheet_name, shapeindex, dto=dto, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsShapesApi->cells_shapes_post_worksheet_shape: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| document name. | 
 **sheet_name** | **str**| worksheet name. | 
 **shapeindex** | **int**| shape index in worksheet shapes. | 
 **dto** | [**Shape**](Shape.md)|  | [optional] 
 **folder** | **str**| Document&#39;s folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**SaaSposeResponse**](SaaSposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_shapes_put_worksheet_shape**
> ShapeResponse cells_shapes_put_worksheet_shape(name, sheet_name, drawing_type, upper_left_row, upper_left_column, top, left, width, height, folder=folder, storage=storage)

Add shape in worksheet

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsShapesApi()
name = 'name_example' # str | document name.
sheet_name = 'sheet_name_example' # str | worksheet name.
drawing_type = 'drawing_type_example' # str | shape object type
upper_left_row = 56 # int | Upper left row index.
upper_left_column = 56 # int | Upper left column index.
top = 56 # int | Represents the vertical offset of Spinner from its left row, in unit of pixel.
left = 56 # int | Represents the horizontal offset of Spinner from its left column, in unit of pixel.
width = 56 # int | Represents the height of Spinner, in unit of pixel.
height = 56 # int | Represents the width of Spinner, in unit of pixel.
folder = 'folder_example' # str | Document's folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Add shape in worksheet
    api_response = api_instance.cells_shapes_put_worksheet_shape(name, sheet_name, drawing_type, upper_left_row, upper_left_column, top, left, width, height, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsShapesApi->cells_shapes_put_worksheet_shape: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| document name. | 
 **sheet_name** | **str**| worksheet name. | 
 **drawing_type** | **str**| shape object type | 
 **upper_left_row** | **int**| Upper left row index. | 
 **upper_left_column** | **int**| Upper left column index. | 
 **top** | **int**| Represents the vertical offset of Spinner from its left row, in unit of pixel. | 
 **left** | **int**| Represents the horizontal offset of Spinner from its left column, in unit of pixel. | 
 **width** | **int**| Represents the height of Spinner, in unit of pixel. | 
 **height** | **int**| Represents the width of Spinner, in unit of pixel. | 
 **folder** | **str**| Document&#39;s folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**ShapeResponse**](ShapeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

