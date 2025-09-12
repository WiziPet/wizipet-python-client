# wizipet_api.FrontContactApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_front_profile_pet_id_contact_count_pending_get**](FrontContactApi.md#api_v1_front_profile_pet_id_contact_count_pending_get) | **GET** /api/v1/front/profile/{pet_id}/contact/count-pending | 
[**api_v1_front_profile_pet_id_contact_publications_get**](FrontContactApi.md#api_v1_front_profile_pet_id_contact_publications_get) | **GET** /api/v1/front/profile/{pet_id}/contact/publications | 
[**api_v1_front_profile_pet_id_contact_summary_get**](FrontContactApi.md#api_v1_front_profile_pet_id_contact_summary_get) | **GET** /api/v1/front/profile/{pet_id}/contact/summary | 
[**api_v1_front_profile_pet_id_contact_target_profile_id_delete**](FrontContactApi.md#api_v1_front_profile_pet_id_contact_target_profile_id_delete) | **DELETE** /api/v1/front/profile/{pet_id}/contact/{target_profile_id} | 
[**api_v1_front_profile_pet_id_contact_target_profile_id_put**](FrontContactApi.md#api_v1_front_profile_pet_id_contact_target_profile_id_put) | **PUT** /api/v1/front/profile/{pet_id}/contact/{target_profile_id} | 


# **api_v1_front_profile_pet_id_contact_count_pending_get**
> WpResponseSystemInt32 api_v1_front_profile_pet_id_contact_count_pending_get(pet_id)



### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.wp_response_system_int32 import WpResponseSystemInt32
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
    api_instance = wizipet_api.FrontContactApi(api_client)
    pet_id = 'pet_id_example' # str | 

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_contact_count_pending_get(pet_id)
        print("The response of FrontContactApi->api_v1_front_profile_pet_id_contact_count_pending_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontContactApi->api_v1_front_profile_pet_id_contact_count_pending_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **str**|  | 

### Return type

[**WpResponseSystemInt32**](WpResponseSystemInt32.md)

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

# **api_v1_front_profile_pet_id_contact_publications_get**
> ResumableListResponsePublicationsPublicationItemDto api_v1_front_profile_pet_id_contact_publications_get(pet_id, continuation_token=continuation_token)



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
    api_instance = wizipet_api.FrontContactApi(api_client)
    pet_id = 'pet_id_example' # str | 
    continuation_token = 'continuation_token_example' # str |  (optional)

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_contact_publications_get(pet_id, continuation_token=continuation_token)
        print("The response of FrontContactApi->api_v1_front_profile_pet_id_contact_publications_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontContactApi->api_v1_front_profile_pet_id_contact_publications_get: %s\n" % e)
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

# **api_v1_front_profile_pet_id_contact_summary_get**
> ListResponseContactsContactSummaryDto api_v1_front_profile_pet_id_contact_summary_get(pet_id)

Error codes : 
  - PROFILE_NOT_FOUND: 
  - PET_UNOWNED: You are trying to make an action as a profile you are not owning

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.list_response_contacts_contact_summary_dto import ListResponseContactsContactSummaryDto
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
    api_instance = wizipet_api.FrontContactApi(api_client)
    pet_id = 'pet_id_example' # str | 

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_contact_summary_get(pet_id)
        print("The response of FrontContactApi->api_v1_front_profile_pet_id_contact_summary_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontContactApi->api_v1_front_profile_pet_id_contact_summary_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **str**|  | 

### Return type

[**ListResponseContactsContactSummaryDto**](ListResponseContactsContactSummaryDto.md)

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

# **api_v1_front_profile_pet_id_contact_target_profile_id_delete**
> WpResponse api_v1_front_profile_pet_id_contact_target_profile_id_delete(pet_id, target_profile_id)

Error codes : 
  - PROFILE_NOT_FOUND: 
  - CONTACT_CONNECTION_NOT_FOUND: 
  - PET_UNOWNED: You are trying to make an action as a profile you are not owning

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
    api_instance = wizipet_api.FrontContactApi(api_client)
    pet_id = 'pet_id_example' # str | 
    target_profile_id = 'target_profile_id_example' # str | 

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_contact_target_profile_id_delete(pet_id, target_profile_id)
        print("The response of FrontContactApi->api_v1_front_profile_pet_id_contact_target_profile_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontContactApi->api_v1_front_profile_pet_id_contact_target_profile_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **str**|  | 
 **target_profile_id** | **str**|  | 

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

# **api_v1_front_profile_pet_id_contact_target_profile_id_put**
> WpResponse api_v1_front_profile_pet_id_contact_target_profile_id_put(pet_id, target_profile_id)

Error codes : 
  - PROFILE_NOT_FOUND: 
  - PET_UNOWNED: You are trying to make an action as a profile you are not owning

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
    api_instance = wizipet_api.FrontContactApi(api_client)
    pet_id = 'pet_id_example' # str | 
    target_profile_id = 'target_profile_id_example' # str | 

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_contact_target_profile_id_put(pet_id, target_profile_id)
        print("The response of FrontContactApi->api_v1_front_profile_pet_id_contact_target_profile_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontContactApi->api_v1_front_profile_pet_id_contact_target_profile_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **str**|  | 
 **target_profile_id** | **str**|  | 

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

