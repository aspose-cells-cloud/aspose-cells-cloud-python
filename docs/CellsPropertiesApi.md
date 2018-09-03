# asposecellscloud.CellsPropertiesApi

All URIs are relative to *https://api.aspose.cloud/v1.1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cells_properties_delete_document_properties**](CellsPropertiesApi.md#cells_properties_delete_document_properties) | **DELETE** /cells/{name}/documentproperties | Delete all custom document properties and clean built-in ones.
[**cells_properties_delete_document_property**](CellsPropertiesApi.md#cells_properties_delete_document_property) | **DELETE** /cells/{name}/documentproperties/{propertyName} | Delete document property.
[**cells_properties_get_document_properties**](CellsPropertiesApi.md#cells_properties_get_document_properties) | **GET** /cells/{name}/documentproperties | Read document properties.
[**cells_properties_get_document_property**](CellsPropertiesApi.md#cells_properties_get_document_property) | **GET** /cells/{name}/documentproperties/{propertyName} | Read document property by name.
[**cells_properties_put_document_property**](CellsPropertiesApi.md#cells_properties_put_document_property) | **PUT** /cells/{name}/documentproperties/{propertyName} | Set/create document property.


# **cells_properties_delete_document_properties**
> CellsDocumentPropertiesResponse cells_properties_delete_document_properties(name, folder=folder, storage=storage)

Delete all custom document properties and clean built-in ones.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsPropertiesApi()
name = 'name_example' # str | The document name.
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Delete all custom document properties and clean built-in ones.
    api_response = api_instance.cells_properties_delete_document_properties(name, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsPropertiesApi->cells_properties_delete_document_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**CellsDocumentPropertiesResponse**](CellsDocumentPropertiesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_properties_delete_document_property**
> CellsDocumentPropertiesResponse cells_properties_delete_document_property(name, property_name, folder=folder, storage=storage)

Delete document property.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsPropertiesApi()
name = 'name_example' # str | The document name.
property_name = 'property_name_example' # str | The property name.
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Delete document property.
    api_response = api_instance.cells_properties_delete_document_property(name, property_name, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsPropertiesApi->cells_properties_delete_document_property: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **property_name** | **str**| The property name. | 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**CellsDocumentPropertiesResponse**](CellsDocumentPropertiesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_properties_get_document_properties**
> CellsDocumentPropertiesResponse cells_properties_get_document_properties(name, folder=folder, storage=storage)

Read document properties.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsPropertiesApi()
name = 'name_example' # str | The document name.
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Read document properties.
    api_response = api_instance.cells_properties_get_document_properties(name, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsPropertiesApi->cells_properties_get_document_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**CellsDocumentPropertiesResponse**](CellsDocumentPropertiesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_properties_get_document_property**
> CellsDocumentPropertyResponse cells_properties_get_document_property(name, property_name, folder=folder, storage=storage)

Read document property by name.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsPropertiesApi()
name = 'name_example' # str | The document name.
property_name = 'property_name_example' # str | The property name.
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Read document property by name.
    api_response = api_instance.cells_properties_get_document_property(name, property_name, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsPropertiesApi->cells_properties_get_document_property: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **property_name** | **str**| The property name. | 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**CellsDocumentPropertyResponse**](CellsDocumentPropertyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cells_properties_put_document_property**
> CellsDocumentPropertyResponse cells_properties_put_document_property(name, property_name, _property=_property, folder=folder, storage=storage)

Set/create document property.

### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.CellsPropertiesApi()
name = 'name_example' # str | The document name.
property_name = 'property_name_example' # str | The property name.
_property = asposecellscloud.CellsDocumentProperty() # CellsDocumentProperty | with new property value. (optional)
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Set/create document property.
    api_response = api_instance.cells_properties_put_document_property(name, property_name, _property=_property, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsPropertiesApi->cells_properties_put_document_property: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **property_name** | **str**| The property name. | 
 **_property** | [**CellsDocumentProperty**](CellsDocumentProperty.md)| with new property value. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**CellsDocumentPropertyResponse**](CellsDocumentPropertyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

