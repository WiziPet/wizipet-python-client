# wizipet_api.FrontEncyclopedieArticleApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_front_profile_pet_id_encyclopedie_articles_article_id_get**](FrontEncyclopedieArticleApi.md#api_v1_front_profile_pet_id_encyclopedie_articles_article_id_get) | **GET** /api/v1/front/profile/{pet_id}/encyclopedie/articles/{article_id} | 
[**api_v1_front_profile_pet_id_encyclopedie_articles_article_id_like_put**](FrontEncyclopedieArticleApi.md#api_v1_front_profile_pet_id_encyclopedie_articles_article_id_like_put) | **PUT** /api/v1/front/profile/{pet_id}/encyclopedie/articles/{article_id}/like | 
[**api_v1_front_profile_pet_id_encyclopedie_articles_get**](FrontEncyclopedieArticleApi.md#api_v1_front_profile_pet_id_encyclopedie_articles_get) | **GET** /api/v1/front/profile/{pet_id}/encyclopedie/articles | 
[**api_v1_front_profile_pet_id_encyclopedie_articles_likes_post**](FrontEncyclopedieArticleApi.md#api_v1_front_profile_pet_id_encyclopedie_articles_likes_post) | **POST** /api/v1/front/profile/{pet_id}/encyclopedie/articles/likes | 


# **api_v1_front_profile_pet_id_encyclopedie_articles_article_id_get**
> WpResponseEncyclopediesFrontArticleDto api_v1_front_profile_pet_id_encyclopedie_articles_article_id_get(article_id, pet_id)



### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.wp_response_encyclopedies_front_article_dto import WpResponseEncyclopediesFrontArticleDto
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
    api_instance = wizipet_api.FrontEncyclopedieArticleApi(api_client)
    article_id = 'article_id_example' # str | 
    pet_id = 'pet_id_example' # str | 

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_encyclopedie_articles_article_id_get(article_id, pet_id)
        print("The response of FrontEncyclopedieArticleApi->api_v1_front_profile_pet_id_encyclopedie_articles_article_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontEncyclopedieArticleApi->api_v1_front_profile_pet_id_encyclopedie_articles_article_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **article_id** | **str**|  | 
 **pet_id** | **str**|  | 

### Return type

[**WpResponseEncyclopediesFrontArticleDto**](WpResponseEncyclopediesFrontArticleDto.md)

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

# **api_v1_front_profile_pet_id_encyclopedie_articles_article_id_like_put**
> WpResponseCommonItemLikeDto api_v1_front_profile_pet_id_encyclopedie_articles_article_id_like_put(pet_id, article_id, liked=liked)



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
    api_instance = wizipet_api.FrontEncyclopedieArticleApi(api_client)
    pet_id = 'pet_id_example' # str | 
    article_id = 'article_id_example' # str | 
    liked = True # bool |  (optional)

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_encyclopedie_articles_article_id_like_put(pet_id, article_id, liked=liked)
        print("The response of FrontEncyclopedieArticleApi->api_v1_front_profile_pet_id_encyclopedie_articles_article_id_like_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontEncyclopedieArticleApi->api_v1_front_profile_pet_id_encyclopedie_articles_article_id_like_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **str**|  | 
 **article_id** | **str**|  | 
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

# **api_v1_front_profile_pet_id_encyclopedie_articles_get**
> WpResponseResumableListResponseEncyclopediesArticleItemDto api_v1_front_profile_pet_id_encyclopedie_articles_get(pet_id, count=count, search=search, categorie=categorie, espece=espece, continuation_token=continuation_token, randomize=randomize)



### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.encyclopedies_unified_article_categorie_dto import EncyclopediesUnifiedArticleCategorieDto
from wizipet_api.models.profiles_espece_dto import ProfilesEspeceDto
from wizipet_api.models.wp_response_resumable_list_response_encyclopedies_article_item_dto import WpResponseResumableListResponseEncyclopediesArticleItemDto
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
    api_instance = wizipet_api.FrontEncyclopedieArticleApi(api_client)
    pet_id = 'pet_id_example' # str | 
    count = 56 # int |  (optional)
    search = 'search_example' # str |  (optional)
    categorie = wizipet_api.EncyclopediesUnifiedArticleCategorieDto() # EncyclopediesUnifiedArticleCategorieDto |  (optional)
    espece = wizipet_api.ProfilesEspeceDto() # ProfilesEspeceDto |  (optional)
    continuation_token = 'continuation_token_example' # str |  (optional)
    randomize = True # bool |  (optional)

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_encyclopedie_articles_get(pet_id, count=count, search=search, categorie=categorie, espece=espece, continuation_token=continuation_token, randomize=randomize)
        print("The response of FrontEncyclopedieArticleApi->api_v1_front_profile_pet_id_encyclopedie_articles_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontEncyclopedieArticleApi->api_v1_front_profile_pet_id_encyclopedie_articles_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **str**|  | 
 **count** | **int**|  | [optional] 
 **search** | **str**|  | [optional] 
 **categorie** | [**EncyclopediesUnifiedArticleCategorieDto**](.md)|  | [optional] 
 **espece** | [**ProfilesEspeceDto**](.md)|  | [optional] 
 **continuation_token** | **str**|  | [optional] 
 **randomize** | **bool**|  | [optional] 

### Return type

[**WpResponseResumableListResponseEncyclopediesArticleItemDto**](WpResponseResumableListResponseEncyclopediesArticleItemDto.md)

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
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_front_profile_pet_id_encyclopedie_articles_likes_post**
> WpResponseCommonListPetLikesDto api_v1_front_profile_pet_id_encyclopedie_articles_likes_post(pet_id, common_list_pet_likes_dto=common_list_pet_likes_dto)



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
    api_instance = wizipet_api.FrontEncyclopedieArticleApi(api_client)
    pet_id = 'pet_id_example' # str | 
    common_list_pet_likes_dto = wizipet_api.CommonListPetLikesDto() # CommonListPetLikesDto |  (optional)

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_encyclopedie_articles_likes_post(pet_id, common_list_pet_likes_dto=common_list_pet_likes_dto)
        print("The response of FrontEncyclopedieArticleApi->api_v1_front_profile_pet_id_encyclopedie_articles_likes_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontEncyclopedieArticleApi->api_v1_front_profile_pet_id_encyclopedie_articles_likes_post: %s\n" % e)
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

