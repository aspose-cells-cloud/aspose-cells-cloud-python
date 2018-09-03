# asposecellscloud.CellsPivotTablesApi

All URIs are relative to *https://api.aspose.cloud/v1.1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cells_pivot_tables_delete_pivot_table_field**](CellsPivotTablesApi.md#cells_pivot_tables_delete_pivot_table_field) | **DELETE** /cells/{name}/worksheets/{sheetName}/pivottables/{pivotTableIndex}/PivotField | Delete pivot field into into pivot table
[**cells_pivot_tables_delete_worksheet_pivot_table**](CellsPivotTablesApi.md#cells_pivot_tables_delete_worksheet_pivot_table) | **DELETE** /cells/{name}/worksheets/{sheetName}/pivottables/{pivotTableIndex} | Delete worksheet pivot table by index
[**cells_pivot_tables_delete_worksheet_pivot_table_filter**](CellsPivotTablesApi.md#cells_pivot_tables_delete_worksheet_pivot_table_filter) | **DELETE** /cells/{name}/worksheets/{sheetName}/pivottables/{pivotTableIndex}/PivotFilters/{fieldIndex} | delete  pivot filter for piovt table             
[**cells_pivot_tables_delete_worksheet_pivot_table_filters**](CellsPivotTablesApi.md#cells_pivot_tables_delete_worksheet_pivot_table_filters) | **DELETE** /cells/{name}/worksheets/{sheetName}/pivottables/{pivotTableIndex}/PivotFilters | delete all pivot filters for piovt table
[**cells_pivot_tables_delete_worksheet_pivot_tables**](CellsPivotTablesApi.md#cells_pivot_tables_delete_worksheet_pivot_tables) | **DELETE** /cells/{name}/worksheets/{sheetName}/pivottables | Delete worksheet pivot tables
[**cells_pivot_tables_get_pivot_table_field**](CellsPivotTablesApi.md#cells_pivot_tables_get_pivot_table_field) | **GET** /cells/{name}/worksheets/{sheetName}/pivottables/{pivotTableIndex}/PivotField | Get pivot field into into pivot table
[**cells_pivot_tables_get_worksheet_pivot_table**](CellsPivotTablesApi.md#cells_pivot_tables_get_worksheet_pivot_table) | **GET** /cells/{name}/worksheets/{sheetName}/pivottables/{pivottableIndex} | Get worksheet pivottable info by index.
[**cells_pivot_tables_get_worksheet_pivot_table_filter**](CellsPivotTablesApi.md#cells_pivot_tables_get_worksheet_pivot_table_filter) | **GET** /cells/{name}/worksheets/{sheetName}/pivottables/{pivotTableIndex}/PivotFilters/{filterIndex} | 
[**cells_pivot_tables_get_worksheet_pivot_table_filters**](CellsPivotTablesApi.md#cells_pivot_tables_get_worksheet_pivot_table_filters) | **GET** /cells/{name}/worksheets/{sheetName}/pivottables/{pivotTableIndex}/PivotFilters | 
[**cells_pivot_tables_get_worksheet_pivot_tables**](CellsPivotTablesApi.md#cells_pivot_tables_get_worksheet_pivot_tables) | **GET** /cells/{name}/worksheets/{sheetName}/pivottables | Get worksheet pivottables info.
[**cells_pivot_tables_post_pivot_table_cell_style**](CellsPivotTablesApi.md#cells_pivot_tables_post_pivot_table_cell_style) | **POST** /cells/{name}/worksheets/{sheetName}/pivottables/{pivotTableIndex}/Format | Update cell style for pivot table
[**cells_pivot_tables_post_pivot_table_field_hide_item**](CellsPivotTablesApi.md#cells_pivot_tables_post_pivot_table_field_hide_item) | **POST** /cells/{name}/worksheets/{sheetName}/pivottables/{pivotTableIndex}/PivotField/Hide | 
[**cells_pivot_tables_post_pivot_table_field_move_to**](CellsPivotTablesApi.md#cells_pivot_tables_post_pivot_table_field_move_to) | **POST** /cells/{name}/worksheets/{sheetName}/pivottables/{pivotTableIndex}/PivotField/Move | 
[**cells_pivot_tables_post_pivot_table_style**](CellsPivotTablesApi.md#cells_pivot_tables_post_pivot_table_style) | **POST** /cells/{name}/worksheets/{sheetName}/pivottables/{pivotTableIndex}/FormatAll | Update style for pivot table
[**cells_pivot_tables_post_worksheet_pivot_table_calculate**](CellsPivotTablesApi.md#cells_pivot_tables_post_worksheet_pivot_table_calculate) | **POST** /cells/{name}/worksheets/{sheetName}/pivottables/{pivotTableIndex}/Calculate | Calculates pivottable&#39;s data to cells.
[**cells_pivot_tables_post_worksheet_pivot_table_move**](CellsPivotTablesApi.md#cells_pivot_tables_post_worksheet_pivot_table_move) | **POST** /cells/{name}/worksheets/{sheetName}/pivottables/{pivotTableIndex}/Move | 
[**cells_pivot_tables_put_pivot_table_field**](CellsPivotTablesApi.md#cells_pivot_tables_put_pivot_table_field) | **PUT** /cells/{name}/worksheets/{sheetName}/pivottables/{pivotTableIndex}/PivotField | Add pivot field into into pivot table
[**cells_pivot_tables_put_worksheet_pivot_table**](CellsPivotTablesApi.md#cells_pivot_tables_put_worksheet_pivot_table) | **PUT** /cells/{name}/worksheets/{sheetName}/pivottables | Add a pivot table into worksheet.
[**cells_pivot_tables_put_worksheet_pivot_table_filter**](CellsPivotTablesApi.md#cells_pivot_tables_put_worksheet_pivot_table_filter) | **PUT** /cells/{name}/worksheets/{sheetName}/pivottables/{pivotTableIndex}/PivotFilters | Add pivot filter for piovt table index


# **cells_pivot_tables_delete_pivot_table_field**
> SaaSposeResponse cells_pivot_tables_delete_pivot_table_field(name, sheet_name, pivot_table_index, pivot_field_type, request=request, folder=folder, storage=storage)

Delete pivot field into into pivot table

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsPivotTablesApi()
name = 'name_example' # str | Document name.
sheet_name = 'sheet_name_example' # str | The worksheet name.
pivot_table_index = 56 # int | Pivot table index
pivot_field_type = 'pivot_field_type_example' # str | The fields area type.
request = asposecellscloud.PivotTableFieldRequest() # PivotTableFieldRequest | Dto that conrains field indexes (optional)
folder = 'folder_example' # str | Document's folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Delete pivot field into into pivot table
    api_response = api_instance.cells_pivot_tables_delete_pivot_table_field(name, sheet_name, pivot_table_index, pivot_field_type, request=request, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsPivotTablesApi->cells_pivot_tables_delete_pivot_table_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document name. | 
 **sheet_name** | **str**| The worksheet name. | 
 **pivot_table_index** | **int**| Pivot table index | 
 **pivot_field_type** | **str**| The fields area type. | 
 **request** | [**PivotTableFieldRequest**](PivotTableFieldRequest.md)| Dto that conrains field indexes | [optional] 
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

# **cells_pivot_tables_delete_worksheet_pivot_table**
> SaaSposeResponse cells_pivot_tables_delete_worksheet_pivot_table(name, sheet_name, pivot_table_index, folder=folder, storage=storage)

Delete worksheet pivot table by index

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsPivotTablesApi()
name = 'name_example' # str | Document name.
sheet_name = 'sheet_name_example' # str | The worksheet name.
pivot_table_index = 56 # int | Pivot table index
folder = 'folder_example' # str | Document's folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Delete worksheet pivot table by index
    api_response = api_instance.cells_pivot_tables_delete_worksheet_pivot_table(name, sheet_name, pivot_table_index, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsPivotTablesApi->cells_pivot_tables_delete_worksheet_pivot_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document name. | 
 **sheet_name** | **str**| The worksheet name. | 
 **pivot_table_index** | **int**| Pivot table index | 
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

# **cells_pivot_tables_delete_worksheet_pivot_table_filter**
> SaaSposeResponse cells_pivot_tables_delete_worksheet_pivot_table_filter(name, sheet_name, pivot_table_index, field_index, need_re_calculate=need_re_calculate, folder=folder, storage=storage)

delete  pivot filter for piovt table             

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsPivotTablesApi()
name = 'name_example' # str | 
sheet_name = 'sheet_name_example' # str | 
pivot_table_index = 56 # int | 
field_index = 56 # int | 
need_re_calculate = false # bool |  (optional) (default to false)
folder = 'folder_example' # str |  (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # delete  pivot filter for piovt table             
    api_response = api_instance.cells_pivot_tables_delete_worksheet_pivot_table_filter(name, sheet_name, pivot_table_index, field_index, need_re_calculate=need_re_calculate, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsPivotTablesApi->cells_pivot_tables_delete_worksheet_pivot_table_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **sheet_name** | **str**|  | 
 **pivot_table_index** | **int**|  | 
 **field_index** | **int**|  | 
 **need_re_calculate** | **bool**|  | [optional] [default to false]
 **folder** | **str**|  | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**SaaSposeResponse**](SaaSposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_pivot_tables_delete_worksheet_pivot_table_filters**
> SaaSposeResponse cells_pivot_tables_delete_worksheet_pivot_table_filters(name, sheet_name, pivot_table_index, need_re_calculate=need_re_calculate, folder=folder, storage=storage)

delete all pivot filters for piovt table

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsPivotTablesApi()
name = 'name_example' # str | 
sheet_name = 'sheet_name_example' # str | 
pivot_table_index = 56 # int | 
need_re_calculate = false # bool |  (optional) (default to false)
folder = 'folder_example' # str |  (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # delete all pivot filters for piovt table
    api_response = api_instance.cells_pivot_tables_delete_worksheet_pivot_table_filters(name, sheet_name, pivot_table_index, need_re_calculate=need_re_calculate, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsPivotTablesApi->cells_pivot_tables_delete_worksheet_pivot_table_filters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **sheet_name** | **str**|  | 
 **pivot_table_index** | **int**|  | 
 **need_re_calculate** | **bool**|  | [optional] [default to false]
 **folder** | **str**|  | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**SaaSposeResponse**](SaaSposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_pivot_tables_delete_worksheet_pivot_tables**
> SaaSposeResponse cells_pivot_tables_delete_worksheet_pivot_tables(name, sheet_name, folder=folder, storage=storage)

Delete worksheet pivot tables

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsPivotTablesApi()
name = 'name_example' # str | Document name.
sheet_name = 'sheet_name_example' # str | The worksheet name.
folder = 'folder_example' # str | Document's folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Delete worksheet pivot tables
    api_response = api_instance.cells_pivot_tables_delete_worksheet_pivot_tables(name, sheet_name, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsPivotTablesApi->cells_pivot_tables_delete_worksheet_pivot_tables: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document name. | 
 **sheet_name** | **str**| The worksheet name. | 
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

# **cells_pivot_tables_get_pivot_table_field**
> PivotFieldResponse cells_pivot_tables_get_pivot_table_field(name, sheet_name, pivot_table_index, pivot_field_index, pivot_field_type, folder=folder, storage=storage)

Get pivot field into into pivot table

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsPivotTablesApi()
name = 'name_example' # str | Document name.
sheet_name = 'sheet_name_example' # str | The worksheet name.
pivot_table_index = 56 # int | Pivot table index
pivot_field_index = 56 # int | The field index in the base fields.
pivot_field_type = 'pivot_field_type_example' # str | The fields area type.
folder = 'folder_example' # str | Document's folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Get pivot field into into pivot table
    api_response = api_instance.cells_pivot_tables_get_pivot_table_field(name, sheet_name, pivot_table_index, pivot_field_index, pivot_field_type, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsPivotTablesApi->cells_pivot_tables_get_pivot_table_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document name. | 
 **sheet_name** | **str**| The worksheet name. | 
 **pivot_table_index** | **int**| Pivot table index | 
 **pivot_field_index** | **int**| The field index in the base fields. | 
 **pivot_field_type** | **str**| The fields area type. | 
 **folder** | **str**| Document&#39;s folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**PivotFieldResponse**](PivotFieldResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_pivot_tables_get_worksheet_pivot_table**
> PivotTableResponse cells_pivot_tables_get_worksheet_pivot_table(name, sheet_name, pivottable_index, folder=folder, storage=storage)

Get worksheet pivottable info by index.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsPivotTablesApi()
name = 'name_example' # str | Document name.
sheet_name = 'sheet_name_example' # str | The worksheet name.
pivottable_index = 56 # int | 
folder = 'folder_example' # str | Document's folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Get worksheet pivottable info by index.
    api_response = api_instance.cells_pivot_tables_get_worksheet_pivot_table(name, sheet_name, pivottable_index, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsPivotTablesApi->cells_pivot_tables_get_worksheet_pivot_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document name. | 
 **sheet_name** | **str**| The worksheet name. | 
 **pivottable_index** | **int**|  | 
 **folder** | **str**| Document&#39;s folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**PivotTableResponse**](PivotTableResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_pivot_tables_get_worksheet_pivot_table_filter**
> PivotFilterResponse cells_pivot_tables_get_worksheet_pivot_table_filter(name, sheet_name, pivot_table_index, filter_index, folder=folder, storage=storage)



### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsPivotTablesApi()
name = 'name_example' # str | 
sheet_name = 'sheet_name_example' # str | 
pivot_table_index = 56 # int | 
filter_index = 56 # int | 
folder = 'folder_example' # str |  (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    api_response = api_instance.cells_pivot_tables_get_worksheet_pivot_table_filter(name, sheet_name, pivot_table_index, filter_index, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsPivotTablesApi->cells_pivot_tables_get_worksheet_pivot_table_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **sheet_name** | **str**|  | 
 **pivot_table_index** | **int**|  | 
 **filter_index** | **int**|  | 
 **folder** | **str**|  | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**PivotFilterResponse**](PivotFilterResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_pivot_tables_get_worksheet_pivot_table_filters**
> PivotFiltersResponse cells_pivot_tables_get_worksheet_pivot_table_filters(name, sheet_name, pivot_table_index, folder=folder, storage=storage)



### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsPivotTablesApi()
name = 'name_example' # str | 
sheet_name = 'sheet_name_example' # str | 
pivot_table_index = 56 # int | 
folder = 'folder_example' # str |  (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    api_response = api_instance.cells_pivot_tables_get_worksheet_pivot_table_filters(name, sheet_name, pivot_table_index, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsPivotTablesApi->cells_pivot_tables_get_worksheet_pivot_table_filters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **sheet_name** | **str**|  | 
 **pivot_table_index** | **int**|  | 
 **folder** | **str**|  | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**PivotFiltersResponse**](PivotFiltersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_pivot_tables_get_worksheet_pivot_tables**
> PivotTablesResponse cells_pivot_tables_get_worksheet_pivot_tables(name, sheet_name, folder=folder, storage=storage)

Get worksheet pivottables info.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsPivotTablesApi()
name = 'name_example' # str | Document name.
sheet_name = 'sheet_name_example' # str | The worksheet name.
folder = 'folder_example' # str | Document's folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Get worksheet pivottables info.
    api_response = api_instance.cells_pivot_tables_get_worksheet_pivot_tables(name, sheet_name, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsPivotTablesApi->cells_pivot_tables_get_worksheet_pivot_tables: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document name. | 
 **sheet_name** | **str**| The worksheet name. | 
 **folder** | **str**| Document&#39;s folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**PivotTablesResponse**](PivotTablesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_pivot_tables_post_pivot_table_cell_style**
> SaaSposeResponse cells_pivot_tables_post_pivot_table_cell_style(name, sheet_name, pivot_table_index, column, row, style=style, need_re_calculate=need_re_calculate, folder=folder, storage=storage)

Update cell style for pivot table

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsPivotTablesApi()
name = 'name_example' # str | Document name.
sheet_name = 'sheet_name_example' # str | The worksheet name.
pivot_table_index = 56 # int | Pivot table index
column = 56 # int | 
row = 56 # int | 
style = asposecellscloud.Style() # Style | Style dto in request body. (optional)
need_re_calculate = false # bool |  (optional) (default to false)
folder = 'folder_example' # str | Document's folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Update cell style for pivot table
    api_response = api_instance.cells_pivot_tables_post_pivot_table_cell_style(name, sheet_name, pivot_table_index, column, row, style=style, need_re_calculate=need_re_calculate, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsPivotTablesApi->cells_pivot_tables_post_pivot_table_cell_style: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document name. | 
 **sheet_name** | **str**| The worksheet name. | 
 **pivot_table_index** | **int**| Pivot table index | 
 **column** | **int**|  | 
 **row** | **int**|  | 
 **style** | [**Style**](Style.md)| Style dto in request body. | [optional] 
 **need_re_calculate** | **bool**|  | [optional] [default to false]
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

# **cells_pivot_tables_post_pivot_table_field_hide_item**
> SaaSposeResponse cells_pivot_tables_post_pivot_table_field_hide_item(name, sheet_name, pivot_table_index, pivot_field_type, field_index, item_index, is_hide, need_re_calculate=need_re_calculate, folder=folder, storage=storage)



### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsPivotTablesApi()
name = 'name_example' # str | 
sheet_name = 'sheet_name_example' # str | 
pivot_table_index = 56 # int | 
pivot_field_type = 'pivot_field_type_example' # str | 
field_index = 56 # int | 
item_index = 56 # int | 
is_hide = true # bool | 
need_re_calculate = false # bool |  (optional) (default to false)
folder = 'folder_example' # str |  (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    api_response = api_instance.cells_pivot_tables_post_pivot_table_field_hide_item(name, sheet_name, pivot_table_index, pivot_field_type, field_index, item_index, is_hide, need_re_calculate=need_re_calculate, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsPivotTablesApi->cells_pivot_tables_post_pivot_table_field_hide_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **sheet_name** | **str**|  | 
 **pivot_table_index** | **int**|  | 
 **pivot_field_type** | **str**|  | 
 **field_index** | **int**|  | 
 **item_index** | **int**|  | 
 **is_hide** | **bool**|  | 
 **need_re_calculate** | **bool**|  | [optional] [default to false]
 **folder** | **str**|  | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**SaaSposeResponse**](SaaSposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_pivot_tables_post_pivot_table_field_move_to**
> SaaSposeResponse cells_pivot_tables_post_pivot_table_field_move_to(name, sheet_name, pivot_table_index, field_index, _from, to, folder=folder, storage=storage)



### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsPivotTablesApi()
name = 'name_example' # str | 
sheet_name = 'sheet_name_example' # str | 
pivot_table_index = 56 # int | 
field_index = 56 # int | 
_from = '_from_example' # str | 
to = 'to_example' # str | 
folder = 'folder_example' # str |  (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    api_response = api_instance.cells_pivot_tables_post_pivot_table_field_move_to(name, sheet_name, pivot_table_index, field_index, _from, to, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsPivotTablesApi->cells_pivot_tables_post_pivot_table_field_move_to: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **sheet_name** | **str**|  | 
 **pivot_table_index** | **int**|  | 
 **field_index** | **int**|  | 
 **_from** | **str**|  | 
 **to** | **str**|  | 
 **folder** | **str**|  | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**SaaSposeResponse**](SaaSposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_pivot_tables_post_pivot_table_style**
> SaaSposeResponse cells_pivot_tables_post_pivot_table_style(name, sheet_name, pivot_table_index, style=style, need_re_calculate=need_re_calculate, folder=folder, storage=storage)

Update style for pivot table

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsPivotTablesApi()
name = 'name_example' # str | Document name.
sheet_name = 'sheet_name_example' # str | The worksheet name.
pivot_table_index = 56 # int | Pivot table index
style = asposecellscloud.Style() # Style | Style dto in request body. (optional)
need_re_calculate = false # bool |  (optional) (default to false)
folder = 'folder_example' # str | Document's folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Update style for pivot table
    api_response = api_instance.cells_pivot_tables_post_pivot_table_style(name, sheet_name, pivot_table_index, style=style, need_re_calculate=need_re_calculate, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsPivotTablesApi->cells_pivot_tables_post_pivot_table_style: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document name. | 
 **sheet_name** | **str**| The worksheet name. | 
 **pivot_table_index** | **int**| Pivot table index | 
 **style** | [**Style**](Style.md)| Style dto in request body. | [optional] 
 **need_re_calculate** | **bool**|  | [optional] [default to false]
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

# **cells_pivot_tables_post_worksheet_pivot_table_calculate**
> SaaSposeResponse cells_pivot_tables_post_worksheet_pivot_table_calculate(name, sheet_name, pivot_table_index, folder=folder, storage=storage)

Calculates pivottable's data to cells.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsPivotTablesApi()
name = 'name_example' # str | Document name.
sheet_name = 'sheet_name_example' # str | The worksheet name.
pivot_table_index = 56 # int | Pivot table index
folder = 'folder_example' # str | Document's folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Calculates pivottable's data to cells.
    api_response = api_instance.cells_pivot_tables_post_worksheet_pivot_table_calculate(name, sheet_name, pivot_table_index, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsPivotTablesApi->cells_pivot_tables_post_worksheet_pivot_table_calculate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document name. | 
 **sheet_name** | **str**| The worksheet name. | 
 **pivot_table_index** | **int**| Pivot table index | 
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

# **cells_pivot_tables_post_worksheet_pivot_table_move**
> SaaSposeResponse cells_pivot_tables_post_worksheet_pivot_table_move(name, sheet_name, pivot_table_index, row=row, column=column, dest_cell_name=dest_cell_name, folder=folder, storage=storage)



### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsPivotTablesApi()
name = 'name_example' # str | 
sheet_name = 'sheet_name_example' # str | 
pivot_table_index = 56 # int | 
row = 56 # int |  (optional)
column = 56 # int |  (optional)
dest_cell_name = 'dest_cell_name_example' # str |  (optional)
folder = 'folder_example' # str |  (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    api_response = api_instance.cells_pivot_tables_post_worksheet_pivot_table_move(name, sheet_name, pivot_table_index, row=row, column=column, dest_cell_name=dest_cell_name, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsPivotTablesApi->cells_pivot_tables_post_worksheet_pivot_table_move: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **sheet_name** | **str**|  | 
 **pivot_table_index** | **int**|  | 
 **row** | **int**|  | [optional] 
 **column** | **int**|  | [optional] 
 **dest_cell_name** | **str**|  | [optional] 
 **folder** | **str**|  | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**SaaSposeResponse**](SaaSposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_pivot_tables_put_pivot_table_field**
> SaaSposeResponse cells_pivot_tables_put_pivot_table_field(name, sheet_name, pivot_table_index, pivot_field_type, request=request, need_re_calculate=need_re_calculate, folder=folder, storage=storage)

Add pivot field into into pivot table

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsPivotTablesApi()
name = 'name_example' # str | Document name.
sheet_name = 'sheet_name_example' # str | The worksheet name.
pivot_table_index = 56 # int | Pivot table index
pivot_field_type = 'pivot_field_type_example' # str | The fields area type.
request = asposecellscloud.PivotTableFieldRequest() # PivotTableFieldRequest | Dto that conrains field indexes (optional)
need_re_calculate = false # bool |  (optional) (default to false)
folder = 'folder_example' # str | Document's folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Add pivot field into into pivot table
    api_response = api_instance.cells_pivot_tables_put_pivot_table_field(name, sheet_name, pivot_table_index, pivot_field_type, request=request, need_re_calculate=need_re_calculate, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsPivotTablesApi->cells_pivot_tables_put_pivot_table_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document name. | 
 **sheet_name** | **str**| The worksheet name. | 
 **pivot_table_index** | **int**| Pivot table index | 
 **pivot_field_type** | **str**| The fields area type. | 
 **request** | [**PivotTableFieldRequest**](PivotTableFieldRequest.md)| Dto that conrains field indexes | [optional] 
 **need_re_calculate** | **bool**|  | [optional] [default to false]
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

# **cells_pivot_tables_put_worksheet_pivot_table**
> PivotTableResponse cells_pivot_tables_put_worksheet_pivot_table(name, sheet_name, request=request, folder=folder, storage=storage, source_data=source_data, dest_cell_name=dest_cell_name, table_name=table_name, use_same_source=use_same_source)

Add a pivot table into worksheet.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsPivotTablesApi()
name = 'name_example' # str | Document name.
sheet_name = 'sheet_name_example' # str | The worksheet name.
request = asposecellscloud.CreatePivotTableRequest() # CreatePivotTableRequest | CreatePivotTableRequest dto in request body. (optional)
folder = 'folder_example' # str | Document's folder. (optional)
storage = 'storage_example' # str | storage name. (optional)
source_data = 'source_data_example' # str | The data for the new PivotTable cache. (optional)
dest_cell_name = 'dest_cell_name_example' # str | The cell in the upper-left corner of the PivotTable report's destination range. (optional)
table_name = 'table_name_example' # str | The name of the new PivotTable report. (optional)
use_same_source = true # bool | Indicates whether using same data source when another existing pivot table has used this data source. If the property is true, it will save memory. (optional)

try: 
    # Add a pivot table into worksheet.
    api_response = api_instance.cells_pivot_tables_put_worksheet_pivot_table(name, sheet_name, request=request, folder=folder, storage=storage, source_data=source_data, dest_cell_name=dest_cell_name, table_name=table_name, use_same_source=use_same_source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsPivotTablesApi->cells_pivot_tables_put_worksheet_pivot_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document name. | 
 **sheet_name** | **str**| The worksheet name. | 
 **request** | [**CreatePivotTableRequest**](CreatePivotTableRequest.md)| CreatePivotTableRequest dto in request body. | [optional] 
 **folder** | **str**| Document&#39;s folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 
 **source_data** | **str**| The data for the new PivotTable cache. | [optional] 
 **dest_cell_name** | **str**| The cell in the upper-left corner of the PivotTable report&#39;s destination range. | [optional] 
 **table_name** | **str**| The name of the new PivotTable report. | [optional] 
 **use_same_source** | **bool**| Indicates whether using same data source when another existing pivot table has used this data source. If the property is true, it will save memory. | [optional] 

### Return type

[**PivotTableResponse**](PivotTableResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_pivot_tables_put_worksheet_pivot_table_filter**
> SaaSposeResponse cells_pivot_tables_put_worksheet_pivot_table_filter(name, sheet_name, pivot_table_index, filter=filter, need_re_calculate=need_re_calculate, folder=folder, storage=storage)

Add pivot filter for piovt table index

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsPivotTablesApi()
name = 'name_example' # str | 
sheet_name = 'sheet_name_example' # str | 
pivot_table_index = 56 # int | 
filter = asposecellscloud.PivotFilter() # PivotFilter |  (optional)
need_re_calculate = false # bool |  (optional) (default to false)
folder = 'folder_example' # str |  (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Add pivot filter for piovt table index
    api_response = api_instance.cells_pivot_tables_put_worksheet_pivot_table_filter(name, sheet_name, pivot_table_index, filter=filter, need_re_calculate=need_re_calculate, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsPivotTablesApi->cells_pivot_tables_put_worksheet_pivot_table_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **sheet_name** | **str**|  | 
 **pivot_table_index** | **int**|  | 
 **filter** | [**PivotFilter**](PivotFilter.md)|  | [optional] 
 **need_re_calculate** | **bool**|  | [optional] [default to false]
 **folder** | **str**|  | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**SaaSposeResponse**](SaaSposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

