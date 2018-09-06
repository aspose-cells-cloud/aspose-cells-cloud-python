# asposecellscloud.CellsWorkbookApi

All URIs are relative to *https://api.aspose.cloud/v1.1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cells_workbook_delete_decrypt_document**](CellsWorkbookApi.md#cells_workbook_delete_decrypt_document) | **DELETE** /cells/{name}/encryption | Decrypt document.
[**cells_workbook_delete_document_unprotect_from_changes**](CellsWorkbookApi.md#cells_workbook_delete_document_unprotect_from_changes) | **DELETE** /cells/{name}/writeProtection | Unprotect document from changes.
[**cells_workbook_delete_unprotect_document**](CellsWorkbookApi.md#cells_workbook_delete_unprotect_document) | **DELETE** /cells/{name}/protection | Unprotect document.
[**cells_workbook_delete_workbook_name**](CellsWorkbookApi.md#cells_workbook_delete_workbook_name) | **DELETE** /cells/{name}/names/{nameName} | Clean workbook&#39;s names.
[**cells_workbook_delete_workbook_names**](CellsWorkbookApi.md#cells_workbook_delete_workbook_names) | **DELETE** /cells/{name}/names | Clean workbook&#39;s names.
[**cells_workbook_get_workbook**](CellsWorkbookApi.md#cells_workbook_get_workbook) | **GET** /cells/{name} | Read workbook info or export.
[**cells_workbook_get_workbook_default_style**](CellsWorkbookApi.md#cells_workbook_get_workbook_default_style) | **GET** /cells/{name}/defaultstyle | Read workbook default style info.
[**cells_workbook_get_workbook_name**](CellsWorkbookApi.md#cells_workbook_get_workbook_name) | **GET** /cells/{name}/names/{nameName} | Read workbook&#39;s name.
[**cells_workbook_get_workbook_name_value**](CellsWorkbookApi.md#cells_workbook_get_workbook_name_value) | **GET** /cells/{name}/names/{nameName}/value | Get workbook&#39;s name value.
[**cells_workbook_get_workbook_names**](CellsWorkbookApi.md#cells_workbook_get_workbook_names) | **GET** /cells/{name}/names | Read workbook&#39;s names.
[**cells_workbook_get_workbook_settings**](CellsWorkbookApi.md#cells_workbook_get_workbook_settings) | **GET** /cells/{name}/settings | Get Workbook Settings DTO
[**cells_workbook_get_workbook_text_items**](CellsWorkbookApi.md#cells_workbook_get_workbook_text_items) | **GET** /cells/{name}/textItems | Read workbook&#39;s text items.
[**cells_workbook_post_autofit_workbook_rows**](CellsWorkbookApi.md#cells_workbook_post_autofit_workbook_rows) | **POST** /cells/{name}/autofitrows | Autofit workbook rows.
[**cells_workbook_post_encrypt_document**](CellsWorkbookApi.md#cells_workbook_post_encrypt_document) | **POST** /cells/{name}/encryption | Encript document.
[**cells_workbook_post_import_data**](CellsWorkbookApi.md#cells_workbook_post_import_data) | **POST** /cells/{name}/importdata | 
[**cells_workbook_post_protect_document**](CellsWorkbookApi.md#cells_workbook_post_protect_document) | **POST** /cells/{name}/protection | Protect document.
[**cells_workbook_post_workbook_calculate_formula**](CellsWorkbookApi.md#cells_workbook_post_workbook_calculate_formula) | **POST** /cells/{name}/calculateformula | Calculate all formulas in workbook.
[**cells_workbook_post_workbook_get_smart_marker_result**](CellsWorkbookApi.md#cells_workbook_post_workbook_get_smart_marker_result) | **POST** /cells/{name}/smartmarker | Smart marker processing result.
[**cells_workbook_post_workbook_settings**](CellsWorkbookApi.md#cells_workbook_post_workbook_settings) | **POST** /cells/{name}/settings | Update Workbook setting 
[**cells_workbook_post_workbook_split**](CellsWorkbookApi.md#cells_workbook_post_workbook_split) | **POST** /cells/{name}/split | Split workbook.
[**cells_workbook_post_workbooks_merge**](CellsWorkbookApi.md#cells_workbook_post_workbooks_merge) | **POST** /cells/{name}/merge | Merge workbooks.
[**cells_workbook_post_workbooks_text_replace**](CellsWorkbookApi.md#cells_workbook_post_workbooks_text_replace) | **POST** /cells/{name}/replaceText | Replace text.
[**cells_workbook_post_workbooks_text_search**](CellsWorkbookApi.md#cells_workbook_post_workbooks_text_search) | **POST** /cells/{name}/findText | Search text.
[**cells_workbook_put_convert_workbook**](CellsWorkbookApi.md#cells_workbook_put_convert_workbook) | **PUT** /cells/convert | Convert workbook from request content to some format.
[**cells_workbook_put_document_protect_from_changes**](CellsWorkbookApi.md#cells_workbook_put_document_protect_from_changes) | **PUT** /cells/{name}/writeProtection | Protect document from changes.
[**cells_workbook_put_workbook_create**](CellsWorkbookApi.md#cells_workbook_put_workbook_create) | **PUT** /cells/{name} | Create new workbook using deferent methods.


# **cells_workbook_delete_decrypt_document**
> SaaSposeResponse cells_workbook_delete_decrypt_document(name, encryption=encryption, folder=folder, storage=storage)

Decrypt document.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsWorkbookApi()
name = 'name_example' # str | The document name.
encryption = asposecellscloud.WorkbookEncryptionRequest() # WorkbookEncryptionRequest | Encryption settings, only password can be specified. (optional)
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Decrypt document.
    api_response = api_instance.cells_workbook_delete_decrypt_document(name, encryption=encryption, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsWorkbookApi->cells_workbook_delete_decrypt_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **encryption** | [**WorkbookEncryptionRequest**](WorkbookEncryptionRequest.md)| Encryption settings, only password can be specified. | [optional] 
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

# **cells_workbook_delete_document_unprotect_from_changes**
> SaaSposeResponse cells_workbook_delete_document_unprotect_from_changes(name, folder=folder, storage=storage)

Unprotect document from changes.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsWorkbookApi()
name = 'name_example' # str | The document name.
folder = 'folder_example' # str | Document's folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Unprotect document from changes.
    api_response = api_instance.cells_workbook_delete_document_unprotect_from_changes(name, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsWorkbookApi->cells_workbook_delete_document_unprotect_from_changes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
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

# **cells_workbook_delete_unprotect_document**
> SaaSposeResponse cells_workbook_delete_unprotect_document(name, protection=protection, folder=folder, storage=storage)

Unprotect document.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsWorkbookApi()
name = 'name_example' # str | The document name.
protection = asposecellscloud.WorkbookProtectionRequest() # WorkbookProtectionRequest | Protection settings, only password can be specified. (optional)
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Unprotect document.
    api_response = api_instance.cells_workbook_delete_unprotect_document(name, protection=protection, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsWorkbookApi->cells_workbook_delete_unprotect_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **protection** | [**WorkbookProtectionRequest**](WorkbookProtectionRequest.md)| Protection settings, only password can be specified. | [optional] 
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

# **cells_workbook_delete_workbook_name**
> SaaSposeResponse cells_workbook_delete_workbook_name(name, name_name, folder=folder, storage=storage)

Clean workbook's names.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsWorkbookApi()
name = 'name_example' # str | The workbook name.
name_name = 'name_name_example' # str | The name.
folder = 'folder_example' # str | The workbook folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Clean workbook's names.
    api_response = api_instance.cells_workbook_delete_workbook_name(name, name_name, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsWorkbookApi->cells_workbook_delete_workbook_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The workbook name. | 
 **name_name** | **str**| The name. | 
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

# **cells_workbook_delete_workbook_names**
> SaaSposeResponse cells_workbook_delete_workbook_names(name, folder=folder, storage=storage)

Clean workbook's names.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsWorkbookApi()
name = 'name_example' # str | The workbook name.
folder = 'folder_example' # str | The workbook folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Clean workbook's names.
    api_response = api_instance.cells_workbook_delete_workbook_names(name, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsWorkbookApi->cells_workbook_delete_workbook_names: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The workbook name. | 
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

# **cells_workbook_get_workbook**
> file cells_workbook_get_workbook(name, password=password, format=format, is_auto_fit=is_auto_fit, only_save_table=only_save_table, folder=folder, storage=storage, out_path=out_path)

Read workbook info or export.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsWorkbookApi()
name = 'name_example' # str | The document name.
password = 'password_example' # str | The document password. (optional)
format = 'format_example' # str | The exported file format. (optional)
is_auto_fit = false # bool | Set document rows to be autofit. (optional) (default to false)
only_save_table = false # bool | Only save table data. (optional) (default to false)
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | storage name. (optional)
out_path = 'out_path_example' # str | The document output folder. (optional)

try: 
    # Read workbook info or export.
    api_response = api_instance.cells_workbook_get_workbook(name, password=password, format=format, is_auto_fit=is_auto_fit, only_save_table=only_save_table, folder=folder, storage=storage, out_path=out_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsWorkbookApi->cells_workbook_get_workbook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **password** | **str**| The document password. | [optional] 
 **format** | **str**| The exported file format. | [optional] 
 **is_auto_fit** | **bool**| Set document rows to be autofit. | [optional] [default to false]
 **only_save_table** | **bool**| Only save table data. | [optional] [default to false]
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 
 **out_path** | **str**| The document output folder. | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_workbook_get_workbook_default_style**
> StyleResponse cells_workbook_get_workbook_default_style(name, folder=folder, storage=storage)

Read workbook default style info.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsWorkbookApi()
name = 'name_example' # str | The workbook name.
folder = 'folder_example' # str | The document's folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Read workbook default style info.
    api_response = api_instance.cells_workbook_get_workbook_default_style(name, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsWorkbookApi->cells_workbook_get_workbook_default_style: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The workbook name. | 
 **folder** | **str**| The document&#39;s folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**StyleResponse**](StyleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_workbook_get_workbook_name**
> NameResponse cells_workbook_get_workbook_name(name, name_name, folder=folder, storage=storage)

Read workbook's name.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsWorkbookApi()
name = 'name_example' # str | The workbook name.
name_name = 'name_name_example' # str | The name.
folder = 'folder_example' # str | The workbook folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Read workbook's name.
    api_response = api_instance.cells_workbook_get_workbook_name(name, name_name, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsWorkbookApi->cells_workbook_get_workbook_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The workbook name. | 
 **name_name** | **str**| The name. | 
 **folder** | **str**| The workbook folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**NameResponse**](NameResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_workbook_get_workbook_name_value**
> RangeValueResponse cells_workbook_get_workbook_name_value(name, name_name, folder=folder, storage=storage)

Get workbook's name value.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsWorkbookApi()
name = 'name_example' # str | The workbook name.
name_name = 'name_name_example' # str | The name.
folder = 'folder_example' # str | The workbook folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Get workbook's name value.
    api_response = api_instance.cells_workbook_get_workbook_name_value(name, name_name, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsWorkbookApi->cells_workbook_get_workbook_name_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The workbook name. | 
 **name_name** | **str**| The name. | 
 **folder** | **str**| The workbook folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**RangeValueResponse**](RangeValueResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_workbook_get_workbook_names**
> NamesResponse cells_workbook_get_workbook_names(name, folder=folder, storage=storage)

Read workbook's names.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsWorkbookApi()
name = 'name_example' # str | The workbook name.
folder = 'folder_example' # str | The workbook folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Read workbook's names.
    api_response = api_instance.cells_workbook_get_workbook_names(name, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsWorkbookApi->cells_workbook_get_workbook_names: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The workbook name. | 
 **folder** | **str**| The workbook folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**NamesResponse**](NamesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_workbook_get_workbook_settings**
> WorkbookSettingsResponse cells_workbook_get_workbook_settings(name, folder=folder, storage=storage)

Get Workbook Settings DTO

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsWorkbookApi()
name = 'name_example' # str | Document name.
folder = 'folder_example' # str | Document's folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Get Workbook Settings DTO
    api_response = api_instance.cells_workbook_get_workbook_settings(name, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsWorkbookApi->cells_workbook_get_workbook_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document name. | 
 **folder** | **str**| Document&#39;s folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**WorkbookSettingsResponse**](WorkbookSettingsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_workbook_get_workbook_text_items**
> TextItemsResponse cells_workbook_get_workbook_text_items(name, folder=folder, storage=storage)

Read workbook's text items.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsWorkbookApi()
name = 'name_example' # str | The workbook name.
folder = 'folder_example' # str | The workbook folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Read workbook's text items.
    api_response = api_instance.cells_workbook_get_workbook_text_items(name, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsWorkbookApi->cells_workbook_get_workbook_text_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The workbook name. | 
 **folder** | **str**| The workbook folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**TextItemsResponse**](TextItemsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_workbook_post_autofit_workbook_rows**
> SaaSposeResponse cells_workbook_post_autofit_workbook_rows(name, auto_fitter_options=auto_fitter_options, start_row=start_row, end_row=end_row, only_auto=only_auto, folder=folder, storage=storage)

Autofit workbook rows.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsWorkbookApi()
name = 'name_example' # str | Document name.
auto_fitter_options = asposecellscloud.AutoFitterOptions() # AutoFitterOptions | Auto Fitter Options. (optional)
start_row = 56 # int | Start row. (optional)
end_row = 56 # int | End row. (optional)
only_auto = false # bool | Only auto. (optional) (default to false)
folder = 'folder_example' # str | Document's folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Autofit workbook rows.
    api_response = api_instance.cells_workbook_post_autofit_workbook_rows(name, auto_fitter_options=auto_fitter_options, start_row=start_row, end_row=end_row, only_auto=only_auto, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsWorkbookApi->cells_workbook_post_autofit_workbook_rows: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document name. | 
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

# **cells_workbook_post_encrypt_document**
> SaaSposeResponse cells_workbook_post_encrypt_document(name, encryption=encryption, folder=folder, storage=storage)

Encript document.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsWorkbookApi()
name = 'name_example' # str | The document name.
encryption = asposecellscloud.WorkbookEncryptionRequest() # WorkbookEncryptionRequest | Encryption parameters. (optional)
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Encript document.
    api_response = api_instance.cells_workbook_post_encrypt_document(name, encryption=encryption, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsWorkbookApi->cells_workbook_post_encrypt_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **encryption** | [**WorkbookEncryptionRequest**](WorkbookEncryptionRequest.md)| Encryption parameters. | [optional] 
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

# **cells_workbook_post_import_data**
> SaaSposeResponse cells_workbook_post_import_data(name, importdata, folder=folder, storage=storage)



### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsWorkbookApi()
name = 'name_example' # str | 
importdata = asposecellscloud.ImportOption() # ImportOption | 
folder = 'folder_example' # str |  (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    api_response = api_instance.cells_workbook_post_import_data(name, importdata, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsWorkbookApi->cells_workbook_post_import_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **importdata** | [**ImportOption**](ImportOption.md)|  | 
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

# **cells_workbook_post_protect_document**
> SaaSposeResponse cells_workbook_post_protect_document(name, protection=protection, folder=folder, storage=storage)

Protect document.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsWorkbookApi()
name = 'name_example' # str | The document name.
protection = asposecellscloud.WorkbookProtectionRequest() # WorkbookProtectionRequest | The protection settings. (optional)
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Protect document.
    api_response = api_instance.cells_workbook_post_protect_document(name, protection=protection, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsWorkbookApi->cells_workbook_post_protect_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **protection** | [**WorkbookProtectionRequest**](WorkbookProtectionRequest.md)| The protection settings. | [optional] 
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

# **cells_workbook_post_workbook_calculate_formula**
> SaaSposeResponse cells_workbook_post_workbook_calculate_formula(name, options=options, ignore_error=ignore_error, folder=folder, storage=storage)

Calculate all formulas in workbook.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsWorkbookApi()
name = 'name_example' # str | Document name.
options = asposecellscloud.CalculationOptions() # CalculationOptions | Calculation Options. (optional)
ignore_error = true # bool | ignore Error. (optional)
folder = 'folder_example' # str | Document's folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Calculate all formulas in workbook.
    api_response = api_instance.cells_workbook_post_workbook_calculate_formula(name, options=options, ignore_error=ignore_error, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsWorkbookApi->cells_workbook_post_workbook_calculate_formula: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document name. | 
 **options** | [**CalculationOptions**](CalculationOptions.md)| Calculation Options. | [optional] 
 **ignore_error** | **bool**| ignore Error. | [optional] 
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

# **cells_workbook_post_workbook_get_smart_marker_result**
> file cells_workbook_post_workbook_get_smart_marker_result(name, xml_file=xml_file, folder=folder, storage=storage, out_path=out_path)

Smart marker processing result.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsWorkbookApi()
name = 'name_example' # str | The workbook name.
xml_file = 'xml_file_example' # str | The xml file full path, if empty the data is read from request body. (optional)
folder = 'folder_example' # str | The workbook folder full path. (optional)
storage = 'storage_example' # str | storage name. (optional)
out_path = 'out_path_example' # str | Path to save result (optional)

try: 
    # Smart marker processing result.
    api_response = api_instance.cells_workbook_post_workbook_get_smart_marker_result(name, xml_file=xml_file, folder=folder, storage=storage, out_path=out_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsWorkbookApi->cells_workbook_post_workbook_get_smart_marker_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The workbook name. | 
 **xml_file** | **str**| The xml file full path, if empty the data is read from request body. | [optional] 
 **folder** | **str**| The workbook folder full path. | [optional] 
 **storage** | **str**| storage name. | [optional] 
 **out_path** | **str**| Path to save result | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_workbook_post_workbook_settings**
> SaaSposeResponse cells_workbook_post_workbook_settings(name, settings=settings, folder=folder, storage=storage)

Update Workbook setting 

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsWorkbookApi()
name = 'name_example' # str | Document name.
settings = asposecellscloud.WorkbookSettings() # WorkbookSettings | Workbook Setting DTO (optional)
folder = 'folder_example' # str | Document's folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Update Workbook setting 
    api_response = api_instance.cells_workbook_post_workbook_settings(name, settings=settings, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsWorkbookApi->cells_workbook_post_workbook_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document name. | 
 **settings** | [**WorkbookSettings**](WorkbookSettings.md)| Workbook Setting DTO | [optional] 
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

# **cells_workbook_post_workbook_split**
> SplitResultResponse cells_workbook_post_workbook_split(name, format=format, _from=_from, to=to, horizontal_resolution=horizontal_resolution, vertical_resolution=vertical_resolution, folder=folder, storage=storage)

Split workbook.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsWorkbookApi()
name = 'name_example' # str | The workbook name.
format = 'format_example' # str | Split format. (optional)
_from = 0 # int | Start worksheet index. (optional) (default to 0)
to = 0 # int | End worksheet index. (optional) (default to 0)
horizontal_resolution = 0 # int | Image horizontal resolution. (optional) (default to 0)
vertical_resolution = 0 # int | Image vertical resolution. (optional) (default to 0)
folder = 'folder_example' # str | The workbook folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Split workbook.
    api_response = api_instance.cells_workbook_post_workbook_split(name, format=format, _from=_from, to=to, horizontal_resolution=horizontal_resolution, vertical_resolution=vertical_resolution, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsWorkbookApi->cells_workbook_post_workbook_split: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The workbook name. | 
 **format** | **str**| Split format. | [optional] 
 **_from** | **int**| Start worksheet index. | [optional] [default to 0]
 **to** | **int**| End worksheet index. | [optional] [default to 0]
 **horizontal_resolution** | **int**| Image horizontal resolution. | [optional] [default to 0]
 **vertical_resolution** | **int**| Image vertical resolution. | [optional] [default to 0]
 **folder** | **str**| The workbook folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**SplitResultResponse**](SplitResultResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_workbook_post_workbooks_merge**
> WorkbookResponse cells_workbook_post_workbooks_merge(name, merge_with, folder=folder, storage=storage)

Merge workbooks.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsWorkbookApi()
name = 'name_example' # str | Workbook name.
merge_with = 'merge_with_example' # str | The workbook to merge with.
folder = 'folder_example' # str | Source workbook folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Merge workbooks.
    api_response = api_instance.cells_workbook_post_workbooks_merge(name, merge_with, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsWorkbookApi->cells_workbook_post_workbooks_merge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Workbook name. | 
 **merge_with** | **str**| The workbook to merge with. | 
 **folder** | **str**| Source workbook folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**WorkbookResponse**](WorkbookResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_workbook_post_workbooks_text_replace**
> WorkbookReplaceResponse cells_workbook_post_workbooks_text_replace(name, old_value, new_value, folder=folder, storage=storage)

Replace text.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsWorkbookApi()
name = 'name_example' # str | Document name.
old_value = 'old_value_example' # str | The old value.
new_value = 'new_value_example' # str | The new value.
folder = 'folder_example' # str | Document's folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Replace text.
    api_response = api_instance.cells_workbook_post_workbooks_text_replace(name, old_value, new_value, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsWorkbookApi->cells_workbook_post_workbooks_text_replace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document name. | 
 **old_value** | **str**| The old value. | 
 **new_value** | **str**| The new value. | 
 **folder** | **str**| Document&#39;s folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**WorkbookReplaceResponse**](WorkbookReplaceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_workbook_post_workbooks_text_search**
> TextItemsResponse cells_workbook_post_workbooks_text_search(name, text, folder=folder, storage=storage)

Search text.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsWorkbookApi()
name = 'name_example' # str | Document name.
text = 'text_example' # str | Text sample.
folder = 'folder_example' # str | Document's folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Search text.
    api_response = api_instance.cells_workbook_post_workbooks_text_search(name, text, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsWorkbookApi->cells_workbook_post_workbooks_text_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document name. | 
 **text** | **str**| Text sample. | 
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

# **cells_workbook_put_convert_workbook**
> file cells_workbook_put_convert_workbook(format=format, password=password, out_path=out_path)

Convert workbook from request content to some format.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsWorkbookApi()
format = 'format_example' # str | The format to convert. (optional)
password = 'password_example' # str | The workbook password. (optional)
out_path = 'out_path_example' # str | Path to save result (optional)

try: 
    # Convert workbook from request content to some format.
    api_response = api_instance.cells_workbook_put_convert_workbook(format=format, password=password, out_path=out_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsWorkbookApi->cells_workbook_put_convert_workbook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| The format to convert. | [optional] 
 **password** | **str**| The workbook password. | [optional] 
 **out_path** | **str**| Path to save result | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_workbook_put_document_protect_from_changes**
> SaaSposeResponse cells_workbook_put_document_protect_from_changes(name, password=password, folder=folder, storage=storage)

Protect document from changes.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsWorkbookApi()
name = 'name_example' # str | Document name.
password = asposecellscloud.PasswordRequest() # PasswordRequest | Modification password. (optional)
folder = 'folder_example' # str | Document's folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Protect document from changes.
    api_response = api_instance.cells_workbook_put_document_protect_from_changes(name, password=password, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsWorkbookApi->cells_workbook_put_document_protect_from_changes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document name. | 
 **password** | [**PasswordRequest**](PasswordRequest.md)| Modification password. | [optional] 
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

# **cells_workbook_put_workbook_create**
> WorkbookResponse cells_workbook_put_workbook_create(name, template_file=template_file, data_file=data_file, folder=folder, storage=storage)

Create new workbook using deferent methods.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsWorkbookApi()
name = 'name_example' # str | The new document name.
template_file = 'template_file_example' # str | The template file, if the data not provided default workbook is created. (optional)
data_file = 'data_file_example' # str | Smart marker data file, if the data not provided the request content is checked for the data. (optional)
folder = 'folder_example' # str | The new document folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Create new workbook using deferent methods.
    api_response = api_instance.cells_workbook_put_workbook_create(name, template_file=template_file, data_file=data_file, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsWorkbookApi->cells_workbook_put_workbook_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The new document name. | 
 **template_file** | **str**| The template file, if the data not provided default workbook is created. | [optional] 
 **data_file** | **str**| Smart marker data file, if the data not provided the request content is checked for the data. | [optional] 
 **folder** | **str**| The new document folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**WorkbookResponse**](WorkbookResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

