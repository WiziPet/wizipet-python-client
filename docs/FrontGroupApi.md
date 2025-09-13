# wizipet_api.FrontGroupApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_front_groups_group_id_patch**](FrontGroupApi.md#api_v1_front_groups_group_id_patch) | **PATCH** /api/v1/front/groups/{group_id} | 
[**api_v1_front_profile_pet_id_groups_get**](FrontGroupApi.md#api_v1_front_profile_pet_id_groups_get) | **GET** /api/v1/front/profile/{pet_id}/groups | 
[**api_v1_front_profile_pet_id_groups_group_id_abonnement_delete**](FrontGroupApi.md#api_v1_front_profile_pet_id_groups_group_id_abonnement_delete) | **DELETE** /api/v1/front/profile/{pet_id}/groups/{group_id}/abonnement | 
[**api_v1_front_profile_pet_id_groups_group_id_abonnement_put**](FrontGroupApi.md#api_v1_front_profile_pet_id_groups_group_id_abonnement_put) | **PUT** /api/v1/front/profile/{pet_id}/groups/{group_id}/abonnement | 
[**api_v1_front_profile_pet_id_groups_group_id_get**](FrontGroupApi.md#api_v1_front_profile_pet_id_groups_group_id_get) | **GET** /api/v1/front/profile/{pet_id}/groups/{group_id} | 
[**api_v1_front_profile_pet_id_groups_post**](FrontGroupApi.md#api_v1_front_profile_pet_id_groups_post) | **POST** /api/v1/front/profile/{pet_id}/groups | 


# **api_v1_front_groups_group_id_patch**
> WpResponse api_v1_front_groups_group_id_patch(group_id, groups_update_group_dto=groups_update_group_dto)

Error codes : 
  - TEXT_TOO_LONG: 
  - INVALID_MEDIA_REFERENCE: 

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.groups_update_group_dto import GroupsUpdateGroupDto
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
    api_instance = wizipet_api.FrontGroupApi(api_client)
    group_id = 'group_id_example' # str | 
    groups_update_group_dto = wizipet_api.GroupsUpdateGroupDto() # GroupsUpdateGroupDto |  (optional)

    try:
        api_response = await api_instance.api_v1_front_groups_group_id_patch(group_id, groups_update_group_dto=groups_update_group_dto)
        print("The response of FrontGroupApi->api_v1_front_groups_group_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontGroupApi->api_v1_front_groups_group_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 
 **groups_update_group_dto** | [**GroupsUpdateGroupDto**](GroupsUpdateGroupDto.md)|  | [optional] 

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

# **api_v1_front_profile_pet_id_groups_get**
> WpListResponseGroupsGroupItemDto api_v1_front_profile_pet_id_groups_get(pet_id)



### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.wp_list_response_groups_group_item_dto import WpListResponseGroupsGroupItemDto
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
    api_instance = wizipet_api.FrontGroupApi(api_client)
    pet_id = 'pet_id_example' # str | 

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_groups_get(pet_id)
        print("The response of FrontGroupApi->api_v1_front_profile_pet_id_groups_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontGroupApi->api_v1_front_profile_pet_id_groups_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **str**|  | 

### Return type

[**WpListResponseGroupsGroupItemDto**](WpListResponseGroupsGroupItemDto.md)

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

# **api_v1_front_profile_pet_id_groups_group_id_abonnement_delete**
> WpResponse api_v1_front_profile_pet_id_groups_group_id_abonnement_delete(pet_id, group_id)



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
    api_instance = wizipet_api.FrontGroupApi(api_client)
    pet_id = 'pet_id_example' # str | 
    group_id = 'group_id_example' # str | 

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_groups_group_id_abonnement_delete(pet_id, group_id)
        print("The response of FrontGroupApi->api_v1_front_profile_pet_id_groups_group_id_abonnement_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontGroupApi->api_v1_front_profile_pet_id_groups_group_id_abonnement_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **str**|  | 
 **group_id** | **str**|  | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_front_profile_pet_id_groups_group_id_abonnement_put**
> WpResponse api_v1_front_profile_pet_id_groups_group_id_abonnement_put(pet_id, group_id)



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
    api_instance = wizipet_api.FrontGroupApi(api_client)
    pet_id = 'pet_id_example' # str | 
    group_id = 'group_id_example' # str | 

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_groups_group_id_abonnement_put(pet_id, group_id)
        print("The response of FrontGroupApi->api_v1_front_profile_pet_id_groups_group_id_abonnement_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontGroupApi->api_v1_front_profile_pet_id_groups_group_id_abonnement_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **str**|  | 
 **group_id** | **str**|  | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_front_profile_pet_id_groups_group_id_get**
> GroupsGroupDto api_v1_front_profile_pet_id_groups_group_id_get(pet_id, group_id)



### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.groups_group_dto import GroupsGroupDto
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
    api_instance = wizipet_api.FrontGroupApi(api_client)
    pet_id = 'pet_id_example' # str | 
    group_id = 'group_id_example' # str | 

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_groups_group_id_get(pet_id, group_id)
        print("The response of FrontGroupApi->api_v1_front_profile_pet_id_groups_group_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontGroupApi->api_v1_front_profile_pet_id_groups_group_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **str**|  | 
 **group_id** | **str**|  | 

### Return type

[**GroupsGroupDto**](GroupsGroupDto.md)

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

# **api_v1_front_profile_pet_id_groups_post**
> WpResponse api_v1_front_profile_pet_id_groups_post(pet_id, groups_create_group_dto=groups_create_group_dto)

Error codes : 
  - TEXT_TOO_LONG: 
  - PET_UNOWNED: You are trying to make an action as a profile you are not owning
  - GROUP_NAME_MUST_BE_UNIQUE: 
  - INVALID_MEDIA_REFERENCE: 

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.groups_create_group_dto import GroupsCreateGroupDto
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
    api_instance = wizipet_api.FrontGroupApi(api_client)
    pet_id = 'pet_id_example' # str | 
    groups_create_group_dto = wizipet_api.GroupsCreateGroupDto() # GroupsCreateGroupDto |  (optional)

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_groups_post(pet_id, groups_create_group_dto=groups_create_group_dto)
        print("The response of FrontGroupApi->api_v1_front_profile_pet_id_groups_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontGroupApi->api_v1_front_profile_pet_id_groups_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **str**|  | 
 **groups_create_group_dto** | [**GroupsCreateGroupDto**](GroupsCreateGroupDto.md)|  | [optional] 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

