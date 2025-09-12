# wizipet_api.FrontVaccinApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_front_profile_pet_id_santes_vaccinations_get**](FrontVaccinApi.md#api_v1_front_profile_pet_id_santes_vaccinations_get) | **GET** /api/v1/front/profile/{pet_id}/santes/vaccinations | 
[**api_v1_front_profile_pet_id_santes_vaccinations_post**](FrontVaccinApi.md#api_v1_front_profile_pet_id_santes_vaccinations_post) | **POST** /api/v1/front/profile/{pet_id}/santes/vaccinations | 
[**api_v1_front_profile_pet_id_santes_vaccinations_vaccination_id_patch**](FrontVaccinApi.md#api_v1_front_profile_pet_id_santes_vaccinations_vaccination_id_patch) | **PATCH** /api/v1/front/profile/{pet_id}/santes/vaccinations/{vaccination_id} | 
[**api_v1_front_vaccins_get**](FrontVaccinApi.md#api_v1_front_vaccins_get) | **GET** /api/v1/front/vaccins | 


# **api_v1_front_profile_pet_id_santes_vaccinations_get**
> ListResponseVaccinsVaccinationItemDto api_v1_front_profile_pet_id_santes_vaccinations_get(pet_id)

Error codes : 
  - PET_UNOWNED: You are trying to make an action as a profile you are not owning

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.list_response_vaccins_vaccination_item_dto import ListResponseVaccinsVaccinationItemDto
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
    api_instance = wizipet_api.FrontVaccinApi(api_client)
    pet_id = 'pet_id_example' # str | 

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_santes_vaccinations_get(pet_id)
        print("The response of FrontVaccinApi->api_v1_front_profile_pet_id_santes_vaccinations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontVaccinApi->api_v1_front_profile_pet_id_santes_vaccinations_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **str**|  | 

### Return type

[**ListResponseVaccinsVaccinationItemDto**](ListResponseVaccinsVaccinationItemDto.md)

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

# **api_v1_front_profile_pet_id_santes_vaccinations_post**
> WpResponse api_v1_front_profile_pet_id_santes_vaccinations_post(pet_id, vaccins_post_vaccination_dto=vaccins_post_vaccination_dto)

Error codes : 
  - PET_UNOWNED: You are trying to make an action as a profile you are not owning
  - INVALID_REFERENCE: 
  - INVALID_SPECIES_PRODUCT: 

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.vaccins_post_vaccination_dto import VaccinsPostVaccinationDto
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
    api_instance = wizipet_api.FrontVaccinApi(api_client)
    pet_id = 'pet_id_example' # str | 
    vaccins_post_vaccination_dto = wizipet_api.VaccinsPostVaccinationDto() # VaccinsPostVaccinationDto |  (optional)

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_santes_vaccinations_post(pet_id, vaccins_post_vaccination_dto=vaccins_post_vaccination_dto)
        print("The response of FrontVaccinApi->api_v1_front_profile_pet_id_santes_vaccinations_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontVaccinApi->api_v1_front_profile_pet_id_santes_vaccinations_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **str**|  | 
 **vaccins_post_vaccination_dto** | [**VaccinsPostVaccinationDto**](VaccinsPostVaccinationDto.md)|  | [optional] 

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

# **api_v1_front_profile_pet_id_santes_vaccinations_vaccination_id_patch**
> WpResponse api_v1_front_profile_pet_id_santes_vaccinations_vaccination_id_patch(pet_id, vaccination_id, vaccins_patch_vaccination_dto=vaccins_patch_vaccination_dto)

Error codes : 
  - PET_UNOWNED: You are trying to make an action as a profile you are not owning
  - INVALID_REFERENCE: 
  - INVALID_SPECIES_PRODUCT: 

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.vaccins_patch_vaccination_dto import VaccinsPatchVaccinationDto
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
    api_instance = wizipet_api.FrontVaccinApi(api_client)
    pet_id = 'pet_id_example' # str | 
    vaccination_id = 'vaccination_id_example' # str | 
    vaccins_patch_vaccination_dto = wizipet_api.VaccinsPatchVaccinationDto() # VaccinsPatchVaccinationDto |  (optional)

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_santes_vaccinations_vaccination_id_patch(pet_id, vaccination_id, vaccins_patch_vaccination_dto=vaccins_patch_vaccination_dto)
        print("The response of FrontVaccinApi->api_v1_front_profile_pet_id_santes_vaccinations_vaccination_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontVaccinApi->api_v1_front_profile_pet_id_santes_vaccinations_vaccination_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **str**|  | 
 **vaccination_id** | **str**|  | 
 **vaccins_patch_vaccination_dto** | [**VaccinsPatchVaccinationDto**](VaccinsPatchVaccinationDto.md)|  | [optional] 

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

# **api_v1_front_vaccins_get**
> WpResponseVaccinsListVaccinDto api_v1_front_vaccins_get()



### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.wp_response_vaccins_list_vaccin_dto import WpResponseVaccinsListVaccinDto
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
    api_instance = wizipet_api.FrontVaccinApi(api_client)

    try:
        api_response = await api_instance.api_v1_front_vaccins_get()
        print("The response of FrontVaccinApi->api_v1_front_vaccins_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontVaccinApi->api_v1_front_vaccins_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**WpResponseVaccinsListVaccinDto**](WpResponseVaccinsListVaccinDto.md)

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

