# wizipet_api.FrontAdsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_front_ads_sponsored_content_allowed_patch**](FrontAdsApi.md#api_v1_front_ads_sponsored_content_allowed_patch) | **PATCH** /api/v1/front/ads/sponsored_content_allowed | 
[**api_v1_front_profile_pet_id_ads_advertisement_id_post**](FrontAdsApi.md#api_v1_front_profile_pet_id_ads_advertisement_id_post) | **POST** /api/v1/front/profile/{pet_id}/ads/{advertisement_id} | 
[**api_v1_front_profile_pet_id_ads_get**](FrontAdsApi.md#api_v1_front_profile_pet_id_ads_get) | **GET** /api/v1/front/profile/{pet_id}/ads | 


# **api_v1_front_ads_sponsored_content_allowed_patch**
> WpResponse api_v1_front_ads_sponsored_content_allowed_patch(sponsored_content_allowed=sponsored_content_allowed)



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
    api_instance = wizipet_api.FrontAdsApi(api_client)
    sponsored_content_allowed = True # bool |  (optional)

    try:
        api_response = await api_instance.api_v1_front_ads_sponsored_content_allowed_patch(sponsored_content_allowed=sponsored_content_allowed)
        print("The response of FrontAdsApi->api_v1_front_ads_sponsored_content_allowed_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontAdsApi->api_v1_front_ads_sponsored_content_allowed_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sponsored_content_allowed** | **bool**|  | [optional] 

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

# **api_v1_front_profile_pet_id_ads_advertisement_id_post**
> WpResponse api_v1_front_profile_pet_id_ads_advertisement_id_post(pet_id, advertisement_id)



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
    api_instance = wizipet_api.FrontAdsApi(api_client)
    pet_id = 'pet_id_example' # str | 
    advertisement_id = 'advertisement_id_example' # str | 

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_ads_advertisement_id_post(pet_id, advertisement_id)
        print("The response of FrontAdsApi->api_v1_front_profile_pet_id_ads_advertisement_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontAdsApi->api_v1_front_profile_pet_id_ads_advertisement_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **str**|  | 
 **advertisement_id** | **str**|  | 

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

# **api_v1_front_profile_pet_id_ads_get**
> List[AdvertisementsAdItemDto] api_v1_front_profile_pet_id_ads_get(pet_id)



### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.advertisements_ad_item_dto import AdvertisementsAdItemDto
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
    api_instance = wizipet_api.FrontAdsApi(api_client)
    pet_id = 'pet_id_example' # str | 

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_ads_get(pet_id)
        print("The response of FrontAdsApi->api_v1_front_profile_pet_id_ads_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontAdsApi->api_v1_front_profile_pet_id_ads_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **str**|  | 

### Return type

[**List[AdvertisementsAdItemDto]**](AdvertisementsAdItemDto.md)

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

