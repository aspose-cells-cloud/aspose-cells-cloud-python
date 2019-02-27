# asposecellscloud.CellsApi

All URIs are relative to *https://api.aspose.cloud/v1.1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cells_delete_worksheet_columns**](CellsApi.md#cells_delete_worksheet_columns) | **DELETE** /cells/{name}/worksheets/{sheetName}/cells/columns/{columnIndex} | Delete worksheet columns.
[**cells_delete_worksheet_row**](CellsApi.md#cells_delete_worksheet_row) | **DELETE** /cells/{name}/worksheets/{sheetName}/cells/rows/{rowIndex} | Delete worksheet row.
[**cells_delete_worksheet_rows**](CellsApi.md#cells_delete_worksheet_rows) | **DELETE** /cells/{name}/worksheets/{sheetName}/cells/rows | Delete several worksheet rows.
[**cells_get_cell_html_string**](CellsApi.md#cells_get_cell_html_string) | **GET** /cells/{name}/worksheets/{sheetName}/cells/{cellName}/htmlstring | Read cell data by cell&#39;s name.
[**cells_get_worksheet_cell**](CellsApi.md#cells_get_worksheet_cell) | **GET** /cells/{name}/worksheets/{sheetName}/cells/{cellOrMethodName} | Read cell data by cell&#39;s name.
[**cells_get_worksheet_cell_style**](CellsApi.md#cells_get_worksheet_cell_style) | **GET** /cells/{name}/worksheets/{sheetName}/cells/{cellName}/style | Read cell&#39;s style info.
[**cells_get_worksheet_cells**](CellsApi.md#cells_get_worksheet_cells) | **GET** /cells/{name}/worksheets/{sheetName}/cells | Get cells info.
[**cells_get_worksheet_column**](CellsApi.md#cells_get_worksheet_column) | **GET** /cells/{name}/worksheets/{sheetName}/cells/columns/{columnIndex} | Read worksheet column data by column&#39;s index.
[**cells_get_worksheet_columns**](CellsApi.md#cells_get_worksheet_columns) | **GET** /cells/{name}/worksheets/{sheetName}/cells/columns | Read worksheet columns info.
[**cells_get_worksheet_row**](CellsApi.md#cells_get_worksheet_row) | **GET** /cells/{name}/worksheets/{sheetName}/cells/rows/{rowIndex} | Read worksheet row data by row&#39;s index.
[**cells_get_worksheet_rows**](CellsApi.md#cells_get_worksheet_rows) | **GET** /cells/{name}/worksheets/{sheetName}/cells/rows | Read worksheet rows info.
[**cells_post_cell_calculate**](CellsApi.md#cells_post_cell_calculate) | **POST** /cells/{name}/worksheets/{sheetName}/cells/{cellName}/calculate | Cell calculate formula
[**cells_post_cell_characters**](CellsApi.md#cells_post_cell_characters) | **POST** /cells/{name}/worksheets/{sheetName}/cells/{cellName}/characters | Set cell characters 
[**cells_post_clear_contents**](CellsApi.md#cells_post_clear_contents) | **POST** /cells/{name}/worksheets/{sheetName}/cells/clearcontents | Clear cells contents.
[**cells_post_clear_formats**](CellsApi.md#cells_post_clear_formats) | **POST** /cells/{name}/worksheets/{sheetName}/cells/clearformats | Clear cells contents.
[**cells_post_column_style**](CellsApi.md#cells_post_column_style) | **POST** /cells/{name}/worksheets/{sheetName}/cells/columns/{columnIndex}/style | Set column style
[**cells_post_copy_cell_into_cell**](CellsApi.md#cells_post_copy_cell_into_cell) | **POST** /cells/{name}/worksheets/{sheetName}/cells/{destCellName}/copy | Copy cell into cell
[**cells_post_copy_worksheet_columns**](CellsApi.md#cells_post_copy_worksheet_columns) | **POST** /cells/{name}/worksheets/{sheetName}/cells/columns/copy | Copy worksheet columns.
[**cells_post_copy_worksheet_rows**](CellsApi.md#cells_post_copy_worksheet_rows) | **POST** /cells/{name}/worksheets/{sheetName}/cells/rows/copy | Copy worksheet rows.
[**cells_post_group_worksheet_columns**](CellsApi.md#cells_post_group_worksheet_columns) | **POST** /cells/{name}/worksheets/{sheetName}/cells/columns/group | Group worksheet columns.
[**cells_post_group_worksheet_rows**](CellsApi.md#cells_post_group_worksheet_rows) | **POST** /cells/{name}/worksheets/{sheetName}/cells/rows/group | Group worksheet rows.
[**cells_post_hide_worksheet_columns**](CellsApi.md#cells_post_hide_worksheet_columns) | **POST** /cells/{name}/worksheets/{sheetName}/cells/columns/hide | Hide worksheet columns.
[**cells_post_hide_worksheet_rows**](CellsApi.md#cells_post_hide_worksheet_rows) | **POST** /cells/{name}/worksheets/{sheetName}/cells/rows/hide | Hide worksheet rows.
[**cells_post_row_style**](CellsApi.md#cells_post_row_style) | **POST** /cells/{name}/worksheets/{sheetName}/cells/rows/{rowIndex}/style | Set row style.
[**cells_post_set_cell_html_string**](CellsApi.md#cells_post_set_cell_html_string) | **POST** /cells/{name}/worksheets/{sheetName}/cells/{cellName}/htmlstring | Set htmlstring value into cell
[**cells_post_set_cell_range_value**](CellsApi.md#cells_post_set_cell_range_value) | **POST** /cells/{name}/worksheets/{sheetName}/cells | Set cell range value 
[**cells_post_set_worksheet_column_width**](CellsApi.md#cells_post_set_worksheet_column_width) | **POST** /cells/{name}/worksheets/{sheetName}/cells/columns/{columnIndex} | Set worksheet column width.
[**cells_post_ungroup_worksheet_columns**](CellsApi.md#cells_post_ungroup_worksheet_columns) | **POST** /cells/{name}/worksheets/{sheetName}/cells/columns/ungroup | Ungroup worksheet columns.
[**cells_post_ungroup_worksheet_rows**](CellsApi.md#cells_post_ungroup_worksheet_rows) | **POST** /cells/{name}/worksheets/{sheetName}/cells/rows/ungroup | Ungroup worksheet rows.
[**cells_post_unhide_worksheet_columns**](CellsApi.md#cells_post_unhide_worksheet_columns) | **POST** /cells/{name}/worksheets/{sheetName}/cells/columns/unhide | Unhide worksheet columns.
[**cells_post_unhide_worksheet_rows**](CellsApi.md#cells_post_unhide_worksheet_rows) | **POST** /cells/{name}/worksheets/{sheetName}/cells/rows/unhide | Unhide worksheet rows.
[**cells_post_update_worksheet_cell_style**](CellsApi.md#cells_post_update_worksheet_cell_style) | **POST** /cells/{name}/worksheets/{sheetName}/cells/{cellName}/style | Update cell&#39;s style.
[**cells_post_update_worksheet_range_style**](CellsApi.md#cells_post_update_worksheet_range_style) | **POST** /cells/{name}/worksheets/{sheetName}/cells/style | Update cell&#39;s range style.
[**cells_post_update_worksheet_row**](CellsApi.md#cells_post_update_worksheet_row) | **POST** /cells/{name}/worksheets/{sheetName}/cells/rows/{rowIndex} | Update worksheet row.
[**cells_post_worksheet_cell_set_value**](CellsApi.md#cells_post_worksheet_cell_set_value) | **POST** /cells/{name}/worksheets/{sheetName}/cells/{cellName} | Set cell value.
[**cells_post_worksheet_merge**](CellsApi.md#cells_post_worksheet_merge) | **POST** /cells/{name}/worksheets/{sheetName}/cells/merge | Merge cells.
[**cells_post_worksheet_unmerge**](CellsApi.md#cells_post_worksheet_unmerge) | **POST** /cells/{name}/worksheets/{sheetName}/cells/unmerge | Unmerge cells.
[**cells_put_insert_worksheet_columns**](CellsApi.md#cells_put_insert_worksheet_columns) | **PUT** /cells/{name}/worksheets/{sheetName}/cells/columns/{columnIndex} | Insert worksheet columns.
[**cells_put_insert_worksheet_row**](CellsApi.md#cells_put_insert_worksheet_row) | **PUT** /cells/{name}/worksheets/{sheetName}/cells/rows/{rowIndex} | Insert new worksheet row.
[**cells_put_insert_worksheet_rows**](CellsApi.md#cells_put_insert_worksheet_rows) | **PUT** /cells/{name}/worksheets/{sheetName}/cells/rows | Insert several new worksheet rows.


# **cells_delete_worksheet_columns**
> ColumnsResponse cells_delete_worksheet_columns(name, sheet_name, column_index, columns, update_reference, folder=folder, storage=storage)

Delete worksheet columns.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsApi()
name = 'name_example' # str | The workbook name.
sheet_name = 'sheet_name_example' # str | The worksheet name.
column_index = 56 # int | The column index.
columns = 56 # int | The columns.
update_reference = true # bool | The update reference.
folder = 'folder_example' # str | The workbook folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Delete worksheet columns.
    api_response = api_instance.cells_delete_worksheet_columns(name, sheet_name, column_index, columns, update_reference, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsApi->cells_delete_worksheet_columns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The workbook name. | 
 **sheet_name** | **str**| The worksheet name. | 
 **column_index** | **int**| The column index. | 
 **columns** | **int**| The columns. | 
 **update_reference** | **bool**| The update reference. | 
 **folder** | **str**| The workbook folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**ColumnsResponse**](ColumnsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_delete_worksheet_row**
> SaaSposeResponse cells_delete_worksheet_row(name, sheet_name, row_index, folder=folder, storage=storage)

Delete worksheet row.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsApi()
name = 'name_example' # str | The workbook name.
sheet_name = 'sheet_name_example' # str | The worksheet bame.
row_index = 56 # int | The row index.
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Delete worksheet row.
    api_response = api_instance.cells_delete_worksheet_row(name, sheet_name, row_index, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsApi->cells_delete_worksheet_row: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The workbook name. | 
 **sheet_name** | **str**| The worksheet bame. | 
 **row_index** | **int**| The row index. | 
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

# **cells_delete_worksheet_rows**
> SaaSposeResponse cells_delete_worksheet_rows(name, sheet_name, startrow, total_rows=total_rows, update_reference=update_reference, folder=folder, storage=storage)

Delete several worksheet rows.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsApi()
name = 'name_example' # str | The workbook name.
sheet_name = 'sheet_name_example' # str | The worksheet bame.
startrow = 56 # int | The begin row index to be operated.
total_rows = 1 # int | Number of rows to be operated. (optional) (default to 1)
update_reference = true # bool | Indicates if update references in other worksheets. (optional) (default to true)
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Delete several worksheet rows.
    api_response = api_instance.cells_delete_worksheet_rows(name, sheet_name, startrow, total_rows=total_rows, update_reference=update_reference, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsApi->cells_delete_worksheet_rows: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The workbook name. | 
 **sheet_name** | **str**| The worksheet bame. | 
 **startrow** | **int**| The begin row index to be operated. | 
 **total_rows** | **int**| Number of rows to be operated. | [optional] [default to 1]
 **update_reference** | **bool**| Indicates if update references in other worksheets. | [optional] [default to true]
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

# **cells_get_cell_html_string**
> object cells_get_cell_html_string(name, sheet_name, cell_name, folder=folder, storage=storage)

Read cell data by cell's name.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsApi()
name = 'name_example' # str | Document name.
sheet_name = 'sheet_name_example' # str | Worksheet name.
cell_name = 'cell_name_example' # str | The cell's  name.
folder = 'folder_example' # str | Document's folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Read cell data by cell's name.
    api_response = api_instance.cells_get_cell_html_string(name, sheet_name, cell_name, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsApi->cells_get_cell_html_string: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document name. | 
 **sheet_name** | **str**| Worksheet name. | 
 **cell_name** | **str**| The cell&#39;s  name. | 
 **folder** | **str**| Document&#39;s folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_get_worksheet_cell**
> object cells_get_worksheet_cell(name, sheet_name, cell_or_method_name, folder=folder, storage=storage)

Read cell data by cell's name.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsApi()
name = 'name_example' # str | Document name.
sheet_name = 'sheet_name_example' # str | Worksheet name.
cell_or_method_name = 'cell_or_method_name_example' # str | The cell's or method name. (Method name like firstcell, endcell etc.)
folder = 'folder_example' # str | Document's folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Read cell data by cell's name.
    api_response = api_instance.cells_get_worksheet_cell(name, sheet_name, cell_or_method_name, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsApi->cells_get_worksheet_cell: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document name. | 
 **sheet_name** | **str**| Worksheet name. | 
 **cell_or_method_name** | **str**| The cell&#39;s or method name. (Method name like firstcell, endcell etc.) | 
 **folder** | **str**| Document&#39;s folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_get_worksheet_cell_style**
> StyleResponse cells_get_worksheet_cell_style(name, sheet_name, cell_name, folder=folder, storage=storage)

Read cell's style info.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsApi()
name = 'name_example' # str | Document name.
sheet_name = 'sheet_name_example' # str | Worksheet name.
cell_name = 'cell_name_example' # str | Cell's name.
folder = 'folder_example' # str | Document's folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Read cell's style info.
    api_response = api_instance.cells_get_worksheet_cell_style(name, sheet_name, cell_name, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsApi->cells_get_worksheet_cell_style: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document name. | 
 **sheet_name** | **str**| Worksheet name. | 
 **cell_name** | **str**| Cell&#39;s name. | 
 **folder** | **str**| Document&#39;s folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**StyleResponse**](StyleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_get_worksheet_cells**
> CellsResponse cells_get_worksheet_cells(name, sheet_name, offest=offest, count=count, folder=folder, storage=storage)

Get cells info.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsApi()
name = 'name_example' # str | Document name.
sheet_name = 'sheet_name_example' # str | Worksheet name.
offest = 0 # int | Begginig offset. (optional) (default to 0)
count = 0 # int | Maximum amount of cells in the response. (optional) (default to 0)
folder = 'folder_example' # str | Document's folder name. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Get cells info.
    api_response = api_instance.cells_get_worksheet_cells(name, sheet_name, offest=offest, count=count, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsApi->cells_get_worksheet_cells: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document name. | 
 **sheet_name** | **str**| Worksheet name. | 
 **offest** | **int**| Begginig offset. | [optional] [default to 0]
 **count** | **int**| Maximum amount of cells in the response. | [optional] [default to 0]
 **folder** | **str**| Document&#39;s folder name. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**CellsResponse**](CellsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_get_worksheet_column**
> ColumnResponse cells_get_worksheet_column(name, sheet_name, column_index, folder=folder, storage=storage)

Read worksheet column data by column's index.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsApi()
name = 'name_example' # str | The workbook name.
sheet_name = 'sheet_name_example' # str | The worksheet name.
column_index = 56 # int | The column index.
folder = 'folder_example' # str | The workbook folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Read worksheet column data by column's index.
    api_response = api_instance.cells_get_worksheet_column(name, sheet_name, column_index, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsApi->cells_get_worksheet_column: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The workbook name. | 
 **sheet_name** | **str**| The worksheet name. | 
 **column_index** | **int**| The column index. | 
 **folder** | **str**| The workbook folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**ColumnResponse**](ColumnResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_get_worksheet_columns**
> ColumnsResponse cells_get_worksheet_columns(name, sheet_name, folder=folder, storage=storage)

Read worksheet columns info.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsApi()
name = 'name_example' # str | The workbook name.
sheet_name = 'sheet_name_example' # str | The worksheet name.
folder = 'folder_example' # str | The workdook folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Read worksheet columns info.
    api_response = api_instance.cells_get_worksheet_columns(name, sheet_name, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsApi->cells_get_worksheet_columns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The workbook name. | 
 **sheet_name** | **str**| The worksheet name. | 
 **folder** | **str**| The workdook folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**ColumnsResponse**](ColumnsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_get_worksheet_row**
> RowResponse cells_get_worksheet_row(name, sheet_name, row_index, folder=folder, storage=storage)

Read worksheet row data by row's index.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsApi()
name = 'name_example' # str | The workbook name.
sheet_name = 'sheet_name_example' # str | The worksheet name.
row_index = 56 # int | The row index.
folder = 'folder_example' # str | The workbook folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Read worksheet row data by row's index.
    api_response = api_instance.cells_get_worksheet_row(name, sheet_name, row_index, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsApi->cells_get_worksheet_row: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The workbook name. | 
 **sheet_name** | **str**| The worksheet name. | 
 **row_index** | **int**| The row index. | 
 **folder** | **str**| The workbook folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**RowResponse**](RowResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_get_worksheet_rows**
> RowsResponse cells_get_worksheet_rows(name, sheet_name, folder=folder, storage=storage)

Read worksheet rows info.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsApi()
name = 'name_example' # str | The workbook name.
sheet_name = 'sheet_name_example' # str | The worksheet name.
folder = 'folder_example' # str | The workdook folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Read worksheet rows info.
    api_response = api_instance.cells_get_worksheet_rows(name, sheet_name, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsApi->cells_get_worksheet_rows: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The workbook name. | 
 **sheet_name** | **str**| The worksheet name. | 
 **folder** | **str**| The workdook folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**RowsResponse**](RowsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_post_cell_calculate**
> SaaSposeResponse cells_post_cell_calculate(name, sheet_name, cell_name, options=options, folder=folder, storage=storage)

Cell calculate formula

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsApi()
name = 'name_example' # str | 
sheet_name = 'sheet_name_example' # str | 
cell_name = 'cell_name_example' # str | 
options = asposecellscloud.CalculationOptions() # CalculationOptions |  (optional)
folder = 'folder_example' # str |  (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Cell calculate formula
    api_response = api_instance.cells_post_cell_calculate(name, sheet_name, cell_name, options=options, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsApi->cells_post_cell_calculate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **sheet_name** | **str**|  | 
 **cell_name** | **str**|  | 
 **options** | [**CalculationOptions**](CalculationOptions.md)|  | [optional] 
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

# **cells_post_cell_characters**
> SaaSposeResponse cells_post_cell_characters(name, sheet_name, cell_name, options=options, folder=folder, storage=storage)

Set cell characters 

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsApi()
name = 'name_example' # str | 
sheet_name = 'sheet_name_example' # str | 
cell_name = 'cell_name_example' # str | 
options = [asposecellscloud.FontSetting()] # list[FontSetting] |  (optional)
folder = 'folder_example' # str |  (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Set cell characters 
    api_response = api_instance.cells_post_cell_characters(name, sheet_name, cell_name, options=options, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsApi->cells_post_cell_characters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **sheet_name** | **str**|  | 
 **cell_name** | **str**|  | 
 **options** | [**list[FontSetting]**](FontSetting.md)|  | [optional] 
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

# **cells_post_clear_contents**
> SaaSposeResponse cells_post_clear_contents(name, sheet_name, range=range, start_row=start_row, start_column=start_column, end_row=end_row, end_column=end_column, folder=folder, storage=storage)

Clear cells contents.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsApi()
name = 'name_example' # str | Workbook name.
sheet_name = 'sheet_name_example' # str | Worksheet name.
range = 'range_example' # str | The range. (optional)
start_row = 56 # int | The start row. (optional)
start_column = 56 # int | The start column. (optional)
end_row = 56 # int | The end row. (optional)
end_column = 56 # int | The end column. (optional)
folder = 'folder_example' # str | The workbook folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Clear cells contents.
    api_response = api_instance.cells_post_clear_contents(name, sheet_name, range=range, start_row=start_row, start_column=start_column, end_row=end_row, end_column=end_column, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsApi->cells_post_clear_contents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Workbook name. | 
 **sheet_name** | **str**| Worksheet name. | 
 **range** | **str**| The range. | [optional] 
 **start_row** | **int**| The start row. | [optional] 
 **start_column** | **int**| The start column. | [optional] 
 **end_row** | **int**| The end row. | [optional] 
 **end_column** | **int**| The end column. | [optional] 
 **folder** | **str**| The workbook folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**SaaSposeResponse**](SaaSposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_post_clear_formats**
> SaaSposeResponse cells_post_clear_formats(name, sheet_name, range=range, start_row=start_row, start_column=start_column, end_row=end_row, end_column=end_column, folder=folder, storage=storage)

Clear cells contents.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsApi()
name = 'name_example' # str | Workbook name.
sheet_name = 'sheet_name_example' # str | Worksheet name.
range = 'range_example' # str | The range. (optional)
start_row = 56 # int | The start row. (optional)
start_column = 56 # int | The start column. (optional)
end_row = 56 # int | The end row. (optional)
end_column = 56 # int | The end column. (optional)
folder = 'folder_example' # str | The workbook folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Clear cells contents.
    api_response = api_instance.cells_post_clear_formats(name, sheet_name, range=range, start_row=start_row, start_column=start_column, end_row=end_row, end_column=end_column, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsApi->cells_post_clear_formats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Workbook name. | 
 **sheet_name** | **str**| Worksheet name. | 
 **range** | **str**| The range. | [optional] 
 **start_row** | **int**| The start row. | [optional] 
 **start_column** | **int**| The start column. | [optional] 
 **end_row** | **int**| The end row. | [optional] 
 **end_column** | **int**| The end column. | [optional] 
 **folder** | **str**| The workbook folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**SaaSposeResponse**](SaaSposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_post_column_style**
> SaaSposeResponse cells_post_column_style(name, sheet_name, column_index, style=style, folder=folder, storage=storage)

Set column style

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsApi()
name = 'name_example' # str | The workbook name.
sheet_name = 'sheet_name_example' # str | The worksheet name.
column_index = 56 # int | The column index.
style = asposecellscloud.Style() # Style | Style dto (optional)
folder = 'folder_example' # str | The workbook folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Set column style
    api_response = api_instance.cells_post_column_style(name, sheet_name, column_index, style=style, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsApi->cells_post_column_style: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The workbook name. | 
 **sheet_name** | **str**| The worksheet name. | 
 **column_index** | **int**| The column index. | 
 **style** | [**Style**](Style.md)| Style dto | [optional] 
 **folder** | **str**| The workbook folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**SaaSposeResponse**](SaaSposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_post_copy_cell_into_cell**
> SaaSposeResponse cells_post_copy_cell_into_cell(name, dest_cell_name, sheet_name, worksheet, cellname=cellname, row=row, column=column, folder=folder, storage=storage)

Copy cell into cell

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsApi()
name = 'name_example' # str | Workbook name.
dest_cell_name = 'dest_cell_name_example' # str | Destination cell name
sheet_name = 'sheet_name_example' # str | Destination worksheet name.
worksheet = 'worksheet_example' # str | Source worksheet name.
cellname = 'cellname_example' # str | Source cell name (optional)
row = 56 # int | Source row (optional)
column = 56 # int | Source column (optional)
folder = 'folder_example' # str | Folder name (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Copy cell into cell
    api_response = api_instance.cells_post_copy_cell_into_cell(name, dest_cell_name, sheet_name, worksheet, cellname=cellname, row=row, column=column, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsApi->cells_post_copy_cell_into_cell: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Workbook name. | 
 **dest_cell_name** | **str**| Destination cell name | 
 **sheet_name** | **str**| Destination worksheet name. | 
 **worksheet** | **str**| Source worksheet name. | 
 **cellname** | **str**| Source cell name | [optional] 
 **row** | **int**| Source row | [optional] 
 **column** | **int**| Source column | [optional] 
 **folder** | **str**| Folder name | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**SaaSposeResponse**](SaaSposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_post_copy_worksheet_columns**
> SaaSposeResponse cells_post_copy_worksheet_columns(name, sheet_name, source_column_index, destination_column_index, column_number, worksheet=worksheet, folder=folder, storage=storage)

Copy worksheet columns.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsApi()
name = 'name_example' # str | The workbook name.
sheet_name = 'sheet_name_example' # str | The worksheet name.
source_column_index = 56 # int | Source column index
destination_column_index = 56 # int | Destination column index
column_number = 56 # int | The copied column number
worksheet = '' # str | The Worksheet (optional) (default to )
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Copy worksheet columns.
    api_response = api_instance.cells_post_copy_worksheet_columns(name, sheet_name, source_column_index, destination_column_index, column_number, worksheet=worksheet, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsApi->cells_post_copy_worksheet_columns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The workbook name. | 
 **sheet_name** | **str**| The worksheet name. | 
 **source_column_index** | **int**| Source column index | 
 **destination_column_index** | **int**| Destination column index | 
 **column_number** | **int**| The copied column number | 
 **worksheet** | **str**| The Worksheet | [optional] [default to ]
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

# **cells_post_copy_worksheet_rows**
> SaaSposeResponse cells_post_copy_worksheet_rows(name, sheet_name, source_row_index, destination_row_index, row_number, worksheet=worksheet, folder=folder, storage=storage)

Copy worksheet rows.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsApi()
name = 'name_example' # str | The workbook name.
sheet_name = 'sheet_name_example' # str | The worksheet name.
source_row_index = 56 # int | Source row index
destination_row_index = 56 # int | Destination row index
row_number = 56 # int | The copied row number
worksheet = 'worksheet_example' # str | worksheet (optional)
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Copy worksheet rows.
    api_response = api_instance.cells_post_copy_worksheet_rows(name, sheet_name, source_row_index, destination_row_index, row_number, worksheet=worksheet, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsApi->cells_post_copy_worksheet_rows: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The workbook name. | 
 **sheet_name** | **str**| The worksheet name. | 
 **source_row_index** | **int**| Source row index | 
 **destination_row_index** | **int**| Destination row index | 
 **row_number** | **int**| The copied row number | 
 **worksheet** | **str**| worksheet | [optional] 
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

# **cells_post_group_worksheet_columns**
> SaaSposeResponse cells_post_group_worksheet_columns(name, sheet_name, first_index, last_index, hide=hide, folder=folder, storage=storage)

Group worksheet columns.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsApi()
name = 'name_example' # str | The workbook name.
sheet_name = 'sheet_name_example' # str | The worksheet name.
first_index = 56 # int | The first column index to be operated.
last_index = 56 # int | The last column index to be operated.
hide = true # bool | columns visible state (optional)
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Group worksheet columns.
    api_response = api_instance.cells_post_group_worksheet_columns(name, sheet_name, first_index, last_index, hide=hide, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsApi->cells_post_group_worksheet_columns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The workbook name. | 
 **sheet_name** | **str**| The worksheet name. | 
 **first_index** | **int**| The first column index to be operated. | 
 **last_index** | **int**| The last column index to be operated. | 
 **hide** | **bool**| columns visible state | [optional] 
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

# **cells_post_group_worksheet_rows**
> SaaSposeResponse cells_post_group_worksheet_rows(name, sheet_name, first_index, last_index, hide=hide, folder=folder, storage=storage)

Group worksheet rows.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsApi()
name = 'name_example' # str | The workbook name.
sheet_name = 'sheet_name_example' # str | The worksheet name.
first_index = 56 # int | The first row index to be operated.
last_index = 56 # int | The last row index to be operated.
hide = true # bool | rows visible state (optional)
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Group worksheet rows.
    api_response = api_instance.cells_post_group_worksheet_rows(name, sheet_name, first_index, last_index, hide=hide, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsApi->cells_post_group_worksheet_rows: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The workbook name. | 
 **sheet_name** | **str**| The worksheet name. | 
 **first_index** | **int**| The first row index to be operated. | 
 **last_index** | **int**| The last row index to be operated. | 
 **hide** | **bool**| rows visible state | [optional] 
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

# **cells_post_hide_worksheet_columns**
> SaaSposeResponse cells_post_hide_worksheet_columns(name, sheet_name, start_column, total_columns, folder=folder, storage=storage)

Hide worksheet columns.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsApi()
name = 'name_example' # str | The workbook name.
sheet_name = 'sheet_name_example' # str | The worksheet name.
start_column = 56 # int | The begin column index to be operated.
total_columns = 56 # int | Number of columns to be operated.
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Hide worksheet columns.
    api_response = api_instance.cells_post_hide_worksheet_columns(name, sheet_name, start_column, total_columns, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsApi->cells_post_hide_worksheet_columns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The workbook name. | 
 **sheet_name** | **str**| The worksheet name. | 
 **start_column** | **int**| The begin column index to be operated. | 
 **total_columns** | **int**| Number of columns to be operated. | 
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

# **cells_post_hide_worksheet_rows**
> SaaSposeResponse cells_post_hide_worksheet_rows(name, sheet_name, startrow, total_rows, folder=folder, storage=storage)

Hide worksheet rows.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsApi()
name = 'name_example' # str | The workbook name.
sheet_name = 'sheet_name_example' # str | The worksheet name.
startrow = 56 # int | The begin row index to be operated.
total_rows = 56 # int | Number of rows to be operated.
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Hide worksheet rows.
    api_response = api_instance.cells_post_hide_worksheet_rows(name, sheet_name, startrow, total_rows, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsApi->cells_post_hide_worksheet_rows: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The workbook name. | 
 **sheet_name** | **str**| The worksheet name. | 
 **startrow** | **int**| The begin row index to be operated. | 
 **total_rows** | **int**| Number of rows to be operated. | 
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

# **cells_post_row_style**
> SaaSposeResponse cells_post_row_style(name, sheet_name, row_index, style=style, folder=folder, storage=storage)

Set row style.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsApi()
name = 'name_example' # str | The workbook name.
sheet_name = 'sheet_name_example' # str | The worksheet name.
row_index = 56 # int | The row index.
style = asposecellscloud.Style() # Style | Style dto (optional)
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Set row style.
    api_response = api_instance.cells_post_row_style(name, sheet_name, row_index, style=style, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsApi->cells_post_row_style: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The workbook name. | 
 **sheet_name** | **str**| The worksheet name. | 
 **row_index** | **int**| The row index. | 
 **style** | [**Style**](Style.md)| Style dto | [optional] 
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

# **cells_post_set_cell_html_string**
> CellResponse cells_post_set_cell_html_string(name, sheet_name, cell_name, folder=folder, storage=storage)

Set htmlstring value into cell

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsApi()
name = 'name_example' # str | Workbook name.
sheet_name = 'sheet_name_example' # str | Worksheet name.
cell_name = 'cell_name_example' # str | The cell name.
folder = 'folder_example' # str | The workbook folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Set htmlstring value into cell
    api_response = api_instance.cells_post_set_cell_html_string(name, sheet_name, cell_name, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsApi->cells_post_set_cell_html_string: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Workbook name. | 
 **sheet_name** | **str**| Worksheet name. | 
 **cell_name** | **str**| The cell name. | 
 **folder** | **str**| The workbook folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**CellResponse**](CellResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_post_set_cell_range_value**
> SaaSposeResponse cells_post_set_cell_range_value(name, sheet_name, cellarea, value, type, folder=folder, storage=storage)

Set cell range value 

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsApi()
name = 'name_example' # str | Workbook name.
sheet_name = 'sheet_name_example' # str | Worksheet name.
cellarea = 'cellarea_example' # str | Cell area (like \"A1:C2\")
value = 'value_example' # str | Range value
type = 'type_example' # str | Value data type (like \"int\")
folder = 'folder_example' # str | Folder name (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Set cell range value 
    api_response = api_instance.cells_post_set_cell_range_value(name, sheet_name, cellarea, value, type, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsApi->cells_post_set_cell_range_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Workbook name. | 
 **sheet_name** | **str**| Worksheet name. | 
 **cellarea** | **str**| Cell area (like \&quot;A1:C2\&quot;) | 
 **value** | **str**| Range value | 
 **type** | **str**| Value data type (like \&quot;int\&quot;) | 
 **folder** | **str**| Folder name | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**SaaSposeResponse**](SaaSposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_post_set_worksheet_column_width**
> ColumnResponse cells_post_set_worksheet_column_width(name, sheet_name, column_index, width, folder=folder, storage=storage)

Set worksheet column width.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsApi()
name = 'name_example' # str | The workbook name.
sheet_name = 'sheet_name_example' # str | The worksheet name.
column_index = 56 # int | The column index.
width = 1.2 # float | The width.
folder = 'folder_example' # str | The workbook folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Set worksheet column width.
    api_response = api_instance.cells_post_set_worksheet_column_width(name, sheet_name, column_index, width, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsApi->cells_post_set_worksheet_column_width: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The workbook name. | 
 **sheet_name** | **str**| The worksheet name. | 
 **column_index** | **int**| The column index. | 
 **width** | **float**| The width. | 
 **folder** | **str**| The workbook folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**ColumnResponse**](ColumnResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_post_ungroup_worksheet_columns**
> SaaSposeResponse cells_post_ungroup_worksheet_columns(name, sheet_name, first_index, last_index, folder=folder, storage=storage)

Ungroup worksheet columns.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsApi()
name = 'name_example' # str | The workbook name.
sheet_name = 'sheet_name_example' # str | The worksheet name.
first_index = 56 # int | The first column index to be operated.
last_index = 56 # int | The last column index to be operated.
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Ungroup worksheet columns.
    api_response = api_instance.cells_post_ungroup_worksheet_columns(name, sheet_name, first_index, last_index, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsApi->cells_post_ungroup_worksheet_columns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The workbook name. | 
 **sheet_name** | **str**| The worksheet name. | 
 **first_index** | **int**| The first column index to be operated. | 
 **last_index** | **int**| The last column index to be operated. | 
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

# **cells_post_ungroup_worksheet_rows**
> SaaSposeResponse cells_post_ungroup_worksheet_rows(name, sheet_name, first_index, last_index, is_all=is_all, folder=folder, storage=storage)

Ungroup worksheet rows.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsApi()
name = 'name_example' # str | The workbook name.
sheet_name = 'sheet_name_example' # str | The worksheet name.
first_index = 56 # int | The first row index to be operated.
last_index = 56 # int | The last row index to be operated.
is_all = true # bool | Is all row to be operated (optional)
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Ungroup worksheet rows.
    api_response = api_instance.cells_post_ungroup_worksheet_rows(name, sheet_name, first_index, last_index, is_all=is_all, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsApi->cells_post_ungroup_worksheet_rows: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The workbook name. | 
 **sheet_name** | **str**| The worksheet name. | 
 **first_index** | **int**| The first row index to be operated. | 
 **last_index** | **int**| The last row index to be operated. | 
 **is_all** | **bool**| Is all row to be operated | [optional] 
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

# **cells_post_unhide_worksheet_columns**
> SaaSposeResponse cells_post_unhide_worksheet_columns(name, sheet_name, startcolumn, total_columns, width=width, folder=folder, storage=storage)

Unhide worksheet columns.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsApi()
name = 'name_example' # str | The workbook name.
sheet_name = 'sheet_name_example' # str | The worksheet name.
startcolumn = 56 # int | The begin column index to be operated.
total_columns = 56 # int | Number of columns to be operated.
width = 50.0 # float | The new column width. (optional) (default to 50.0)
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Unhide worksheet columns.
    api_response = api_instance.cells_post_unhide_worksheet_columns(name, sheet_name, startcolumn, total_columns, width=width, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsApi->cells_post_unhide_worksheet_columns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The workbook name. | 
 **sheet_name** | **str**| The worksheet name. | 
 **startcolumn** | **int**| The begin column index to be operated. | 
 **total_columns** | **int**| Number of columns to be operated. | 
 **width** | **float**| The new column width. | [optional] [default to 50.0]
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

# **cells_post_unhide_worksheet_rows**
> SaaSposeResponse cells_post_unhide_worksheet_rows(name, sheet_name, startrow, total_rows, height=height, folder=folder, storage=storage)

Unhide worksheet rows.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsApi()
name = 'name_example' # str | The workbook name.
sheet_name = 'sheet_name_example' # str | The worksheet name.
startrow = 56 # int | The begin row index to be operated.
total_rows = 56 # int | Number of rows to be operated.
height = 15.0 # float | The new row height. (optional) (default to 15.0)
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Unhide worksheet rows.
    api_response = api_instance.cells_post_unhide_worksheet_rows(name, sheet_name, startrow, total_rows, height=height, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsApi->cells_post_unhide_worksheet_rows: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The workbook name. | 
 **sheet_name** | **str**| The worksheet name. | 
 **startrow** | **int**| The begin row index to be operated. | 
 **total_rows** | **int**| Number of rows to be operated. | 
 **height** | **float**| The new row height. | [optional] [default to 15.0]
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

# **cells_post_update_worksheet_cell_style**
> StyleResponse cells_post_update_worksheet_cell_style(name, sheet_name, cell_name, style=style, folder=folder, storage=storage)

Update cell's style.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsApi()
name = 'name_example' # str | Workbook name.
sheet_name = 'sheet_name_example' # str | Worksheet name.
cell_name = 'cell_name_example' # str | The cell name.
style = asposecellscloud.Style() # Style | with update style settings. (optional)
folder = 'folder_example' # str | The workbook folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Update cell's style.
    api_response = api_instance.cells_post_update_worksheet_cell_style(name, sheet_name, cell_name, style=style, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsApi->cells_post_update_worksheet_cell_style: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Workbook name. | 
 **sheet_name** | **str**| Worksheet name. | 
 **cell_name** | **str**| The cell name. | 
 **style** | [**Style**](Style.md)| with update style settings. | [optional] 
 **folder** | **str**| The workbook folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**StyleResponse**](StyleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_post_update_worksheet_range_style**
> SaaSposeResponse cells_post_update_worksheet_range_style(name, sheet_name, range, style=style, folder=folder, storage=storage)

Update cell's range style.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsApi()
name = 'name_example' # str | Workbook name.
sheet_name = 'sheet_name_example' # str | Worksheet name.
range = 'range_example' # str | The range.
style = asposecellscloud.Style() # Style | with update style settings. (optional)
folder = 'folder_example' # str | The workbook folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Update cell's range style.
    api_response = api_instance.cells_post_update_worksheet_range_style(name, sheet_name, range, style=style, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsApi->cells_post_update_worksheet_range_style: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Workbook name. | 
 **sheet_name** | **str**| Worksheet name. | 
 **range** | **str**| The range. | 
 **style** | [**Style**](Style.md)| with update style settings. | [optional] 
 **folder** | **str**| The workbook folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**SaaSposeResponse**](SaaSposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_post_update_worksheet_row**
> RowResponse cells_post_update_worksheet_row(name, sheet_name, row_index, height=height, folder=folder, storage=storage)

Update worksheet row.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsApi()
name = 'name_example' # str | The workbook name.
sheet_name = 'sheet_name_example' # str | The worksheet name.
row_index = 56 # int | The row index.
height = 0.0 # float | The new row height. (optional) (default to 0.0)
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Update worksheet row.
    api_response = api_instance.cells_post_update_worksheet_row(name, sheet_name, row_index, height=height, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsApi->cells_post_update_worksheet_row: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The workbook name. | 
 **sheet_name** | **str**| The worksheet name. | 
 **row_index** | **int**| The row index. | 
 **height** | **float**| The new row height. | [optional] [default to 0.0]
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**RowResponse**](RowResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_post_worksheet_cell_set_value**
> CellResponse cells_post_worksheet_cell_set_value(name, sheet_name, cell_name, value=value, type=type, formula=formula, folder=folder, storage=storage)

Set cell value.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsApi()
name = 'name_example' # str | The document name.
sheet_name = 'sheet_name_example' # str | The worksheet name.
cell_name = 'cell_name_example' # str | The cell name.
value = 'value_example' # str | The cell value. (optional)
type = 'type_example' # str | The value type. (optional)
formula = 'formula_example' # str | Formula for cell (optional)
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Set cell value.
    api_response = api_instance.cells_post_worksheet_cell_set_value(name, sheet_name, cell_name, value=value, type=type, formula=formula, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsApi->cells_post_worksheet_cell_set_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **sheet_name** | **str**| The worksheet name. | 
 **cell_name** | **str**| The cell name. | 
 **value** | **str**| The cell value. | [optional] 
 **type** | **str**| The value type. | [optional] 
 **formula** | **str**| Formula for cell | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**CellResponse**](CellResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_post_worksheet_merge**
> SaaSposeResponse cells_post_worksheet_merge(name, sheet_name, start_row, start_column, total_rows, total_columns, folder=folder, storage=storage)

Merge cells.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsApi()
name = 'name_example' # str | The workbook name.
sheet_name = 'sheet_name_example' # str | The worksheet name.
start_row = 56 # int | The start row.
start_column = 56 # int | The start column.
total_rows = 56 # int | The total rows
total_columns = 56 # int | The total columns.
folder = 'folder_example' # str | The workbook folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Merge cells.
    api_response = api_instance.cells_post_worksheet_merge(name, sheet_name, start_row, start_column, total_rows, total_columns, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsApi->cells_post_worksheet_merge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The workbook name. | 
 **sheet_name** | **str**| The worksheet name. | 
 **start_row** | **int**| The start row. | 
 **start_column** | **int**| The start column. | 
 **total_rows** | **int**| The total rows | 
 **total_columns** | **int**| The total columns. | 
 **folder** | **str**| The workbook folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**SaaSposeResponse**](SaaSposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_post_worksheet_unmerge**
> SaaSposeResponse cells_post_worksheet_unmerge(name, sheet_name, start_row, start_column, total_rows, total_columns, folder=folder, storage=storage)

Unmerge cells.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsApi()
name = 'name_example' # str | The workbook name.
sheet_name = 'sheet_name_example' # str | The worksheet name.
start_row = 56 # int | The start row.
start_column = 56 # int | The start column.
total_rows = 56 # int | The total rows
total_columns = 56 # int | The total columns.
folder = 'folder_example' # str | The workbook folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Unmerge cells.
    api_response = api_instance.cells_post_worksheet_unmerge(name, sheet_name, start_row, start_column, total_rows, total_columns, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsApi->cells_post_worksheet_unmerge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The workbook name. | 
 **sheet_name** | **str**| The worksheet name. | 
 **start_row** | **int**| The start row. | 
 **start_column** | **int**| The start column. | 
 **total_rows** | **int**| The total rows | 
 **total_columns** | **int**| The total columns. | 
 **folder** | **str**| The workbook folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**SaaSposeResponse**](SaaSposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_put_insert_worksheet_columns**
> ColumnsResponse cells_put_insert_worksheet_columns(name, sheet_name, column_index, columns, update_reference=update_reference, folder=folder, storage=storage)

Insert worksheet columns.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsApi()
name = 'name_example' # str | The workbook name.
sheet_name = 'sheet_name_example' # str | The worksheet name.
column_index = 56 # int | The column index.
columns = 56 # int | The columns.
update_reference = true # bool | The update reference. (optional) (default to true)
folder = 'folder_example' # str | The workbook folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Insert worksheet columns.
    api_response = api_instance.cells_put_insert_worksheet_columns(name, sheet_name, column_index, columns, update_reference=update_reference, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsApi->cells_put_insert_worksheet_columns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The workbook name. | 
 **sheet_name** | **str**| The worksheet name. | 
 **column_index** | **int**| The column index. | 
 **columns** | **int**| The columns. | 
 **update_reference** | **bool**| The update reference. | [optional] [default to true]
 **folder** | **str**| The workbook folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**ColumnsResponse**](ColumnsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_put_insert_worksheet_row**
> RowResponse cells_put_insert_worksheet_row(name, sheet_name, row_index, folder=folder, storage=storage)

Insert new worksheet row.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsApi()
name = 'name_example' # str | The workbook name.
sheet_name = 'sheet_name_example' # str | The worksheet name.
row_index = 56 # int | The new row index.
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Insert new worksheet row.
    api_response = api_instance.cells_put_insert_worksheet_row(name, sheet_name, row_index, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsApi->cells_put_insert_worksheet_row: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The workbook name. | 
 **sheet_name** | **str**| The worksheet name. | 
 **row_index** | **int**| The new row index. | 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**RowResponse**](RowResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_put_insert_worksheet_rows**
> SaaSposeResponse cells_put_insert_worksheet_rows(name, sheet_name, startrow, total_rows=total_rows, update_reference=update_reference, folder=folder, storage=storage)

Insert several new worksheet rows.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsApi()
name = 'name_example' # str | The workbook name.
sheet_name = 'sheet_name_example' # str | The worksheet name.
startrow = 56 # int | The begin row index to be operated.
total_rows = 1 # int | Number of rows to be operated. (optional) (default to 1)
update_reference = true # bool | Indicates if update references in other worksheets. (optional) (default to true)
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Insert several new worksheet rows.
    api_response = api_instance.cells_put_insert_worksheet_rows(name, sheet_name, startrow, total_rows=total_rows, update_reference=update_reference, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsApi->cells_put_insert_worksheet_rows: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The workbook name. | 
 **sheet_name** | **str**| The worksheet name. | 
 **startrow** | **int**| The begin row index to be operated. | 
 **total_rows** | **int**| Number of rows to be operated. | [optional] [default to 1]
 **update_reference** | **bool**| Indicates if update references in other worksheets. | [optional] [default to true]
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

