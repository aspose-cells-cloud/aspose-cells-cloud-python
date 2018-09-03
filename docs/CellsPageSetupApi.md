# asposecellscloud.CellsPageSetupApi

All URIs are relative to *https://api.aspose.cloud/v1.1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cells_page_setup_delete_header_footer**](CellsPageSetupApi.md#cells_page_setup_delete_header_footer) | **DELETE** /cells/{name}/worksheets/{sheetName}/pagesetup/clearheaderfooter | clear header footer
[**cells_page_setup_get_footer**](CellsPageSetupApi.md#cells_page_setup_get_footer) | **GET** /cells/{name}/worksheets/{sheetName}/pagesetup/footer | get page footer information
[**cells_page_setup_get_header**](CellsPageSetupApi.md#cells_page_setup_get_header) | **GET** /cells/{name}/worksheets/{sheetName}/pagesetup/header | get page header information
[**cells_page_setup_get_page_setup**](CellsPageSetupApi.md#cells_page_setup_get_page_setup) | **GET** /cells/{name}/worksheets/{sheetName}/pagesetup | Get Page Setup information.             
[**cells_page_setup_post_footer**](CellsPageSetupApi.md#cells_page_setup_post_footer) | **POST** /cells/{name}/worksheets/{sheetName}/pagesetup/footer | update  page footer information 
[**cells_page_setup_post_header**](CellsPageSetupApi.md#cells_page_setup_post_header) | **POST** /cells/{name}/worksheets/{sheetName}/pagesetup/header | update  page header information 
[**cells_page_setup_post_page_setup**](CellsPageSetupApi.md#cells_page_setup_post_page_setup) | **POST** /cells/{name}/worksheets/{sheetName}/pagesetup | Update Page Setup information.


# **cells_page_setup_delete_header_footer**
> SaaSposeResponse cells_page_setup_delete_header_footer(name, sheet_name, folder=folder, storage=storage)

clear header footer

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsPageSetupApi()
name = 'name_example' # str | 
sheet_name = 'sheet_name_example' # str | 
folder = 'folder_example' # str |  (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # clear header footer
    api_response = api_instance.cells_page_setup_delete_header_footer(name, sheet_name, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsPageSetupApi->cells_page_setup_delete_header_footer: %s\n" % e)
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

# **cells_page_setup_get_footer**
> PageSectionsResponse cells_page_setup_get_footer(name, sheet_name, folder=folder, storage=storage)

get page footer information

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsPageSetupApi()
name = 'name_example' # str | 
sheet_name = 'sheet_name_example' # str | 
folder = 'folder_example' # str |  (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # get page footer information
    api_response = api_instance.cells_page_setup_get_footer(name, sheet_name, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsPageSetupApi->cells_page_setup_get_footer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **sheet_name** | **str**|  | 
 **folder** | **str**|  | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**PageSectionsResponse**](PageSectionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_page_setup_get_header**
> PageSectionsResponse cells_page_setup_get_header(name, sheet_name, folder=folder, storage=storage)

get page header information

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsPageSetupApi()
name = 'name_example' # str | 
sheet_name = 'sheet_name_example' # str | 
folder = 'folder_example' # str |  (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # get page header information
    api_response = api_instance.cells_page_setup_get_header(name, sheet_name, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsPageSetupApi->cells_page_setup_get_header: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **sheet_name** | **str**|  | 
 **folder** | **str**|  | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**PageSectionsResponse**](PageSectionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_page_setup_get_page_setup**
> PageSetupResponse cells_page_setup_get_page_setup(name, sheet_name, folder=folder, storage=storage)

Get Page Setup information.             

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsPageSetupApi()
name = 'name_example' # str | 
sheet_name = 'sheet_name_example' # str | 
folder = 'folder_example' # str |  (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Get Page Setup information.             
    api_response = api_instance.cells_page_setup_get_page_setup(name, sheet_name, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsPageSetupApi->cells_page_setup_get_page_setup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **sheet_name** | **str**|  | 
 **folder** | **str**|  | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**PageSetupResponse**](PageSetupResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_page_setup_post_footer**
> SaaSposeResponse cells_page_setup_post_footer(name, sheet_name, section, script, is_first_page, folder=folder, storage=storage)

update  page footer information 

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsPageSetupApi()
name = 'name_example' # str | 
sheet_name = 'sheet_name_example' # str | 
section = 56 # int | 
script = 'script_example' # str | 
is_first_page = true # bool | 
folder = 'folder_example' # str |  (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # update  page footer information 
    api_response = api_instance.cells_page_setup_post_footer(name, sheet_name, section, script, is_first_page, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsPageSetupApi->cells_page_setup_post_footer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **sheet_name** | **str**|  | 
 **section** | **int**|  | 
 **script** | **str**|  | 
 **is_first_page** | **bool**|  | 
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

# **cells_page_setup_post_header**
> SaaSposeResponse cells_page_setup_post_header(name, sheet_name, section, script, is_first_page, folder=folder, storage=storage)

update  page header information 

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsPageSetupApi()
name = 'name_example' # str | 
sheet_name = 'sheet_name_example' # str | 
section = 56 # int | 
script = 'script_example' # str | 
is_first_page = true # bool | 
folder = 'folder_example' # str |  (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # update  page header information 
    api_response = api_instance.cells_page_setup_post_header(name, sheet_name, section, script, is_first_page, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsPageSetupApi->cells_page_setup_post_header: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **sheet_name** | **str**|  | 
 **section** | **int**|  | 
 **script** | **str**|  | 
 **is_first_page** | **bool**|  | 
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

# **cells_page_setup_post_page_setup**
> SaaSposeResponse cells_page_setup_post_page_setup(name, sheet_name, page_setup=page_setup, folder=folder, storage=storage)

Update Page Setup information.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsPageSetupApi()
name = 'name_example' # str | 
sheet_name = 'sheet_name_example' # str | 
page_setup = asposecellscloud.PageSetup() # PageSetup |  (optional)
folder = 'folder_example' # str |  (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Update Page Setup information.
    api_response = api_instance.cells_page_setup_post_page_setup(name, sheet_name, page_setup=page_setup, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsPageSetupApi->cells_page_setup_post_page_setup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **sheet_name** | **str**|  | 
 **page_setup** | [**PageSetup**](PageSetup.md)|  | [optional] 
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

