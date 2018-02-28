# asposecellscloud.CellsAutoFilterApi

All URIs are relative to *https://api.aspose.cloud/v1.1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cells_auto_filter_delete_worksheet_date_filter**](CellsAutoFilterApi.md#cells_auto_filter_delete_worksheet_date_filter) | **DELETE** /cells/{name}/worksheets/{sheetName}/autoFilter/dateFilter | Removes a date filter.             
[**cells_auto_filter_delete_worksheet_filter**](CellsAutoFilterApi.md#cells_auto_filter_delete_worksheet_filter) | **DELETE** /cells/{name}/worksheets/{sheetName}/autoFilter/filter | Delete a filter for a filter column.             
[**cells_auto_filter_get_worksheet_auto_filter**](CellsAutoFilterApi.md#cells_auto_filter_get_worksheet_auto_filter) | **GET** /cells/{name}/worksheets/{sheetName}/autoFilter | Get Auto filter Description
[**cells_auto_filter_post_worksheet_auto_filter_refresh**](CellsAutoFilterApi.md#cells_auto_filter_post_worksheet_auto_filter_refresh) | **POST** /cells/{name}/worksheets/{sheetName}/autoFilter/refresh | 
[**cells_auto_filter_post_worksheet_match_blanks**](CellsAutoFilterApi.md#cells_auto_filter_post_worksheet_match_blanks) | **POST** /cells/{name}/worksheets/{sheetName}/autoFilter/matchBlanks | Match all blank cell in the list.
[**cells_auto_filter_post_worksheet_match_non_blanks**](CellsAutoFilterApi.md#cells_auto_filter_post_worksheet_match_non_blanks) | **POST** /cells/{name}/worksheets/{sheetName}/autoFilter/matchNonBlanks | Match all not blank cell in the list.             
[**cells_auto_filter_put_worksheet_color_filter**](CellsAutoFilterApi.md#cells_auto_filter_put_worksheet_color_filter) | **PUT** /cells/{name}/worksheets/{sheetName}/autoFilter/colorFilter | 
[**cells_auto_filter_put_worksheet_custom_filter**](CellsAutoFilterApi.md#cells_auto_filter_put_worksheet_custom_filter) | **PUT** /cells/{name}/worksheets/{sheetName}/autoFilter/custom | Filters a list with a custom criteria.             
[**cells_auto_filter_put_worksheet_date_filter**](CellsAutoFilterApi.md#cells_auto_filter_put_worksheet_date_filter) | **PUT** /cells/{name}/worksheets/{sheetName}/autoFilter/dateFilter | add date filter in worksheet 
[**cells_auto_filter_put_worksheet_dynamic_filter**](CellsAutoFilterApi.md#cells_auto_filter_put_worksheet_dynamic_filter) | **PUT** /cells/{name}/worksheets/{sheetName}/autoFilter/dynamicFilter | 
[**cells_auto_filter_put_worksheet_filter**](CellsAutoFilterApi.md#cells_auto_filter_put_worksheet_filter) | **PUT** /cells/{name}/worksheets/{sheetName}/autoFilter/filter | Adds a filter for a filter column.             
[**cells_auto_filter_put_worksheet_filter_top10**](CellsAutoFilterApi.md#cells_auto_filter_put_worksheet_filter_top10) | **PUT** /cells/{name}/worksheets/{sheetName}/autoFilter/filterTop10 | Filter the top 10 item in the list
[**cells_auto_filter_put_worksheet_icon_filter**](CellsAutoFilterApi.md#cells_auto_filter_put_worksheet_icon_filter) | **PUT** /cells/{name}/worksheets/{sheetName}/autoFilter/iconFilter | Adds an icon filter.


# **cells_auto_filter_delete_worksheet_date_filter**
> SaaSposeResponse cells_auto_filter_delete_worksheet_date_filter(name, sheet_name, field_index, date_time_grouping_type, year=year, month=month, day=day, hour=hour, minute=minute, second=second, folder=folder)

Removes a date filter.             

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsAutoFilterApi()
name = 'name_example' # str | 
sheet_name = 'sheet_name_example' # str | 
field_index = 56 # int | 
date_time_grouping_type = 'date_time_grouping_type_example' # str | 
year = 0 # int |  (optional) (default to 0)
month = 0 # int |  (optional) (default to 0)
day = 0 # int |  (optional) (default to 0)
hour = 0 # int |  (optional) (default to 0)
minute = 0 # int |  (optional) (default to 0)
second = 0 # int |  (optional) (default to 0)
folder = 'folder_example' # str |  (optional)

try: 
    # Removes a date filter.             
    api_response = api_instance.cells_auto_filter_delete_worksheet_date_filter(name, sheet_name, field_index, date_time_grouping_type, year=year, month=month, day=day, hour=hour, minute=minute, second=second, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsAutoFilterApi->cells_auto_filter_delete_worksheet_date_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **sheet_name** | **str**|  | 
 **field_index** | **int**|  | 
 **date_time_grouping_type** | **str**|  | 
 **year** | **int**|  | [optional] [default to 0]
 **month** | **int**|  | [optional] [default to 0]
 **day** | **int**|  | [optional] [default to 0]
 **hour** | **int**|  | [optional] [default to 0]
 **minute** | **int**|  | [optional] [default to 0]
 **second** | **int**|  | [optional] [default to 0]
 **folder** | **str**|  | [optional] 

### Return type

[**SaaSposeResponse**](SaaSposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_auto_filter_delete_worksheet_filter**
> SaaSposeResponse cells_auto_filter_delete_worksheet_filter(name, sheet_name, field_index, criteria=criteria, folder=folder)

Delete a filter for a filter column.             

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsAutoFilterApi()
name = 'name_example' # str | 
sheet_name = 'sheet_name_example' # str | 
field_index = 56 # int | 
criteria = 'criteria_example' # str |  (optional)
folder = 'folder_example' # str |  (optional)

try: 
    # Delete a filter for a filter column.             
    api_response = api_instance.cells_auto_filter_delete_worksheet_filter(name, sheet_name, field_index, criteria=criteria, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsAutoFilterApi->cells_auto_filter_delete_worksheet_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **sheet_name** | **str**|  | 
 **field_index** | **int**|  | 
 **criteria** | **str**|  | [optional] 
 **folder** | **str**|  | [optional] 

### Return type

[**SaaSposeResponse**](SaaSposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_auto_filter_get_worksheet_auto_filter**
> AutoFilterResponse cells_auto_filter_get_worksheet_auto_filter(name, sheet_name, folder=folder)

Get Auto filter Description

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsAutoFilterApi()
name = 'name_example' # str | 
sheet_name = 'sheet_name_example' # str | 
folder = 'folder_example' # str |  (optional)

try: 
    # Get Auto filter Description
    api_response = api_instance.cells_auto_filter_get_worksheet_auto_filter(name, sheet_name, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsAutoFilterApi->cells_auto_filter_get_worksheet_auto_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **sheet_name** | **str**|  | 
 **folder** | **str**|  | [optional] 

### Return type

[**AutoFilterResponse**](AutoFilterResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_auto_filter_post_worksheet_auto_filter_refresh**
> SaaSposeResponse cells_auto_filter_post_worksheet_auto_filter_refresh(name, sheet_name, folder=folder)



### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsAutoFilterApi()
name = 'name_example' # str | 
sheet_name = 'sheet_name_example' # str | 
folder = 'folder_example' # str |  (optional)

try: 
    api_response = api_instance.cells_auto_filter_post_worksheet_auto_filter_refresh(name, sheet_name, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsAutoFilterApi->cells_auto_filter_post_worksheet_auto_filter_refresh: %s\n" % e)
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

# **cells_auto_filter_post_worksheet_match_blanks**
> SaaSposeResponse cells_auto_filter_post_worksheet_match_blanks(name, sheet_name, field_index, folder=folder)

Match all blank cell in the list.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsAutoFilterApi()
name = 'name_example' # str | 
sheet_name = 'sheet_name_example' # str | 
field_index = 56 # int | 
folder = 'folder_example' # str |  (optional)

try: 
    # Match all blank cell in the list.
    api_response = api_instance.cells_auto_filter_post_worksheet_match_blanks(name, sheet_name, field_index, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsAutoFilterApi->cells_auto_filter_post_worksheet_match_blanks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **sheet_name** | **str**|  | 
 **field_index** | **int**|  | 
 **folder** | **str**|  | [optional] 

### Return type

[**SaaSposeResponse**](SaaSposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_auto_filter_post_worksheet_match_non_blanks**
> SaaSposeResponse cells_auto_filter_post_worksheet_match_non_blanks(name, sheet_name, field_index, folder=folder)

Match all not blank cell in the list.             

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsAutoFilterApi()
name = 'name_example' # str | 
sheet_name = 'sheet_name_example' # str | 
field_index = 56 # int | 
folder = 'folder_example' # str |  (optional)

try: 
    # Match all not blank cell in the list.             
    api_response = api_instance.cells_auto_filter_post_worksheet_match_non_blanks(name, sheet_name, field_index, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsAutoFilterApi->cells_auto_filter_post_worksheet_match_non_blanks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **sheet_name** | **str**|  | 
 **field_index** | **int**|  | 
 **folder** | **str**|  | [optional] 

### Return type

[**SaaSposeResponse**](SaaSposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_auto_filter_put_worksheet_color_filter**
> SaaSposeResponse cells_auto_filter_put_worksheet_color_filter(name, sheet_name, range, field_index, color_filter=color_filter, match_blanks=match_blanks, refresh=refresh, folder=folder)



### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsAutoFilterApi()
name = 'name_example' # str | 
sheet_name = 'sheet_name_example' # str | 
range = 'range_example' # str | 
field_index = 56 # int | 
color_filter = asposecellscloud.ColorFilterRequest() # ColorFilterRequest |  (optional)
match_blanks = true # bool |  (optional)
refresh = true # bool |  (optional)
folder = 'folder_example' # str |  (optional)

try: 
    api_response = api_instance.cells_auto_filter_put_worksheet_color_filter(name, sheet_name, range, field_index, color_filter=color_filter, match_blanks=match_blanks, refresh=refresh, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsAutoFilterApi->cells_auto_filter_put_worksheet_color_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **sheet_name** | **str**|  | 
 **range** | **str**|  | 
 **field_index** | **int**|  | 
 **color_filter** | [**ColorFilterRequest**](ColorFilterRequest.md)|  | [optional] 
 **match_blanks** | **bool**|  | [optional] 
 **refresh** | **bool**|  | [optional] 
 **folder** | **str**|  | [optional] 

### Return type

[**SaaSposeResponse**](SaaSposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_auto_filter_put_worksheet_custom_filter**
> SaaSposeResponse cells_auto_filter_put_worksheet_custom_filter(name, sheet_name, range, field_index, operator_type1, criteria1, is_and=is_and, operator_type2=operator_type2, criteria2=criteria2, match_blanks=match_blanks, refresh=refresh, folder=folder)

Filters a list with a custom criteria.             

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsAutoFilterApi()
name = 'name_example' # str | 
sheet_name = 'sheet_name_example' # str | 
range = 'range_example' # str | 
field_index = 56 # int | 
operator_type1 = 'operator_type1_example' # str | 
criteria1 = 'criteria1_example' # str | 
is_and = true # bool |  (optional)
operator_type2 = 'operator_type2_example' # str |  (optional)
criteria2 = 'criteria2_example' # str |  (optional)
match_blanks = true # bool |  (optional)
refresh = true # bool |  (optional)
folder = 'folder_example' # str |  (optional)

try: 
    # Filters a list with a custom criteria.             
    api_response = api_instance.cells_auto_filter_put_worksheet_custom_filter(name, sheet_name, range, field_index, operator_type1, criteria1, is_and=is_and, operator_type2=operator_type2, criteria2=criteria2, match_blanks=match_blanks, refresh=refresh, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsAutoFilterApi->cells_auto_filter_put_worksheet_custom_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **sheet_name** | **str**|  | 
 **range** | **str**|  | 
 **field_index** | **int**|  | 
 **operator_type1** | **str**|  | 
 **criteria1** | **str**|  | 
 **is_and** | **bool**|  | [optional] 
 **operator_type2** | **str**|  | [optional] 
 **criteria2** | **str**|  | [optional] 
 **match_blanks** | **bool**|  | [optional] 
 **refresh** | **bool**|  | [optional] 
 **folder** | **str**|  | [optional] 

### Return type

[**SaaSposeResponse**](SaaSposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_auto_filter_put_worksheet_date_filter**
> SaaSposeResponse cells_auto_filter_put_worksheet_date_filter(name, sheet_name, range, field_index, date_time_grouping_type, year=year, month=month, day=day, hour=hour, minute=minute, second=second, match_blanks=match_blanks, refresh=refresh, folder=folder)

add date filter in worksheet 

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsAutoFilterApi()
name = 'name_example' # str | 
sheet_name = 'sheet_name_example' # str | 
range = 'range_example' # str | 
field_index = 56 # int | 
date_time_grouping_type = 'date_time_grouping_type_example' # str | 
year = 0 # int |  (optional) (default to 0)
month = 0 # int |  (optional) (default to 0)
day = 0 # int |  (optional) (default to 0)
hour = 0 # int |  (optional) (default to 0)
minute = 0 # int |  (optional) (default to 0)
second = 0 # int |  (optional) (default to 0)
match_blanks = true # bool |  (optional)
refresh = true # bool |  (optional)
folder = 'folder_example' # str |  (optional)

try: 
    # add date filter in worksheet 
    api_response = api_instance.cells_auto_filter_put_worksheet_date_filter(name, sheet_name, range, field_index, date_time_grouping_type, year=year, month=month, day=day, hour=hour, minute=minute, second=second, match_blanks=match_blanks, refresh=refresh, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsAutoFilterApi->cells_auto_filter_put_worksheet_date_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **sheet_name** | **str**|  | 
 **range** | **str**|  | 
 **field_index** | **int**|  | 
 **date_time_grouping_type** | **str**|  | 
 **year** | **int**|  | [optional] [default to 0]
 **month** | **int**|  | [optional] [default to 0]
 **day** | **int**|  | [optional] [default to 0]
 **hour** | **int**|  | [optional] [default to 0]
 **minute** | **int**|  | [optional] [default to 0]
 **second** | **int**|  | [optional] [default to 0]
 **match_blanks** | **bool**|  | [optional] 
 **refresh** | **bool**|  | [optional] 
 **folder** | **str**|  | [optional] 

### Return type

[**SaaSposeResponse**](SaaSposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_auto_filter_put_worksheet_dynamic_filter**
> SaaSposeResponse cells_auto_filter_put_worksheet_dynamic_filter(name, sheet_name, range, field_index, dynamic_filter_type, match_blanks=match_blanks, refresh=refresh, folder=folder)



### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsAutoFilterApi()
name = 'name_example' # str | 
sheet_name = 'sheet_name_example' # str | 
range = 'range_example' # str | 
field_index = 56 # int | 
dynamic_filter_type = 'dynamic_filter_type_example' # str | 
match_blanks = true # bool |  (optional)
refresh = true # bool |  (optional)
folder = 'folder_example' # str |  (optional)

try: 
    api_response = api_instance.cells_auto_filter_put_worksheet_dynamic_filter(name, sheet_name, range, field_index, dynamic_filter_type, match_blanks=match_blanks, refresh=refresh, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsAutoFilterApi->cells_auto_filter_put_worksheet_dynamic_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **sheet_name** | **str**|  | 
 **range** | **str**|  | 
 **field_index** | **int**|  | 
 **dynamic_filter_type** | **str**|  | 
 **match_blanks** | **bool**|  | [optional] 
 **refresh** | **bool**|  | [optional] 
 **folder** | **str**|  | [optional] 

### Return type

[**SaaSposeResponse**](SaaSposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_auto_filter_put_worksheet_filter**
> SaaSposeResponse cells_auto_filter_put_worksheet_filter(name, sheet_name, range, field_index, criteria, match_blanks=match_blanks, refresh=refresh, folder=folder)

Adds a filter for a filter column.             

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsAutoFilterApi()
name = 'name_example' # str | 
sheet_name = 'sheet_name_example' # str | 
range = 'range_example' # str | 
field_index = 56 # int | 
criteria = 'criteria_example' # str | 
match_blanks = true # bool |  (optional)
refresh = true # bool |  (optional)
folder = 'folder_example' # str |  (optional)

try: 
    # Adds a filter for a filter column.             
    api_response = api_instance.cells_auto_filter_put_worksheet_filter(name, sheet_name, range, field_index, criteria, match_blanks=match_blanks, refresh=refresh, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsAutoFilterApi->cells_auto_filter_put_worksheet_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **sheet_name** | **str**|  | 
 **range** | **str**|  | 
 **field_index** | **int**|  | 
 **criteria** | **str**|  | 
 **match_blanks** | **bool**|  | [optional] 
 **refresh** | **bool**|  | [optional] 
 **folder** | **str**|  | [optional] 

### Return type

[**SaaSposeResponse**](SaaSposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_auto_filter_put_worksheet_filter_top10**
> SaaSposeResponse cells_auto_filter_put_worksheet_filter_top10(name, sheet_name, range, field_index, is_top, is_percent, item_count, match_blanks=match_blanks, refresh=refresh, folder=folder)

Filter the top 10 item in the list

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsAutoFilterApi()
name = 'name_example' # str | 
sheet_name = 'sheet_name_example' # str | 
range = 'range_example' # str | 
field_index = 56 # int | 
is_top = true # bool | 
is_percent = true # bool | 
item_count = 56 # int | 
match_blanks = true # bool |  (optional)
refresh = true # bool |  (optional)
folder = 'folder_example' # str |  (optional)

try: 
    # Filter the top 10 item in the list
    api_response = api_instance.cells_auto_filter_put_worksheet_filter_top10(name, sheet_name, range, field_index, is_top, is_percent, item_count, match_blanks=match_blanks, refresh=refresh, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsAutoFilterApi->cells_auto_filter_put_worksheet_filter_top10: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **sheet_name** | **str**|  | 
 **range** | **str**|  | 
 **field_index** | **int**|  | 
 **is_top** | **bool**|  | 
 **is_percent** | **bool**|  | 
 **item_count** | **int**|  | 
 **match_blanks** | **bool**|  | [optional] 
 **refresh** | **bool**|  | [optional] 
 **folder** | **str**|  | [optional] 

### Return type

[**SaaSposeResponse**](SaaSposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_auto_filter_put_worksheet_icon_filter**
> SaaSposeResponse cells_auto_filter_put_worksheet_icon_filter(name, sheet_name, range, field_index, icon_set_type, icon_id, match_blanks=match_blanks, refresh=refresh, folder=folder)

Adds an icon filter.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsAutoFilterApi()
name = 'name_example' # str | 
sheet_name = 'sheet_name_example' # str | 
range = 'range_example' # str | 
field_index = 56 # int | 
icon_set_type = 'icon_set_type_example' # str | 
icon_id = 56 # int | 
match_blanks = true # bool |  (optional)
refresh = true # bool |  (optional)
folder = 'folder_example' # str |  (optional)

try: 
    # Adds an icon filter.
    api_response = api_instance.cells_auto_filter_put_worksheet_icon_filter(name, sheet_name, range, field_index, icon_set_type, icon_id, match_blanks=match_blanks, refresh=refresh, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsAutoFilterApi->cells_auto_filter_put_worksheet_icon_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **sheet_name** | **str**|  | 
 **range** | **str**|  | 
 **field_index** | **int**|  | 
 **icon_set_type** | **str**|  | 
 **icon_id** | **int**|  | 
 **match_blanks** | **bool**|  | [optional] 
 **refresh** | **bool**|  | [optional] 
 **folder** | **str**|  | [optional] 

### Return type

[**SaaSposeResponse**](SaaSposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

