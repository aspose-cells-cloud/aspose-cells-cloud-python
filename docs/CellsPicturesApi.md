# asposecellscloud.CellsPicturesApi

All URIs are relative to *https://api.aspose.cloud/v1.1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cells_pictures_delete_worksheet_picture**](CellsPicturesApi.md#cells_pictures_delete_worksheet_picture) | **DELETE** /cells/{name}/worksheets/{sheetName}/pictures/{pictureIndex} | Delete a picture object in worksheet
[**cells_pictures_delete_worksheet_pictures**](CellsPicturesApi.md#cells_pictures_delete_worksheet_pictures) | **DELETE** /cells/{name}/worksheets/{sheetName}/pictures | Delete all pictures in worksheet.
[**cells_pictures_get_worksheet_picture**](CellsPicturesApi.md#cells_pictures_get_worksheet_picture) | **GET** /cells/{name}/worksheets/{sheetName}/pictures/{pictureNumber} | GRead worksheet picture by number.
[**cells_pictures_get_worksheet_pictures**](CellsPicturesApi.md#cells_pictures_get_worksheet_pictures) | **GET** /cells/{name}/worksheets/{sheetName}/pictures | Read worksheet pictures.
[**cells_pictures_post_worksheet_picture**](CellsPicturesApi.md#cells_pictures_post_worksheet_picture) | **POST** /cells/{name}/worksheets/{sheetName}/pictures/{pictureIndex} | Update worksheet picture by index.
[**cells_pictures_put_worksheet_add_picture**](CellsPicturesApi.md#cells_pictures_put_worksheet_add_picture) | **PUT** /cells/{name}/worksheets/{sheetName}/pictures | Add a new worksheet picture.


# **cells_pictures_delete_worksheet_picture**
> SaaSposeResponse cells_pictures_delete_worksheet_picture(name, sheet_name, picture_index, folder=folder)

Delete a picture object in worksheet

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsPicturesApi()
name = 'name_example' # str | The workbook name.
sheet_name = 'sheet_name_example' # str | The worsheet name.
picture_index = 56 # int | Picture index
folder = 'folder_example' # str | The workbook folder. (optional)

try: 
    # Delete a picture object in worksheet
    api_response = api_instance.cells_pictures_delete_worksheet_picture(name, sheet_name, picture_index, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsPicturesApi->cells_pictures_delete_worksheet_picture: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The workbook name. | 
 **sheet_name** | **str**| The worsheet name. | 
 **picture_index** | **int**| Picture index | 
 **folder** | **str**| The workbook folder. | [optional] 

### Return type

[**SaaSposeResponse**](SaaSposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_pictures_delete_worksheet_pictures**
> SaaSposeResponse cells_pictures_delete_worksheet_pictures(name, sheet_name, folder=folder)

Delete all pictures in worksheet.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsPicturesApi()
name = 'name_example' # str | Document name.
sheet_name = 'sheet_name_example' # str | Worksheet name.
folder = 'folder_example' # str | The document folder. (optional)

try: 
    # Delete all pictures in worksheet.
    api_response = api_instance.cells_pictures_delete_worksheet_pictures(name, sheet_name, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsPicturesApi->cells_pictures_delete_worksheet_pictures: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document name. | 
 **sheet_name** | **str**| Worksheet name. | 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**SaaSposeResponse**](SaaSposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_pictures_get_worksheet_picture**
> file cells_pictures_get_worksheet_picture(name, sheet_name, picture_number, folder=folder)

GRead worksheet picture by number.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsPicturesApi()
name = 'name_example' # str | Document name.
sheet_name = 'sheet_name_example' # str | Worksheet name.
picture_number = 56 # int | The picture number.
folder = 'folder_example' # str | The document folder. (optional)

try: 
    # GRead worksheet picture by number.
    api_response = api_instance.cells_pictures_get_worksheet_picture(name, sheet_name, picture_number, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsPicturesApi->cells_pictures_get_worksheet_picture: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document name. | 
 **sheet_name** | **str**| Worksheet name. | 
 **picture_number** | **int**| The picture number. | 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_pictures_get_worksheet_pictures**
> PicturesResponse cells_pictures_get_worksheet_pictures(name, sheet_name, folder=folder)

Read worksheet pictures.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsPicturesApi()
name = 'name_example' # str | Document name.
sheet_name = 'sheet_name_example' # str | The worksheet name.
folder = 'folder_example' # str | Document's folder. (optional)

try: 
    # Read worksheet pictures.
    api_response = api_instance.cells_pictures_get_worksheet_pictures(name, sheet_name, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsPicturesApi->cells_pictures_get_worksheet_pictures: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document name. | 
 **sheet_name** | **str**| The worksheet name. | 
 **folder** | **str**| Document&#39;s folder. | [optional] 

### Return type

[**PicturesResponse**](PicturesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_pictures_post_worksheet_picture**
> PictureResponse cells_pictures_post_worksheet_picture(name, sheet_name, picture_index, picture=picture, folder=folder)

Update worksheet picture by index.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsPicturesApi()
name = 'name_example' # str | Document name.
sheet_name = 'sheet_name_example' # str | Worksheet name.
picture_index = 56 # int | The picture's index.
picture = asposecellscloud.Picture() # Picture | Picture object (optional)
folder = 'folder_example' # str | The document folder. (optional)

try: 
    # Update worksheet picture by index.
    api_response = api_instance.cells_pictures_post_worksheet_picture(name, sheet_name, picture_index, picture=picture, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsPicturesApi->cells_pictures_post_worksheet_picture: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document name. | 
 **sheet_name** | **str**| Worksheet name. | 
 **picture_index** | **int**| The picture&#39;s index. | 
 **picture** | [**Picture**](Picture.md)| Picture object | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**PictureResponse**](PictureResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_pictures_put_worksheet_add_picture**
> PicturesResponse cells_pictures_put_worksheet_add_picture(name, sheet_name, picture=picture, upper_left_row=upper_left_row, upper_left_column=upper_left_column, lower_right_row=lower_right_row, lower_right_column=lower_right_column, picture_path=picture_path, folder=folder)

Add a new worksheet picture.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsPicturesApi()
name = 'name_example' # str | The workbook name.
sheet_name = 'sheet_name_example' # str | The worsheet name.
picture = asposecellscloud.Picture() # Picture | Pictute object (optional)
upper_left_row = 0 # int | The image upper left row. (optional) (default to 0)
upper_left_column = 0 # int | The image upper left column. (optional) (default to 0)
lower_right_row = 0 # int | The image low right row. (optional) (default to 0)
lower_right_column = 0 # int | The image low right column. (optional) (default to 0)
picture_path = 'picture_path_example' # str | The picture path, if not provided the picture data is inspected in the request body. (optional)
folder = 'folder_example' # str | The workbook folder. (optional)

try: 
    # Add a new worksheet picture.
    api_response = api_instance.cells_pictures_put_worksheet_add_picture(name, sheet_name, picture=picture, upper_left_row=upper_left_row, upper_left_column=upper_left_column, lower_right_row=lower_right_row, lower_right_column=lower_right_column, picture_path=picture_path, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsPicturesApi->cells_pictures_put_worksheet_add_picture: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The workbook name. | 
 **sheet_name** | **str**| The worsheet name. | 
 **picture** | [**Picture**](Picture.md)| Pictute object | [optional] 
 **upper_left_row** | **int**| The image upper left row. | [optional] [default to 0]
 **upper_left_column** | **int**| The image upper left column. | [optional] [default to 0]
 **lower_right_row** | **int**| The image low right row. | [optional] [default to 0]
 **lower_right_column** | **int**| The image low right column. | [optional] [default to 0]
 **picture_path** | **str**| The picture path, if not provided the picture data is inspected in the request body. | [optional] 
 **folder** | **str**| The workbook folder. | [optional] 

### Return type

[**PicturesResponse**](PicturesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

