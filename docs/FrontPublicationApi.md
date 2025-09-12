# wizipet_api.FrontPublicationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_front_profile_pet_id_groups_publications_get**](FrontPublicationApi.md#api_v1_front_profile_pet_id_groups_publications_get) | **GET** /api/v1/front/profile/{pet_id}/groups/publications | 
[**api_v1_front_profile_pet_id_publications_get**](FrontPublicationApi.md#api_v1_front_profile_pet_id_publications_get) | **GET** /api/v1/front/profile/{pet_id}/publications | 
[**api_v1_front_profile_pet_id_publications_likes_post**](FrontPublicationApi.md#api_v1_front_profile_pet_id_publications_likes_post) | **POST** /api/v1/front/profile/{pet_id}/publications/likes | 
[**api_v1_front_profile_pet_id_publications_post**](FrontPublicationApi.md#api_v1_front_profile_pet_id_publications_post) | **POST** /api/v1/front/profile/{pet_id}/publications | 
[**api_v1_front_profile_pet_id_publications_publication_id_delete**](FrontPublicationApi.md#api_v1_front_profile_pet_id_publications_publication_id_delete) | **DELETE** /api/v1/front/profile/{pet_id}/publications/{publication_id} | 
[**api_v1_front_profile_pet_id_publications_publication_id_get**](FrontPublicationApi.md#api_v1_front_profile_pet_id_publications_publication_id_get) | **GET** /api/v1/front/profile/{pet_id}/publications/{publication_id} | 
[**api_v1_front_profile_pet_id_publications_publication_id_like_put**](FrontPublicationApi.md#api_v1_front_profile_pet_id_publications_publication_id_like_put) | **PUT** /api/v1/front/profile/{pet_id}/publications/{publication_id}/like | 
[**api_v1_front_profile_pet_id_publications_publication_id_report_post**](FrontPublicationApi.md#api_v1_front_profile_pet_id_publications_publication_id_report_post) | **POST** /api/v1/front/profile/{pet_id}/publications/{publication_id}/report | 
[**api_v1_front_profile_pet_id_publications_publication_id_share_post**](FrontPublicationApi.md#api_v1_front_profile_pet_id_publications_publication_id_share_post) | **POST** /api/v1/front/profile/{pet_id}/publications/{publication_id}/share | Déclare qu&#39;un nouveau partage de la publication à eu lieu.


# **api_v1_front_profile_pet_id_groups_publications_get**
> ResumableListResponsePublicationsPublicationItemDto api_v1_front_profile_pet_id_groups_publications_get(pet_id, continuation_token=continuation_token)



### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.resumable_list_response_publications_publication_item_dto import ResumableListResponsePublicationsPublicationItemDto
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
    api_instance = wizipet_api.FrontPublicationApi(api_client)
    pet_id = 'pet_id_example' # str | 
    continuation_token = 'continuation_token_example' # str |  (optional)

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_groups_publications_get(pet_id, continuation_token=continuation_token)
        print("The response of FrontPublicationApi->api_v1_front_profile_pet_id_groups_publications_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontPublicationApi->api_v1_front_profile_pet_id_groups_publications_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **str**|  | 
 **continuation_token** | **str**|  | [optional] 

### Return type

[**ResumableListResponsePublicationsPublicationItemDto**](ResumableListResponsePublicationsPublicationItemDto.md)

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

# **api_v1_front_profile_pet_id_publications_get**
> PublicationsPublicationsResumableListDto api_v1_front_profile_pet_id_publications_get(pet_id, search=search, with_media=with_media, group_id=group_id, continuation_token=continuation_token, author_id=author_id, on_challenge_feed=on_challenge_feed)



### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.publications_publications_resumable_list_dto import PublicationsPublicationsResumableListDto
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
    api_instance = wizipet_api.FrontPublicationApi(api_client)
    pet_id = 'pet_id_example' # str | 
    search = 'search_example' # str |  (optional)
    with_media = True # bool |  (optional)
    group_id = 'group_id_example' # str |  (optional)
    continuation_token = 'continuation_token_example' # str |  (optional)
    author_id = 'author_id_example' # str |  (optional)
    on_challenge_feed = True # bool |  (optional)

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_publications_get(pet_id, search=search, with_media=with_media, group_id=group_id, continuation_token=continuation_token, author_id=author_id, on_challenge_feed=on_challenge_feed)
        print("The response of FrontPublicationApi->api_v1_front_profile_pet_id_publications_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontPublicationApi->api_v1_front_profile_pet_id_publications_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **str**|  | 
 **search** | **str**|  | [optional] 
 **with_media** | **bool**|  | [optional] 
 **group_id** | **str**|  | [optional] 
 **continuation_token** | **str**|  | [optional] 
 **author_id** | **str**|  | [optional] 
 **on_challenge_feed** | **bool**|  | [optional] 

### Return type

[**PublicationsPublicationsResumableListDto**](PublicationsPublicationsResumableListDto.md)

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

# **api_v1_front_profile_pet_id_publications_likes_post**
> WpResponseCommonListPetLikesDto api_v1_front_profile_pet_id_publications_likes_post(pet_id, common_list_pet_likes_dto=common_list_pet_likes_dto)



### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.common_list_pet_likes_dto import CommonListPetLikesDto
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
    api_instance = wizipet_api.FrontPublicationApi(api_client)
    pet_id = 'pet_id_example' # str | 
    common_list_pet_likes_dto = wizipet_api.CommonListPetLikesDto() # CommonListPetLikesDto |  (optional)

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_publications_likes_post(pet_id, common_list_pet_likes_dto=common_list_pet_likes_dto)
        print("The response of FrontPublicationApi->api_v1_front_profile_pet_id_publications_likes_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontPublicationApi->api_v1_front_profile_pet_id_publications_likes_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **str**|  | 
 **common_list_pet_likes_dto** | [**CommonListPetLikesDto**](CommonListPetLikesDto.md)|  | [optional] 

### Return type

[**WpResponseCommonListPetLikesDto**](WpResponseCommonListPetLikesDto.md)

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

# **api_v1_front_profile_pet_id_publications_post**
> WpResponseCreateReplyDto api_v1_front_profile_pet_id_publications_post(pet_id, publications_post_publication_dto=publications_post_publication_dto)

Error codes : 
  - TOO_MANY_MEDIA: 
  - INVALID_MEDIA_REFERENCE: 
  - TEXT_TOO_LONG: 
  - GROUP_PUBLICATION_REQUIRES_ABONNEMENT: Seuls les abonnés d'un groupe peuvent effectuer des publications dans ce groupe
  - INVALID_GROUP_REFERENCE: 

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.publications_post_publication_dto import PublicationsPostPublicationDto
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
    api_instance = wizipet_api.FrontPublicationApi(api_client)
    pet_id = 'pet_id_example' # str | 
    publications_post_publication_dto = wizipet_api.PublicationsPostPublicationDto() # PublicationsPostPublicationDto |  (optional)

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_publications_post(pet_id, publications_post_publication_dto=publications_post_publication_dto)
        print("The response of FrontPublicationApi->api_v1_front_profile_pet_id_publications_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontPublicationApi->api_v1_front_profile_pet_id_publications_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **str**|  | 
 **publications_post_publication_dto** | [**PublicationsPostPublicationDto**](PublicationsPostPublicationDto.md)|  | [optional] 

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

# **api_v1_front_profile_pet_id_publications_publication_id_delete**
> WpResponse api_v1_front_profile_pet_id_publications_publication_id_delete(publication_id, pet_id)

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
    api_instance = wizipet_api.FrontPublicationApi(api_client)
    publication_id = 'publication_id_example' # str | 
    pet_id = 'pet_id_example' # str | 

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_publications_publication_id_delete(publication_id, pet_id)
        print("The response of FrontPublicationApi->api_v1_front_profile_pet_id_publications_publication_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontPublicationApi->api_v1_front_profile_pet_id_publications_publication_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **publication_id** | **str**|  | 
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
**404** | Not Found |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_front_profile_pet_id_publications_publication_id_get**
> PublicationsPublicationItemDto api_v1_front_profile_pet_id_publications_publication_id_get(publication_id, pet_id)



### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.publications_publication_item_dto import PublicationsPublicationItemDto
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
    api_instance = wizipet_api.FrontPublicationApi(api_client)
    publication_id = 'publication_id_example' # str | 
    pet_id = 'pet_id_example' # str | 

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_publications_publication_id_get(publication_id, pet_id)
        print("The response of FrontPublicationApi->api_v1_front_profile_pet_id_publications_publication_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontPublicationApi->api_v1_front_profile_pet_id_publications_publication_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **publication_id** | **str**|  | 
 **pet_id** | **str**|  | 

### Return type

[**PublicationsPublicationItemDto**](PublicationsPublicationItemDto.md)

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

# **api_v1_front_profile_pet_id_publications_publication_id_like_put**
> WpResponseCommonItemLikeDto api_v1_front_profile_pet_id_publications_publication_id_like_put(pet_id, publication_id, liked=liked)



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
    api_instance = wizipet_api.FrontPublicationApi(api_client)
    pet_id = 'pet_id_example' # str | 
    publication_id = 'publication_id_example' # str | 
    liked = True # bool |  (optional)

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_publications_publication_id_like_put(pet_id, publication_id, liked=liked)
        print("The response of FrontPublicationApi->api_v1_front_profile_pet_id_publications_publication_id_like_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontPublicationApi->api_v1_front_profile_pet_id_publications_publication_id_like_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **str**|  | 
 **publication_id** | **str**|  | 
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

# **api_v1_front_profile_pet_id_publications_publication_id_report_post**
> WpResponse api_v1_front_profile_pet_id_publications_publication_id_report_post(pet_id, publication_id)



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
    api_instance = wizipet_api.FrontPublicationApi(api_client)
    pet_id = 'pet_id_example' # str | 
    publication_id = 'publication_id_example' # str | 

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_publications_publication_id_report_post(pet_id, publication_id)
        print("The response of FrontPublicationApi->api_v1_front_profile_pet_id_publications_publication_id_report_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontPublicationApi->api_v1_front_profile_pet_id_publications_publication_id_report_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_front_profile_pet_id_publications_publication_id_share_post**
> WpResponse api_v1_front_profile_pet_id_publications_publication_id_share_post(pet_id, publication_id)

Déclare qu'un nouveau partage de la publication à eu lieu.



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
    api_instance = wizipet_api.FrontPublicationApi(api_client)
    pet_id = 'pet_id_example' # str | 
    publication_id = 'publication_id_example' # str | 

    try:
        # Déclare qu'un nouveau partage de la publication à eu lieu.
        api_response = await api_instance.api_v1_front_profile_pet_id_publications_publication_id_share_post(pet_id, publication_id)
        print("The response of FrontPublicationApi->api_v1_front_profile_pet_id_publications_publication_id_share_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontPublicationApi->api_v1_front_profile_pet_id_publications_publication_id_share_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

