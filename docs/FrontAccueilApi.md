# wizipet_api.FrontAccueilApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_front_profile_pet_id_accueil_assistant_personnel_get**](FrontAccueilApi.md#api_v1_front_profile_pet_id_accueil_assistant_personnel_get) | **GET** /api/v1/front/profile/{pet_id}/accueil/assistant_personnel | 
[**api_v1_front_profile_pet_id_accueil_assistant_personnel_type_element_id_delete**](FrontAccueilApi.md#api_v1_front_profile_pet_id_accueil_assistant_personnel_type_element_id_delete) | **DELETE** /api/v1/front/profile/{pet_id}/accueil/assistant_personnel/{type}/{element_id} | 
[**api_v1_front_profile_pet_id_accueil_profile_completion_get**](FrontAccueilApi.md#api_v1_front_profile_pet_id_accueil_profile_completion_get) | **GET** /api/v1/front/profile/{pet_id}/accueil/profile_completion | 


# **api_v1_front_profile_pet_id_accueil_assistant_personnel_get**
> ListResponseAccueilAssistantPersonnelItemDto api_v1_front_profile_pet_id_accueil_assistant_personnel_get(pet_id)

Error codes : 
  - PET_UNOWNED: You are trying to make an action as a profile you are not owning

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.list_response_accueil_assistant_personnel_item_dto import ListResponseAccueilAssistantPersonnelItemDto
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
    api_instance = wizipet_api.FrontAccueilApi(api_client)
    pet_id = 'pet_id_example' # str | 

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_accueil_assistant_personnel_get(pet_id)
        print("The response of FrontAccueilApi->api_v1_front_profile_pet_id_accueil_assistant_personnel_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontAccueilApi->api_v1_front_profile_pet_id_accueil_assistant_personnel_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **str**|  | 

### Return type

[**ListResponseAccueilAssistantPersonnelItemDto**](ListResponseAccueilAssistantPersonnelItemDto.md)

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

# **api_v1_front_profile_pet_id_accueil_assistant_personnel_type_element_id_delete**
> WpResponse api_v1_front_profile_pet_id_accueil_assistant_personnel_type_element_id_delete(pet_id, type, element_id)

Error codes : 
  - PET_UNOWNED: You are trying to make an action as a profile you are not owning

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.accueil_assistant_personnel_type_dto import AccueilAssistantPersonnelTypeDto
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
    api_instance = wizipet_api.FrontAccueilApi(api_client)
    pet_id = 'pet_id_example' # str | 
    type = wizipet_api.AccueilAssistantPersonnelTypeDto() # AccueilAssistantPersonnelTypeDto | 
    element_id = 'element_id_example' # str | 

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_accueil_assistant_personnel_type_element_id_delete(pet_id, type, element_id)
        print("The response of FrontAccueilApi->api_v1_front_profile_pet_id_accueil_assistant_personnel_type_element_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontAccueilApi->api_v1_front_profile_pet_id_accueil_assistant_personnel_type_element_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **str**|  | 
 **type** | [**AccueilAssistantPersonnelTypeDto**](.md)|  | 
 **element_id** | **str**|  | 

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

# **api_v1_front_profile_pet_id_accueil_profile_completion_get**
> WpResponseSystemInt32 api_v1_front_profile_pet_id_accueil_profile_completion_get(pet_id)

Error codes : 
  - PET_UNOWNED: You are trying to make an action as a profile you are not owning

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.wp_response_system_int32 import WpResponseSystemInt32
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
    api_instance = wizipet_api.FrontAccueilApi(api_client)
    pet_id = 'pet_id_example' # str | 

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_accueil_profile_completion_get(pet_id)
        print("The response of FrontAccueilApi->api_v1_front_profile_pet_id_accueil_profile_completion_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontAccueilApi->api_v1_front_profile_pet_id_accueil_profile_completion_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **str**|  | 

### Return type

[**WpResponseSystemInt32**](WpResponseSystemInt32.md)

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

