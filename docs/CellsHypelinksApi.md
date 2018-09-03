# asposecellscloud.CellsHypelinksApi

All URIs are relative to *https://api.aspose.cloud/v1.1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cells_hypelinks_delete_worksheet_hyperlink**](CellsHypelinksApi.md#cells_hypelinks_delete_worksheet_hyperlink) | **DELETE** /cells/{name}/worksheets/{sheetName}/hyperlinks/{hyperlinkIndex} | Delete worksheet hyperlink by index.
[**cells_hypelinks_delete_worksheet_hyperlinks**](CellsHypelinksApi.md#cells_hypelinks_delete_worksheet_hyperlinks) | **DELETE** /cells/{name}/worksheets/{sheetName}/hyperlinks | Delete all hyperlinks in worksheet.
[**cells_hypelinks_get_worksheet_hyperlink**](CellsHypelinksApi.md#cells_hypelinks_get_worksheet_hyperlink) | **GET** /cells/{name}/worksheets/{sheetName}/hyperlinks/{hyperlinkIndex} | Get worksheet hyperlink by index.
[**cells_hypelinks_get_worksheet_hyperlinks**](CellsHypelinksApi.md#cells_hypelinks_get_worksheet_hyperlinks) | **GET** /cells/{name}/worksheets/{sheetName}/hyperlinks | Get worksheet hyperlinks.
[**cells_hypelinks_post_worksheet_hyperlink**](CellsHypelinksApi.md#cells_hypelinks_post_worksheet_hyperlink) | **POST** /cells/{name}/worksheets/{sheetName}/hyperlinks/{hyperlinkIndex} | Update worksheet hyperlink by index.
[**cells_hypelinks_put_worksheet_hyperlink**](CellsHypelinksApi.md#cells_hypelinks_put_worksheet_hyperlink) | **PUT** /cells/{name}/worksheets/{sheetName}/hyperlinks | Add worksheet hyperlink.


# **cells_hypelinks_delete_worksheet_hyperlink**
> SaaSposeResponse cells_hypelinks_delete_worksheet_hyperlink(name, sheet_name, hyperlink_index, folder=folder, storage=storage)

Delete worksheet hyperlink by index.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsHypelinksApi()
name = 'name_example' # str | Document name.
sheet_name = 'sheet_name_example' # str | Worksheet name.
hyperlink_index = 56 # int | The hyperlink's index.
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Delete worksheet hyperlink by index.
    api_response = api_instance.cells_hypelinks_delete_worksheet_hyperlink(name, sheet_name, hyperlink_index, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsHypelinksApi->cells_hypelinks_delete_worksheet_hyperlink: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document name. | 
 **sheet_name** | **str**| Worksheet name. | 
 **hyperlink_index** | **int**| The hyperlink&#39;s index. | 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**SaaSposeResponse**](SaaSposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_hypelinks_delete_worksheet_hyperlinks**
> SaaSposeResponse cells_hypelinks_delete_worksheet_hyperlinks(name, sheet_name, folder=folder, storage=storage)

Delete all hyperlinks in worksheet.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsHypelinksApi()
name = 'name_example' # str | Document name.
sheet_name = 'sheet_name_example' # str | Worksheet name.
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Delete all hyperlinks in worksheet.
    api_response = api_instance.cells_hypelinks_delete_worksheet_hyperlinks(name, sheet_name, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsHypelinksApi->cells_hypelinks_delete_worksheet_hyperlinks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document name. | 
 **sheet_name** | **str**| Worksheet name. | 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**SaaSposeResponse**](SaaSposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_hypelinks_get_worksheet_hyperlink**
> HyperlinkResponse cells_hypelinks_get_worksheet_hyperlink(name, sheet_name, hyperlink_index, folder=folder, storage=storage)

Get worksheet hyperlink by index.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsHypelinksApi()
name = 'name_example' # str | Document name.
sheet_name = 'sheet_name_example' # str | Worksheet name.
hyperlink_index = 56 # int | The hyperlink's index.
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Get worksheet hyperlink by index.
    api_response = api_instance.cells_hypelinks_get_worksheet_hyperlink(name, sheet_name, hyperlink_index, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsHypelinksApi->cells_hypelinks_get_worksheet_hyperlink: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document name. | 
 **sheet_name** | **str**| Worksheet name. | 
 **hyperlink_index** | **int**| The hyperlink&#39;s index. | 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**HyperlinkResponse**](HyperlinkResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_hypelinks_get_worksheet_hyperlinks**
> HyperlinksResponse cells_hypelinks_get_worksheet_hyperlinks(name, sheet_name, folder=folder, storage=storage)

Get worksheet hyperlinks.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsHypelinksApi()
name = 'name_example' # str | Document name.
sheet_name = 'sheet_name_example' # str | The worksheet name.
folder = 'folder_example' # str | Document's folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Get worksheet hyperlinks.
    api_response = api_instance.cells_hypelinks_get_worksheet_hyperlinks(name, sheet_name, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsHypelinksApi->cells_hypelinks_get_worksheet_hyperlinks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document name. | 
 **sheet_name** | **str**| The worksheet name. | 
 **folder** | **str**| Document&#39;s folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**HyperlinksResponse**](HyperlinksResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_hypelinks_post_worksheet_hyperlink**
> HyperlinkResponse cells_hypelinks_post_worksheet_hyperlink(name, sheet_name, hyperlink_index, hyperlink=hyperlink, folder=folder, storage=storage)

Update worksheet hyperlink by index.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsHypelinksApi()
name = 'name_example' # str | Document name.
sheet_name = 'sheet_name_example' # str | Worksheet name.
hyperlink_index = 56 # int | The hyperlink's index.
hyperlink = asposecellscloud.Hyperlink() # Hyperlink | Hyperlink object (optional)
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Update worksheet hyperlink by index.
    api_response = api_instance.cells_hypelinks_post_worksheet_hyperlink(name, sheet_name, hyperlink_index, hyperlink=hyperlink, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsHypelinksApi->cells_hypelinks_post_worksheet_hyperlink: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document name. | 
 **sheet_name** | **str**| Worksheet name. | 
 **hyperlink_index** | **int**| The hyperlink&#39;s index. | 
 **hyperlink** | [**Hyperlink**](Hyperlink.md)| Hyperlink object | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**HyperlinkResponse**](HyperlinkResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_hypelinks_put_worksheet_hyperlink**
> HyperlinkResponse cells_hypelinks_put_worksheet_hyperlink(name, sheet_name, first_row, first_column, total_rows, total_columns, address, folder=folder, storage=storage)

Add worksheet hyperlink.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsHypelinksApi()
name = 'name_example' # str | Document name.
sheet_name = 'sheet_name_example' # str | Worksheet name.
first_row = 56 # int | 
first_column = 56 # int | 
total_rows = 56 # int | 
total_columns = 56 # int | 
address = 'address_example' # str | 
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Add worksheet hyperlink.
    api_response = api_instance.cells_hypelinks_put_worksheet_hyperlink(name, sheet_name, first_row, first_column, total_rows, total_columns, address, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsHypelinksApi->cells_hypelinks_put_worksheet_hyperlink: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document name. | 
 **sheet_name** | **str**| Worksheet name. | 
 **first_row** | **int**|  | 
 **first_column** | **int**|  | 
 **total_rows** | **int**|  | 
 **total_columns** | **int**|  | 
 **address** | **str**|  | 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**HyperlinkResponse**](HyperlinkResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

