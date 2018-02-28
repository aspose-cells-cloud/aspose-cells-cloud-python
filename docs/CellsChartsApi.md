# asposecellscloud.CellsChartsApi

All URIs are relative to *https://api.aspose.cloud/v1.1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cells_charts_delete_worksheet_chart_legend**](CellsChartsApi.md#cells_charts_delete_worksheet_chart_legend) | **DELETE** /cells/{name}/worksheets/{sheetName}/charts/{chartIndex}/legend | Hide legend in chart
[**cells_charts_delete_worksheet_chart_title**](CellsChartsApi.md#cells_charts_delete_worksheet_chart_title) | **DELETE** /cells/{name}/worksheets/{sheetName}/charts/{chartIndex}/title | Hide title in chart
[**cells_charts_delete_worksheet_clear_charts**](CellsChartsApi.md#cells_charts_delete_worksheet_clear_charts) | **DELETE** /cells/{name}/worksheets/{sheetName}/charts | Clear the charts.
[**cells_charts_delete_worksheet_delete_chart**](CellsChartsApi.md#cells_charts_delete_worksheet_delete_chart) | **DELETE** /cells/{name}/worksheets/{sheetName}/charts/{chartIndex} | Delete worksheet chart by index.
[**cells_charts_get_worksheet_chart**](CellsChartsApi.md#cells_charts_get_worksheet_chart) | **GET** /cells/{name}/worksheets/{sheetName}/charts/{chartNumber} | Get chart info.
[**cells_charts_get_worksheet_chart_legend**](CellsChartsApi.md#cells_charts_get_worksheet_chart_legend) | **GET** /cells/{name}/worksheets/{sheetName}/charts/{chartIndex}/legend | Get chart legend
[**cells_charts_get_worksheet_chart_title**](CellsChartsApi.md#cells_charts_get_worksheet_chart_title) | **GET** /cells/{name}/worksheets/{sheetName}/charts/{chartIndex}/title | Get chart title
[**cells_charts_get_worksheet_charts**](CellsChartsApi.md#cells_charts_get_worksheet_charts) | **GET** /cells/{name}/worksheets/{sheetName}/charts | Get worksheet charts info.
[**cells_charts_post_worksheet_chart**](CellsChartsApi.md#cells_charts_post_worksheet_chart) | **POST** /cells/{name}/worksheets/{sheetName}/charts/{chartIndex} | Update chart propreties
[**cells_charts_post_worksheet_chart_legend**](CellsChartsApi.md#cells_charts_post_worksheet_chart_legend) | **POST** /cells/{name}/worksheets/{sheetName}/charts/{chartIndex}/legend | Update chart legend
[**cells_charts_post_worksheet_chart_title**](CellsChartsApi.md#cells_charts_post_worksheet_chart_title) | **POST** /cells/{name}/worksheets/{sheetName}/charts/{chartIndex}/title | Update chart title
[**cells_charts_put_worksheet_add_chart**](CellsChartsApi.md#cells_charts_put_worksheet_add_chart) | **PUT** /cells/{name}/worksheets/{sheetName}/charts | Add new chart to worksheet.
[**cells_charts_put_worksheet_chart_legend**](CellsChartsApi.md#cells_charts_put_worksheet_chart_legend) | **PUT** /cells/{name}/worksheets/{sheetName}/charts/{chartIndex}/legend | Show legend in chart
[**cells_charts_put_worksheet_chart_title**](CellsChartsApi.md#cells_charts_put_worksheet_chart_title) | **PUT** /cells/{name}/worksheets/{sheetName}/charts/{chartIndex}/title | Add chart title / Set chart title visible


# **cells_charts_delete_worksheet_chart_legend**
> SaaSposeResponse cells_charts_delete_worksheet_chart_legend(name, sheet_name, chart_index, folder=folder)

Hide legend in chart

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsChartsApi()
name = 'name_example' # str | Workbook name.
sheet_name = 'sheet_name_example' # str | Worksheet name.
chart_index = 56 # int | The chart index.
folder = 'folder_example' # str | The workbook folder. (optional)

try: 
    # Hide legend in chart
    api_response = api_instance.cells_charts_delete_worksheet_chart_legend(name, sheet_name, chart_index, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsChartsApi->cells_charts_delete_worksheet_chart_legend: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Workbook name. | 
 **sheet_name** | **str**| Worksheet name. | 
 **chart_index** | **int**| The chart index. | 
 **folder** | **str**| The workbook folder. | [optional] 

### Return type

[**SaaSposeResponse**](SaaSposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_charts_delete_worksheet_chart_title**
> SaaSposeResponse cells_charts_delete_worksheet_chart_title(name, sheet_name, chart_index, folder=folder)

Hide title in chart

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsChartsApi()
name = 'name_example' # str | Workbook name.
sheet_name = 'sheet_name_example' # str | Worksheet name.
chart_index = 56 # int | The chart index.
folder = 'folder_example' # str | The workbook folder. (optional)

try: 
    # Hide title in chart
    api_response = api_instance.cells_charts_delete_worksheet_chart_title(name, sheet_name, chart_index, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsChartsApi->cells_charts_delete_worksheet_chart_title: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Workbook name. | 
 **sheet_name** | **str**| Worksheet name. | 
 **chart_index** | **int**| The chart index. | 
 **folder** | **str**| The workbook folder. | [optional] 

### Return type

[**SaaSposeResponse**](SaaSposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_charts_delete_worksheet_clear_charts**
> SaaSposeResponse cells_charts_delete_worksheet_clear_charts(name, sheet_name, folder=folder)

Clear the charts.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsChartsApi()
name = 'name_example' # str | Workbook name.
sheet_name = 'sheet_name_example' # str | The worksheet name.
folder = 'folder_example' # str | The workbook folder. (optional)

try: 
    # Clear the charts.
    api_response = api_instance.cells_charts_delete_worksheet_clear_charts(name, sheet_name, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsChartsApi->cells_charts_delete_worksheet_clear_charts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Workbook name. | 
 **sheet_name** | **str**| The worksheet name. | 
 **folder** | **str**| The workbook folder. | [optional] 

### Return type

[**SaaSposeResponse**](SaaSposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_charts_delete_worksheet_delete_chart**
> ChartsResponse cells_charts_delete_worksheet_delete_chart(name, sheet_name, chart_index, folder=folder)

Delete worksheet chart by index.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsChartsApi()
name = 'name_example' # str | Workbook name.
sheet_name = 'sheet_name_example' # str | Worksheet name.
chart_index = 56 # int | The chart index.
folder = 'folder_example' # str | The workbook folder. (optional)

try: 
    # Delete worksheet chart by index.
    api_response = api_instance.cells_charts_delete_worksheet_delete_chart(name, sheet_name, chart_index, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsChartsApi->cells_charts_delete_worksheet_delete_chart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Workbook name. | 
 **sheet_name** | **str**| Worksheet name. | 
 **chart_index** | **int**| The chart index. | 
 **folder** | **str**| The workbook folder. | [optional] 

### Return type

[**ChartsResponse**](ChartsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_charts_get_worksheet_chart**
> file cells_charts_get_worksheet_chart(name, sheet_name, chart_number, folder=folder)

Get chart info.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsChartsApi()
name = 'name_example' # str | Document name.
sheet_name = 'sheet_name_example' # str | Worksheet name.
chart_number = 56 # int | The chart number.
folder = 'folder_example' # str | The document folder. (optional)

try: 
    # Get chart info.
    api_response = api_instance.cells_charts_get_worksheet_chart(name, sheet_name, chart_number, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsChartsApi->cells_charts_get_worksheet_chart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document name. | 
 **sheet_name** | **str**| Worksheet name. | 
 **chart_number** | **int**| The chart number. | 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_charts_get_worksheet_chart_legend**
> LegendResponse cells_charts_get_worksheet_chart_legend(name, sheet_name, chart_index, folder=folder)

Get chart legend

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsChartsApi()
name = 'name_example' # str | Workbook name.
sheet_name = 'sheet_name_example' # str | Worksheet name.
chart_index = 56 # int | The chart index.
folder = 'folder_example' # str | The workbook folder. (optional)

try: 
    # Get chart legend
    api_response = api_instance.cells_charts_get_worksheet_chart_legend(name, sheet_name, chart_index, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsChartsApi->cells_charts_get_worksheet_chart_legend: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Workbook name. | 
 **sheet_name** | **str**| Worksheet name. | 
 **chart_index** | **int**| The chart index. | 
 **folder** | **str**| The workbook folder. | [optional] 

### Return type

[**LegendResponse**](LegendResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_charts_get_worksheet_chart_title**
> TitleResponse cells_charts_get_worksheet_chart_title(name, sheet_name, chart_index, folder=folder)

Get chart title

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsChartsApi()
name = 'name_example' # str | Workbook name.
sheet_name = 'sheet_name_example' # str | Worksheet name.
chart_index = 56 # int | The chart index.
folder = 'folder_example' # str | The workbook folder. (optional)

try: 
    # Get chart title
    api_response = api_instance.cells_charts_get_worksheet_chart_title(name, sheet_name, chart_index, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsChartsApi->cells_charts_get_worksheet_chart_title: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Workbook name. | 
 **sheet_name** | **str**| Worksheet name. | 
 **chart_index** | **int**| The chart index. | 
 **folder** | **str**| The workbook folder. | [optional] 

### Return type

[**TitleResponse**](TitleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_charts_get_worksheet_charts**
> ChartsResponse cells_charts_get_worksheet_charts(name, sheet_name, folder=folder)

Get worksheet charts info.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsChartsApi()
name = 'name_example' # str | Document name.
sheet_name = 'sheet_name_example' # str | The worksheet name.
folder = 'folder_example' # str | Document's folder. (optional)

try: 
    # Get worksheet charts info.
    api_response = api_instance.cells_charts_get_worksheet_charts(name, sheet_name, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsChartsApi->cells_charts_get_worksheet_charts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document name. | 
 **sheet_name** | **str**| The worksheet name. | 
 **folder** | **str**| Document&#39;s folder. | [optional] 

### Return type

[**ChartsResponse**](ChartsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_charts_post_worksheet_chart**
> SaaSposeResponse cells_charts_post_worksheet_chart(name, sheet_name, chart_index, chart=chart, folder=folder)

Update chart propreties

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsChartsApi()
name = 'name_example' # str | 
sheet_name = 'sheet_name_example' # str | 
chart_index = 56 # int | 
chart = asposecellscloud.Chart() # Chart |  (optional)
folder = 'folder_example' # str |  (optional)

try: 
    # Update chart propreties
    api_response = api_instance.cells_charts_post_worksheet_chart(name, sheet_name, chart_index, chart=chart, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsChartsApi->cells_charts_post_worksheet_chart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **sheet_name** | **str**|  | 
 **chart_index** | **int**|  | 
 **chart** | [**Chart**](Chart.md)|  | [optional] 
 **folder** | **str**|  | [optional] 

### Return type

[**SaaSposeResponse**](SaaSposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_charts_post_worksheet_chart_legend**
> LegendResponse cells_charts_post_worksheet_chart_legend(name, sheet_name, chart_index, legend=legend, folder=folder)

Update chart legend

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsChartsApi()
name = 'name_example' # str | Workbook name.
sheet_name = 'sheet_name_example' # str | Worksheet name.
chart_index = 56 # int | The chart index.
legend = asposecellscloud.Legend() # Legend |  (optional)
folder = 'folder_example' # str | The workbook folder. (optional)

try: 
    # Update chart legend
    api_response = api_instance.cells_charts_post_worksheet_chart_legend(name, sheet_name, chart_index, legend=legend, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsChartsApi->cells_charts_post_worksheet_chart_legend: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Workbook name. | 
 **sheet_name** | **str**| Worksheet name. | 
 **chart_index** | **int**| The chart index. | 
 **legend** | [**Legend**](Legend.md)|  | [optional] 
 **folder** | **str**| The workbook folder. | [optional] 

### Return type

[**LegendResponse**](LegendResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_charts_post_worksheet_chart_title**
> TitleResponse cells_charts_post_worksheet_chart_title(name, sheet_name, chart_index, title=title, folder=folder)

Update chart title

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsChartsApi()
name = 'name_example' # str | Workbook name.
sheet_name = 'sheet_name_example' # str | Worksheet name.
chart_index = 56 # int | The chart index.
title = asposecellscloud.Title() # Title | Chart title (optional)
folder = 'folder_example' # str | The workbook folder. (optional)

try: 
    # Update chart title
    api_response = api_instance.cells_charts_post_worksheet_chart_title(name, sheet_name, chart_index, title=title, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsChartsApi->cells_charts_post_worksheet_chart_title: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Workbook name. | 
 **sheet_name** | **str**| Worksheet name. | 
 **chart_index** | **int**| The chart index. | 
 **title** | [**Title**](Title.md)| Chart title | [optional] 
 **folder** | **str**| The workbook folder. | [optional] 

### Return type

[**TitleResponse**](TitleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_charts_put_worksheet_add_chart**
> ChartsResponse cells_charts_put_worksheet_add_chart(name, sheet_name, chart_type, upper_left_row=upper_left_row, upper_left_column=upper_left_column, lower_right_row=lower_right_row, lower_right_column=lower_right_column, area=area, is_vertical=is_vertical, category_data=category_data, is_auto_get_serial_name=is_auto_get_serial_name, title=title, folder=folder)

Add new chart to worksheet.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsChartsApi()
name = 'name_example' # str | Workbook name.
sheet_name = 'sheet_name_example' # str | The worksheet name.
chart_type = 'chart_type_example' # str | Chart type, please refer property Type in chart resource.
upper_left_row = 0 # int | New chart upper left row. (optional) (default to 0)
upper_left_column = 0 # int | New chart upperleft column. (optional) (default to 0)
lower_right_row = 0 # int | New chart lower right row. (optional) (default to 0)
lower_right_column = 0 # int | New chart lower right column. (optional) (default to 0)
area = 'area_example' # str | Specifies values from which to plot the data series.  (optional)
is_vertical = true # bool | Specifies whether to plot the series from a range of cell values by row or by column.  (optional) (default to true)
category_data = 'category_data_example' # str | Gets or sets the range of category Axis values. It can be a range of cells (such as, \"d1:e10\").  (optional)
is_auto_get_serial_name = true # bool | Specifies whether auto update serial name.  (optional) (default to true)
title = 'title_example' # str | Specifies chart title name. (optional)
folder = 'folder_example' # str | The workbook folder. (optional)

try: 
    # Add new chart to worksheet.
    api_response = api_instance.cells_charts_put_worksheet_add_chart(name, sheet_name, chart_type, upper_left_row=upper_left_row, upper_left_column=upper_left_column, lower_right_row=lower_right_row, lower_right_column=lower_right_column, area=area, is_vertical=is_vertical, category_data=category_data, is_auto_get_serial_name=is_auto_get_serial_name, title=title, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsChartsApi->cells_charts_put_worksheet_add_chart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Workbook name. | 
 **sheet_name** | **str**| The worksheet name. | 
 **chart_type** | **str**| Chart type, please refer property Type in chart resource. | 
 **upper_left_row** | **int**| New chart upper left row. | [optional] [default to 0]
 **upper_left_column** | **int**| New chart upperleft column. | [optional] [default to 0]
 **lower_right_row** | **int**| New chart lower right row. | [optional] [default to 0]
 **lower_right_column** | **int**| New chart lower right column. | [optional] [default to 0]
 **area** | **str**| Specifies values from which to plot the data series.  | [optional] 
 **is_vertical** | **bool**| Specifies whether to plot the series from a range of cell values by row or by column.  | [optional] [default to true]
 **category_data** | **str**| Gets or sets the range of category Axis values. It can be a range of cells (such as, \&quot;d1:e10\&quot;).  | [optional] 
 **is_auto_get_serial_name** | **bool**| Specifies whether auto update serial name.  | [optional] [default to true]
 **title** | **str**| Specifies chart title name. | [optional] 
 **folder** | **str**| The workbook folder. | [optional] 

### Return type

[**ChartsResponse**](ChartsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_charts_put_worksheet_chart_legend**
> SaaSposeResponse cells_charts_put_worksheet_chart_legend(name, sheet_name, chart_index, folder=folder)

Show legend in chart

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsChartsApi()
name = 'name_example' # str | Workbook name.
sheet_name = 'sheet_name_example' # str | Worksheet name.
chart_index = 56 # int | The chart index.
folder = 'folder_example' # str | The workbook folder. (optional)

try: 
    # Show legend in chart
    api_response = api_instance.cells_charts_put_worksheet_chart_legend(name, sheet_name, chart_index, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsChartsApi->cells_charts_put_worksheet_chart_legend: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Workbook name. | 
 **sheet_name** | **str**| Worksheet name. | 
 **chart_index** | **int**| The chart index. | 
 **folder** | **str**| The workbook folder. | [optional] 

### Return type

[**SaaSposeResponse**](SaaSposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_charts_put_worksheet_chart_title**
> TitleResponse cells_charts_put_worksheet_chart_title(name, sheet_name, chart_index, title=title, folder=folder)

Add chart title / Set chart title visible

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsChartsApi()
name = 'name_example' # str | Workbook name.
sheet_name = 'sheet_name_example' # str | Worksheet name.
chart_index = 56 # int | The chart index.
title = asposecellscloud.Title() # Title | Chart title. (optional)
folder = 'folder_example' # str | The workbook folder. (optional)

try: 
    # Add chart title / Set chart title visible
    api_response = api_instance.cells_charts_put_worksheet_chart_title(name, sheet_name, chart_index, title=title, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsChartsApi->cells_charts_put_worksheet_chart_title: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Workbook name. | 
 **sheet_name** | **str**| Worksheet name. | 
 **chart_index** | **int**| The chart index. | 
 **title** | [**Title**](Title.md)| Chart title. | [optional] 
 **folder** | **str**| The workbook folder. | [optional] 

### Return type

[**TitleResponse**](TitleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

