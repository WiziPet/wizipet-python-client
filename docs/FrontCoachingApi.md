# wizipet_api.FrontCoachingApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_front_profile_pet_id_santes_coaching_delete**](FrontCoachingApi.md#api_v1_front_profile_pet_id_santes_coaching_delete) | **DELETE** /api/v1/front/profile/{pet_id}/santes/coaching | 
[**api_v1_front_profile_pet_id_santes_coaching_get**](FrontCoachingApi.md#api_v1_front_profile_pet_id_santes_coaching_get) | **GET** /api/v1/front/profile/{pet_id}/santes/coaching | 
[**api_v1_front_profile_pet_id_santes_coaching_infos_put**](FrontCoachingApi.md#api_v1_front_profile_pet_id_santes_coaching_infos_put) | **PUT** /api/v1/front/profile/{pet_id}/santes/coaching/infos | 
[**api_v1_front_profile_pet_id_santes_coaching_post**](FrontCoachingApi.md#api_v1_front_profile_pet_id_santes_coaching_post) | **POST** /api/v1/front/profile/{pet_id}/santes/coaching | 


# **api_v1_front_profile_pet_id_santes_coaching_delete**
> WpResponse api_v1_front_profile_pet_id_santes_coaching_delete(pet_id)

Error codes : 
  - PET_UNOWNED: You are trying to make an action as a profile you are not owning

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.wp_response import WpResponse
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
    api_instance = wizipet_api.FrontCoachingApi(api_client)
    pet_id = 'pet_id_example' # str | 

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_santes_coaching_delete(pet_id)
        print("The response of FrontCoachingApi->api_v1_front_profile_pet_id_santes_coaching_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontCoachingApi->api_v1_front_profile_pet_id_santes_coaching_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **str**|  | 

### Return type

[**WpResponse**](WpResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Not Found |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_front_profile_pet_id_santes_coaching_get**
> WpResponseSantesCoachingDto api_v1_front_profile_pet_id_santes_coaching_get(pet_id)

Error codes : 
  - PET_UNOWNED: You are trying to make an action as a profile you are not owning
  - MISSING_INFORMATION: 

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.wp_response_santes_coaching_dto import WpResponseSantesCoachingDto
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
    api_instance = wizipet_api.FrontCoachingApi(api_client)
    pet_id = 'pet_id_example' # str | 

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_santes_coaching_get(pet_id)
        print("The response of FrontCoachingApi->api_v1_front_profile_pet_id_santes_coaching_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontCoachingApi->api_v1_front_profile_pet_id_santes_coaching_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **str**|  | 

### Return type

[**WpResponseSantesCoachingDto**](WpResponseSantesCoachingDto.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Not Found |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_front_profile_pet_id_santes_coaching_infos_put**
> WpResponse api_v1_front_profile_pet_id_santes_coaching_infos_put(pet_id, santes_put_coaching_infos_dto=santes_put_coaching_infos_dto)

Error codes : 
  - PET_UNOWNED: You are trying to make an action as a profile you are not owning

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.santes_put_coaching_infos_dto import SantesPutCoachingInfosDto
from wizipet_api.models.wp_response import WpResponse
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
    api_instance = wizipet_api.FrontCoachingApi(api_client)
    pet_id = 'pet_id_example' # str | 
    santes_put_coaching_infos_dto = [wizipet_api.SantesPutCoachingInfosDto()] # List[SantesPutCoachingInfosDto] |  (optional)

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_santes_coaching_infos_put(pet_id, santes_put_coaching_infos_dto=santes_put_coaching_infos_dto)
        print("The response of FrontCoachingApi->api_v1_front_profile_pet_id_santes_coaching_infos_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontCoachingApi->api_v1_front_profile_pet_id_santes_coaching_infos_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **str**|  | 
 **santes_put_coaching_infos_dto** | [**List[SantesPutCoachingInfosDto]**](SantesPutCoachingInfosDto.md)|  | [optional] 

### Return type

[**WpResponse**](WpResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Not Found |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_front_profile_pet_id_santes_coaching_post**
> WpResponse api_v1_front_profile_pet_id_santes_coaching_post(pet_id, santes_post_coaching_dto=santes_post_coaching_dto)

Error codes : 
  - PET_UNOWNED: You are trying to make an action as a profile you are not owning
  - MISSING_INFORMATION: 
  - COACHING_ALREADY_EXISTS: 

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.santes_post_coaching_dto import SantesPostCoachingDto
from wizipet_api.models.wp_response import WpResponse
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
    api_instance = wizipet_api.FrontCoachingApi(api_client)
    pet_id = 'pet_id_example' # str | 
    santes_post_coaching_dto = wizipet_api.SantesPostCoachingDto() # SantesPostCoachingDto |  (optional)

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_santes_coaching_post(pet_id, santes_post_coaching_dto=santes_post_coaching_dto)
        print("The response of FrontCoachingApi->api_v1_front_profile_pet_id_santes_coaching_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontCoachingApi->api_v1_front_profile_pet_id_santes_coaching_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **str**|  | 
 **santes_post_coaching_dto** | [**SantesPostCoachingDto**](SantesPostCoachingDto.md)|  | [optional] 

### Return type

[**WpResponse**](WpResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Not Found |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

