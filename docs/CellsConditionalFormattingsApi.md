# asposecellscloud.CellsConditionalFormattingsApi

All URIs are relative to *https://api.aspose.cloud/v1.1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cells_conditional_formattings_delete_worksheet_conditional_formatting**](CellsConditionalFormattingsApi.md#cells_conditional_formattings_delete_worksheet_conditional_formatting) | **DELETE** /cells/{name}/worksheets/{sheetName}/conditionalFormattings/{index} | Remove conditional formatting
[**cells_conditional_formattings_delete_worksheet_conditional_formatting_area**](CellsConditionalFormattingsApi.md#cells_conditional_formattings_delete_worksheet_conditional_formatting_area) | **DELETE** /cells/{name}/worksheets/{sheetName}/conditionalFormattings/area | Remove cell area from conditional formatting.
[**cells_conditional_formattings_delete_worksheet_conditional_formattings**](CellsConditionalFormattingsApi.md#cells_conditional_formattings_delete_worksheet_conditional_formattings) | **DELETE** /cells/{name}/worksheets/{sheetName}/conditionalFormattings | Clear all condition formattings
[**cells_conditional_formattings_get_worksheet_conditional_formatting**](CellsConditionalFormattingsApi.md#cells_conditional_formattings_get_worksheet_conditional_formatting) | **GET** /cells/{name}/worksheets/{sheetName}/conditionalFormattings/{index} | Get conditional formatting
[**cells_conditional_formattings_get_worksheet_conditional_formattings**](CellsConditionalFormattingsApi.md#cells_conditional_formattings_get_worksheet_conditional_formattings) | **GET** /cells/{name}/worksheets/{sheetName}/conditionalFormattings | Get conditional formattings 
[**cells_conditional_formattings_put_worksheet_conditional_formatting**](CellsConditionalFormattingsApi.md#cells_conditional_formattings_put_worksheet_conditional_formatting) | **PUT** /cells/{name}/worksheets/{sheetName}/conditionalFormattings | Add a condition formatting.
[**cells_conditional_formattings_put_worksheet_format_condition**](CellsConditionalFormattingsApi.md#cells_conditional_formattings_put_worksheet_format_condition) | **PUT** /cells/{name}/worksheets/{sheetName}/conditionalFormattings/{index} | Add a format condition.
[**cells_conditional_formattings_put_worksheet_format_condition_area**](CellsConditionalFormattingsApi.md#cells_conditional_formattings_put_worksheet_format_condition_area) | **PUT** /cells/{name}/worksheets/{sheetName}/conditionalFormattings/{index}/area | add a cell area for format condition             
[**cells_conditional_formattings_put_worksheet_format_condition_condition**](CellsConditionalFormattingsApi.md#cells_conditional_formattings_put_worksheet_format_condition_condition) | **PUT** /cells/{name}/worksheets/{sheetName}/conditionalFormattings/{index}/condition | Add a condition for format condition.


# **cells_conditional_formattings_delete_worksheet_conditional_formatting**
> SaaSposeResponse cells_conditional_formattings_delete_worksheet_conditional_formatting(name, sheet_name, index, folder=folder)

Remove conditional formatting

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsConditionalFormattingsApi()
name = 'name_example' # str | 
sheet_name = 'sheet_name_example' # str | 
index = 56 # int | 
folder = 'folder_example' # str |  (optional)

try: 
    # Remove conditional formatting
    api_response = api_instance.cells_conditional_formattings_delete_worksheet_conditional_formatting(name, sheet_name, index, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsConditionalFormattingsApi->cells_conditional_formattings_delete_worksheet_conditional_formatting: %s\n" % e)
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

# **cells_conditional_formattings_delete_worksheet_conditional_formatting_area**
> SaaSposeResponse cells_conditional_formattings_delete_worksheet_conditional_formatting_area(name, sheet_name, start_row, start_column, total_rows, total_columns, folder=folder)

Remove cell area from conditional formatting.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsConditionalFormattingsApi()
name = 'name_example' # str | 
sheet_name = 'sheet_name_example' # str | 
start_row = 56 # int | 
start_column = 56 # int | 
total_rows = 56 # int | 
total_columns = 56 # int | 
folder = 'folder_example' # str |  (optional)

try: 
    # Remove cell area from conditional formatting.
    api_response = api_instance.cells_conditional_formattings_delete_worksheet_conditional_formatting_area(name, sheet_name, start_row, start_column, total_rows, total_columns, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsConditionalFormattingsApi->cells_conditional_formattings_delete_worksheet_conditional_formatting_area: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **sheet_name** | **str**|  | 
 **start_row** | **int**|  | 
 **start_column** | **int**|  | 
 **total_rows** | **int**|  | 
 **total_columns** | **int**|  | 
 **folder** | **str**|  | [optional] 

### Return type

[**SaaSposeResponse**](SaaSposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_conditional_formattings_delete_worksheet_conditional_formattings**
> SaaSposeResponse cells_conditional_formattings_delete_worksheet_conditional_formattings(name, sheet_name, folder=folder)

Clear all condition formattings

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsConditionalFormattingsApi()
name = 'name_example' # str | 
sheet_name = 'sheet_name_example' # str | 
folder = 'folder_example' # str |  (optional)

try: 
    # Clear all condition formattings
    api_response = api_instance.cells_conditional_formattings_delete_worksheet_conditional_formattings(name, sheet_name, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsConditionalFormattingsApi->cells_conditional_formattings_delete_worksheet_conditional_formattings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **sheet_name** | **str**|  | 
 **folder** | **str**|  | [optional] 

### Return type

[**SaaSposeResponse**](SaaSposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_conditional_formattings_get_worksheet_conditional_formatting**
> ConditionalFormattingResponse cells_conditional_formattings_get_worksheet_conditional_formatting(name, sheet_name, index, folder=folder)

Get conditional formatting

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsConditionalFormattingsApi()
name = 'name_example' # str | 
sheet_name = 'sheet_name_example' # str | 
index = 56 # int | 
folder = 'folder_example' # str |  (optional)

try: 
    # Get conditional formatting
    api_response = api_instance.cells_conditional_formattings_get_worksheet_conditional_formatting(name, sheet_name, index, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsConditionalFormattingsApi->cells_conditional_formattings_get_worksheet_conditional_formatting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **sheet_name** | **str**|  | 
 **index** | **int**|  | 
 **folder** | **str**|  | [optional] 

### Return type

[**ConditionalFormattingResponse**](ConditionalFormattingResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_conditional_formattings_get_worksheet_conditional_formattings**
> ConditionalFormattingsResponse cells_conditional_formattings_get_worksheet_conditional_formattings(name, sheet_name, folder=folder)

Get conditional formattings 

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsConditionalFormattingsApi()
name = 'name_example' # str | 
sheet_name = 'sheet_name_example' # str | 
folder = 'folder_example' # str |  (optional)

try: 
    # Get conditional formattings 
    api_response = api_instance.cells_conditional_formattings_get_worksheet_conditional_formattings(name, sheet_name, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsConditionalFormattingsApi->cells_conditional_formattings_get_worksheet_conditional_formattings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **sheet_name** | **str**|  | 
 **folder** | **str**|  | [optional] 

### Return type

[**ConditionalFormattingsResponse**](ConditionalFormattingsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_conditional_formattings_put_worksheet_conditional_formatting**
> SaaSposeResponse cells_conditional_formattings_put_worksheet_conditional_formatting(name, sheet_name, cell_area, formatcondition=formatcondition, folder=folder)

Add a condition formatting.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsConditionalFormattingsApi()
name = 'name_example' # str | 
sheet_name = 'sheet_name_example' # str | 
cell_area = 'cell_area_example' # str | 
formatcondition = asposecellscloud.FormatCondition() # FormatCondition |  (optional)
folder = 'folder_example' # str |  (optional)

try: 
    # Add a condition formatting.
    api_response = api_instance.cells_conditional_formattings_put_worksheet_conditional_formatting(name, sheet_name, cell_area, formatcondition=formatcondition, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsConditionalFormattingsApi->cells_conditional_formattings_put_worksheet_conditional_formatting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **sheet_name** | **str**|  | 
 **cell_area** | **str**|  | 
 **formatcondition** | [**FormatCondition**](FormatCondition.md)|  | [optional] 
 **folder** | **str**|  | [optional] 

### Return type

[**SaaSposeResponse**](SaaSposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_conditional_formattings_put_worksheet_format_condition**
> SaaSposeResponse cells_conditional_formattings_put_worksheet_format_condition(name, sheet_name, index, cell_area, type, operator_type, formula1, formula2, folder=folder)

Add a format condition.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsConditionalFormattingsApi()
name = 'name_example' # str | 
sheet_name = 'sheet_name_example' # str | 
index = 56 # int | 
cell_area = 'cell_area_example' # str | 
type = 'type_example' # str | 
operator_type = 'operator_type_example' # str | 
formula1 = 'formula1_example' # str | 
formula2 = 'formula2_example' # str | 
folder = 'folder_example' # str |  (optional)

try: 
    # Add a format condition.
    api_response = api_instance.cells_conditional_formattings_put_worksheet_format_condition(name, sheet_name, index, cell_area, type, operator_type, formula1, formula2, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsConditionalFormattingsApi->cells_conditional_formattings_put_worksheet_format_condition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **sheet_name** | **str**|  | 
 **index** | **int**|  | 
 **cell_area** | **str**|  | 
 **type** | **str**|  | 
 **operator_type** | **str**|  | 
 **formula1** | **str**|  | 
 **formula2** | **str**|  | 
 **folder** | **str**|  | [optional] 

### Return type

[**SaaSposeResponse**](SaaSposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_conditional_formattings_put_worksheet_format_condition_area**
> SaaSposeResponse cells_conditional_formattings_put_worksheet_format_condition_area(name, sheet_name, index, cell_area, folder=folder)

add a cell area for format condition             

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsConditionalFormattingsApi()
name = 'name_example' # str | 
sheet_name = 'sheet_name_example' # str | 
index = 56 # int | 
cell_area = 'cell_area_example' # str | 
folder = 'folder_example' # str |  (optional)

try: 
    # add a cell area for format condition             
    api_response = api_instance.cells_conditional_formattings_put_worksheet_format_condition_area(name, sheet_name, index, cell_area, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsConditionalFormattingsApi->cells_conditional_formattings_put_worksheet_format_condition_area: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **sheet_name** | **str**|  | 
 **index** | **int**|  | 
 **cell_area** | **str**|  | 
 **folder** | **str**|  | [optional] 

### Return type

[**SaaSposeResponse**](SaaSposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_conditional_formattings_put_worksheet_format_condition_condition**
> SaaSposeResponse cells_conditional_formattings_put_worksheet_format_condition_condition(name, sheet_name, index, type, operator_type, formula1, formula2, folder=folder)

Add a condition for format condition.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsConditionalFormattingsApi()
name = 'name_example' # str | 
sheet_name = 'sheet_name_example' # str | 
index = 56 # int | 
type = 'type_example' # str | 
operator_type = 'operator_type_example' # str | 
formula1 = 'formula1_example' # str | 
formula2 = 'formula2_example' # str | 
folder = 'folder_example' # str |  (optional)

try: 
    # Add a condition for format condition.
    api_response = api_instance.cells_conditional_formattings_put_worksheet_format_condition_condition(name, sheet_name, index, type, operator_type, formula1, formula2, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsConditionalFormattingsApi->cells_conditional_formattings_put_worksheet_format_condition_condition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **sheet_name** | **str**|  | 
 **index** | **int**|  | 
 **type** | **str**|  | 
 **operator_type** | **str**|  | 
 **formula1** | **str**|  | 
 **formula2** | **str**|  | 
 **folder** | **str**|  | [optional] 

### Return type

[**SaaSposeResponse**](SaaSposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

