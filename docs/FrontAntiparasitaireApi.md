# wizipet_api.FrontAntiparasitaireApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_front_antiparasitaires_get**](FrontAntiparasitaireApi.md#api_v1_front_antiparasitaires_get) | **GET** /api/v1/front/antiparasitaires | 
[**api_v1_front_profile_pet_id_santes_antiparasitaires_medicamentations_get**](FrontAntiparasitaireApi.md#api_v1_front_profile_pet_id_santes_antiparasitaires_medicamentations_get) | **GET** /api/v1/front/profile/{pet_id}/santes/antiparasitaires/medicamentations | 
[**api_v1_front_profile_pet_id_santes_antiparasitaires_medicamentations_medicamentation_id_patch**](FrontAntiparasitaireApi.md#api_v1_front_profile_pet_id_santes_antiparasitaires_medicamentations_medicamentation_id_patch) | **PATCH** /api/v1/front/profile/{pet_id}/santes/antiparasitaires/medicamentations/{medicamentation_id} | 
[**api_v1_front_profile_pet_id_santes_antiparasitaires_medicamentations_post**](FrontAntiparasitaireApi.md#api_v1_front_profile_pet_id_santes_antiparasitaires_medicamentations_post) | **POST** /api/v1/front/profile/{pet_id}/santes/antiparasitaires/medicamentations | 


# **api_v1_front_antiparasitaires_get**
> WpListResponseAntiparasitairesAntiparasitaireDto api_v1_front_antiparasitaires_get()



### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.wp_list_response_antiparasitaires_antiparasitaire_dto import WpListResponseAntiparasitairesAntiparasitaireDto
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
    api_instance = wizipet_api.FrontAntiparasitaireApi(api_client)

    try:
        api_response = await api_instance.api_v1_front_antiparasitaires_get()
        print("The response of FrontAntiparasitaireApi->api_v1_front_antiparasitaires_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontAntiparasitaireApi->api_v1_front_antiparasitaires_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**WpListResponseAntiparasitairesAntiparasitaireDto**](WpListResponseAntiparasitairesAntiparasitaireDto.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_front_profile_pet_id_santes_antiparasitaires_medicamentations_get**
> WpListResponseSantesMedicamentationItemDto api_v1_front_profile_pet_id_santes_antiparasitaires_medicamentations_get(pet_id)

Error codes : 
  - PET_UNOWNED: You are trying to make an action as a profile you are not owning

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.wp_list_response_santes_medicamentation_item_dto import WpListResponseSantesMedicamentationItemDto
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
    api_instance = wizipet_api.FrontAntiparasitaireApi(api_client)
    pet_id = 'pet_id_example' # str | 

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_santes_antiparasitaires_medicamentations_get(pet_id)
        print("The response of FrontAntiparasitaireApi->api_v1_front_profile_pet_id_santes_antiparasitaires_medicamentations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontAntiparasitaireApi->api_v1_front_profile_pet_id_santes_antiparasitaires_medicamentations_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **str**|  | 

### Return type

[**WpListResponseSantesMedicamentationItemDto**](WpListResponseSantesMedicamentationItemDto.md)

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

# **api_v1_front_profile_pet_id_santes_antiparasitaires_medicamentations_medicamentation_id_patch**
> WpResponse api_v1_front_profile_pet_id_santes_antiparasitaires_medicamentations_medicamentation_id_patch(pet_id, medicamentation_id, santes_set_medicamentation_dto=santes_set_medicamentation_dto)

Error codes : 
  - PET_UNOWNED: You are trying to make an action as a profile you are not owning
  - INVALID_REFERENCE: 
  - INVALID_SPECIES_PRODUCT: 

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.santes_set_medicamentation_dto import SantesSetMedicamentationDto
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
    api_instance = wizipet_api.FrontAntiparasitaireApi(api_client)
    pet_id = 'pet_id_example' # str | 
    medicamentation_id = 'medicamentation_id_example' # str | 
    santes_set_medicamentation_dto = wizipet_api.SantesSetMedicamentationDto() # SantesSetMedicamentationDto |  (optional)

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_santes_antiparasitaires_medicamentations_medicamentation_id_patch(pet_id, medicamentation_id, santes_set_medicamentation_dto=santes_set_medicamentation_dto)
        print("The response of FrontAntiparasitaireApi->api_v1_front_profile_pet_id_santes_antiparasitaires_medicamentations_medicamentation_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontAntiparasitaireApi->api_v1_front_profile_pet_id_santes_antiparasitaires_medicamentations_medicamentation_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **str**|  | 
 **medicamentation_id** | **str**|  | 
 **santes_set_medicamentation_dto** | [**SantesSetMedicamentationDto**](SantesSetMedicamentationDto.md)|  | [optional] 

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_front_profile_pet_id_santes_antiparasitaires_medicamentations_post**
> WpResponseCreateReplyDto api_v1_front_profile_pet_id_santes_antiparasitaires_medicamentations_post(pet_id, santes_set_medicamentation_dto=santes_set_medicamentation_dto)

Error codes : 
  - PET_UNOWNED: You are trying to make an action as a profile you are not owning
  - INVALID_REFERENCE: 
  - INVALID_SPECIES_PRODUCT: 

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.santes_set_medicamentation_dto import SantesSetMedicamentationDto
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
    api_instance = wizipet_api.FrontAntiparasitaireApi(api_client)
    pet_id = 'pet_id_example' # str | 
    santes_set_medicamentation_dto = wizipet_api.SantesSetMedicamentationDto() # SantesSetMedicamentationDto |  (optional)

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_santes_antiparasitaires_medicamentations_post(pet_id, santes_set_medicamentation_dto=santes_set_medicamentation_dto)
        print("The response of FrontAntiparasitaireApi->api_v1_front_profile_pet_id_santes_antiparasitaires_medicamentations_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontAntiparasitaireApi->api_v1_front_profile_pet_id_santes_antiparasitaires_medicamentations_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **str**|  | 
 **santes_set_medicamentation_dto** | [**SantesSetMedicamentationDto**](SantesSetMedicamentationDto.md)|  | [optional] 

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

