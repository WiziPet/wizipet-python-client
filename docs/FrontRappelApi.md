# wizipet_api.FrontRappelApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_front_profile_pet_id_santes_rappels_post**](FrontRappelApi.md#api_v1_front_profile_pet_id_santes_rappels_post) | **POST** /api/v1/front/profile/{pet_id}/santes/rappels | 
[**api_v1_front_profile_pet_id_santes_rappels_rappel_id_delete**](FrontRappelApi.md#api_v1_front_profile_pet_id_santes_rappels_rappel_id_delete) | **DELETE** /api/v1/front/profile/{pet_id}/santes/rappels/{rappel_id} | 


# **api_v1_front_profile_pet_id_santes_rappels_post**
> WpResponseCreateReplyDto api_v1_front_profile_pet_id_santes_rappels_post(pet_id, pense_betes_post_rappel_dto=pense_betes_post_rappel_dto)

Error codes : 
  - PET_UNOWNED: You are trying to make an action as a profile you are not owning

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.pense_betes_post_rappel_dto import PenseBetesPostRappelDto
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
    api_instance = wizipet_api.FrontRappelApi(api_client)
    pet_id = 'pet_id_example' # str | 
    pense_betes_post_rappel_dto = wizipet_api.PenseBetesPostRappelDto() # PenseBetesPostRappelDto |  (optional)

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_santes_rappels_post(pet_id, pense_betes_post_rappel_dto=pense_betes_post_rappel_dto)
        print("The response of FrontRappelApi->api_v1_front_profile_pet_id_santes_rappels_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontRappelApi->api_v1_front_profile_pet_id_santes_rappels_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **str**|  | 
 **pense_betes_post_rappel_dto** | [**PenseBetesPostRappelDto**](PenseBetesPostRappelDto.md)|  | [optional] 

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_front_profile_pet_id_santes_rappels_rappel_id_delete**
> WpResponse api_v1_front_profile_pet_id_santes_rappels_rappel_id_delete(pet_id, rappel_id)

Error codes : 
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
    api_instance = wizipet_api.FrontRappelApi(api_client)
    pet_id = 'pet_id_example' # str | 
    rappel_id = 'rappel_id_example' # str | 

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_santes_rappels_rappel_id_delete(pet_id, rappel_id)
        print("The response of FrontRappelApi->api_v1_front_profile_pet_id_santes_rappels_rappel_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontRappelApi->api_v1_front_profile_pet_id_santes_rappels_rappel_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **str**|  | 
 **rappel_id** | **str**|  | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

