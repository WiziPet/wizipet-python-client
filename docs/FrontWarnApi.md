# wizipet_api.FrontWarnApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_front_profile_pet_id_warns_get**](FrontWarnApi.md#api_v1_front_profile_pet_id_warns_get) | **GET** /api/v1/front/profile/{pet_id}/warns | 
[**api_v1_front_profile_pet_id_warns_warn_id_delete**](FrontWarnApi.md#api_v1_front_profile_pet_id_warns_warn_id_delete) | **DELETE** /api/v1/front/profile/{pet_id}/warns/{warn_id} | 


# **api_v1_front_profile_pet_id_warns_get**
> ListResponseWarnsWarnItemDto api_v1_front_profile_pet_id_warns_get(pet_id)



### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.list_response_warns_warn_item_dto import ListResponseWarnsWarnItemDto
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
    api_instance = wizipet_api.FrontWarnApi(api_client)
    pet_id = 'pet_id_example' # str | 

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_warns_get(pet_id)
        print("The response of FrontWarnApi->api_v1_front_profile_pet_id_warns_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontWarnApi->api_v1_front_profile_pet_id_warns_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **str**|  | 

### Return type

[**ListResponseWarnsWarnItemDto**](ListResponseWarnsWarnItemDto.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_front_profile_pet_id_warns_warn_id_delete**
> WpResponse api_v1_front_profile_pet_id_warns_warn_id_delete(pet_id, warn_id)

Error codes : 
  - INVALID_WARN_REFERENCE: 

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
    api_instance = wizipet_api.FrontWarnApi(api_client)
    pet_id = 'pet_id_example' # str | 
    warn_id = 'warn_id_example' # str | 

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_warns_warn_id_delete(pet_id, warn_id)
        print("The response of FrontWarnApi->api_v1_front_profile_pet_id_warns_warn_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontWarnApi->api_v1_front_profile_pet_id_warns_warn_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **str**|  | 
 **warn_id** | **str**|  | 

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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

