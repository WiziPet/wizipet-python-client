# wizipet_api.FrontCarteApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_front_cartes_animaute_local_pages_post**](FrontCarteApi.md#api_v1_front_cartes_animaute_local_pages_post) | **POST** /api/v1/front/cartes/animaute/local_pages | 
[**api_v1_front_cartes_expedia_hotels_post**](FrontCarteApi.md#api_v1_front_cartes_expedia_hotels_post) | **POST** /api/v1/front/cartes/expedia/hotels | 
[**api_v1_front_cartes_geocode_get**](FrontCarteApi.md#api_v1_front_cartes_geocode_get) | **GET** /api/v1/front/cartes/geocode | Obtient une position latitude longitude à partir d&#39;une addresse.
[**api_v1_front_cartes_pets_perdus_post**](FrontCarteApi.md#api_v1_front_cartes_pets_perdus_post) | **POST** /api/v1/front/cartes/pets/perdus | Obtient les profils des animaux perdus dans une zone géographique donnée.
[**api_v1_front_cartes_places_pet_friendly_place_id_get**](FrontCarteApi.md#api_v1_front_cartes_places_pet_friendly_place_id_get) | **GET** /api/v1/front/cartes/places/pet_friendly/{place_id} | 
[**api_v1_front_cartes_places_pet_friendly_post**](FrontCarteApi.md#api_v1_front_cartes_places_pet_friendly_post) | **POST** /api/v1/front/cartes/places/pet_friendly | 
[**api_v1_front_cartes_places_place_id_get**](FrontCarteApi.md#api_v1_front_cartes_places_place_id_get) | **GET** /api/v1/front/cartes/places/{place_id} | 
[**api_v1_front_cartes_places_post**](FrontCarteApi.md#api_v1_front_cartes_places_post) | **POST** /api/v1/front/cartes/places | 
[**api_v1_front_cartes_position_get**](FrontCarteApi.md#api_v1_front_cartes_position_get) | **GET** /api/v1/front/cartes/position | 
[**api_v1_front_cartes_position_image_get**](FrontCarteApi.md#api_v1_front_cartes_position_image_get) | **GET** /api/v1/front/cartes/position/image | Obtient une image avec une position demandée ou là dernière position connue de l&#39;utilisateur•trice
[**api_v1_front_cartes_position_put**](FrontCarteApi.md#api_v1_front_cartes_position_put) | **PUT** /api/v1/front/cartes/position | 
[**api_v1_front_cartes_shared_position_allowed_patch**](FrontCarteApi.md#api_v1_front_cartes_shared_position_allowed_patch) | **PATCH** /api/v1/front/cartes/shared_position_allowed | 
[**api_v1_front_cartes_users_post**](FrontCarteApi.md#api_v1_front_cartes_users_post) | **POST** /api/v1/front/cartes/users | Obtient les utilisateurs partageant leur position et leurs profils (non perdus), exclus l&#39;utilisateur couramment identifié.
[**api_v1_front_profile_pet_id_cartes_places_pet_friendly_place_id_delete**](FrontCarteApi.md#api_v1_front_profile_pet_id_cartes_places_pet_friendly_place_id_delete) | **DELETE** /api/v1/front/profile/{pet_id}/cartes/places/pet_friendly/{place_id} | 
[**api_v1_front_profile_pet_id_cartes_places_pet_friendly_place_id_patch**](FrontCarteApi.md#api_v1_front_profile_pet_id_cartes_places_pet_friendly_place_id_patch) | **PATCH** /api/v1/front/profile/{pet_id}/cartes/places/pet_friendly/{place_id} | 
[**api_v1_front_profile_pet_id_cartes_places_pet_friendly_place_id_post**](FrontCarteApi.md#api_v1_front_profile_pet_id_cartes_places_pet_friendly_place_id_post) | **POST** /api/v1/front/profile/{pet_id}/cartes/places/pet_friendly/{place_id} | 
[**api_v1_front_profile_pet_id_cartes_places_pet_friendly_post**](FrontCarteApi.md#api_v1_front_profile_pet_id_cartes_places_pet_friendly_post) | **POST** /api/v1/front/profile/{pet_id}/cartes/places/pet_friendly | 


# **api_v1_front_cartes_animaute_local_pages_post**
> ListResponsePlacesAnimauteLocalPageItemDto api_v1_front_cartes_animaute_local_pages_post(places_list_places_from_bounds_dto=places_list_places_from_bounds_dto)



### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.list_response_places_animaute_local_page_item_dto import ListResponsePlacesAnimauteLocalPageItemDto
from wizipet_api.models.places_list_places_from_bounds_dto import PlacesListPlacesFromBoundsDto
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
    api_instance = wizipet_api.FrontCarteApi(api_client)
    places_list_places_from_bounds_dto = wizipet_api.PlacesListPlacesFromBoundsDto() # PlacesListPlacesFromBoundsDto |  (optional)

    try:
        api_response = await api_instance.api_v1_front_cartes_animaute_local_pages_post(places_list_places_from_bounds_dto=places_list_places_from_bounds_dto)
        print("The response of FrontCarteApi->api_v1_front_cartes_animaute_local_pages_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontCarteApi->api_v1_front_cartes_animaute_local_pages_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **places_list_places_from_bounds_dto** | [**PlacesListPlacesFromBoundsDto**](PlacesListPlacesFromBoundsDto.md)|  | [optional] 

### Return type

[**ListResponsePlacesAnimauteLocalPageItemDto**](ListResponsePlacesAnimauteLocalPageItemDto.md)

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

# **api_v1_front_cartes_expedia_hotels_post**
> ListResponsePlacesExpediaHotelItemDto api_v1_front_cartes_expedia_hotels_post(places_list_expedia_hotel_search_dto=places_list_expedia_hotel_search_dto)

Error codes : 
  - EXPEDIA_REQUEST_ERROR: 
  - EXPEDIA_INVALID_DATE_RANGE: 

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.list_response_places_expedia_hotel_item_dto import ListResponsePlacesExpediaHotelItemDto
from wizipet_api.models.places_list_expedia_hotel_search_dto import PlacesListExpediaHotelSearchDto
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
    api_instance = wizipet_api.FrontCarteApi(api_client)
    places_list_expedia_hotel_search_dto = wizipet_api.PlacesListExpediaHotelSearchDto() # PlacesListExpediaHotelSearchDto |  (optional)

    try:
        api_response = await api_instance.api_v1_front_cartes_expedia_hotels_post(places_list_expedia_hotel_search_dto=places_list_expedia_hotel_search_dto)
        print("The response of FrontCarteApi->api_v1_front_cartes_expedia_hotels_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontCarteApi->api_v1_front_cartes_expedia_hotels_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **places_list_expedia_hotel_search_dto** | [**PlacesListExpediaHotelSearchDto**](PlacesListExpediaHotelSearchDto.md)|  | [optional] 

### Return type

[**ListResponsePlacesExpediaHotelItemDto**](ListResponsePlacesExpediaHotelItemDto.md)

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

# **api_v1_front_cartes_geocode_get**
> WpResponseCartesGeocodeResultsDto api_v1_front_cartes_geocode_get(address=address)

Obtient une position latitude longitude à partir d'une addresse.

Error codes : 
  - ZERO_RESULTS: Aucun résultat trouvé pour cette requête.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.wp_response_cartes_geocode_results_dto import WpResponseCartesGeocodeResultsDto
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
    api_instance = wizipet_api.FrontCarteApi(api_client)
    address = 'address_example' # str |  (optional)

    try:
        # Obtient une position latitude longitude à partir d'une addresse.
        api_response = await api_instance.api_v1_front_cartes_geocode_get(address=address)
        print("The response of FrontCarteApi->api_v1_front_cartes_geocode_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontCarteApi->api_v1_front_cartes_geocode_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**|  | [optional] 

### Return type

[**WpResponseCartesGeocodeResultsDto**](WpResponseCartesGeocodeResultsDto.md)

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

# **api_v1_front_cartes_pets_perdus_post**
> ListResponseCartesPetItemDto api_v1_front_cartes_pets_perdus_post(cartes_list_profiles_param_dto=cartes_list_profiles_param_dto)

Obtient les profils des animaux perdus dans une zone géographique donnée.



### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.cartes_list_profiles_param_dto import CartesListProfilesParamDto
from wizipet_api.models.list_response_cartes_pet_item_dto import ListResponseCartesPetItemDto
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
    api_instance = wizipet_api.FrontCarteApi(api_client)
    cartes_list_profiles_param_dto = wizipet_api.CartesListProfilesParamDto() # CartesListProfilesParamDto |  (optional)

    try:
        # Obtient les profils des animaux perdus dans une zone géographique donnée.
        api_response = await api_instance.api_v1_front_cartes_pets_perdus_post(cartes_list_profiles_param_dto=cartes_list_profiles_param_dto)
        print("The response of FrontCarteApi->api_v1_front_cartes_pets_perdus_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontCarteApi->api_v1_front_cartes_pets_perdus_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cartes_list_profiles_param_dto** | [**CartesListProfilesParamDto**](CartesListProfilesParamDto.md)|  | [optional] 

### Return type

[**ListResponseCartesPetItemDto**](ListResponseCartesPetItemDto.md)

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

# **api_v1_front_cartes_places_pet_friendly_place_id_get**
> WpResponseCartesPetFriendlyPlaceDetailsDto api_v1_front_cartes_places_pet_friendly_place_id_get(place_id)



### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.wp_response_cartes_pet_friendly_place_details_dto import WpResponseCartesPetFriendlyPlaceDetailsDto
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
    api_instance = wizipet_api.FrontCarteApi(api_client)
    place_id = 'place_id_example' # str | 

    try:
        api_response = await api_instance.api_v1_front_cartes_places_pet_friendly_place_id_get(place_id)
        print("The response of FrontCarteApi->api_v1_front_cartes_places_pet_friendly_place_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontCarteApi->api_v1_front_cartes_places_pet_friendly_place_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **place_id** | **str**|  | 

### Return type

[**WpResponseCartesPetFriendlyPlaceDetailsDto**](WpResponseCartesPetFriendlyPlaceDetailsDto.md)

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

# **api_v1_front_cartes_places_pet_friendly_post**
> ListResponseCartesPetFriendlyLocationItemDto api_v1_front_cartes_places_pet_friendly_post(places_list_places_from_bounds_dto=places_list_places_from_bounds_dto)



### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.list_response_cartes_pet_friendly_location_item_dto import ListResponseCartesPetFriendlyLocationItemDto
from wizipet_api.models.places_list_places_from_bounds_dto import PlacesListPlacesFromBoundsDto
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
    api_instance = wizipet_api.FrontCarteApi(api_client)
    places_list_places_from_bounds_dto = wizipet_api.PlacesListPlacesFromBoundsDto() # PlacesListPlacesFromBoundsDto |  (optional)

    try:
        api_response = await api_instance.api_v1_front_cartes_places_pet_friendly_post(places_list_places_from_bounds_dto=places_list_places_from_bounds_dto)
        print("The response of FrontCarteApi->api_v1_front_cartes_places_pet_friendly_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontCarteApi->api_v1_front_cartes_places_pet_friendly_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **places_list_places_from_bounds_dto** | [**PlacesListPlacesFromBoundsDto**](PlacesListPlacesFromBoundsDto.md)|  | [optional] 

### Return type

[**ListResponseCartesPetFriendlyLocationItemDto**](ListResponseCartesPetFriendlyLocationItemDto.md)

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

# **api_v1_front_cartes_places_place_id_get**
> WpResponseCartesPlaceDetailsDto api_v1_front_cartes_places_place_id_get(place_id)



### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.wp_response_cartes_place_details_dto import WpResponseCartesPlaceDetailsDto
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
    api_instance = wizipet_api.FrontCarteApi(api_client)
    place_id = 'place_id_example' # str | 

    try:
        api_response = await api_instance.api_v1_front_cartes_places_place_id_get(place_id)
        print("The response of FrontCarteApi->api_v1_front_cartes_places_place_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontCarteApi->api_v1_front_cartes_places_place_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **place_id** | **str**|  | 

### Return type

[**WpResponseCartesPlaceDetailsDto**](WpResponseCartesPlaceDetailsDto.md)

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

# **api_v1_front_cartes_places_post**
> ListResponsePlacesPlaceItemDto api_v1_front_cartes_places_post(places_list_places_dto=places_list_places_dto)



### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.list_response_places_place_item_dto import ListResponsePlacesPlaceItemDto
from wizipet_api.models.places_list_places_dto import PlacesListPlacesDto
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
    api_instance = wizipet_api.FrontCarteApi(api_client)
    places_list_places_dto = wizipet_api.PlacesListPlacesDto() # PlacesListPlacesDto |  (optional)

    try:
        api_response = await api_instance.api_v1_front_cartes_places_post(places_list_places_dto=places_list_places_dto)
        print("The response of FrontCarteApi->api_v1_front_cartes_places_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontCarteApi->api_v1_front_cartes_places_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **places_list_places_dto** | [**PlacesListPlacesDto**](PlacesListPlacesDto.md)|  | [optional] 

### Return type

[**ListResponsePlacesPlaceItemDto**](ListResponsePlacesPlaceItemDto.md)

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

# **api_v1_front_cartes_position_get**
> WpResponseCartesPositionDto api_v1_front_cartes_position_get()



### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.wp_response_cartes_position_dto import WpResponseCartesPositionDto
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
    api_instance = wizipet_api.FrontCarteApi(api_client)

    try:
        api_response = await api_instance.api_v1_front_cartes_position_get()
        print("The response of FrontCarteApi->api_v1_front_cartes_position_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontCarteApi->api_v1_front_cartes_position_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**WpResponseCartesPositionDto**](WpResponseCartesPositionDto.md)

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

# **api_v1_front_cartes_position_image_get**
> WpResponseSystemBytes api_v1_front_cartes_position_image_get(width=width, height=height, aspect=aspect, lat=lat, lng=lng)

Obtient une image avec une position demandée ou là dernière position connue de l'utilisateur•trice



### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.medias_image_aspect_dto import MediasImageAspectDto
from wizipet_api.models.wp_response_system_bytes import WpResponseSystemBytes
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
    api_instance = wizipet_api.FrontCarteApi(api_client)
    width = 56 # int |  (optional)
    height = 56 # int |  (optional)
    aspect = wizipet_api.MediasImageAspectDto() # MediasImageAspectDto |  (optional)
    lat = 3.4 # float | Position sur le référentiel nord-sud. (optional)
    lng = 3.4 # float | Position sur un référentiel est-ouest. (optional)

    try:
        # Obtient une image avec une position demandée ou là dernière position connue de l'utilisateur•trice
        api_response = await api_instance.api_v1_front_cartes_position_image_get(width=width, height=height, aspect=aspect, lat=lat, lng=lng)
        print("The response of FrontCarteApi->api_v1_front_cartes_position_image_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontCarteApi->api_v1_front_cartes_position_image_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **width** | **int**|  | [optional] 
 **height** | **int**|  | [optional] 
 **aspect** | [**MediasImageAspectDto**](.md)|  | [optional] 
 **lat** | **float**| Position sur le référentiel nord-sud. | [optional] 
 **lng** | **float**| Position sur un référentiel est-ouest. | [optional] 

### Return type

[**WpResponseSystemBytes**](WpResponseSystemBytes.md)

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

# **api_v1_front_cartes_position_put**
> WpResponse api_v1_front_cartes_position_put(cartes_put_position_dto=cartes_put_position_dto)



### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.cartes_put_position_dto import CartesPutPositionDto
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
    api_instance = wizipet_api.FrontCarteApi(api_client)
    cartes_put_position_dto = wizipet_api.CartesPutPositionDto() # CartesPutPositionDto |  (optional)

    try:
        api_response = await api_instance.api_v1_front_cartes_position_put(cartes_put_position_dto=cartes_put_position_dto)
        print("The response of FrontCarteApi->api_v1_front_cartes_position_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontCarteApi->api_v1_front_cartes_position_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cartes_put_position_dto** | [**CartesPutPositionDto**](CartesPutPositionDto.md)|  | [optional] 

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

# **api_v1_front_cartes_shared_position_allowed_patch**
> WpResponse api_v1_front_cartes_shared_position_allowed_patch(shared_position_allowed=shared_position_allowed)



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
    api_instance = wizipet_api.FrontCarteApi(api_client)
    shared_position_allowed = True # bool |  (optional)

    try:
        api_response = await api_instance.api_v1_front_cartes_shared_position_allowed_patch(shared_position_allowed=shared_position_allowed)
        print("The response of FrontCarteApi->api_v1_front_cartes_shared_position_allowed_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontCarteApi->api_v1_front_cartes_shared_position_allowed_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shared_position_allowed** | **bool**|  | [optional] 

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

# **api_v1_front_cartes_users_post**
> ListResponseCartesUserItemDto api_v1_front_cartes_users_post(cartes_list_users_param_dto=cartes_list_users_param_dto)

Obtient les utilisateurs partageant leur position et leurs profils (non perdus), exclus l'utilisateur couramment identifié.

Verbe POST pour être compatible avec RestSharp

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.cartes_list_users_param_dto import CartesListUsersParamDto
from wizipet_api.models.list_response_cartes_user_item_dto import ListResponseCartesUserItemDto
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
    api_instance = wizipet_api.FrontCarteApi(api_client)
    cartes_list_users_param_dto = wizipet_api.CartesListUsersParamDto() # CartesListUsersParamDto |  (optional)

    try:
        # Obtient les utilisateurs partageant leur position et leurs profils (non perdus), exclus l'utilisateur couramment identifié.
        api_response = await api_instance.api_v1_front_cartes_users_post(cartes_list_users_param_dto=cartes_list_users_param_dto)
        print("The response of FrontCarteApi->api_v1_front_cartes_users_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontCarteApi->api_v1_front_cartes_users_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cartes_list_users_param_dto** | [**CartesListUsersParamDto**](CartesListUsersParamDto.md)|  | [optional] 

### Return type

[**ListResponseCartesUserItemDto**](ListResponseCartesUserItemDto.md)

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

# **api_v1_front_profile_pet_id_cartes_places_pet_friendly_place_id_delete**
> WpResponse api_v1_front_profile_pet_id_cartes_places_pet_friendly_place_id_delete(pet_id, place_id)

Error codes : 
  - PET_FRIENDLY_LOCATION_NOT_CREATED_BY_USER: 

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
    api_instance = wizipet_api.FrontCarteApi(api_client)
    pet_id = 'pet_id_example' # str | 
    place_id = 'place_id_example' # str | 

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_cartes_places_pet_friendly_place_id_delete(pet_id, place_id)
        print("The response of FrontCarteApi->api_v1_front_profile_pet_id_cartes_places_pet_friendly_place_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontCarteApi->api_v1_front_profile_pet_id_cartes_places_pet_friendly_place_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **str**|  | 
 **place_id** | **str**|  | 

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_front_profile_pet_id_cartes_places_pet_friendly_place_id_patch**
> WpResponseCreateReplyDto api_v1_front_profile_pet_id_cartes_places_pet_friendly_place_id_patch(pet_id, place_id, cartes_post_pet_friendly_location_param_dto=cartes_post_pet_friendly_location_param_dto)

Error codes : 
  - PET_FRIENDLY_LOCATION_NO_ADDRESS_FOUND: Aucune adresse n'a pu être obtenue avec la position indiquée.
  - PET_FRIENDLY_LOCATION_NO_POSITION_FOUND: Aucune position n'a pu être obtenue avec l'adresse indiquée.
  - INVALID_MEDIA_REFERENCE: 
  - TEXT_TOO_LONG: 

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.cartes_post_pet_friendly_location_param_dto import CartesPostPetFriendlyLocationParamDto
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
    api_instance = wizipet_api.FrontCarteApi(api_client)
    pet_id = 'pet_id_example' # str | 
    place_id = 'place_id_example' # str | 
    cartes_post_pet_friendly_location_param_dto = wizipet_api.CartesPostPetFriendlyLocationParamDto() # CartesPostPetFriendlyLocationParamDto |  (optional)

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_cartes_places_pet_friendly_place_id_patch(pet_id, place_id, cartes_post_pet_friendly_location_param_dto=cartes_post_pet_friendly_location_param_dto)
        print("The response of FrontCarteApi->api_v1_front_profile_pet_id_cartes_places_pet_friendly_place_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontCarteApi->api_v1_front_profile_pet_id_cartes_places_pet_friendly_place_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **str**|  | 
 **place_id** | **str**|  | 
 **cartes_post_pet_friendly_location_param_dto** | [**CartesPostPetFriendlyLocationParamDto**](CartesPostPetFriendlyLocationParamDto.md)|  | [optional] 

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_front_profile_pet_id_cartes_places_pet_friendly_place_id_post**
> WpResponseCreateReplyDto api_v1_front_profile_pet_id_cartes_places_pet_friendly_place_id_post(pet_id, place_id, star_rating=star_rating)



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
    api_instance = wizipet_api.FrontCarteApi(api_client)
    pet_id = 'pet_id_example' # str | 
    place_id = 'place_id_example' # str | 
    star_rating = 3.4 # float |  (optional)

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_cartes_places_pet_friendly_place_id_post(pet_id, place_id, star_rating=star_rating)
        print("The response of FrontCarteApi->api_v1_front_profile_pet_id_cartes_places_pet_friendly_place_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontCarteApi->api_v1_front_profile_pet_id_cartes_places_pet_friendly_place_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **str**|  | 
 **place_id** | **str**|  | 
 **star_rating** | **float**|  | [optional] 

### Return type

[**WpResponseCreateReplyDto**](WpResponseCreateReplyDto.md)

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

# **api_v1_front_profile_pet_id_cartes_places_pet_friendly_post**
> WpResponseCreateReplyDto api_v1_front_profile_pet_id_cartes_places_pet_friendly_post(pet_id, cartes_post_pet_friendly_location_param_dto=cartes_post_pet_friendly_location_param_dto)

Error codes : 
  - PET_FRIENDLY_LOCATION_NO_ADDRESS_FOUND: Aucune adresse n'a pu être obtenue avec la position indiquée.
  - PET_FRIENDLY_LOCATION_NO_POSITION_FOUND: Aucune position n'a pu être obtenue avec l'adresse indiquée.
  - INVALID_MEDIA_REFERENCE: 
  - TEXT_TOO_LONG: 

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.cartes_post_pet_friendly_location_param_dto import CartesPostPetFriendlyLocationParamDto
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
    api_instance = wizipet_api.FrontCarteApi(api_client)
    pet_id = 'pet_id_example' # str | 
    cartes_post_pet_friendly_location_param_dto = wizipet_api.CartesPostPetFriendlyLocationParamDto() # CartesPostPetFriendlyLocationParamDto |  (optional)

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_cartes_places_pet_friendly_post(pet_id, cartes_post_pet_friendly_location_param_dto=cartes_post_pet_friendly_location_param_dto)
        print("The response of FrontCarteApi->api_v1_front_profile_pet_id_cartes_places_pet_friendly_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontCarteApi->api_v1_front_profile_pet_id_cartes_places_pet_friendly_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **str**|  | 
 **cartes_post_pet_friendly_location_param_dto** | [**CartesPostPetFriendlyLocationParamDto**](CartesPostPetFriendlyLocationParamDto.md)|  | [optional] 

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

