# wizipet_api.FrontProfileApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_front_profile_list_get**](FrontProfileApi.md#api_v1_front_profile_list_get) | **GET** /api/v1/front/profile/list | 
[**api_v1_front_profile_pet_id_delete**](FrontProfileApi.md#api_v1_front_profile_pet_id_delete) | **DELETE** /api/v1/front/profile/{pet_id} | 
[**api_v1_front_profile_pet_id_get**](FrontProfileApi.md#api_v1_front_profile_pet_id_get) | **GET** /api/v1/front/profile/{pet_id} | 
[**api_v1_front_profile_pet_id_other_profile_get**](FrontProfileApi.md#api_v1_front_profile_pet_id_other_profile_get) | **GET** /api/v1/front/profile/{pet_id}/other_profile | 
[**api_v1_front_profile_pet_id_other_profile_resume_get**](FrontProfileApi.md#api_v1_front_profile_pet_id_other_profile_resume_get) | **GET** /api/v1/front/profile/{pet_id}/other_profile/resume | 
[**api_v1_front_profile_pet_id_other_profile_target_pet_id_get**](FrontProfileApi.md#api_v1_front_profile_pet_id_other_profile_target_pet_id_get) | **GET** /api/v1/front/profile/{pet_id}/other_profile/{target_pet_id} | 
[**api_v1_front_profile_pet_id_other_profile_target_pet_id_ignore_patch**](FrontProfileApi.md#api_v1_front_profile_pet_id_other_profile_target_pet_id_ignore_patch) | **PATCH** /api/v1/front/profile/{pet_id}/other_profile/{target_pet_id}/ignore | 
[**api_v1_front_profile_pet_id_patch**](FrontProfileApi.md#api_v1_front_profile_pet_id_patch) | **PATCH** /api/v1/front/profile/{pet_id} | 
[**api_v1_front_profile_post**](FrontProfileApi.md#api_v1_front_profile_post) | **POST** /api/v1/front/profile | 
[**api_v1_front_races_get**](FrontProfileApi.md#api_v1_front_races_get) | **GET** /api/v1/front/races | 


# **api_v1_front_profile_list_get**
> WpResponseProfilesMyProfilesListDto api_v1_front_profile_list_get()



### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.wp_response_profiles_my_profiles_list_dto import WpResponseProfilesMyProfilesListDto
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
    api_instance = wizipet_api.FrontProfileApi(api_client)

    try:
        api_response = await api_instance.api_v1_front_profile_list_get()
        print("The response of FrontProfileApi->api_v1_front_profile_list_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontProfileApi->api_v1_front_profile_list_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**WpResponseProfilesMyProfilesListDto**](WpResponseProfilesMyProfilesListDto.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_front_profile_pet_id_delete**
> WpResponse api_v1_front_profile_pet_id_delete(pet_id)

Error codes : 
  - PROFILE_NOT_FOUND: 
  - PET_UNOWNED: 
  - LAST_PET_PROFILE_NOT_DELETABLE: 

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
    api_instance = wizipet_api.FrontProfileApi(api_client)
    pet_id = 'pet_id_example' # str | 

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_delete(pet_id)
        print("The response of FrontProfileApi->api_v1_front_profile_pet_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontProfileApi->api_v1_front_profile_pet_id_delete: %s\n" % e)
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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_front_profile_pet_id_get**
> WpResponseProfilesMyProfileItemDto api_v1_front_profile_pet_id_get(pet_id)



### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.wp_response_profiles_my_profile_item_dto import WpResponseProfilesMyProfileItemDto
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
    api_instance = wizipet_api.FrontProfileApi(api_client)
    pet_id = 'pet_id_example' # str | 

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_get(pet_id)
        print("The response of FrontProfileApi->api_v1_front_profile_pet_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontProfileApi->api_v1_front_profile_pet_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **str**|  | 

### Return type

[**WpResponseProfilesMyProfileItemDto**](WpResponseProfilesMyProfileItemDto.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_front_profile_pet_id_other_profile_get**
> ProfilesOtherProfilesListDto api_v1_front_profile_pet_id_other_profile_get(pet_id, group_id=group_id, search=search, is_contact=is_contact)

Error codes : 
  - INVALID_GROUP_REFERENCE: 
  - IS_CONTACT_FALSE_NOT_SUPPORTED: Le paramètre is_contact = false n'est pas pris en charge

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.profiles_other_profiles_list_dto import ProfilesOtherProfilesListDto
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
    api_instance = wizipet_api.FrontProfileApi(api_client)
    pet_id = 'pet_id_example' # str | 
    group_id = 'group_id_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    is_contact = True # bool | Seules les valeurs ```true```,```null``` sont supportées.              ```true``` ne retourne que les demandes reçues et les demandes validées. (optional)

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_other_profile_get(pet_id, group_id=group_id, search=search, is_contact=is_contact)
        print("The response of FrontProfileApi->api_v1_front_profile_pet_id_other_profile_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontProfileApi->api_v1_front_profile_pet_id_other_profile_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **str**|  | 
 **group_id** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 
 **is_contact** | **bool**| Seules les valeurs &#x60;&#x60;&#x60;true&#x60;&#x60;&#x60;,&#x60;&#x60;&#x60;null&#x60;&#x60;&#x60; sont supportées.              &#x60;&#x60;&#x60;true&#x60;&#x60;&#x60; ne retourne que les demandes reçues et les demandes validées. | [optional] 

### Return type

[**ProfilesOtherProfilesListDto**](ProfilesOtherProfilesListDto.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_front_profile_pet_id_other_profile_resume_get**
> ProfilesOtherProfilesListDto api_v1_front_profile_pet_id_other_profile_resume_get(pet_id, continuation_token=continuation_token)

Error codes : 
  - INVALID_GROUP_REFERENCE: 

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.profiles_other_profiles_list_dto import ProfilesOtherProfilesListDto
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
    api_instance = wizipet_api.FrontProfileApi(api_client)
    pet_id = 'pet_id_example' # str | 
    continuation_token = 'continuation_token_example' # str |  (optional)

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_other_profile_resume_get(pet_id, continuation_token=continuation_token)
        print("The response of FrontProfileApi->api_v1_front_profile_pet_id_other_profile_resume_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontProfileApi->api_v1_front_profile_pet_id_other_profile_resume_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **str**|  | 
 **continuation_token** | **str**|  | [optional] 

### Return type

[**ProfilesOtherProfilesListDto**](ProfilesOtherProfilesListDto.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_front_profile_pet_id_other_profile_target_pet_id_get**
> WpResponseProfilesOtherProfileDto api_v1_front_profile_pet_id_other_profile_target_pet_id_get(pet_id, target_pet_id)



### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.wp_response_profiles_other_profile_dto import WpResponseProfilesOtherProfileDto
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
    api_instance = wizipet_api.FrontProfileApi(api_client)
    pet_id = 'pet_id_example' # str | 
    target_pet_id = 'target_pet_id_example' # str | 

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_other_profile_target_pet_id_get(pet_id, target_pet_id)
        print("The response of FrontProfileApi->api_v1_front_profile_pet_id_other_profile_target_pet_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontProfileApi->api_v1_front_profile_pet_id_other_profile_target_pet_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **str**|  | 
 **target_pet_id** | **str**|  | 

### Return type

[**WpResponseProfilesOtherProfileDto**](WpResponseProfilesOtherProfileDto.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_front_profile_pet_id_other_profile_target_pet_id_ignore_patch**
> WpResponse api_v1_front_profile_pet_id_other_profile_target_pet_id_ignore_patch(pet_id, target_pet_id, is_ignored=is_ignored)

Error codes : 
  - PET_UNOWNED: 

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
    api_instance = wizipet_api.FrontProfileApi(api_client)
    pet_id = 'pet_id_example' # str | 
    target_pet_id = 'target_pet_id_example' # str | 
    is_ignored = True # bool |  (optional)

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_other_profile_target_pet_id_ignore_patch(pet_id, target_pet_id, is_ignored=is_ignored)
        print("The response of FrontProfileApi->api_v1_front_profile_pet_id_other_profile_target_pet_id_ignore_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontProfileApi->api_v1_front_profile_pet_id_other_profile_target_pet_id_ignore_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **str**|  | 
 **target_pet_id** | **str**|  | 
 **is_ignored** | **bool**|  | [optional] 

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_front_profile_pet_id_patch**
> WpResponse api_v1_front_profile_pet_id_patch(pet_id, profiles_patch_profile_dto=profiles_patch_profile_dto)

Error codes : 
  - PROFILE_PICTURE_NOT_FOUND: 
  - PET_UNOWNED: 
  - TEXT_TOO_LONG: 

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.profiles_patch_profile_dto import ProfilesPatchProfileDto
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
    api_instance = wizipet_api.FrontProfileApi(api_client)
    pet_id = 'pet_id_example' # str | 
    profiles_patch_profile_dto = wizipet_api.ProfilesPatchProfileDto() # ProfilesPatchProfileDto |  (optional)

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_patch(pet_id, profiles_patch_profile_dto=profiles_patch_profile_dto)
        print("The response of FrontProfileApi->api_v1_front_profile_pet_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontProfileApi->api_v1_front_profile_pet_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **str**|  | 
 **profiles_patch_profile_dto** | [**ProfilesPatchProfileDto**](ProfilesPatchProfileDto.md)|  | [optional] 

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

# **api_v1_front_profile_post**
> WpResponseCreateReplyDto api_v1_front_profile_post(profiles_pet_profile_request=profiles_pet_profile_request)

Error codes : 
  - PROFILE_PICTURE_NOT_FOUND: 
  - TEXT_TOO_LONG: 

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.profiles_pet_profile_request import ProfilesPetProfileRequest
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
    api_instance = wizipet_api.FrontProfileApi(api_client)
    profiles_pet_profile_request = wizipet_api.ProfilesPetProfileRequest() # ProfilesPetProfileRequest |  (optional)

    try:
        api_response = await api_instance.api_v1_front_profile_post(profiles_pet_profile_request=profiles_pet_profile_request)
        print("The response of FrontProfileApi->api_v1_front_profile_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontProfileApi->api_v1_front_profile_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profiles_pet_profile_request** | [**ProfilesPetProfileRequest**](ProfilesPetProfileRequest.md)|  | [optional] 

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

# **api_v1_front_races_get**
> WpListResponseProfilesPetRaceItemDto api_v1_front_races_get()



### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.wp_list_response_profiles_pet_race_item_dto import WpListResponseProfilesPetRaceItemDto
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
    api_instance = wizipet_api.FrontProfileApi(api_client)

    try:
        api_response = await api_instance.api_v1_front_races_get()
        print("The response of FrontProfileApi->api_v1_front_races_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontProfileApi->api_v1_front_races_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**WpListResponseProfilesPetRaceItemDto**](WpListResponseProfilesPetRaceItemDto.md)

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

