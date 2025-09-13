# wizipet_api.FrontPenseBeteApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_front_profile_pet_id_santes_pensebetes_get**](FrontPenseBeteApi.md#api_v1_front_profile_pet_id_santes_pensebetes_get) | **GET** /api/v1/front/profile/{pet_id}/santes/pensebetes | 
[**api_v1_front_profile_pet_id_santes_pensebetes_pensebete_id_get**](FrontPenseBeteApi.md#api_v1_front_profile_pet_id_santes_pensebetes_pensebete_id_get) | **GET** /api/v1/front/profile/{pet_id}/santes/pensebetes/{pensebete_id} | 
[**api_v1_front_profile_pet_id_santes_pensebetes_pensebete_id_patch**](FrontPenseBeteApi.md#api_v1_front_profile_pet_id_santes_pensebetes_pensebete_id_patch) | **PATCH** /api/v1/front/profile/{pet_id}/santes/pensebetes/{pensebete_id} | 


# **api_v1_front_profile_pet_id_santes_pensebetes_get**
> WpListResponsePenseBetesPenseBeteItemDto api_v1_front_profile_pet_id_santes_pensebetes_get(pet_id)

Error codes : 
  - PET_UNOWNED: You are trying to make an action as a profile you are not owning

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.wp_list_response_pense_betes_pense_bete_item_dto import WpListResponsePenseBetesPenseBeteItemDto
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
    api_instance = wizipet_api.FrontPenseBeteApi(api_client)
    pet_id = 'pet_id_example' # str | 

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_santes_pensebetes_get(pet_id)
        print("The response of FrontPenseBeteApi->api_v1_front_profile_pet_id_santes_pensebetes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontPenseBeteApi->api_v1_front_profile_pet_id_santes_pensebetes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **str**|  | 

### Return type

[**WpListResponsePenseBetesPenseBeteItemDto**](WpListResponsePenseBetesPenseBeteItemDto.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_front_profile_pet_id_santes_pensebetes_pensebete_id_get**
> WpResponsePenseBetesPenseBeteDto api_v1_front_profile_pet_id_santes_pensebetes_pensebete_id_get(pet_id, pensebete_id)

Error codes : 
  - PET_UNOWNED: You are trying to make an action as a profile you are not owning

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.wp_response_pense_betes_pense_bete_dto import WpResponsePenseBetesPenseBeteDto
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
    api_instance = wizipet_api.FrontPenseBeteApi(api_client)
    pet_id = 'pet_id_example' # str | 
    pensebete_id = 'pensebete_id_example' # str | 

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_santes_pensebetes_pensebete_id_get(pet_id, pensebete_id)
        print("The response of FrontPenseBeteApi->api_v1_front_profile_pet_id_santes_pensebetes_pensebete_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontPenseBeteApi->api_v1_front_profile_pet_id_santes_pensebetes_pensebete_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **str**|  | 
 **pensebete_id** | **str**|  | 

### Return type

[**WpResponsePenseBetesPenseBeteDto**](WpResponsePenseBetesPenseBeteDto.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_front_profile_pet_id_santes_pensebetes_pensebete_id_patch**
> WpResponse api_v1_front_profile_pet_id_santes_pensebetes_pensebete_id_patch(pet_id, pensebete_id, pense_betes_patch_pense_bete_dto=pense_betes_patch_pense_bete_dto)

Error codes : 
  - PET_UNOWNED: You are trying to make an action as a profile you are not owning

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.pense_betes_patch_pense_bete_dto import PenseBetesPatchPenseBeteDto
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
    api_instance = wizipet_api.FrontPenseBeteApi(api_client)
    pet_id = 'pet_id_example' # str | 
    pensebete_id = 'pensebete_id_example' # str | 
    pense_betes_patch_pense_bete_dto = wizipet_api.PenseBetesPatchPenseBeteDto() # PenseBetesPatchPenseBeteDto |  (optional)

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_santes_pensebetes_pensebete_id_patch(pet_id, pensebete_id, pense_betes_patch_pense_bete_dto=pense_betes_patch_pense_bete_dto)
        print("The response of FrontPenseBeteApi->api_v1_front_profile_pet_id_santes_pensebetes_pensebete_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontPenseBeteApi->api_v1_front_profile_pet_id_santes_pensebetes_pensebete_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **str**|  | 
 **pensebete_id** | **str**|  | 
 **pense_betes_patch_pense_bete_dto** | [**PenseBetesPatchPenseBeteDto**](PenseBetesPatchPenseBeteDto.md)|  | [optional] 

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

