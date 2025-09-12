# wizipet_api.FrontAuthApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_front_auth_helloworld_get**](FrontAuthApi.md#api_v1_front_auth_helloworld_get) | **GET** /api/v1/front/auth/helloworld | 
[**api_v1_front_auth_login_post**](FrontAuthApi.md#api_v1_front_auth_login_post) | **POST** /api/v1/front/auth/login | 
[**api_v1_front_auth_password_patch**](FrontAuthApi.md#api_v1_front_auth_password_patch) | **PATCH** /api/v1/front/auth/password | 
[**api_v1_front_auth_refresh_post**](FrontAuthApi.md#api_v1_front_auth_refresh_post) | **POST** /api/v1/front/auth/refresh | 


# **api_v1_front_auth_helloworld_get**
> WpResponseSystemString api_v1_front_auth_helloworld_get()



### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.wp_response_system_string import WpResponseSystemString
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
    api_instance = wizipet_api.FrontAuthApi(api_client)

    try:
        api_response = await api_instance.api_v1_front_auth_helloworld_get()
        print("The response of FrontAuthApi->api_v1_front_auth_helloworld_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontAuthApi->api_v1_front_auth_helloworld_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**WpResponseSystemString**](WpResponseSystemString.md)

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

# **api_v1_front_auth_login_post**
> WpResponseAuthTokensResponse api_v1_front_auth_login_post(auth_login_user_request=auth_login_user_request)

Error codes : 
  - HttpStatusCode Forbidden: Invalid client id or client secret
  - HttpStatusCode Forbidden: Invalid email/password pair

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.auth_login_user_request import AuthLoginUserRequest
from wizipet_api.models.wp_response_auth_tokens_response import WpResponseAuthTokensResponse
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
    api_instance = wizipet_api.FrontAuthApi(api_client)
    auth_login_user_request = wizipet_api.AuthLoginUserRequest() # AuthLoginUserRequest |  (optional)

    try:
        api_response = await api_instance.api_v1_front_auth_login_post(auth_login_user_request=auth_login_user_request)
        print("The response of FrontAuthApi->api_v1_front_auth_login_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontAuthApi->api_v1_front_auth_login_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_login_user_request** | [**AuthLoginUserRequest**](AuthLoginUserRequest.md)|  | [optional] 

### Return type

[**WpResponseAuthTokensResponse**](WpResponseAuthTokensResponse.md)

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

# **api_v1_front_auth_password_patch**
> WpResponse api_v1_front_auth_password_patch(auth_patch_password_dto=auth_patch_password_dto)

Error codes : 
  - WEAK_PASSWORD: 
  - PASSWORD_AUTH_NOT_USED: 
  - ACCOUNT_NOT_FOUND: 

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.auth_patch_password_dto import AuthPatchPasswordDto
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
    api_instance = wizipet_api.FrontAuthApi(api_client)
    auth_patch_password_dto = wizipet_api.AuthPatchPasswordDto() # AuthPatchPasswordDto |  (optional)

    try:
        api_response = await api_instance.api_v1_front_auth_password_patch(auth_patch_password_dto=auth_patch_password_dto)
        print("The response of FrontAuthApi->api_v1_front_auth_password_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontAuthApi->api_v1_front_auth_password_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_patch_password_dto** | [**AuthPatchPasswordDto**](AuthPatchPasswordDto.md)|  | [optional] 

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
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_front_auth_refresh_post**
> WpResponseAuthTokensResponse api_v1_front_auth_refresh_post(auth_refresh_token_request=auth_refresh_token_request)



### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.auth_refresh_token_request import AuthRefreshTokenRequest
from wizipet_api.models.wp_response_auth_tokens_response import WpResponseAuthTokensResponse
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
    api_instance = wizipet_api.FrontAuthApi(api_client)
    auth_refresh_token_request = wizipet_api.AuthRefreshTokenRequest() # AuthRefreshTokenRequest |  (optional)

    try:
        api_response = await api_instance.api_v1_front_auth_refresh_post(auth_refresh_token_request=auth_refresh_token_request)
        print("The response of FrontAuthApi->api_v1_front_auth_refresh_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontAuthApi->api_v1_front_auth_refresh_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_refresh_token_request** | [**AuthRefreshTokenRequest**](AuthRefreshTokenRequest.md)|  | [optional] 

### Return type

[**WpResponseAuthTokensResponse**](WpResponseAuthTokensResponse.md)

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
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

