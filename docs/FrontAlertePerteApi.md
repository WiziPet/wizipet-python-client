# wizipet_api.FrontAlertePerteApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_front_profile_pet_id_alertes_perte_current_delete**](FrontAlertePerteApi.md#api_v1_front_profile_pet_id_alertes_perte_current_delete) | **DELETE** /api/v1/front/profile/{pet_id}/alertes_perte/current | Supprime l&#39;alerte actuelle, indiquant que l&#39;animal a été retrouvé.
[**api_v1_front_profile_pet_id_alertes_perte_post**](FrontAlertePerteApi.md#api_v1_front_profile_pet_id_alertes_perte_post) | **POST** /api/v1/front/profile/{pet_id}/alertes_perte | Déclenche une alerte indiquant la perte du profil animal.


# **api_v1_front_profile_pet_id_alertes_perte_current_delete**
> WpResponse api_v1_front_profile_pet_id_alertes_perte_current_delete(pet_id)

Supprime l'alerte actuelle, indiquant que l'animal a été retrouvé.



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
    api_instance = wizipet_api.FrontAlertePerteApi(api_client)
    pet_id = 'pet_id_example' # str | 

    try:
        # Supprime l'alerte actuelle, indiquant que l'animal a été retrouvé.
        api_response = await api_instance.api_v1_front_profile_pet_id_alertes_perte_current_delete(pet_id)
        print("The response of FrontAlertePerteApi->api_v1_front_profile_pet_id_alertes_perte_current_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontAlertePerteApi->api_v1_front_profile_pet_id_alertes_perte_current_delete: %s\n" % e)
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
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_front_profile_pet_id_alertes_perte_post**
> WpResponse api_v1_front_profile_pet_id_alertes_perte_post(pet_id, alerte_perte_post_alerte_perte_dto=alerte_perte_post_alerte_perte_dto)

Déclenche une alerte indiquant la perte du profil animal.

Error codes : 
  - ALERTE_PERTE_ALREADY_EXISTS: Une alerte de perte existe déjà pour ce profil
  - ALERTE_PERTE_NO_ADDRESS_FOUND: Aucune adresse n'a pu être obtenue avec la position indiquée.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.alerte_perte_post_alerte_perte_dto import AlertePertePostAlertePerteDto
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
    api_instance = wizipet_api.FrontAlertePerteApi(api_client)
    pet_id = 'pet_id_example' # str | 
    alerte_perte_post_alerte_perte_dto = wizipet_api.AlertePertePostAlertePerteDto() # AlertePertePostAlertePerteDto |  (optional)

    try:
        # Déclenche une alerte indiquant la perte du profil animal.
        api_response = await api_instance.api_v1_front_profile_pet_id_alertes_perte_post(pet_id, alerte_perte_post_alerte_perte_dto=alerte_perte_post_alerte_perte_dto)
        print("The response of FrontAlertePerteApi->api_v1_front_profile_pet_id_alertes_perte_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontAlertePerteApi->api_v1_front_profile_pet_id_alertes_perte_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **str**|  | 
 **alerte_perte_post_alerte_perte_dto** | [**AlertePertePostAlertePerteDto**](AlertePertePostAlertePerteDto.md)|  | [optional] 

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

