# wizipet_api.FrontVersionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_front_version_compatibility_get**](FrontVersionApi.md#api_v1_front_version_compatibility_get) | **GET** /api/v1/front/version/compatibility | 


# **api_v1_front_version_compatibility_get**
> WpResponseVersionsVersionDto api_v1_front_version_compatibility_get(version=version)



### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.wp_response_versions_version_dto import WpResponseVersionsVersionDto
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
    api_instance = wizipet_api.FrontVersionApi(api_client)
    version = 'version_example' # str |  (optional)

    try:
        api_response = await api_instance.api_v1_front_version_compatibility_get(version=version)
        print("The response of FrontVersionApi->api_v1_front_version_compatibility_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontVersionApi->api_v1_front_version_compatibility_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [optional] 

### Return type

[**WpResponseVersionsVersionDto**](WpResponseVersionsVersionDto.md)

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

