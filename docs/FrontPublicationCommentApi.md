# wizipet_api.FrontPublicationCommentApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_front_profile_pet_id_publications_publication_id_comments_comment_id_delete**](FrontPublicationCommentApi.md#api_v1_front_profile_pet_id_publications_publication_id_comments_comment_id_delete) | **DELETE** /api/v1/front/profile/{pet_id}/publications/{publication_id}/comments/{comment_id} | 
[**api_v1_front_profile_pet_id_publications_publication_id_comments_comment_id_like_put**](FrontPublicationCommentApi.md#api_v1_front_profile_pet_id_publications_publication_id_comments_comment_id_like_put) | **PUT** /api/v1/front/profile/{pet_id}/publications/{publication_id}/comments/{comment_id}/like | 
[**api_v1_front_profile_pet_id_publications_publication_id_comments_get**](FrontPublicationCommentApi.md#api_v1_front_profile_pet_id_publications_publication_id_comments_get) | **GET** /api/v1/front/profile/{pet_id}/publications/{publication_id}/comments | 
[**api_v1_front_profile_pet_id_publications_publication_id_comments_likes_get**](FrontPublicationCommentApi.md#api_v1_front_profile_pet_id_publications_publication_id_comments_likes_get) | **GET** /api/v1/front/profile/{pet_id}/publications/{publication_id}/comments/likes | 
[**api_v1_front_profile_pet_id_publications_publication_id_comments_post**](FrontPublicationCommentApi.md#api_v1_front_profile_pet_id_publications_publication_id_comments_post) | **POST** /api/v1/front/profile/{pet_id}/publications/{publication_id}/comments | 


# **api_v1_front_profile_pet_id_publications_publication_id_comments_comment_id_delete**
> WpResponse api_v1_front_profile_pet_id_publications_publication_id_comments_comment_id_delete(comment_id, pet_id, publication_id)

Error codes : 
  - CANNOT_DELETE_NOT_OWNED_ELEMENT: 

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
    api_instance = wizipet_api.FrontPublicationCommentApi(api_client)
    comment_id = 'comment_id_example' # str | 
    pet_id = 'pet_id_example' # str | 
    publication_id = 'publication_id_example' # str | 

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_publications_publication_id_comments_comment_id_delete(comment_id, pet_id, publication_id)
        print("The response of FrontPublicationCommentApi->api_v1_front_profile_pet_id_publications_publication_id_comments_comment_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontPublicationCommentApi->api_v1_front_profile_pet_id_publications_publication_id_comments_comment_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | **str**|  | 
 **pet_id** | **str**|  | 
 **publication_id** | **str**|  | 

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

# **api_v1_front_profile_pet_id_publications_publication_id_comments_comment_id_like_put**
> WpResponseCommonItemLikeDto api_v1_front_profile_pet_id_publications_publication_id_comments_comment_id_like_put(pet_id, publication_id, comment_id, liked=liked)



### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.wp_response_common_item_like_dto import WpResponseCommonItemLikeDto
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
    api_instance = wizipet_api.FrontPublicationCommentApi(api_client)
    pet_id = 'pet_id_example' # str | 
    publication_id = 'publication_id_example' # str | 
    comment_id = 'comment_id_example' # str | 
    liked = True # bool |  (optional)

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_publications_publication_id_comments_comment_id_like_put(pet_id, publication_id, comment_id, liked=liked)
        print("The response of FrontPublicationCommentApi->api_v1_front_profile_pet_id_publications_publication_id_comments_comment_id_like_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontPublicationCommentApi->api_v1_front_profile_pet_id_publications_publication_id_comments_comment_id_like_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **str**|  | 
 **publication_id** | **str**|  | 
 **comment_id** | **str**|  | 
 **liked** | **bool**|  | [optional] 

### Return type

[**WpResponseCommonItemLikeDto**](WpResponseCommonItemLikeDto.md)

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

# **api_v1_front_profile_pet_id_publications_publication_id_comments_get**
> ResumableListResponsePublicationsCommentsPublicationCommentItemDto api_v1_front_profile_pet_id_publications_publication_id_comments_get(pet_id, publication_id, continuation_token=continuation_token)



### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.resumable_list_response_publications_comments_publication_comment_item_dto import ResumableListResponsePublicationsCommentsPublicationCommentItemDto
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
    api_instance = wizipet_api.FrontPublicationCommentApi(api_client)
    pet_id = 'pet_id_example' # str | 
    publication_id = 'publication_id_example' # str | 
    continuation_token = 'continuation_token_example' # str |  (optional)

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_publications_publication_id_comments_get(pet_id, publication_id, continuation_token=continuation_token)
        print("The response of FrontPublicationCommentApi->api_v1_front_profile_pet_id_publications_publication_id_comments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontPublicationCommentApi->api_v1_front_profile_pet_id_publications_publication_id_comments_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **str**|  | 
 **publication_id** | **str**|  | 
 **continuation_token** | **str**|  | [optional] 

### Return type

[**ResumableListResponsePublicationsCommentsPublicationCommentItemDto**](ResumableListResponsePublicationsCommentsPublicationCommentItemDto.md)

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

# **api_v1_front_profile_pet_id_publications_publication_id_comments_likes_get**
> WpResponseCommonListPetLikesDto api_v1_front_profile_pet_id_publications_publication_id_comments_likes_get(pet_id, publication_id)



### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.wp_response_common_list_pet_likes_dto import WpResponseCommonListPetLikesDto
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
    api_instance = wizipet_api.FrontPublicationCommentApi(api_client)
    pet_id = 'pet_id_example' # str | 
    publication_id = 'publication_id_example' # str | 

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_publications_publication_id_comments_likes_get(pet_id, publication_id)
        print("The response of FrontPublicationCommentApi->api_v1_front_profile_pet_id_publications_publication_id_comments_likes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontPublicationCommentApi->api_v1_front_profile_pet_id_publications_publication_id_comments_likes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **str**|  | 
 **publication_id** | **str**|  | 

### Return type

[**WpResponseCommonListPetLikesDto**](WpResponseCommonListPetLikesDto.md)

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

# **api_v1_front_profile_pet_id_publications_publication_id_comments_post**
> WpResponseCreateReplyDto api_v1_front_profile_pet_id_publications_publication_id_comments_post(pet_id, publication_id, common_comments_post_comment_dto=common_comments_post_comment_dto)

Error codes : 
  - TEXT_TOO_LONG: 

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.common_comments_post_comment_dto import CommonCommentsPostCommentDto
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
    api_instance = wizipet_api.FrontPublicationCommentApi(api_client)
    pet_id = 'pet_id_example' # str | 
    publication_id = 'publication_id_example' # str | 
    common_comments_post_comment_dto = wizipet_api.CommonCommentsPostCommentDto() # CommonCommentsPostCommentDto |  (optional)

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_publications_publication_id_comments_post(pet_id, publication_id, common_comments_post_comment_dto=common_comments_post_comment_dto)
        print("The response of FrontPublicationCommentApi->api_v1_front_profile_pet_id_publications_publication_id_comments_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontPublicationCommentApi->api_v1_front_profile_pet_id_publications_publication_id_comments_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **str**|  | 
 **publication_id** | **str**|  | 
 **common_comments_post_comment_dto** | [**CommonCommentsPostCommentDto**](CommonCommentsPostCommentDto.md)|  | [optional] 

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

