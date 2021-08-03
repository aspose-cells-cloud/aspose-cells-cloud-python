# asposecellscloud.LiteCellsApi

All URIs are relative to *https://api.aspose.cloud/v3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_metadata**](LiteCellsApi.md#delete_metadata) | **POST** /cells/metadata/delete | 
[**get_metadata**](LiteCellsApi.md#get_metadata) | **POST** /cells/metadata/get | 
[**post_assemble**](LiteCellsApi.md#post_assemble) | **POST** /cells/assemble | 
[**post_clear_objects**](LiteCellsApi.md#post_clear_objects) | **POST** /cells/clearobjects | 
[**post_export**](LiteCellsApi.md#post_export) | **POST** /cells/export | 
[**post_merge**](LiteCellsApi.md#post_merge) | **POST** /cells/merge | 
[**post_metadata**](LiteCellsApi.md#post_metadata) | **POST** /cells/metadata/update | 
[**post_protect**](LiteCellsApi.md#post_protect) | **POST** /cells/protect | 
[**post_search**](LiteCellsApi.md#post_search) | **POST** /cells/search | 
[**post_split**](LiteCellsApi.md#post_split) | **POST** /cells/split | 
[**post_unlock**](LiteCellsApi.md#post_unlock) | **POST** /cells/unlock | 
[**post_watermark**](LiteCellsApi.md#post_watermark) | **POST** /cells/watermark | 


# **delete_metadata**
> FilesResult delete_metadata(file, type=type)



### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.LiteCellsApi()
file = '/path/to/file.txt' # file | File to upload
type = 'all' # str |  (optional) (default to all)

try: 
    api_response = api_instance.delete_metadata(file, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LiteCellsApi->delete_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| File to upload | 
 **type** | **str**|  | [optional] [default to all]

### Return type

[**FilesResult**](FilesResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metadata**
> list[CellsDocumentProperty] get_metadata(file, type=type)



### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.LiteCellsApi()
file = '/path/to/file.txt' # file | File to upload
type = 'all' # str |  (optional) (default to all)

try: 
    api_response = api_instance.get_metadata(file, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LiteCellsApi->get_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| File to upload | 
 **type** | **str**|  | [optional] [default to all]

### Return type

[**list[CellsDocumentProperty]**](CellsDocumentProperty.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_assemble**
> FilesResult post_assemble(file, datasource, format=format)



### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.LiteCellsApi()
file = '/path/to/file.txt' # file | File to upload
datasource = 'datasource_example' # str | 
format = 'Xlsx' # str |  (optional) (default to Xlsx)

try: 
    api_response = api_instance.post_assemble(file, datasource, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LiteCellsApi->post_assemble: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| File to upload | 
 **datasource** | **str**|  | 
 **format** | **str**|  | [optional] [default to Xlsx]

### Return type

[**FilesResult**](FilesResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_clear_objects**
> FilesResult post_clear_objects(file, objecttype)



### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.LiteCellsApi()
file = '/path/to/file.txt' # file | File to upload
objecttype = 'objecttype_example' # str | 

try: 
    api_response = api_instance.post_clear_objects(file, objecttype)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LiteCellsApi->post_clear_objects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| File to upload | 
 **objecttype** | **str**|  | 

### Return type

[**FilesResult**](FilesResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_export**
> FilesResult post_export(file, object_type, format)



### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.LiteCellsApi()
file = '/path/to/file.txt' # file | File to upload
object_type = 'object_type_example' # str | 
format = 'format_example' # str | 

try: 
    api_response = api_instance.post_export(file, object_type, format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LiteCellsApi->post_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| File to upload | 
 **object_type** | **str**|  | 
 **format** | **str**|  | 

### Return type

[**FilesResult**](FilesResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_merge**
> FileInfo post_merge(file, format=format, merge_to_one_sheet=merge_to_one_sheet)



### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.LiteCellsApi()
file = '/path/to/file.txt' # file | File to upload
format = 'xlsx' # str |  (optional) (default to xlsx)
merge_to_one_sheet = false # bool |  (optional) (default to false)

try: 
    api_response = api_instance.post_merge(file, format=format, merge_to_one_sheet=merge_to_one_sheet)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LiteCellsApi->post_merge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| File to upload | 
 **format** | **str**|  | [optional] [default to xlsx]
 **merge_to_one_sheet** | **bool**|  | [optional] [default to false]

### Return type

[**FileInfo**](FileInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_metadata**
> FilesResult post_metadata(file, document_properties)



### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.LiteCellsApi()
file = '/path/to/file.txt' # file | File to upload
document_properties = asposecellscloud.CellsDocumentProperty() # CellsDocumentProperty | Cells document property.

try: 
    api_response = api_instance.post_metadata(file, document_properties)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LiteCellsApi->post_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| File to upload | 
 **document_properties** | [**CellsDocumentProperty**](CellsDocumentProperty.md)| Cells document property. | 

### Return type

[**FilesResult**](FilesResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_protect**
> FilesResult post_protect(file, password)



### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.LiteCellsApi()
file = '/path/to/file.txt' # file | File to upload
password = 'password_example' # str | 

try: 
    api_response = api_instance.post_protect(file, password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LiteCellsApi->post_protect: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| File to upload | 
 **password** | **str**|  | 

### Return type

[**FilesResult**](FilesResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_search**
> list[TextItem] post_search(file, text, password=password, sheetname=sheetname)



### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.LiteCellsApi()
file = '/path/to/file.txt' # file | File to upload
text = 'text_example' # str | 
password = 'password_example' # str |  (optional)
sheetname = 'sheetname_example' # str |  (optional)

try: 
    api_response = api_instance.post_search(file, text, password=password, sheetname=sheetname)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LiteCellsApi->post_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| File to upload | 
 **text** | **str**|  | 
 **password** | **str**|  | [optional] 
 **sheetname** | **str**|  | [optional] 

### Return type

[**list[TextItem]**](TextItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_split**
> FilesResult post_split(file, format, password=password, _from=_from, to=to)



### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.LiteCellsApi()
file = '/path/to/file.txt' # file | File to upload
format = 'format_example' # str | 
password = 'password_example' # str |  (optional)
_from = 56 # int |  (optional)
to = 56 # int |  (optional)

try: 
    api_response = api_instance.post_split(file, format, password=password, _from=_from, to=to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LiteCellsApi->post_split: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| File to upload | 
 **format** | **str**|  | 
 **password** | **str**|  | [optional] 
 **_from** | **int**|  | [optional] 
 **to** | **int**|  | [optional] 

### Return type

[**FilesResult**](FilesResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_unlock**
> FilesResult post_unlock(file, password)



### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.LiteCellsApi()
file = '/path/to/file.txt' # file | File to upload
password = 'password_example' # str | 

try: 
    api_response = api_instance.post_unlock(file, password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LiteCellsApi->post_unlock: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| File to upload | 
 **password** | **str**|  | 

### Return type

[**FilesResult**](FilesResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_watermark**
> FilesResult post_watermark(file, text, color)



### Example 
```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposecellscloud.LiteCellsApi()
file = '/path/to/file.txt' # file | File to upload
text = 'text_example' # str | 
color = 'color_example' # str | 

try: 
    api_response = api_instance.post_watermark(file, text, color)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LiteCellsApi->post_watermark: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| File to upload | 
 **text** | **str**|  | 
 **color** | **str**|  | 

### Return type

[**FilesResult**](FilesResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

