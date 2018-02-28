# asposecellscloud.CellsPageBreaksApi

All URIs are relative to *https://api.aspose.cloud/v1.1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cells_page_breaks_delete_horizontal_page_break**](CellsPageBreaksApi.md#cells_page_breaks_delete_horizontal_page_break) | **DELETE** /cells/{name}/worksheets/{sheetName}/horizontalpagebreaks/{index} | 
[**cells_page_breaks_delete_horizontal_page_breaks**](CellsPageBreaksApi.md#cells_page_breaks_delete_horizontal_page_breaks) | **DELETE** /cells/{name}/worksheets/{sheetName}/horizontalpagebreaks | 
[**cells_page_breaks_delete_vertical_page_break**](CellsPageBreaksApi.md#cells_page_breaks_delete_vertical_page_break) | **DELETE** /cells/{name}/worksheets/{sheetName}/verticalpagebreaks/{index} | 
[**cells_page_breaks_delete_vertical_page_breaks**](CellsPageBreaksApi.md#cells_page_breaks_delete_vertical_page_breaks) | **DELETE** /cells/{name}/worksheets/{sheetName}/verticalpagebreaks | 
[**cells_page_breaks_get_horizontal_page_break**](CellsPageBreaksApi.md#cells_page_breaks_get_horizontal_page_break) | **GET** /cells/{name}/worksheets/{sheetName}/horizontalpagebreaks/{index} | 
[**cells_page_breaks_get_horizontal_page_breaks**](CellsPageBreaksApi.md#cells_page_breaks_get_horizontal_page_breaks) | **GET** /cells/{name}/worksheets/{sheetName}/horizontalpagebreaks | 
[**cells_page_breaks_get_vertical_page_break**](CellsPageBreaksApi.md#cells_page_breaks_get_vertical_page_break) | **GET** /cells/{name}/worksheets/{sheetName}/verticalpagebreaks/{index} | 
[**cells_page_breaks_get_vertical_page_breaks**](CellsPageBreaksApi.md#cells_page_breaks_get_vertical_page_breaks) | **GET** /cells/{name}/worksheets/{sheetName}/verticalpagebreaks | 
[**cells_page_breaks_put_horizontal_page_break**](CellsPageBreaksApi.md#cells_page_breaks_put_horizontal_page_break) | **PUT** /cells/{name}/worksheets/{sheetName}/horizontalpagebreaks | 
[**cells_page_breaks_put_vertical_page_break**](CellsPageBreaksApi.md#cells_page_breaks_put_vertical_page_break) | **PUT** /cells/{name}/worksheets/{sheetName}/verticalpagebreaks | 


# **cells_page_breaks_delete_horizontal_page_break**
> SaaSposeResponse cells_page_breaks_delete_horizontal_page_break(name, sheet_name, index, folder=folder)



### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsPageBreaksApi()
name = 'name_example' # str | 
sheet_name = 'sheet_name_example' # str | 
index = 56 # int | 
folder = 'folder_example' # str |  (optional)

try: 
    api_response = api_instance.cells_page_breaks_delete_horizontal_page_break(name, sheet_name, index, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsPageBreaksApi->cells_page_breaks_delete_horizontal_page_break: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **sheet_name** | **str**|  | 
 **index** | **int**|  | 
 **folder** | **str**|  | [optional] 

### Return type

[**SaaSposeResponse**](SaaSposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_page_breaks_delete_horizontal_page_breaks**
> SaaSposeResponse cells_page_breaks_delete_horizontal_page_breaks(name, sheet_name, row=row, folder=folder)



### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsPageBreaksApi()
name = 'name_example' # str | 
sheet_name = 'sheet_name_example' # str | 
row = 56 # int |  (optional)
folder = 'folder_example' # str |  (optional)

try: 
    api_response = api_instance.cells_page_breaks_delete_horizontal_page_breaks(name, sheet_name, row=row, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsPageBreaksApi->cells_page_breaks_delete_horizontal_page_breaks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **sheet_name** | **str**|  | 
 **row** | **int**|  | [optional] 
 **folder** | **str**|  | [optional] 

### Return type

[**SaaSposeResponse**](SaaSposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_page_breaks_delete_vertical_page_break**
> SaaSposeResponse cells_page_breaks_delete_vertical_page_break(name, sheet_name, index, folder=folder)



### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsPageBreaksApi()
name = 'name_example' # str | 
sheet_name = 'sheet_name_example' # str | 
index = 56 # int | 
folder = 'folder_example' # str |  (optional)

try: 
    api_response = api_instance.cells_page_breaks_delete_vertical_page_break(name, sheet_name, index, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsPageBreaksApi->cells_page_breaks_delete_vertical_page_break: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **sheet_name** | **str**|  | 
 **index** | **int**|  | 
 **folder** | **str**|  | [optional] 

### Return type

[**SaaSposeResponse**](SaaSposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_page_breaks_delete_vertical_page_breaks**
> SaaSposeResponse cells_page_breaks_delete_vertical_page_breaks(name, sheet_name, column=column, folder=folder)



### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsPageBreaksApi()
name = 'name_example' # str | 
sheet_name = 'sheet_name_example' # str | 
column = 56 # int |  (optional)
folder = 'folder_example' # str |  (optional)

try: 
    api_response = api_instance.cells_page_breaks_delete_vertical_page_breaks(name, sheet_name, column=column, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsPageBreaksApi->cells_page_breaks_delete_vertical_page_breaks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **sheet_name** | **str**|  | 
 **column** | **int**|  | [optional] 
 **folder** | **str**|  | [optional] 

### Return type

[**SaaSposeResponse**](SaaSposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_page_breaks_get_horizontal_page_break**
> HorizontalPageBreakResponse cells_page_breaks_get_horizontal_page_break(name, sheet_name, index, folder=folder)



### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsPageBreaksApi()
name = 'name_example' # str | 
sheet_name = 'sheet_name_example' # str | 
index = 56 # int | 
folder = 'folder_example' # str |  (optional)

try: 
    api_response = api_instance.cells_page_breaks_get_horizontal_page_break(name, sheet_name, index, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsPageBreaksApi->cells_page_breaks_get_horizontal_page_break: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **sheet_name** | **str**|  | 
 **index** | **int**|  | 
 **folder** | **str**|  | [optional] 

### Return type

[**HorizontalPageBreakResponse**](HorizontalPageBreakResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_page_breaks_get_horizontal_page_breaks**
> HorizontalPageBreaksResponse cells_page_breaks_get_horizontal_page_breaks(name, sheet_name, folder=folder)



### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsPageBreaksApi()
name = 'name_example' # str | 
sheet_name = 'sheet_name_example' # str | 
folder = 'folder_example' # str |  (optional)

try: 
    api_response = api_instance.cells_page_breaks_get_horizontal_page_breaks(name, sheet_name, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsPageBreaksApi->cells_page_breaks_get_horizontal_page_breaks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **sheet_name** | **str**|  | 
 **folder** | **str**|  | [optional] 

### Return type

[**HorizontalPageBreaksResponse**](HorizontalPageBreaksResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_page_breaks_get_vertical_page_break**
> VerticalPageBreakResponse cells_page_breaks_get_vertical_page_break(name, sheet_name, index, folder=folder)



### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsPageBreaksApi()
name = 'name_example' # str | 
sheet_name = 'sheet_name_example' # str | 
index = 56 # int | 
folder = 'folder_example' # str |  (optional)

try: 
    api_response = api_instance.cells_page_breaks_get_vertical_page_break(name, sheet_name, index, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsPageBreaksApi->cells_page_breaks_get_vertical_page_break: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **sheet_name** | **str**|  | 
 **index** | **int**|  | 
 **folder** | **str**|  | [optional] 

### Return type

[**VerticalPageBreakResponse**](VerticalPageBreakResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_page_breaks_get_vertical_page_breaks**
> VerticalPageBreaksResponse cells_page_breaks_get_vertical_page_breaks(name, sheet_name, folder=folder)



### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsPageBreaksApi()
name = 'name_example' # str | 
sheet_name = 'sheet_name_example' # str | 
folder = 'folder_example' # str |  (optional)

try: 
    api_response = api_instance.cells_page_breaks_get_vertical_page_breaks(name, sheet_name, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsPageBreaksApi->cells_page_breaks_get_vertical_page_breaks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **sheet_name** | **str**|  | 
 **folder** | **str**|  | [optional] 

### Return type

[**VerticalPageBreaksResponse**](VerticalPageBreaksResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_page_breaks_put_horizontal_page_break**
> SaaSposeResponse cells_page_breaks_put_horizontal_page_break(name, sheet_name, cellname=cellname, row=row, column=column, start_column=start_column, end_column=end_column, folder=folder)



### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsPageBreaksApi()
name = 'name_example' # str | 
sheet_name = 'sheet_name_example' # str | 
cellname = 'cellname_example' # str |  (optional)
row = 56 # int |  (optional)
column = 56 # int |  (optional)
start_column = 56 # int |  (optional)
end_column = 56 # int |  (optional)
folder = 'folder_example' # str |  (optional)

try: 
    api_response = api_instance.cells_page_breaks_put_horizontal_page_break(name, sheet_name, cellname=cellname, row=row, column=column, start_column=start_column, end_column=end_column, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsPageBreaksApi->cells_page_breaks_put_horizontal_page_break: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **sheet_name** | **str**|  | 
 **cellname** | **str**|  | [optional] 
 **row** | **int**|  | [optional] 
 **column** | **int**|  | [optional] 
 **start_column** | **int**|  | [optional] 
 **end_column** | **int**|  | [optional] 
 **folder** | **str**|  | [optional] 

### Return type

[**SaaSposeResponse**](SaaSposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_page_breaks_put_vertical_page_break**
> SaaSposeResponse cells_page_breaks_put_vertical_page_break(name, sheet_name, cellname=cellname, column=column, row=row, start_row=start_row, end_row=end_row, folder=folder)



### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsPageBreaksApi()
name = 'name_example' # str | 
sheet_name = 'sheet_name_example' # str | 
cellname = 'cellname_example' # str |  (optional)
column = 56 # int |  (optional)
row = 56 # int |  (optional)
start_row = 56 # int |  (optional)
end_row = 56 # int |  (optional)
folder = 'folder_example' # str |  (optional)

try: 
    api_response = api_instance.cells_page_breaks_put_vertical_page_break(name, sheet_name, cellname=cellname, column=column, row=row, start_row=start_row, end_row=end_row, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsPageBreaksApi->cells_page_breaks_put_vertical_page_break: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **sheet_name** | **str**|  | 
 **cellname** | **str**|  | [optional] 
 **column** | **int**|  | [optional] 
 **row** | **int**|  | [optional] 
 **start_row** | **int**|  | [optional] 
 **end_row** | **int**|  | [optional] 
 **folder** | **str**|  | [optional] 

### Return type

[**SaaSposeResponse**](SaaSposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

