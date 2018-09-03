# asposecellscloud.CellsWorksheetsApi

All URIs are relative to *https://api.aspose.cloud/v1.1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cells_worksheets_delete_unprotect_worksheet**](CellsWorksheetsApi.md#cells_worksheets_delete_unprotect_worksheet) | **DELETE** /cells/{name}/worksheets/{sheetName}/protection | Unprotect worksheet.
[**cells_worksheets_delete_worksheet**](CellsWorksheetsApi.md#cells_worksheets_delete_worksheet) | **DELETE** /cells/{name}/worksheets/{sheetName} | Delete worksheet.
[**cells_worksheets_delete_worksheet_background**](CellsWorksheetsApi.md#cells_worksheets_delete_worksheet_background) | **DELETE** /cells/{name}/worksheets/{sheetName}/background | Set worksheet background image.
[**cells_worksheets_delete_worksheet_comment**](CellsWorksheetsApi.md#cells_worksheets_delete_worksheet_comment) | **DELETE** /cells/{name}/worksheets/{sheetName}/comments/{cellName} | Delete worksheet&#39;s cell comment.
[**cells_worksheets_delete_worksheet_comments**](CellsWorksheetsApi.md#cells_worksheets_delete_worksheet_comments) | **DELETE** /cells/{name}/worksheets/{sheetName}/comments | Delete all comments for worksheet.
[**cells_worksheets_delete_worksheet_freeze_panes**](CellsWorksheetsApi.md#cells_worksheets_delete_worksheet_freeze_panes) | **DELETE** /cells/{name}/worksheets/{sheetName}/freezepanes | Unfreeze panes
[**cells_worksheets_get_named_ranges**](CellsWorksheetsApi.md#cells_worksheets_get_named_ranges) | **GET** /cells/{name}/worksheets/ranges | Read worksheets ranges info.
[**cells_worksheets_get_worksheet**](CellsWorksheetsApi.md#cells_worksheets_get_worksheet) | **GET** /cells/{name}/worksheets/{sheetName} | Read worksheet info or export.
[**cells_worksheets_get_worksheet_calculate_formula**](CellsWorksheetsApi.md#cells_worksheets_get_worksheet_calculate_formula) | **GET** /cells/{name}/worksheets/{sheetName}/formulaResult | Calculate formula value.
[**cells_worksheets_get_worksheet_comment**](CellsWorksheetsApi.md#cells_worksheets_get_worksheet_comment) | **GET** /cells/{name}/worksheets/{sheetName}/comments/{cellName} | Get worksheet comment by cell name.
[**cells_worksheets_get_worksheet_comments**](CellsWorksheetsApi.md#cells_worksheets_get_worksheet_comments) | **GET** /cells/{name}/worksheets/{sheetName}/comments | Get worksheet comments.
[**cells_worksheets_get_worksheet_merged_cell**](CellsWorksheetsApi.md#cells_worksheets_get_worksheet_merged_cell) | **GET** /cells/{name}/worksheets/{sheetName}/mergedCells/{mergedCellIndex} | Get worksheet merged cell by its index.
[**cells_worksheets_get_worksheet_merged_cells**](CellsWorksheetsApi.md#cells_worksheets_get_worksheet_merged_cells) | **GET** /cells/{name}/worksheets/{sheetName}/mergedCells | Get worksheet merged cells.
[**cells_worksheets_get_worksheet_text_items**](CellsWorksheetsApi.md#cells_worksheets_get_worksheet_text_items) | **GET** /cells/{name}/worksheets/{sheetName}/textItems | Get worksheet text items.
[**cells_worksheets_get_worksheets**](CellsWorksheetsApi.md#cells_worksheets_get_worksheets) | **GET** /cells/{name}/worksheets | Read worksheets info.
[**cells_worksheets_post_autofit_worksheet_columns**](CellsWorksheetsApi.md#cells_worksheets_post_autofit_worksheet_columns) | **POST** /cells/{name}/worksheets/{sheetName}/autofitcolumns | 
[**cells_worksheets_post_autofit_worksheet_row**](CellsWorksheetsApi.md#cells_worksheets_post_autofit_worksheet_row) | **POST** /cells/{name}/worksheets/{sheetName}/autofitrow | 
[**cells_worksheets_post_autofit_worksheet_rows**](CellsWorksheetsApi.md#cells_worksheets_post_autofit_worksheet_rows) | **POST** /cells/{name}/worksheets/{sheetName}/autofitrows | Autofit worksheet rows.
[**cells_worksheets_post_copy_worksheet**](CellsWorksheetsApi.md#cells_worksheets_post_copy_worksheet) | **POST** /cells/{name}/worksheets/{sheetName}/copy | 
[**cells_worksheets_post_move_worksheet**](CellsWorksheetsApi.md#cells_worksheets_post_move_worksheet) | **POST** /cells/{name}/worksheets/{sheetName}/position | Move worksheet.
[**cells_worksheets_post_rename_worksheet**](CellsWorksheetsApi.md#cells_worksheets_post_rename_worksheet) | **POST** /cells/{name}/worksheets/{sheetName}/rename | Rename worksheet
[**cells_worksheets_post_update_worksheet_property**](CellsWorksheetsApi.md#cells_worksheets_post_update_worksheet_property) | **POST** /cells/{name}/worksheets/{sheetName} | Update worksheet property
[**cells_worksheets_post_update_worksheet_zoom**](CellsWorksheetsApi.md#cells_worksheets_post_update_worksheet_zoom) | **POST** /cells/{name}/worksheets/{sheetName}/zoom | 
[**cells_worksheets_post_worksheet_comment**](CellsWorksheetsApi.md#cells_worksheets_post_worksheet_comment) | **POST** /cells/{name}/worksheets/{sheetName}/comments/{cellName} | Update worksheet&#39;s cell comment.
[**cells_worksheets_post_worksheet_range_sort**](CellsWorksheetsApi.md#cells_worksheets_post_worksheet_range_sort) | **POST** /cells/{name}/worksheets/{sheetName}/sort | Sort worksheet range.
[**cells_worksheets_post_worksheet_text_search**](CellsWorksheetsApi.md#cells_worksheets_post_worksheet_text_search) | **POST** /cells/{name}/worksheets/{sheetName}/findText | Search text.
[**cells_worksheets_post_worsheet_text_replace**](CellsWorksheetsApi.md#cells_worksheets_post_worsheet_text_replace) | **POST** /cells/{name}/worksheets/{sheetName}/replaceText | Replace text.
[**cells_worksheets_put_add_new_worksheet**](CellsWorksheetsApi.md#cells_worksheets_put_add_new_worksheet) | **PUT** /cells/{name}/worksheets/{sheetName} | Add new worksheet.
[**cells_worksheets_put_change_visibility_worksheet**](CellsWorksheetsApi.md#cells_worksheets_put_change_visibility_worksheet) | **PUT** /cells/{name}/worksheets/{sheetName}/visible | Change worksheet visibility.
[**cells_worksheets_put_protect_worksheet**](CellsWorksheetsApi.md#cells_worksheets_put_protect_worksheet) | **PUT** /cells/{name}/worksheets/{sheetName}/protection | Protect worksheet.
[**cells_worksheets_put_worksheet_background**](CellsWorksheetsApi.md#cells_worksheets_put_worksheet_background) | **PUT** /cells/{name}/worksheets/{sheetName}/background | Set worksheet background image.
[**cells_worksheets_put_worksheet_comment**](CellsWorksheetsApi.md#cells_worksheets_put_worksheet_comment) | **PUT** /cells/{name}/worksheets/{sheetName}/comments/{cellName} | Add worksheet&#39;s cell comment.
[**cells_worksheets_put_worksheet_freeze_panes**](CellsWorksheetsApi.md#cells_worksheets_put_worksheet_freeze_panes) | **PUT** /cells/{name}/worksheets/{sheetName}/freezepanes | Set freeze panes


# **cells_worksheets_delete_unprotect_worksheet**
> WorksheetResponse cells_worksheets_delete_unprotect_worksheet(name, sheet_name, protect_parameter=protect_parameter, folder=folder, storage=storage)

Unprotect worksheet.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsWorksheetsApi()
name = 'name_example' # str | Document name.
sheet_name = 'sheet_name_example' # str | The worksheet name.
protect_parameter = asposecellscloud.ProtectSheetParameter() # ProtectSheetParameter | with protection settings. Only password is used here. (optional)
folder = 'folder_example' # str | Document folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Unprotect worksheet.
    api_response = api_instance.cells_worksheets_delete_unprotect_worksheet(name, sheet_name, protect_parameter=protect_parameter, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsWorksheetsApi->cells_worksheets_delete_unprotect_worksheet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document name. | 
 **sheet_name** | **str**| The worksheet name. | 
 **protect_parameter** | [**ProtectSheetParameter**](ProtectSheetParameter.md)| with protection settings. Only password is used here. | [optional] 
 **folder** | **str**| Document folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**WorksheetResponse**](WorksheetResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_worksheets_delete_worksheet**
> WorksheetsResponse cells_worksheets_delete_worksheet(name, sheet_name, folder=folder, storage=storage)

Delete worksheet.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsWorksheetsApi()
name = 'name_example' # str | Document name.
sheet_name = 'sheet_name_example' # str | The worksheet name.
folder = 'folder_example' # str | Document's folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Delete worksheet.
    api_response = api_instance.cells_worksheets_delete_worksheet(name, sheet_name, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsWorksheetsApi->cells_worksheets_delete_worksheet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document name. | 
 **sheet_name** | **str**| The worksheet name. | 
 **folder** | **str**| Document&#39;s folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**WorksheetsResponse**](WorksheetsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_worksheets_delete_worksheet_background**
> SaaSposeResponse cells_worksheets_delete_worksheet_background(name, sheet_name, folder=folder, storage=storage)

Set worksheet background image.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsWorksheetsApi()
name = 'name_example' # str | 
sheet_name = 'sheet_name_example' # str | 
folder = 'folder_example' # str |  (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Set worksheet background image.
    api_response = api_instance.cells_worksheets_delete_worksheet_background(name, sheet_name, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsWorksheetsApi->cells_worksheets_delete_worksheet_background: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **sheet_name** | **str**|  | 
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

# **cells_worksheets_delete_worksheet_comment**
> SaaSposeResponse cells_worksheets_delete_worksheet_comment(name, sheet_name, cell_name, folder=folder, storage=storage)

Delete worksheet's cell comment.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsWorksheetsApi()
name = 'name_example' # str | The document name.
sheet_name = 'sheet_name_example' # str | The worksheet name.
cell_name = 'cell_name_example' # str | The cell name
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Delete worksheet's cell comment.
    api_response = api_instance.cells_worksheets_delete_worksheet_comment(name, sheet_name, cell_name, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsWorksheetsApi->cells_worksheets_delete_worksheet_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **sheet_name** | **str**| The worksheet name. | 
 **cell_name** | **str**| The cell name | 
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

# **cells_worksheets_delete_worksheet_comments**
> SaaSposeResponse cells_worksheets_delete_worksheet_comments(name, sheet_name, folder=folder, storage=storage)

Delete all comments for worksheet.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsWorksheetsApi()
name = 'name_example' # str | 
sheet_name = 'sheet_name_example' # str | 
folder = 'folder_example' # str |  (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Delete all comments for worksheet.
    api_response = api_instance.cells_worksheets_delete_worksheet_comments(name, sheet_name, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsWorksheetsApi->cells_worksheets_delete_worksheet_comments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **sheet_name** | **str**|  | 
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

# **cells_worksheets_delete_worksheet_freeze_panes**
> SaaSposeResponse cells_worksheets_delete_worksheet_freeze_panes(name, sheet_name, row, column, freezed_rows, freezed_columns, folder=folder, storage=storage)

Unfreeze panes

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsWorksheetsApi()
name = 'name_example' # str | 
sheet_name = 'sheet_name_example' # str | 
row = 56 # int | 
column = 56 # int | 
freezed_rows = 56 # int | 
freezed_columns = 56 # int | 
folder = 'folder_example' # str |  (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Unfreeze panes
    api_response = api_instance.cells_worksheets_delete_worksheet_freeze_panes(name, sheet_name, row, column, freezed_rows, freezed_columns, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsWorksheetsApi->cells_worksheets_delete_worksheet_freeze_panes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **sheet_name** | **str**|  | 
 **row** | **int**|  | 
 **column** | **int**|  | 
 **freezed_rows** | **int**|  | 
 **freezed_columns** | **int**|  | 
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

# **cells_worksheets_get_named_ranges**
> RangesResponse cells_worksheets_get_named_ranges(name, folder=folder, storage=storage)

Read worksheets ranges info.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsWorksheetsApi()
name = 'name_example' # str | Document name.
folder = 'folder_example' # str | Document folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Read worksheets ranges info.
    api_response = api_instance.cells_worksheets_get_named_ranges(name, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsWorksheetsApi->cells_worksheets_get_named_ranges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document name. | 
 **folder** | **str**| Document folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**RangesResponse**](RangesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_worksheets_get_worksheet**
> file cells_worksheets_get_worksheet(name, sheet_name, format=format, vertical_resolution=vertical_resolution, horizontal_resolution=horizontal_resolution, folder=folder, storage=storage)

Read worksheet info or export.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsWorksheetsApi()
name = 'name_example' # str | The document name.
sheet_name = 'sheet_name_example' # str | The worksheet name.
format = 'format_example' # str | The exported file format. (optional)
vertical_resolution = 0 # int | Image vertical resolution. (optional) (default to 0)
horizontal_resolution = 0 # int | Image horizontal resolution. (optional) (default to 0)
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Read worksheet info or export.
    api_response = api_instance.cells_worksheets_get_worksheet(name, sheet_name, format=format, vertical_resolution=vertical_resolution, horizontal_resolution=horizontal_resolution, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsWorksheetsApi->cells_worksheets_get_worksheet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **sheet_name** | **str**| The worksheet name. | 
 **format** | **str**| The exported file format. | [optional] 
 **vertical_resolution** | **int**| Image vertical resolution. | [optional] [default to 0]
 **horizontal_resolution** | **int**| Image horizontal resolution. | [optional] [default to 0]
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_worksheets_get_worksheet_calculate_formula**
> SingleValueResponse cells_worksheets_get_worksheet_calculate_formula(name, sheet_name, formula, folder=folder, storage=storage)

Calculate formula value.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsWorksheetsApi()
name = 'name_example' # str | Document name.
sheet_name = 'sheet_name_example' # str | Worksheet name.
formula = 'formula_example' # str | The formula.
folder = 'folder_example' # str | Document's folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Calculate formula value.
    api_response = api_instance.cells_worksheets_get_worksheet_calculate_formula(name, sheet_name, formula, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsWorksheetsApi->cells_worksheets_get_worksheet_calculate_formula: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document name. | 
 **sheet_name** | **str**| Worksheet name. | 
 **formula** | **str**| The formula. | 
 **folder** | **str**| Document&#39;s folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**SingleValueResponse**](SingleValueResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_worksheets_get_worksheet_comment**
> CommentResponse cells_worksheets_get_worksheet_comment(name, sheet_name, cell_name, folder=folder, storage=storage)

Get worksheet comment by cell name.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsWorksheetsApi()
name = 'name_example' # str | The document name.
sheet_name = 'sheet_name_example' # str | The worksheet name.
cell_name = 'cell_name_example' # str | The cell name
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Get worksheet comment by cell name.
    api_response = api_instance.cells_worksheets_get_worksheet_comment(name, sheet_name, cell_name, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsWorksheetsApi->cells_worksheets_get_worksheet_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **sheet_name** | **str**| The worksheet name. | 
 **cell_name** | **str**| The cell name | 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**CommentResponse**](CommentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_worksheets_get_worksheet_comments**
> CommentsResponse cells_worksheets_get_worksheet_comments(name, sheet_name, folder=folder, storage=storage)

Get worksheet comments.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsWorksheetsApi()
name = 'name_example' # str | Workbook name.
sheet_name = 'sheet_name_example' # str | The worksheet name.
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Get worksheet comments.
    api_response = api_instance.cells_worksheets_get_worksheet_comments(name, sheet_name, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsWorksheetsApi->cells_worksheets_get_worksheet_comments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Workbook name. | 
 **sheet_name** | **str**| The worksheet name. | 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**CommentsResponse**](CommentsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_worksheets_get_worksheet_merged_cell**
> MergedCellResponse cells_worksheets_get_worksheet_merged_cell(name, sheet_name, merged_cell_index, folder=folder, storage=storage)

Get worksheet merged cell by its index.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsWorksheetsApi()
name = 'name_example' # str | Document name.
sheet_name = 'sheet_name_example' # str | Worksheet name.
merged_cell_index = 56 # int | Merged cell index.
folder = 'folder_example' # str | Document folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Get worksheet merged cell by its index.
    api_response = api_instance.cells_worksheets_get_worksheet_merged_cell(name, sheet_name, merged_cell_index, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsWorksheetsApi->cells_worksheets_get_worksheet_merged_cell: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document name. | 
 **sheet_name** | **str**| Worksheet name. | 
 **merged_cell_index** | **int**| Merged cell index. | 
 **folder** | **str**| Document folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**MergedCellResponse**](MergedCellResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_worksheets_get_worksheet_merged_cells**
> MergedCellsResponse cells_worksheets_get_worksheet_merged_cells(name, sheet_name, folder=folder, storage=storage)

Get worksheet merged cells.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsWorksheetsApi()
name = 'name_example' # str | Document name.
sheet_name = 'sheet_name_example' # str | The workseet name.
folder = 'folder_example' # str | Document folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Get worksheet merged cells.
    api_response = api_instance.cells_worksheets_get_worksheet_merged_cells(name, sheet_name, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsWorksheetsApi->cells_worksheets_get_worksheet_merged_cells: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document name. | 
 **sheet_name** | **str**| The workseet name. | 
 **folder** | **str**| Document folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**MergedCellsResponse**](MergedCellsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_worksheets_get_worksheet_text_items**
> TextItemsResponse cells_worksheets_get_worksheet_text_items(name, sheet_name, folder=folder, storage=storage)

Get worksheet text items.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsWorksheetsApi()
name = 'name_example' # str | Workbook name.
sheet_name = 'sheet_name_example' # str | The worksheet name.
folder = 'folder_example' # str | The workbook's folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Get worksheet text items.
    api_response = api_instance.cells_worksheets_get_worksheet_text_items(name, sheet_name, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsWorksheetsApi->cells_worksheets_get_worksheet_text_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Workbook name. | 
 **sheet_name** | **str**| The worksheet name. | 
 **folder** | **str**| The workbook&#39;s folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**TextItemsResponse**](TextItemsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_worksheets_get_worksheets**
> WorksheetsResponse cells_worksheets_get_worksheets(name, folder=folder, storage=storage)

Read worksheets info.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsWorksheetsApi()
name = 'name_example' # str | Document name.
folder = 'folder_example' # str | Document folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Read worksheets info.
    api_response = api_instance.cells_worksheets_get_worksheets(name, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsWorksheetsApi->cells_worksheets_get_worksheets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document name. | 
 **folder** | **str**| Document folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**WorksheetsResponse**](WorksheetsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_worksheets_post_autofit_worksheet_columns**
> SaaSposeResponse cells_worksheets_post_autofit_worksheet_columns(name, sheet_name, first_column, last_column, auto_fitter_options=auto_fitter_options, first_row=first_row, last_row=last_row, folder=folder, storage=storage)



### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsWorksheetsApi()
name = 'name_example' # str | 
sheet_name = 'sheet_name_example' # str | 
first_column = 56 # int | 
last_column = 56 # int | 
auto_fitter_options = asposecellscloud.AutoFitterOptions() # AutoFitterOptions |  (optional)
first_row = 56 # int |  (optional)
last_row = 56 # int |  (optional)
folder = 'folder_example' # str |  (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    api_response = api_instance.cells_worksheets_post_autofit_worksheet_columns(name, sheet_name, first_column, last_column, auto_fitter_options=auto_fitter_options, first_row=first_row, last_row=last_row, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsWorksheetsApi->cells_worksheets_post_autofit_worksheet_columns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **sheet_name** | **str**|  | 
 **first_column** | **int**|  | 
 **last_column** | **int**|  | 
 **auto_fitter_options** | [**AutoFitterOptions**](AutoFitterOptions.md)|  | [optional] 
 **first_row** | **int**|  | [optional] 
 **last_row** | **int**|  | [optional] 
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

# **cells_worksheets_post_autofit_worksheet_row**
> SaaSposeResponse cells_worksheets_post_autofit_worksheet_row(name, sheet_name, row_index, first_column, last_column, auto_fitter_options=auto_fitter_options, folder=folder, storage=storage)



### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsWorksheetsApi()
name = 'name_example' # str | 
sheet_name = 'sheet_name_example' # str | 
row_index = 56 # int | 
first_column = 56 # int | 
last_column = 56 # int | 
auto_fitter_options = asposecellscloud.AutoFitterOptions() # AutoFitterOptions |  (optional)
folder = 'folder_example' # str |  (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    api_response = api_instance.cells_worksheets_post_autofit_worksheet_row(name, sheet_name, row_index, first_column, last_column, auto_fitter_options=auto_fitter_options, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsWorksheetsApi->cells_worksheets_post_autofit_worksheet_row: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **sheet_name** | **str**|  | 
 **row_index** | **int**|  | 
 **first_column** | **int**|  | 
 **last_column** | **int**|  | 
 **auto_fitter_options** | [**AutoFitterOptions**](AutoFitterOptions.md)|  | [optional] 
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

# **cells_worksheets_post_autofit_worksheet_rows**
> SaaSposeResponse cells_worksheets_post_autofit_worksheet_rows(name, sheet_name, auto_fitter_options=auto_fitter_options, start_row=start_row, end_row=end_row, only_auto=only_auto, folder=folder, storage=storage)

Autofit worksheet rows.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsWorksheetsApi()
name = 'name_example' # str | Document name.
sheet_name = 'sheet_name_example' # str | The worksheet name.
auto_fitter_options = asposecellscloud.AutoFitterOptions() # AutoFitterOptions | Auto Fitter Options. (optional)
start_row = 56 # int | Start row. (optional)
end_row = 56 # int | End row. (optional)
only_auto = false # bool | Only auto. (optional) (default to false)
folder = 'folder_example' # str | Document's folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Autofit worksheet rows.
    api_response = api_instance.cells_worksheets_post_autofit_worksheet_rows(name, sheet_name, auto_fitter_options=auto_fitter_options, start_row=start_row, end_row=end_row, only_auto=only_auto, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsWorksheetsApi->cells_worksheets_post_autofit_worksheet_rows: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document name. | 
 **sheet_name** | **str**| The worksheet name. | 
 **auto_fitter_options** | [**AutoFitterOptions**](AutoFitterOptions.md)| Auto Fitter Options. | [optional] 
 **start_row** | **int**| Start row. | [optional] 
 **end_row** | **int**| End row. | [optional] 
 **only_auto** | **bool**| Only auto. | [optional] [default to false]
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

# **cells_worksheets_post_copy_worksheet**
> SaaSposeResponse cells_worksheets_post_copy_worksheet(name, sheet_name, source_sheet, options=options, source_workbook=source_workbook, source_folder=source_folder, folder=folder, storage=storage)



### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsWorksheetsApi()
name = 'name_example' # str | 
sheet_name = 'sheet_name_example' # str | 
source_sheet = 'source_sheet_example' # str | 
options = asposecellscloud.CopyOptions() # CopyOptions |  (optional)
source_workbook = 'source_workbook_example' # str |  (optional)
source_folder = 'source_folder_example' # str |  (optional)
folder = 'folder_example' # str |  (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    api_response = api_instance.cells_worksheets_post_copy_worksheet(name, sheet_name, source_sheet, options=options, source_workbook=source_workbook, source_folder=source_folder, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsWorksheetsApi->cells_worksheets_post_copy_worksheet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **sheet_name** | **str**|  | 
 **source_sheet** | **str**|  | 
 **options** | [**CopyOptions**](CopyOptions.md)|  | [optional] 
 **source_workbook** | **str**|  | [optional] 
 **source_folder** | **str**|  | [optional] 
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

# **cells_worksheets_post_move_worksheet**
> WorksheetsResponse cells_worksheets_post_move_worksheet(name, sheet_name, moving=moving, folder=folder, storage=storage)

Move worksheet.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsWorksheetsApi()
name = 'name_example' # str | Document name.
sheet_name = 'sheet_name_example' # str | The worksheet name.
moving = asposecellscloud.WorksheetMovingRequest() # WorksheetMovingRequest | with moving parameters. (optional)
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Move worksheet.
    api_response = api_instance.cells_worksheets_post_move_worksheet(name, sheet_name, moving=moving, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsWorksheetsApi->cells_worksheets_post_move_worksheet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document name. | 
 **sheet_name** | **str**| The worksheet name. | 
 **moving** | [**WorksheetMovingRequest**](WorksheetMovingRequest.md)| with moving parameters. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**WorksheetsResponse**](WorksheetsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_worksheets_post_rename_worksheet**
> SaaSposeResponse cells_worksheets_post_rename_worksheet(name, sheet_name, newname, folder=folder, storage=storage)

Rename worksheet

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsWorksheetsApi()
name = 'name_example' # str | 
sheet_name = 'sheet_name_example' # str | 
newname = 'newname_example' # str | 
folder = 'folder_example' # str |  (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Rename worksheet
    api_response = api_instance.cells_worksheets_post_rename_worksheet(name, sheet_name, newname, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsWorksheetsApi->cells_worksheets_post_rename_worksheet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **sheet_name** | **str**|  | 
 **newname** | **str**|  | 
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

# **cells_worksheets_post_update_worksheet_property**
> WorksheetResponse cells_worksheets_post_update_worksheet_property(name, sheet_name, sheet=sheet, folder=folder, storage=storage)

Update worksheet property

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsWorksheetsApi()
name = 'name_example' # str | 
sheet_name = 'sheet_name_example' # str | 
sheet = asposecellscloud.Worksheet() # Worksheet |  (optional)
folder = 'folder_example' # str |  (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Update worksheet property
    api_response = api_instance.cells_worksheets_post_update_worksheet_property(name, sheet_name, sheet=sheet, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsWorksheetsApi->cells_worksheets_post_update_worksheet_property: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **sheet_name** | **str**|  | 
 **sheet** | [**Worksheet**](Worksheet.md)|  | [optional] 
 **folder** | **str**|  | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**WorksheetResponse**](WorksheetResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_worksheets_post_update_worksheet_zoom**
> SaaSposeResponse cells_worksheets_post_update_worksheet_zoom(name, sheet_name, value, folder=folder, storage=storage)



### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsWorksheetsApi()
name = 'name_example' # str | 
sheet_name = 'sheet_name_example' # str | 
value = 56 # int | 
folder = 'folder_example' # str |  (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    api_response = api_instance.cells_worksheets_post_update_worksheet_zoom(name, sheet_name, value, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsWorksheetsApi->cells_worksheets_post_update_worksheet_zoom: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **sheet_name** | **str**|  | 
 **value** | **int**|  | 
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

# **cells_worksheets_post_worksheet_comment**
> SaaSposeResponse cells_worksheets_post_worksheet_comment(name, sheet_name, cell_name, comment=comment, folder=folder, storage=storage)

Update worksheet's cell comment.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsWorksheetsApi()
name = 'name_example' # str | The document name.
sheet_name = 'sheet_name_example' # str | The worksheet name.
cell_name = 'cell_name_example' # str | The cell name
comment = asposecellscloud.Comment() # Comment | Comment object (optional)
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Update worksheet's cell comment.
    api_response = api_instance.cells_worksheets_post_worksheet_comment(name, sheet_name, cell_name, comment=comment, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsWorksheetsApi->cells_worksheets_post_worksheet_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **sheet_name** | **str**| The worksheet name. | 
 **cell_name** | **str**| The cell name | 
 **comment** | [**Comment**](Comment.md)| Comment object | [optional] 
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

# **cells_worksheets_post_worksheet_range_sort**
> SaaSposeResponse cells_worksheets_post_worksheet_range_sort(name, sheet_name, cell_area, data_sorter=data_sorter, folder=folder, storage=storage)

Sort worksheet range.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsWorksheetsApi()
name = 'name_example' # str | The workbook name.
sheet_name = 'sheet_name_example' # str | The worksheet name.
cell_area = 'cell_area_example' # str | The range to sort.
data_sorter = asposecellscloud.DataSorter() # DataSorter | with sorting settings. (optional)
folder = 'folder_example' # str | The workbook folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Sort worksheet range.
    api_response = api_instance.cells_worksheets_post_worksheet_range_sort(name, sheet_name, cell_area, data_sorter=data_sorter, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsWorksheetsApi->cells_worksheets_post_worksheet_range_sort: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The workbook name. | 
 **sheet_name** | **str**| The worksheet name. | 
 **cell_area** | **str**| The range to sort. | 
 **data_sorter** | [**DataSorter**](DataSorter.md)| with sorting settings. | [optional] 
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

# **cells_worksheets_post_worksheet_text_search**
> TextItemsResponse cells_worksheets_post_worksheet_text_search(name, sheet_name, text, folder=folder, storage=storage)

Search text.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsWorksheetsApi()
name = 'name_example' # str | Document name.
sheet_name = 'sheet_name_example' # str | The worksheet name.
text = 'text_example' # str | Text to search.
folder = 'folder_example' # str | Document's folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Search text.
    api_response = api_instance.cells_worksheets_post_worksheet_text_search(name, sheet_name, text, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsWorksheetsApi->cells_worksheets_post_worksheet_text_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document name. | 
 **sheet_name** | **str**| The worksheet name. | 
 **text** | **str**| Text to search. | 
 **folder** | **str**| Document&#39;s folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**TextItemsResponse**](TextItemsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_worksheets_post_worsheet_text_replace**
> WorksheetReplaceResponse cells_worksheets_post_worsheet_text_replace(name, sheet_name, old_value, new_value, folder=folder, storage=storage)

Replace text.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsWorksheetsApi()
name = 'name_example' # str | Document name.
sheet_name = 'sheet_name_example' # str | Worksheet name.
old_value = 'old_value_example' # str | The old text to replace.
new_value = 'new_value_example' # str | The new text to replace by.
folder = 'folder_example' # str | Document's folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Replace text.
    api_response = api_instance.cells_worksheets_post_worsheet_text_replace(name, sheet_name, old_value, new_value, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsWorksheetsApi->cells_worksheets_post_worsheet_text_replace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document name. | 
 **sheet_name** | **str**| Worksheet name. | 
 **old_value** | **str**| The old text to replace. | 
 **new_value** | **str**| The new text to replace by. | 
 **folder** | **str**| Document&#39;s folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**WorksheetReplaceResponse**](WorksheetReplaceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_worksheets_put_add_new_worksheet**
> WorksheetsResponse cells_worksheets_put_add_new_worksheet(name, sheet_name, position=position, sheettype=sheettype, folder=folder, storage=storage)

Add new worksheet.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsWorksheetsApi()
name = 'name_example' # str | Document name.
sheet_name = 'sheet_name_example' # str | The new sheet name.
position = 56 # int | The new sheet position. (optional)
sheettype = 'sheettype_example' # str | The new sheet type. (optional)
folder = 'folder_example' # str | Document folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Add new worksheet.
    api_response = api_instance.cells_worksheets_put_add_new_worksheet(name, sheet_name, position=position, sheettype=sheettype, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsWorksheetsApi->cells_worksheets_put_add_new_worksheet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document name. | 
 **sheet_name** | **str**| The new sheet name. | 
 **position** | **int**| The new sheet position. | [optional] 
 **sheettype** | **str**| The new sheet type. | [optional] 
 **folder** | **str**| Document folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**WorksheetsResponse**](WorksheetsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_worksheets_put_change_visibility_worksheet**
> WorksheetResponse cells_worksheets_put_change_visibility_worksheet(name, sheet_name, is_visible, folder=folder, storage=storage)

Change worksheet visibility.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsWorksheetsApi()
name = 'name_example' # str | Document name.
sheet_name = 'sheet_name_example' # str | Worksheet name.
is_visible = true # bool | New worksheet visibility value.
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Change worksheet visibility.
    api_response = api_instance.cells_worksheets_put_change_visibility_worksheet(name, sheet_name, is_visible, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsWorksheetsApi->cells_worksheets_put_change_visibility_worksheet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document name. | 
 **sheet_name** | **str**| Worksheet name. | 
 **is_visible** | **bool**| New worksheet visibility value. | 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**WorksheetResponse**](WorksheetResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_worksheets_put_protect_worksheet**
> WorksheetResponse cells_worksheets_put_protect_worksheet(name, sheet_name, protect_parameter=protect_parameter, folder=folder, storage=storage)

Protect worksheet.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsWorksheetsApi()
name = 'name_example' # str | Document name.
sheet_name = 'sheet_name_example' # str | The worksheet name.
protect_parameter = asposecellscloud.ProtectSheetParameter() # ProtectSheetParameter | with protection settings. (optional)
folder = 'folder_example' # str | Document folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Protect worksheet.
    api_response = api_instance.cells_worksheets_put_protect_worksheet(name, sheet_name, protect_parameter=protect_parameter, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsWorksheetsApi->cells_worksheets_put_protect_worksheet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document name. | 
 **sheet_name** | **str**| The worksheet name. | 
 **protect_parameter** | [**ProtectSheetParameter**](ProtectSheetParameter.md)| with protection settings. | [optional] 
 **folder** | **str**| Document folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**WorksheetResponse**](WorksheetResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_worksheets_put_worksheet_background**
> SaaSposeResponse cells_worksheets_put_worksheet_background(name, sheet_name, png, folder=folder, storage=storage)

Set worksheet background image.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsWorksheetsApi()
name = 'name_example' # str | 
sheet_name = 'sheet_name_example' # str | 
png = 'B' # str | 
folder = 'folder_example' # str |  (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Set worksheet background image.
    api_response = api_instance.cells_worksheets_put_worksheet_background(name, sheet_name, png, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsWorksheetsApi->cells_worksheets_put_worksheet_background: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **sheet_name** | **str**|  | 
 **png** | **str**|  | 
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

# **cells_worksheets_put_worksheet_comment**
> CommentResponse cells_worksheets_put_worksheet_comment(name, sheet_name, cell_name, comment=comment, folder=folder, storage=storage)

Add worksheet's cell comment.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsWorksheetsApi()
name = 'name_example' # str | The document name.
sheet_name = 'sheet_name_example' # str | The worksheet name.
cell_name = 'cell_name_example' # str | The cell name
comment = asposecellscloud.Comment() # Comment | Comment object (optional)
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Add worksheet's cell comment.
    api_response = api_instance.cells_worksheets_put_worksheet_comment(name, sheet_name, cell_name, comment=comment, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsWorksheetsApi->cells_worksheets_put_worksheet_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **sheet_name** | **str**| The worksheet name. | 
 **cell_name** | **str**| The cell name | 
 **comment** | [**Comment**](Comment.md)| Comment object | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**CommentResponse**](CommentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_worksheets_put_worksheet_freeze_panes**
> SaaSposeResponse cells_worksheets_put_worksheet_freeze_panes(name, sheet_name, row, column, freezed_rows, freezed_columns, folder=folder, storage=storage)

Set freeze panes

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsWorksheetsApi()
name = 'name_example' # str | 
sheet_name = 'sheet_name_example' # str | 
row = 56 # int | 
column = 56 # int | 
freezed_rows = 56 # int | 
freezed_columns = 56 # int | 
folder = 'folder_example' # str |  (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Set freeze panes
    api_response = api_instance.cells_worksheets_put_worksheet_freeze_panes(name, sheet_name, row, column, freezed_rows, freezed_columns, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsWorksheetsApi->cells_worksheets_put_worksheet_freeze_panes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **sheet_name** | **str**|  | 
 **row** | **int**|  | 
 **column** | **int**|  | 
 **freezed_rows** | **int**|  | 
 **freezed_columns** | **int**|  | 
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

