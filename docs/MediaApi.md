# wizipet_api.MediaApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_media_image_google_image_reference_get**](MediaApi.md#api_v1_media_image_google_image_reference_get) | **GET** /api/v1/media/image/google/{image_reference} | 
[**api_v1_media_image_image_id_get**](MediaApi.md#api_v1_media_image_image_id_get) | **GET** /api/v1/media/image/{imageId} | 
[**api_v1_media_image_image_id_post**](MediaApi.md#api_v1_media_image_image_id_post) | **POST** /api/v1/media/image/{imageId} | 
[**api_v1_media_image_post**](MediaApi.md#api_v1_media_image_post) | **POST** /api/v1/media/image | 
[**api_v1_media_video_post**](MediaApi.md#api_v1_media_video_post) | **POST** /api/v1/media/video | 


# **api_v1_media_image_google_image_reference_get**
> WpResponseMediaImageFileDto api_v1_media_image_google_image_reference_get(image_reference, width=width, height=height, aspect=aspect)



### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.medias_image_aspect_dto import MediasImageAspectDto
from wizipet_api.models.wp_response_media_image_file_dto import WpResponseMediaImageFileDto
from wizipet_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = wizipet_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = wizipet_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with wizipet_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wizipet_api.MediaApi(api_client)
    image_reference = 'image_reference_example' # str | 
    width = 56 # int |  (optional)
    height = 56 # int |  (optional)
    aspect = wizipet_api.MediasImageAspectDto() # MediasImageAspectDto |  (optional)

    try:
        api_response = await api_instance.api_v1_media_image_google_image_reference_get(image_reference, width=width, height=height, aspect=aspect)
        print("The response of MediaApi->api_v1_media_image_google_image_reference_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaApi->api_v1_media_image_google_image_reference_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_reference** | **str**|  | 
 **width** | **int**|  | [optional] 
 **height** | **int**|  | [optional] 
 **aspect** | [**MediasImageAspectDto**](.md)|  | [optional] 

### Return type

[**WpResponseMediaImageFileDto**](WpResponseMediaImageFileDto.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_media_image_image_id_get**
> WpResponseMediaImageFileDto api_v1_media_image_image_id_get(image_id, width=width, height=height, aspect=aspect)



### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.medias_image_aspect_dto import MediasImageAspectDto
from wizipet_api.models.wp_response_media_image_file_dto import WpResponseMediaImageFileDto
from wizipet_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = wizipet_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = wizipet_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with wizipet_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wizipet_api.MediaApi(api_client)
    image_id = 'image_id_example' # str | 
    width = 56 # int |  (optional)
    height = 56 # int |  (optional)
    aspect = wizipet_api.MediasImageAspectDto() # MediasImageAspectDto |  (optional)

    try:
        api_response = await api_instance.api_v1_media_image_image_id_get(image_id, width=width, height=height, aspect=aspect)
        print("The response of MediaApi->api_v1_media_image_image_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaApi->api_v1_media_image_image_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **str**|  | 
 **width** | **int**|  | [optional] 
 **height** | **int**|  | [optional] 
 **aspect** | [**MediasImageAspectDto**](.md)|  | [optional] 

### Return type

[**WpResponseMediaImageFileDto**](WpResponseMediaImageFileDto.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_media_image_image_id_post**
> WpResponseMediaImageFileDto api_v1_media_image_image_id_post(image_id, file=file)



### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.wp_response_media_image_file_dto import WpResponseMediaImageFileDto
from wizipet_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = wizipet_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = wizipet_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with wizipet_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wizipet_api.MediaApi(api_client)
    image_id = 'image_id_example' # str | 
    file = None # bytearray |  (optional)

    try:
        api_response = await api_instance.api_v1_media_image_image_id_post(image_id, file=file)
        print("The response of MediaApi->api_v1_media_image_image_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaApi->api_v1_media_image_image_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **str**|  | 
 **file** | **bytearray**|  | [optional] 

### Return type

[**WpResponseMediaImageFileDto**](WpResponseMediaImageFileDto.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_media_image_post**
> WpResponseMediaImageFileDto api_v1_media_image_post(file=file)



### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.wp_response_media_image_file_dto import WpResponseMediaImageFileDto
from wizipet_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = wizipet_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = wizipet_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with wizipet_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wizipet_api.MediaApi(api_client)
    file = None # bytearray |  (optional)

    try:
        api_response = await api_instance.api_v1_media_image_post(file=file)
        print("The response of MediaApi->api_v1_media_image_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaApi->api_v1_media_image_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**|  | [optional] 

### Return type

[**WpResponseMediaImageFileDto**](WpResponseMediaImageFileDto.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_media_video_post**
> WpResponseCreateReplyDto api_v1_media_video_post(file=file)

Error codes : 
  - VIDEO_FORMAT_NOT_SUPPORTED: 
  - FILE_IS_TOO_BIG: 

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.wp_response_create_reply_dto import WpResponseCreateReplyDto
from wizipet_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = wizipet_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = wizipet_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with wizipet_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wizipet_api.MediaApi(api_client)
    file = None # bytearray |  (optional)

    try:
        api_response = await api_instance.api_v1_media_video_post(file=file)
        print("The response of MediaApi->api_v1_media_video_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaApi->api_v1_media_video_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**|  | [optional] 

### Return type

[**WpResponseCreateReplyDto**](WpResponseCreateReplyDto.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

