# wizipet_api.FrontPromenadeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_front_profile_pet_id_promenades_historique_get**](FrontPromenadeApi.md#api_v1_front_profile_pet_id_promenades_historique_get) | **GET** /api/v1/front/profile/{pet_id}/promenades/historique | 
[**api_v1_front_profile_pet_id_promenades_post**](FrontPromenadeApi.md#api_v1_front_profile_pet_id_promenades_post) | **POST** /api/v1/front/profile/{pet_id}/promenades | 
[**api_v1_front_profile_pet_id_promenades_promenade_id_get**](FrontPromenadeApi.md#api_v1_front_profile_pet_id_promenades_promenade_id_get) | **GET** /api/v1/front/profile/{pet_id}/promenades/{promenade_id} | 
[**api_v1_front_profile_pet_id_promenades_promenade_id_patch**](FrontPromenadeApi.md#api_v1_front_profile_pet_id_promenades_promenade_id_patch) | **PATCH** /api/v1/front/profile/{pet_id}/promenades/{promenade_id} | 


# **api_v1_front_profile_pet_id_promenades_historique_get**
> WpResponsePromenadesPromenadeDto api_v1_front_profile_pet_id_promenades_historique_get(pet_id, search=search, date_gte=date_gte, date_lte=date_lte, count=count, continuation_token=continuation_token)



### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.wp_response_promenades_promenade_dto import WpResponsePromenadesPromenadeDto
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
    api_instance = wizipet_api.FrontPromenadeApi(api_client)
    pet_id = 'pet_id_example' # str | 
    search = 'search_example' # str |  (optional)
    date_gte = 'date_gte_example' # str |  (optional)
    date_lte = 'date_lte_example' # str |  (optional)
    count = 56 # int |  (optional)
    continuation_token = 'continuation_token_example' # str |  (optional)

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_promenades_historique_get(pet_id, search=search, date_gte=date_gte, date_lte=date_lte, count=count, continuation_token=continuation_token)
        print("The response of FrontPromenadeApi->api_v1_front_profile_pet_id_promenades_historique_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontPromenadeApi->api_v1_front_profile_pet_id_promenades_historique_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **str**|  | 
 **search** | **str**|  | [optional] 
 **date_gte** | **str**|  | [optional] 
 **date_lte** | **str**|  | [optional] 
 **count** | **int**|  | [optional] 
 **continuation_token** | **str**|  | [optional] 

### Return type

[**WpResponsePromenadesPromenadeDto**](WpResponsePromenadesPromenadeDto.md)

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

# **api_v1_front_profile_pet_id_promenades_post**
> WpResponseCreateReplyDto api_v1_front_profile_pet_id_promenades_post(pet_id, promenades_post_promenade_dto=promenades_post_promenade_dto)

Error codes : 
  - PROMENADE_MAP_STATIC_TOO_MUCH_CHARACTERS: 
  - PROMENADE_AT_LEAST_TWO_POSITIONS_NEEDED: 
  - PROMENADE_MINIMUM_DISTANCE: 

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.promenades_post_promenade_dto import PromenadesPostPromenadeDto
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
    api_instance = wizipet_api.FrontPromenadeApi(api_client)
    pet_id = 'pet_id_example' # str | 
    promenades_post_promenade_dto = wizipet_api.PromenadesPostPromenadeDto() # PromenadesPostPromenadeDto |  (optional)

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_promenades_post(pet_id, promenades_post_promenade_dto=promenades_post_promenade_dto)
        print("The response of FrontPromenadeApi->api_v1_front_profile_pet_id_promenades_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontPromenadeApi->api_v1_front_profile_pet_id_promenades_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **str**|  | 
 **promenades_post_promenade_dto** | [**PromenadesPostPromenadeDto**](PromenadesPostPromenadeDto.md)|  | [optional] 

### Return type

[**WpResponseCreateReplyDto**](WpResponseCreateReplyDto.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_front_profile_pet_id_promenades_promenade_id_get**
> WpResponsePromenadesPromenadeDto api_v1_front_profile_pet_id_promenades_promenade_id_get(pet_id, promenade_id)



### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.wp_response_promenades_promenade_dto import WpResponsePromenadesPromenadeDto
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
    api_instance = wizipet_api.FrontPromenadeApi(api_client)
    pet_id = 'pet_id_example' # str | 
    promenade_id = 'promenade_id_example' # str | 

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_promenades_promenade_id_get(pet_id, promenade_id)
        print("The response of FrontPromenadeApi->api_v1_front_profile_pet_id_promenades_promenade_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontPromenadeApi->api_v1_front_profile_pet_id_promenades_promenade_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **str**|  | 
 **promenade_id** | **str**|  | 

### Return type

[**WpResponsePromenadesPromenadeDto**](WpResponsePromenadesPromenadeDto.md)

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

# **api_v1_front_profile_pet_id_promenades_promenade_id_patch**
> WpResponseCreateReplyDto api_v1_front_profile_pet_id_promenades_promenade_id_patch(pet_id, promenade_id, promenades_patch_promenade_dto=promenades_patch_promenade_dto)



### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.promenades_patch_promenade_dto import PromenadesPatchPromenadeDto
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
    api_instance = wizipet_api.FrontPromenadeApi(api_client)
    pet_id = 'pet_id_example' # str | 
    promenade_id = 'promenade_id_example' # str | 
    promenades_patch_promenade_dto = wizipet_api.PromenadesPatchPromenadeDto() # PromenadesPatchPromenadeDto |  (optional)

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_promenades_promenade_id_patch(pet_id, promenade_id, promenades_patch_promenade_dto=promenades_patch_promenade_dto)
        print("The response of FrontPromenadeApi->api_v1_front_profile_pet_id_promenades_promenade_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontPromenadeApi->api_v1_front_profile_pet_id_promenades_promenade_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **str**|  | 
 **promenade_id** | **str**|  | 
 **promenades_patch_promenade_dto** | [**PromenadesPatchPromenadeDto**](PromenadesPatchPromenadeDto.md)|  | [optional] 

### Return type

[**WpResponseCreateReplyDto**](WpResponseCreateReplyDto.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

