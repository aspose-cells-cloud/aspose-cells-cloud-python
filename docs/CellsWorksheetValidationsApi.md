# asposecellscloud.CellsWorksheetValidationsApi

All URIs are relative to *https://api.aspose.cloud/v1.1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cells_worksheet_validations_delete_worksheet_validation**](CellsWorksheetValidationsApi.md#cells_worksheet_validations_delete_worksheet_validation) | **DELETE** /cells/{name}/worksheets/{sheetName}/validations/{validationIndex} | Delete worksheet validation by index.
[**cells_worksheet_validations_get_worksheet_validation**](CellsWorksheetValidationsApi.md#cells_worksheet_validations_get_worksheet_validation) | **GET** /cells/{name}/worksheets/{sheetName}/validations/{validationIndex} | Get worksheet validation by index.
[**cells_worksheet_validations_get_worksheet_validations**](CellsWorksheetValidationsApi.md#cells_worksheet_validations_get_worksheet_validations) | **GET** /cells/{name}/worksheets/{sheetName}/validations | Get worksheet validations.
[**cells_worksheet_validations_post_worksheet_validation**](CellsWorksheetValidationsApi.md#cells_worksheet_validations_post_worksheet_validation) | **POST** /cells/{name}/worksheets/{sheetName}/validations/{validationIndex} | Update worksheet validation by index.
[**cells_worksheet_validations_put_worksheet_validation**](CellsWorksheetValidationsApi.md#cells_worksheet_validations_put_worksheet_validation) | **PUT** /cells/{name}/worksheets/{sheetName}/validations | Add worksheet validation at index.


# **cells_worksheet_validations_delete_worksheet_validation**
> ValidationResponse cells_worksheet_validations_delete_worksheet_validation(name, sheet_name, validation_index, folder=folder)

Delete worksheet validation by index.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsWorksheetValidationsApi()
name = 'name_example' # str | Document name.
sheet_name = 'sheet_name_example' # str | Worksheet name.
validation_index = 56 # int | The validation index.
folder = 'folder_example' # str | Document's folder. (optional)

try: 
    # Delete worksheet validation by index.
    api_response = api_instance.cells_worksheet_validations_delete_worksheet_validation(name, sheet_name, validation_index, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsWorksheetValidationsApi->cells_worksheet_validations_delete_worksheet_validation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document name. | 
 **sheet_name** | **str**| Worksheet name. | 
 **validation_index** | **int**| The validation index. | 
 **folder** | **str**| Document&#39;s folder. | [optional] 

### Return type

[**ValidationResponse**](ValidationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_worksheet_validations_get_worksheet_validation**
> ValidationResponse cells_worksheet_validations_get_worksheet_validation(name, sheet_name, validation_index, folder=folder)

Get worksheet validation by index.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsWorksheetValidationsApi()
name = 'name_example' # str | Document name.
sheet_name = 'sheet_name_example' # str | Worksheet name.
validation_index = 56 # int | The validation index.
folder = 'folder_example' # str | Document's folder. (optional)

try: 
    # Get worksheet validation by index.
    api_response = api_instance.cells_worksheet_validations_get_worksheet_validation(name, sheet_name, validation_index, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsWorksheetValidationsApi->cells_worksheet_validations_get_worksheet_validation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document name. | 
 **sheet_name** | **str**| Worksheet name. | 
 **validation_index** | **int**| The validation index. | 
 **folder** | **str**| Document&#39;s folder. | [optional] 

### Return type

[**ValidationResponse**](ValidationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_worksheet_validations_get_worksheet_validations**
> ValidationsResponse cells_worksheet_validations_get_worksheet_validations(name, sheet_name, folder=folder)

Get worksheet validations.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsWorksheetValidationsApi()
name = 'name_example' # str | Document name.
sheet_name = 'sheet_name_example' # str | Worksheet name.
folder = 'folder_example' # str | Document folder. (optional)

try: 
    # Get worksheet validations.
    api_response = api_instance.cells_worksheet_validations_get_worksheet_validations(name, sheet_name, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsWorksheetValidationsApi->cells_worksheet_validations_get_worksheet_validations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document name. | 
 **sheet_name** | **str**| Worksheet name. | 
 **folder** | **str**| Document folder. | [optional] 

### Return type

[**ValidationsResponse**](ValidationsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_worksheet_validations_post_worksheet_validation**
> ValidationResponse cells_worksheet_validations_post_worksheet_validation(name, sheet_name, validation_index, validation=validation, folder=folder)

Update worksheet validation by index.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsWorksheetValidationsApi()
name = 'name_example' # str | Document name.
sheet_name = 'sheet_name_example' # str | Worksheet name.
validation_index = 56 # int | The validation index.
validation = asposecellscloud.Validation() # Validation |  (optional)
folder = 'folder_example' # str | Document's folder. (optional)

try: 
    # Update worksheet validation by index.
    api_response = api_instance.cells_worksheet_validations_post_worksheet_validation(name, sheet_name, validation_index, validation=validation, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsWorksheetValidationsApi->cells_worksheet_validations_post_worksheet_validation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document name. | 
 **sheet_name** | **str**| Worksheet name. | 
 **validation_index** | **int**| The validation index. | 
 **validation** | [**Validation**](Validation.md)|  | [optional] 
 **folder** | **str**| Document&#39;s folder. | [optional] 

### Return type

[**ValidationResponse**](ValidationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_worksheet_validations_put_worksheet_validation**
> ValidationResponse cells_worksheet_validations_put_worksheet_validation(name, sheet_name, range=range, folder=folder)

Add worksheet validation at index.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsWorksheetValidationsApi()
name = 'name_example' # str | Document name.
sheet_name = 'sheet_name_example' # str | Worksheet name.
range = 'range_example' # str | Specified cells area (optional)
folder = 'folder_example' # str | Document's folder. (optional)

try: 
    # Add worksheet validation at index.
    api_response = api_instance.cells_worksheet_validations_put_worksheet_validation(name, sheet_name, range=range, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsWorksheetValidationsApi->cells_worksheet_validations_put_worksheet_validation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document name. | 
 **sheet_name** | **str**| Worksheet name. | 
 **range** | **str**| Specified cells area | [optional] 
 **folder** | **str**| Document&#39;s folder. | [optional] 

### Return type

[**ValidationResponse**](ValidationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

