# wizipet_api.FrontShoppingApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_front_catalogue_aliment_get**](FrontShoppingApi.md#api_v1_front_catalogue_aliment_get) | **GET** /api/v1/front/catalogue_aliment | 


# **api_v1_front_catalogue_aliment_get**
> ResumableListResponseSantesAlimentCatalogueItemDto api_v1_front_catalogue_aliment_get(search=search, continuation_token=continuation_token, espece=espece)



### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.profiles_espece_dto import ProfilesEspeceDto
from wizipet_api.models.resumable_list_response_santes_aliment_catalogue_item_dto import ResumableListResponseSantesAlimentCatalogueItemDto
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
    api_instance = wizipet_api.FrontShoppingApi(api_client)
    search = 'search_example' # str |  (optional)
    continuation_token = 'continuation_token_example' # str |  (optional)
    espece = wizipet_api.ProfilesEspeceDto() # ProfilesEspeceDto |  (optional)

    try:
        api_response = await api_instance.api_v1_front_catalogue_aliment_get(search=search, continuation_token=continuation_token, espece=espece)
        print("The response of FrontShoppingApi->api_v1_front_catalogue_aliment_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontShoppingApi->api_v1_front_catalogue_aliment_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**|  | [optional] 
 **continuation_token** | **str**|  | [optional] 
 **espece** | [**ProfilesEspeceDto**](.md)|  | [optional] 

### Return type

[**ResumableListResponseSantesAlimentCatalogueItemDto**](ResumableListResponseSantesAlimentCatalogueItemDto.md)

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

