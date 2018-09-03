# asposecellscloud.CellsChartAreaApi

All URIs are relative to *https://api.aspose.cloud/v1.1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cells_chart_area_get_chart_area**](CellsChartAreaApi.md#cells_chart_area_get_chart_area) | **GET** /cells/{name}/worksheets/{sheetName}/charts/{chartIndex}/chartArea | Get chart area info.
[**cells_chart_area_get_chart_area_border**](CellsChartAreaApi.md#cells_chart_area_get_chart_area_border) | **GET** /cells/{name}/worksheets/{sheetName}/charts/{chartIndex}/chartArea/border | Get chart area border info.
[**cells_chart_area_get_chart_area_fill_format**](CellsChartAreaApi.md#cells_chart_area_get_chart_area_fill_format) | **GET** /cells/{name}/worksheets/{sheetName}/charts/{chartIndex}/chartArea/fillFormat | Get chart area fill format info.


# **cells_chart_area_get_chart_area**
> ChartAreaResponse cells_chart_area_get_chart_area(name, sheet_name, chart_index, folder=folder, storage=storage)

Get chart area info.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsChartAreaApi()
name = 'name_example' # str | Workbook name.
sheet_name = 'sheet_name_example' # str | Worksheet name.
chart_index = 56 # int | The chart index.
folder = 'folder_example' # str | Workbook folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Get chart area info.
    api_response = api_instance.cells_chart_area_get_chart_area(name, sheet_name, chart_index, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsChartAreaApi->cells_chart_area_get_chart_area: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Workbook name. | 
 **sheet_name** | **str**| Worksheet name. | 
 **chart_index** | **int**| The chart index. | 
 **folder** | **str**| Workbook folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**ChartAreaResponse**](ChartAreaResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_chart_area_get_chart_area_border**
> LineResponse cells_chart_area_get_chart_area_border(name, sheet_name, chart_index, folder=folder, storage=storage)

Get chart area border info.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsChartAreaApi()
name = 'name_example' # str | Workbook name.
sheet_name = 'sheet_name_example' # str | Worksheet name.
chart_index = 56 # int | The chart index.
folder = 'folder_example' # str | Workbook folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Get chart area border info.
    api_response = api_instance.cells_chart_area_get_chart_area_border(name, sheet_name, chart_index, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsChartAreaApi->cells_chart_area_get_chart_area_border: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Workbook name. | 
 **sheet_name** | **str**| Worksheet name. | 
 **chart_index** | **int**| The chart index. | 
 **folder** | **str**| Workbook folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**LineResponse**](LineResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_chart_area_get_chart_area_fill_format**
> FillFormatResponse cells_chart_area_get_chart_area_fill_format(name, sheet_name, chart_index, folder=folder, storage=storage)

Get chart area fill format info.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsChartAreaApi()
name = 'name_example' # str | Workbook name.
sheet_name = 'sheet_name_example' # str | Worksheet name.
chart_index = 56 # int | The chart index.
folder = 'folder_example' # str | Workbook folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Get chart area fill format info.
    api_response = api_instance.cells_chart_area_get_chart_area_fill_format(name, sheet_name, chart_index, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsChartAreaApi->cells_chart_area_get_chart_area_fill_format: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Workbook name. | 
 **sheet_name** | **str**| Worksheet name. | 
 **chart_index** | **int**| The chart index. | 
 **folder** | **str**| Workbook folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**FillFormatResponse**](FillFormatResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

