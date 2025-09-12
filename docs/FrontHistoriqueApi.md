# wizipet_api.FrontHistoriqueApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_front_profile_pet_id_historiques_activite_get**](FrontHistoriqueApi.md#api_v1_front_profile_pet_id_historiques_activite_get) | **GET** /api/v1/front/profile/{pet_id}/historiques/activite | 
[**api_v1_front_profile_pet_id_historiques_alimentations_get**](FrontHistoriqueApi.md#api_v1_front_profile_pet_id_historiques_alimentations_get) | **GET** /api/v1/front/profile/{pet_id}/historiques/alimentations | 
[**api_v1_front_profile_pet_id_historiques_poids_get**](FrontHistoriqueApi.md#api_v1_front_profile_pet_id_historiques_poids_get) | **GET** /api/v1/front/profile/{pet_id}/historiques/poids | 


# **api_v1_front_profile_pet_id_historiques_activite_get**
> ListResponseSantesHistoriqueDto api_v1_front_profile_pet_id_historiques_activite_get(pet_id)

Error codes : 
  - PET_UNOWNED: You are trying to make an action as a profile you are not owning

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.list_response_santes_historique_dto import ListResponseSantesHistoriqueDto
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
    api_instance = wizipet_api.FrontHistoriqueApi(api_client)
    pet_id = 'pet_id_example' # str | 

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_historiques_activite_get(pet_id)
        print("The response of FrontHistoriqueApi->api_v1_front_profile_pet_id_historiques_activite_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontHistoriqueApi->api_v1_front_profile_pet_id_historiques_activite_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **str**|  | 

### Return type

[**ListResponseSantesHistoriqueDto**](ListResponseSantesHistoriqueDto.md)

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

# **api_v1_front_profile_pet_id_historiques_alimentations_get**
> ListResponseSantesHistoriqueDto api_v1_front_profile_pet_id_historiques_alimentations_get(pet_id)

Error codes : 
  - PET_UNOWNED: You are trying to make an action as a profile you are not owning

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.list_response_santes_historique_dto import ListResponseSantesHistoriqueDto
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
    api_instance = wizipet_api.FrontHistoriqueApi(api_client)
    pet_id = 'pet_id_example' # str | 

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_historiques_alimentations_get(pet_id)
        print("The response of FrontHistoriqueApi->api_v1_front_profile_pet_id_historiques_alimentations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontHistoriqueApi->api_v1_front_profile_pet_id_historiques_alimentations_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **str**|  | 

### Return type

[**ListResponseSantesHistoriqueDto**](ListResponseSantesHistoriqueDto.md)

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

# **api_v1_front_profile_pet_id_historiques_poids_get**
> ListResponseSantesHistoriqueDto api_v1_front_profile_pet_id_historiques_poids_get(pet_id)

Error codes : 
  - PET_UNOWNED: You are trying to make an action as a profile you are not owning

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.list_response_santes_historique_dto import ListResponseSantesHistoriqueDto
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
    api_instance = wizipet_api.FrontHistoriqueApi(api_client)
    pet_id = 'pet_id_example' # str | 

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_historiques_poids_get(pet_id)
        print("The response of FrontHistoriqueApi->api_v1_front_profile_pet_id_historiques_poids_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontHistoriqueApi->api_v1_front_profile_pet_id_historiques_poids_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **str**|  | 

### Return type

[**ListResponseSantesHistoriqueDto**](ListResponseSantesHistoriqueDto.md)

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

