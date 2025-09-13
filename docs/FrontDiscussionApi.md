# wizipet_api.FrontDiscussionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_front_profile_pet_id_discussions_discussion_id_get**](FrontDiscussionApi.md#api_v1_front_profile_pet_id_discussions_discussion_id_get) | **GET** /api/v1/front/profile/{pet_id}/discussions/{discussion_id} | 
[**api_v1_front_profile_pet_id_discussions_discussion_id_is_archived_put**](FrontDiscussionApi.md#api_v1_front_profile_pet_id_discussions_discussion_id_is_archived_put) | **PUT** /api/v1/front/profile/{pet_id}/discussions/{discussion_id}/is_archived | 
[**api_v1_front_profile_pet_id_discussions_discussion_id_messages_get**](FrontDiscussionApi.md#api_v1_front_profile_pet_id_discussions_discussion_id_messages_get) | **GET** /api/v1/front/profile/{pet_id}/discussions/{discussion_id}/messages | 
[**api_v1_front_profile_pet_id_discussions_discussion_id_messages_post**](FrontDiscussionApi.md#api_v1_front_profile_pet_id_discussions_discussion_id_messages_post) | **POST** /api/v1/front/profile/{pet_id}/discussions/{discussion_id}/messages | 
[**api_v1_front_profile_pet_id_discussions_discussion_id_messages_read_put**](FrontDiscussionApi.md#api_v1_front_profile_pet_id_discussions_discussion_id_messages_read_put) | **PUT** /api/v1/front/profile/{pet_id}/discussions/{discussion_id}/messages/read | 
[**api_v1_front_profile_pet_id_discussions_discussion_id_messages_resume_get**](FrontDiscussionApi.md#api_v1_front_profile_pet_id_discussions_discussion_id_messages_resume_get) | **GET** /api/v1/front/profile/{pet_id}/discussions/{discussion_id}/messages/resume | 
[**api_v1_front_profile_pet_id_discussions_discussion_id_participants_me_delete**](FrontDiscussionApi.md#api_v1_front_profile_pet_id_discussions_discussion_id_participants_me_delete) | **DELETE** /api/v1/front/profile/{pet_id}/discussions/{discussion_id}/participants/me | 
[**api_v1_front_profile_pet_id_discussions_discussion_id_patch**](FrontDiscussionApi.md#api_v1_front_profile_pet_id_discussions_discussion_id_patch) | **PATCH** /api/v1/front/profile/{pet_id}/discussions/{discussion_id} | 
[**api_v1_front_profile_pet_id_discussions_get**](FrontDiscussionApi.md#api_v1_front_profile_pet_id_discussions_get) | **GET** /api/v1/front/profile/{pet_id}/discussions | 
[**api_v1_front_profile_pet_id_discussions_post**](FrontDiscussionApi.md#api_v1_front_profile_pet_id_discussions_post) | **POST** /api/v1/front/profile/{pet_id}/discussions | 


# **api_v1_front_profile_pet_id_discussions_discussion_id_get**
> WpResponseDiscussionsDiscussionDto api_v1_front_profile_pet_id_discussions_discussion_id_get(pet_id, discussion_id)

Error codes : 
  - PET_UNOWNED: You are trying to make an action as a profile you are not owning
  - PET_IS_NOT_A_PARTICIPANT: 

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.wp_response_discussions_discussion_dto import WpResponseDiscussionsDiscussionDto
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
    api_instance = wizipet_api.FrontDiscussionApi(api_client)
    pet_id = 'pet_id_example' # str | 
    discussion_id = 'discussion_id_example' # str | 

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_discussions_discussion_id_get(pet_id, discussion_id)
        print("The response of FrontDiscussionApi->api_v1_front_profile_pet_id_discussions_discussion_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontDiscussionApi->api_v1_front_profile_pet_id_discussions_discussion_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **str**|  | 
 **discussion_id** | **str**|  | 

### Return type

[**WpResponseDiscussionsDiscussionDto**](WpResponseDiscussionsDiscussionDto.md)

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

# **api_v1_front_profile_pet_id_discussions_discussion_id_is_archived_put**
> WpResponse api_v1_front_profile_pet_id_discussions_discussion_id_is_archived_put(pet_id, discussion_id, discussions_is_archived_dto=discussions_is_archived_dto)

Error codes : 
  - PET_UNOWNED: You are trying to make an action as a profile you are not owning
  - PET_IS_NOT_A_PARTICIPANT: 

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.discussions_is_archived_dto import DiscussionsIsArchivedDto
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
    api_instance = wizipet_api.FrontDiscussionApi(api_client)
    pet_id = 'pet_id_example' # str | 
    discussion_id = 'discussion_id_example' # str | 
    discussions_is_archived_dto = wizipet_api.DiscussionsIsArchivedDto() # DiscussionsIsArchivedDto |  (optional)

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_discussions_discussion_id_is_archived_put(pet_id, discussion_id, discussions_is_archived_dto=discussions_is_archived_dto)
        print("The response of FrontDiscussionApi->api_v1_front_profile_pet_id_discussions_discussion_id_is_archived_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontDiscussionApi->api_v1_front_profile_pet_id_discussions_discussion_id_is_archived_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **str**|  | 
 **discussion_id** | **str**|  | 
 **discussions_is_archived_dto** | [**DiscussionsIsArchivedDto**](DiscussionsIsArchivedDto.md)|  | [optional] 

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

# **api_v1_front_profile_pet_id_discussions_discussion_id_messages_get**
> ResumableListResponseDiscussionsMessageDto api_v1_front_profile_pet_id_discussions_discussion_id_messages_get(pet_id, discussion_id)

Error codes : 
  - PET_UNOWNED: You are trying to make an action as a profile you are not owning
  - PET_IS_NOT_A_PARTICIPANT: 

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.resumable_list_response_discussions_message_dto import ResumableListResponseDiscussionsMessageDto
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
    api_instance = wizipet_api.FrontDiscussionApi(api_client)
    pet_id = 'pet_id_example' # str | 
    discussion_id = 'discussion_id_example' # str | 

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_discussions_discussion_id_messages_get(pet_id, discussion_id)
        print("The response of FrontDiscussionApi->api_v1_front_profile_pet_id_discussions_discussion_id_messages_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontDiscussionApi->api_v1_front_profile_pet_id_discussions_discussion_id_messages_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **str**|  | 
 **discussion_id** | **str**|  | 

### Return type

[**ResumableListResponseDiscussionsMessageDto**](ResumableListResponseDiscussionsMessageDto.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_front_profile_pet_id_discussions_discussion_id_messages_post**
> WpResponse api_v1_front_profile_pet_id_discussions_discussion_id_messages_post(pet_id, discussion_id, discussions_post_message_dto=discussions_post_message_dto)

Error codes : 
  - TEXT_TOO_LONG: 
  - PET_UNOWNED: You are trying to make an action as a profile you are not owning
  - PET_IS_NOT_A_PARTICIPANT: 

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.discussions_post_message_dto import DiscussionsPostMessageDto
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
    api_instance = wizipet_api.FrontDiscussionApi(api_client)
    pet_id = 'pet_id_example' # str | 
    discussion_id = 'discussion_id_example' # str | 
    discussions_post_message_dto = wizipet_api.DiscussionsPostMessageDto() # DiscussionsPostMessageDto |  (optional)

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_discussions_discussion_id_messages_post(pet_id, discussion_id, discussions_post_message_dto=discussions_post_message_dto)
        print("The response of FrontDiscussionApi->api_v1_front_profile_pet_id_discussions_discussion_id_messages_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontDiscussionApi->api_v1_front_profile_pet_id_discussions_discussion_id_messages_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **str**|  | 
 **discussion_id** | **str**|  | 
 **discussions_post_message_dto** | [**DiscussionsPostMessageDto**](DiscussionsPostMessageDto.md)|  | [optional] 

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_front_profile_pet_id_discussions_discussion_id_messages_read_put**
> WpResponse api_v1_front_profile_pet_id_discussions_discussion_id_messages_read_put(pet_id, discussion_id, discussions_put_message_read_dto=discussions_put_message_read_dto)

Error codes : 
  - PET_UNOWNED: You are trying to make an action as a profile you are not owning
  - PET_IS_NOT_A_PARTICIPANT: 

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.discussions_put_message_read_dto import DiscussionsPutMessageReadDto
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
    api_instance = wizipet_api.FrontDiscussionApi(api_client)
    pet_id = 'pet_id_example' # str | 
    discussion_id = 'discussion_id_example' # str | 
    discussions_put_message_read_dto = wizipet_api.DiscussionsPutMessageReadDto() # DiscussionsPutMessageReadDto |  (optional)

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_discussions_discussion_id_messages_read_put(pet_id, discussion_id, discussions_put_message_read_dto=discussions_put_message_read_dto)
        print("The response of FrontDiscussionApi->api_v1_front_profile_pet_id_discussions_discussion_id_messages_read_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontDiscussionApi->api_v1_front_profile_pet_id_discussions_discussion_id_messages_read_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **str**|  | 
 **discussion_id** | **str**|  | 
 **discussions_put_message_read_dto** | [**DiscussionsPutMessageReadDto**](DiscussionsPutMessageReadDto.md)|  | [optional] 

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_front_profile_pet_id_discussions_discussion_id_messages_resume_get**
> ResumableListResponseDiscussionsMessageDto api_v1_front_profile_pet_id_discussions_discussion_id_messages_resume_get(pet_id, discussion_id, continuation_token=continuation_token)

Error codes : 
  - PET_UNOWNED: You are trying to make an action as a profile you are not owning
  - PET_IS_NOT_A_PARTICIPANT: 

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.resumable_list_response_discussions_message_dto import ResumableListResponseDiscussionsMessageDto
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
    api_instance = wizipet_api.FrontDiscussionApi(api_client)
    pet_id = 'pet_id_example' # str | 
    discussion_id = 'discussion_id_example' # str | 
    continuation_token = 'continuation_token_example' # str |  (optional)

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_discussions_discussion_id_messages_resume_get(pet_id, discussion_id, continuation_token=continuation_token)
        print("The response of FrontDiscussionApi->api_v1_front_profile_pet_id_discussions_discussion_id_messages_resume_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontDiscussionApi->api_v1_front_profile_pet_id_discussions_discussion_id_messages_resume_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **str**|  | 
 **discussion_id** | **str**|  | 
 **continuation_token** | **str**|  | [optional] 

### Return type

[**ResumableListResponseDiscussionsMessageDto**](ResumableListResponseDiscussionsMessageDto.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_front_profile_pet_id_discussions_discussion_id_participants_me_delete**
> WpResponse api_v1_front_profile_pet_id_discussions_discussion_id_participants_me_delete(pet_id, discussion_id)

Error codes : 
  - PET_UNOWNED: You are trying to make an action as a profile you are not owning
  - PET_IS_NOT_A_PARTICIPANT: 

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
    api_instance = wizipet_api.FrontDiscussionApi(api_client)
    pet_id = 'pet_id_example' # str | 
    discussion_id = 'discussion_id_example' # str | 

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_discussions_discussion_id_participants_me_delete(pet_id, discussion_id)
        print("The response of FrontDiscussionApi->api_v1_front_profile_pet_id_discussions_discussion_id_participants_me_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontDiscussionApi->api_v1_front_profile_pet_id_discussions_discussion_id_participants_me_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **str**|  | 
 **discussion_id** | **str**|  | 

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

# **api_v1_front_profile_pet_id_discussions_discussion_id_patch**
> WpResponse api_v1_front_profile_pet_id_discussions_discussion_id_patch(pet_id, discussion_id, discussions_patch_discussion_dto=discussions_patch_discussion_dto)

Error codes : 
  - PET_UNOWNED: You are trying to make an action as a profile you are not owning
  - PET_IS_NOT_A_PARTICIPANT: 
  - TEXT_TOO_LONG: 
  - INVALID_MEDIA_REFERENCE: 
  - INVALID_PET_REFERENCE: 

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.discussions_patch_discussion_dto import DiscussionsPatchDiscussionDto
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
    api_instance = wizipet_api.FrontDiscussionApi(api_client)
    pet_id = 'pet_id_example' # str | 
    discussion_id = 'discussion_id_example' # str | 
    discussions_patch_discussion_dto = wizipet_api.DiscussionsPatchDiscussionDto() # DiscussionsPatchDiscussionDto |  (optional)

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_discussions_discussion_id_patch(pet_id, discussion_id, discussions_patch_discussion_dto=discussions_patch_discussion_dto)
        print("The response of FrontDiscussionApi->api_v1_front_profile_pet_id_discussions_discussion_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontDiscussionApi->api_v1_front_profile_pet_id_discussions_discussion_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **str**|  | 
 **discussion_id** | **str**|  | 
 **discussions_patch_discussion_dto** | [**DiscussionsPatchDiscussionDto**](DiscussionsPatchDiscussionDto.md)|  | [optional] 

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

# **api_v1_front_profile_pet_id_discussions_get**
> WpListResponseDiscussionsDiscussionItemDto api_v1_front_profile_pet_id_discussions_get(pet_id)



### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.wp_list_response_discussions_discussion_item_dto import WpListResponseDiscussionsDiscussionItemDto
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
    api_instance = wizipet_api.FrontDiscussionApi(api_client)
    pet_id = 'pet_id_example' # str | 

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_discussions_get(pet_id)
        print("The response of FrontDiscussionApi->api_v1_front_profile_pet_id_discussions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontDiscussionApi->api_v1_front_profile_pet_id_discussions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **str**|  | 

### Return type

[**WpListResponseDiscussionsDiscussionItemDto**](WpListResponseDiscussionsDiscussionItemDto.md)

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

# **api_v1_front_profile_pet_id_discussions_post**
> DiscussionsCreateDiscussionResponse api_v1_front_profile_pet_id_discussions_post(pet_id, discussions_create_discussion_dto=discussions_create_discussion_dto)

Error codes : 
  - TEXT_TOO_LONG: 
  - PET_UNOWNED: You are trying to make an action as a profile you are not owning
  - NOT_ENOUGH_PARTICIPANTS: 
  - INVALID_MEDIA_REFERENCE: 

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.discussions_create_discussion_dto import DiscussionsCreateDiscussionDto
from wizipet_api.models.discussions_create_discussion_response import DiscussionsCreateDiscussionResponse
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
    api_instance = wizipet_api.FrontDiscussionApi(api_client)
    pet_id = 'pet_id_example' # str | 
    discussions_create_discussion_dto = wizipet_api.DiscussionsCreateDiscussionDto() # DiscussionsCreateDiscussionDto |  (optional)

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_discussions_post(pet_id, discussions_create_discussion_dto=discussions_create_discussion_dto)
        print("The response of FrontDiscussionApi->api_v1_front_profile_pet_id_discussions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontDiscussionApi->api_v1_front_profile_pet_id_discussions_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **str**|  | 
 **discussions_create_discussion_dto** | [**DiscussionsCreateDiscussionDto**](DiscussionsCreateDiscussionDto.md)|  | [optional] 

### Return type

[**DiscussionsCreateDiscussionResponse**](DiscussionsCreateDiscussionResponse.md)

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

