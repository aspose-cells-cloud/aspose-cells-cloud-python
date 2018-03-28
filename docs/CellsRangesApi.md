# asposecellscloud.CellsRangesApi

All URIs are relative to *https://api.aspose.cloud/v1.1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cells_ranges_get_worksheet_cells_range_value**](CellsRangesApi.md#cells_ranges_get_worksheet_cells_range_value) | **GET** /cells/{name}/worksheets/{sheetName}/ranges/value | Get cells list in a range by range name or row column indexes  
[**cells_ranges_post_worksheet_cells_range_column_width**](CellsRangesApi.md#cells_ranges_post_worksheet_cells_range_column_width) | **POST** /cells/{name}/worksheets/{sheetName}/ranges/columnWidth | Set column width of range
[**cells_ranges_post_worksheet_cells_range_merge**](CellsRangesApi.md#cells_ranges_post_worksheet_cells_range_merge) | **POST** /cells/{name}/worksheets/{sheetName}/ranges/merge | Combines a range of cells into a single cell.              
[**cells_ranges_post_worksheet_cells_range_move_to**](CellsRangesApi.md#cells_ranges_post_worksheet_cells_range_move_to) | **POST** /cells/{name}/worksheets/{sheetName}/ranges/moveto | Move the current range to the dest range.             
[**cells_ranges_post_worksheet_cells_range_outline_border**](CellsRangesApi.md#cells_ranges_post_worksheet_cells_range_outline_border) | **POST** /cells/{name}/worksheets/{sheetName}/ranges/outlineBorder | Sets outline border around a range of cells.
[**cells_ranges_post_worksheet_cells_range_row_height**](CellsRangesApi.md#cells_ranges_post_worksheet_cells_range_row_height) | **POST** /cells/{name}/worksheets/{sheetName}/ranges/rowHeight | set row height of range
[**cells_ranges_post_worksheet_cells_range_style**](CellsRangesApi.md#cells_ranges_post_worksheet_cells_range_style) | **POST** /cells/{name}/worksheets/{sheetName}/ranges/style | Sets the style of the range.             
[**cells_ranges_post_worksheet_cells_range_unmerge**](CellsRangesApi.md#cells_ranges_post_worksheet_cells_range_unmerge) | **POST** /cells/{name}/worksheets/{sheetName}/ranges/unmerge | Unmerges merged cells of this range.             
[**cells_ranges_post_worksheet_cells_range_value**](CellsRangesApi.md#cells_ranges_post_worksheet_cells_range_value) | **POST** /cells/{name}/worksheets/{sheetName}/ranges/value | Puts a value into the range, if appropriate the value will be converted to other data type and cell&#39;s number format will be reset.             
[**cells_ranges_post_worksheet_cells_ranges**](CellsRangesApi.md#cells_ranges_post_worksheet_cells_ranges) | **POST** /cells/{name}/worksheets/{sheetName}/ranges | copy range in the worksheet


# **cells_ranges_get_worksheet_cells_range_value**
> RangeValueResponse cells_ranges_get_worksheet_cells_range_value(name, sheet_name, namerange=namerange, first_row=first_row, first_column=first_column, row_count=row_count, column_count=column_count, folder=folder)

Get cells list in a range by range name or row column indexes  

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsRangesApi()
name = 'name_example' # str | workbook name
sheet_name = 'sheet_name_example' # str | worksheet name
namerange = 'namerange_example' # str | range name, for example: 'A1:B2' or 'range_name1' (optional)
first_row = 56 # int | the first row of the range (optional)
first_column = 56 # int | the first column of the range (optional)
row_count = 56 # int | the count of rows in the range (optional)
column_count = 56 # int | the count of columns in the range (optional)
folder = 'folder_example' # str | Workbook folder. (optional)

try: 
    # Get cells list in a range by range name or row column indexes  
    api_response = api_instance.cells_ranges_get_worksheet_cells_range_value(name, sheet_name, namerange=namerange, first_row=first_row, first_column=first_column, row_count=row_count, column_count=column_count, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsRangesApi->cells_ranges_get_worksheet_cells_range_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| workbook name | 
 **sheet_name** | **str**| worksheet name | 
 **namerange** | **str**| range name, for example: &#39;A1:B2&#39; or &#39;range_name1&#39; | [optional] 
 **first_row** | **int**| the first row of the range | [optional] 
 **first_column** | **int**| the first column of the range | [optional] 
 **row_count** | **int**| the count of rows in the range | [optional] 
 **column_count** | **int**| the count of columns in the range | [optional] 
 **folder** | **str**| Workbook folder. | [optional] 

### Return type

[**RangeValueResponse**](RangeValueResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_ranges_post_worksheet_cells_range_column_width**
> SaaSposeResponse cells_ranges_post_worksheet_cells_range_column_width(name, sheet_name, value, range=range, folder=folder)

Set column width of range

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsRangesApi()
name = 'name_example' # str | 
sheet_name = 'sheet_name_example' # str | 
value = 1.2 # float | 
range = asposecellscloud.Range() # Range |  (optional)
folder = 'folder_example' # str |  (optional)

try: 
    # Set column width of range
    api_response = api_instance.cells_ranges_post_worksheet_cells_range_column_width(name, sheet_name, value, range=range, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsRangesApi->cells_ranges_post_worksheet_cells_range_column_width: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **sheet_name** | **str**|  | 
 **value** | **float**|  | 
 **range** | [**Range**](Range.md)|  | [optional] 
 **folder** | **str**|  | [optional] 

### Return type

[**SaaSposeResponse**](SaaSposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_ranges_post_worksheet_cells_range_merge**
> SaaSposeResponse cells_ranges_post_worksheet_cells_range_merge(name, sheet_name, range=range, folder=folder)

Combines a range of cells into a single cell.              

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsRangesApi()
name = 'name_example' # str | workbook name
sheet_name = 'sheet_name_example' # str | worksheet name
range = asposecellscloud.Range() # Range | range in worksheet  (optional)
folder = 'folder_example' # str | Workbook folder. (optional)

try: 
    # Combines a range of cells into a single cell.              
    api_response = api_instance.cells_ranges_post_worksheet_cells_range_merge(name, sheet_name, range=range, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsRangesApi->cells_ranges_post_worksheet_cells_range_merge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| workbook name | 
 **sheet_name** | **str**| worksheet name | 
 **range** | [**Range**](Range.md)| range in worksheet  | [optional] 
 **folder** | **str**| Workbook folder. | [optional] 

### Return type

[**SaaSposeResponse**](SaaSposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_ranges_post_worksheet_cells_range_move_to**
> SaaSposeResponse cells_ranges_post_worksheet_cells_range_move_to(name, sheet_name, dest_row, dest_column, range=range, folder=folder)

Move the current range to the dest range.             

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsRangesApi()
name = 'name_example' # str | workbook name
sheet_name = 'sheet_name_example' # str | worksheet name
dest_row = 56 # int | The start row of the dest range.
dest_column = 56 # int | The start column of the dest range.
range = asposecellscloud.Range() # Range | range in worksheet  (optional)
folder = 'folder_example' # str | Workbook folder. (optional)

try: 
    # Move the current range to the dest range.             
    api_response = api_instance.cells_ranges_post_worksheet_cells_range_move_to(name, sheet_name, dest_row, dest_column, range=range, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsRangesApi->cells_ranges_post_worksheet_cells_range_move_to: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| workbook name | 
 **sheet_name** | **str**| worksheet name | 
 **dest_row** | **int**| The start row of the dest range. | 
 **dest_column** | **int**| The start column of the dest range. | 
 **range** | [**Range**](Range.md)| range in worksheet  | [optional] 
 **folder** | **str**| Workbook folder. | [optional] 

### Return type

[**SaaSposeResponse**](SaaSposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_ranges_post_worksheet_cells_range_outline_border**
> SaaSposeResponse cells_ranges_post_worksheet_cells_range_outline_border(name, sheet_name, range_operate=range_operate, folder=folder)

Sets outline border around a range of cells.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsRangesApi()
name = 'name_example' # str | workbook name
sheet_name = 'sheet_name_example' # str | worksheet name
range_operate = asposecellscloud.RangeSetOutlineBorderRequest() # RangeSetOutlineBorderRequest | Range Set OutlineBorder Request  (optional)
folder = 'folder_example' # str | Workbook folder. (optional)

try: 
    # Sets outline border around a range of cells.
    api_response = api_instance.cells_ranges_post_worksheet_cells_range_outline_border(name, sheet_name, range_operate=range_operate, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsRangesApi->cells_ranges_post_worksheet_cells_range_outline_border: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| workbook name | 
 **sheet_name** | **str**| worksheet name | 
 **range_operate** | [**RangeSetOutlineBorderRequest**](RangeSetOutlineBorderRequest.md)| Range Set OutlineBorder Request  | [optional] 
 **folder** | **str**| Workbook folder. | [optional] 

### Return type

[**SaaSposeResponse**](SaaSposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_ranges_post_worksheet_cells_range_row_height**
> SaaSposeResponse cells_ranges_post_worksheet_cells_range_row_height(name, sheet_name, value, range=range, folder=folder)

set row height of range

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsRangesApi()
name = 'name_example' # str | 
sheet_name = 'sheet_name_example' # str | 
value = 1.2 # float | 
range = asposecellscloud.Range() # Range |  (optional)
folder = 'folder_example' # str |  (optional)

try: 
    # set row height of range
    api_response = api_instance.cells_ranges_post_worksheet_cells_range_row_height(name, sheet_name, value, range=range, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsRangesApi->cells_ranges_post_worksheet_cells_range_row_height: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **sheet_name** | **str**|  | 
 **value** | **float**|  | 
 **range** | [**Range**](Range.md)|  | [optional] 
 **folder** | **str**|  | [optional] 

### Return type

[**SaaSposeResponse**](SaaSposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_ranges_post_worksheet_cells_range_style**
> SaaSposeResponse cells_ranges_post_worksheet_cells_range_style(name, sheet_name, range_operate=range_operate, folder=folder)

Sets the style of the range.             

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsRangesApi()
name = 'name_example' # str | workbook name
sheet_name = 'sheet_name_example' # str | worksheet name
range_operate = asposecellscloud.RangeSetStyleRequest() # RangeSetStyleRequest | Range Set Style Request  (optional)
folder = 'folder_example' # str | Workbook folder. (optional)

try: 
    # Sets the style of the range.             
    api_response = api_instance.cells_ranges_post_worksheet_cells_range_style(name, sheet_name, range_operate=range_operate, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsRangesApi->cells_ranges_post_worksheet_cells_range_style: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| workbook name | 
 **sheet_name** | **str**| worksheet name | 
 **range_operate** | [**RangeSetStyleRequest**](RangeSetStyleRequest.md)| Range Set Style Request  | [optional] 
 **folder** | **str**| Workbook folder. | [optional] 

### Return type

[**SaaSposeResponse**](SaaSposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_ranges_post_worksheet_cells_range_unmerge**
> SaaSposeResponse cells_ranges_post_worksheet_cells_range_unmerge(name, sheet_name, range=range, folder=folder)

Unmerges merged cells of this range.             

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsRangesApi()
name = 'name_example' # str | workbook name
sheet_name = 'sheet_name_example' # str | worksheet name
range = asposecellscloud.Range() # Range | range in worksheet  (optional)
folder = 'folder_example' # str | Workbook folder. (optional)

try: 
    # Unmerges merged cells of this range.             
    api_response = api_instance.cells_ranges_post_worksheet_cells_range_unmerge(name, sheet_name, range=range, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsRangesApi->cells_ranges_post_worksheet_cells_range_unmerge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| workbook name | 
 **sheet_name** | **str**| worksheet name | 
 **range** | [**Range**](Range.md)| range in worksheet  | [optional] 
 **folder** | **str**| Workbook folder. | [optional] 

### Return type

[**SaaSposeResponse**](SaaSposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_ranges_post_worksheet_cells_range_value**
> SaaSposeResponse cells_ranges_post_worksheet_cells_range_value(name, sheet_name, value, range=range, is_converted=is_converted, set_style=set_style, folder=folder)

Puts a value into the range, if appropriate the value will be converted to other data type and cell's number format will be reset.             

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsRangesApi()
name = 'name_example' # str | workbook name
sheet_name = 'sheet_name_example' # str | worksheet name
value = 'value_example' # str | Input value
range = asposecellscloud.Range() # Range | range in worksheet  (optional)
is_converted = false # bool | True: converted to other data type if appropriate. (optional) (default to false)
set_style = false # bool | True: set the number format to cell's style when converting to other data type (optional) (default to false)
folder = 'folder_example' # str | Workbook folder. (optional)

try: 
    # Puts a value into the range, if appropriate the value will be converted to other data type and cell's number format will be reset.             
    api_response = api_instance.cells_ranges_post_worksheet_cells_range_value(name, sheet_name, value, range=range, is_converted=is_converted, set_style=set_style, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsRangesApi->cells_ranges_post_worksheet_cells_range_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| workbook name | 
 **sheet_name** | **str**| worksheet name | 
 **value** | **str**| Input value | 
 **range** | [**Range**](Range.md)| range in worksheet  | [optional] 
 **is_converted** | **bool**| True: converted to other data type if appropriate. | [optional] [default to false]
 **set_style** | **bool**| True: set the number format to cell&#39;s style when converting to other data type | [optional] [default to false]
 **folder** | **str**| Workbook folder. | [optional] 

### Return type

[**SaaSposeResponse**](SaaSposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_ranges_post_worksheet_cells_ranges**
> SaaSposeResponse cells_ranges_post_worksheet_cells_ranges(name, sheet_name, range_operate=range_operate, folder=folder)

copy range in the worksheet

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsRangesApi()
name = 'name_example' # str | workbook name
sheet_name = 'sheet_name_example' # str | worksheet name
range_operate = asposecellscloud.RangeCopyRequest() # RangeCopyRequest | copydata,copystyle,copyto,copyvalue (optional)
folder = 'folder_example' # str | Workbook folder. (optional)

try: 
    # copy range in the worksheet
    api_response = api_instance.cells_ranges_post_worksheet_cells_ranges(name, sheet_name, range_operate=range_operate, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsRangesApi->cells_ranges_post_worksheet_cells_ranges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| workbook name | 
 **sheet_name** | **str**| worksheet name | 
 **range_operate** | [**RangeCopyRequest**](RangeCopyRequest.md)| copydata,copystyle,copyto,copyvalue | [optional] 
 **folder** | **str**| Workbook folder. | [optional] 

### Return type

[**SaaSposeResponse**](SaaSposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

