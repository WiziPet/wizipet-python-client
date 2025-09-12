# wizipet_api.FrontAccountApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_front_account_me_delete**](FrontAccountApi.md#api_v1_front_account_me_delete) | **DELETE** /api/v1/front/account/me | 
[**api_v1_front_account_me_get**](FrontAccountApi.md#api_v1_front_account_me_get) | **GET** /api/v1/front/account/me | 
[**api_v1_front_account_register_post**](FrontAccountApi.md#api_v1_front_account_register_post) | **POST** /api/v1/front/account/register | 
[**api_v1_front_analytics_allowed_patch**](FrontAccountApi.md#api_v1_front_analytics_allowed_patch) | **PATCH** /api/v1/front/analytics/allowed | Définit si l&#39;utiliateur•trice autorise les analytics.
[**api_v1_front_auth_apple_login_post**](FrontAccountApi.md#api_v1_front_auth_apple_login_post) | **POST** /api/v1/front/auth/apple/login | Login With Apple : create access/refresh token from an Apple JWT
[**api_v1_front_auth_apple_register_post**](FrontAccountApi.md#api_v1_front_auth_apple_register_post) | **POST** /api/v1/front/auth/apple/register | Register With Apple : create access/refresh token from an Apple JWT
[**api_v1_front_auth_apple_sts_v2_post**](FrontAccountApi.md#api_v1_front_auth_apple_sts_v2_post) | **POST** /api/v1/front/auth/apple/sts/v2 | Called by apple servers when users changed preferences in Apple portal.
[**api_v1_front_auth_google_login_post**](FrontAccountApi.md#api_v1_front_auth_google_login_post) | **POST** /api/v1/front/auth/google/login | Login With Google : create access/refresh token from an Google JWT
[**api_v1_front_auth_google_register_post**](FrontAccountApi.md#api_v1_front_auth_google_register_post) | **POST** /api/v1/front/auth/google/register | Register With Google : create access/refresh token from an Google JWT


# **api_v1_front_account_me_delete**
> WpResponse api_v1_front_account_me_delete()

Error codes : 
  - ACCOUNT_NOT_FOUND: 

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
    api_instance = wizipet_api.FrontAccountApi(api_client)

    try:
        api_response = await api_instance.api_v1_front_account_me_delete()
        print("The response of FrontAccountApi->api_v1_front_account_me_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontAccountApi->api_v1_front_account_me_delete: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

# **api_v1_front_account_me_get**
> WpResponseAuthMeDto api_v1_front_account_me_get()

Error codes : 
  - ACCOUNT_NOT_FOUND: 

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.wp_response_auth_me_dto import WpResponseAuthMeDto
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
    api_instance = wizipet_api.FrontAccountApi(api_client)

    try:
        api_response = await api_instance.api_v1_front_account_me_get()
        print("The response of FrontAccountApi->api_v1_front_account_me_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontAccountApi->api_v1_front_account_me_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**WpResponseAuthMeDto**](WpResponseAuthMeDto.md)

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

# **api_v1_front_account_register_post**
> WpResponseAuthTokensResponse api_v1_front_account_register_post(auth_register_user_request=auth_register_user_request)

Error codes : 
  - HttpStatusCode Forbidden: Invalid client id or client secret
  - EMAIL_ALREADY_EXISTS: 
  - WEAK_PASSWORD: 

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.auth_register_user_request import AuthRegisterUserRequest
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
    api_instance = wizipet_api.FrontAccountApi(api_client)
    auth_register_user_request = wizipet_api.AuthRegisterUserRequest() # AuthRegisterUserRequest |  (optional)

    try:
        api_response = await api_instance.api_v1_front_account_register_post(auth_register_user_request=auth_register_user_request)
        print("The response of FrontAccountApi->api_v1_front_account_register_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontAccountApi->api_v1_front_account_register_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_register_user_request** | [**AuthRegisterUserRequest**](AuthRegisterUserRequest.md)|  | [optional] 

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

# **api_v1_front_analytics_allowed_patch**
> WpResponse api_v1_front_analytics_allowed_patch(analytics_allowed=analytics_allowed)

Définit si l'utiliateur•trice autorise les analytics.



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
    api_instance = wizipet_api.FrontAccountApi(api_client)
    analytics_allowed = True # bool |  (optional)

    try:
        # Définit si l'utiliateur•trice autorise les analytics.
        api_response = await api_instance.api_v1_front_analytics_allowed_patch(analytics_allowed=analytics_allowed)
        print("The response of FrontAccountApi->api_v1_front_analytics_allowed_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontAccountApi->api_v1_front_analytics_allowed_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analytics_allowed** | **bool**|  | [optional] 

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

# **api_v1_front_auth_apple_login_post**
> WpResponseAuthTokensResponse api_v1_front_auth_apple_login_post(auth_login_with_apple_dto=auth_login_with_apple_dto)

Login With Apple : create access/refresh token from an Apple JWT

Error codes : 
  - INVALID_CREDENTIALS: Invalid email/password pair
  - MISSING_JWT_EMAIL: Le jeton JWT n'inclut pas l'information demandée 'email'. L'inscription avec ce jeton sera impossible
  - MISSING_JWT_APPLE_ID: Le jeton JWT d'Apple n'inclut pas l'information demandée 'sub'. L'inscription avec ce jeton sera impossible
  - ACCOUNT_NOT_FOUND: 

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.auth_login_with_apple_dto import AuthLoginWithAppleDto
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
    api_instance = wizipet_api.FrontAccountApi(api_client)
    auth_login_with_apple_dto = wizipet_api.AuthLoginWithAppleDto() # AuthLoginWithAppleDto |  (optional)

    try:
        # Login With Apple : create access/refresh token from an Apple JWT
        api_response = await api_instance.api_v1_front_auth_apple_login_post(auth_login_with_apple_dto=auth_login_with_apple_dto)
        print("The response of FrontAccountApi->api_v1_front_auth_apple_login_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontAccountApi->api_v1_front_auth_apple_login_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_login_with_apple_dto** | [**AuthLoginWithAppleDto**](AuthLoginWithAppleDto.md)|  | [optional] 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_front_auth_apple_register_post**
> WpResponseAuthTokensResponse api_v1_front_auth_apple_register_post(auth_login_with_apple_dto=auth_login_with_apple_dto)

Register With Apple : create access/refresh token from an Apple JWT

Error codes : 
  - INVALID_CREDENTIALS: Invalid email/password pair
  - MISSING_JWT_EMAIL: Le jeton JWT n'inclut pas l'information demandée 'email'. L'inscription avec ce jeton sera impossible
  - MISSING_JWT_APPLE_ID: Le jeton JWT d'Apple n'inclut pas l'information demandée 'sub'. L'inscription avec ce jeton sera impossible

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.auth_login_with_apple_dto import AuthLoginWithAppleDto
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
    api_instance = wizipet_api.FrontAccountApi(api_client)
    auth_login_with_apple_dto = wizipet_api.AuthLoginWithAppleDto() # AuthLoginWithAppleDto |  (optional)

    try:
        # Register With Apple : create access/refresh token from an Apple JWT
        api_response = await api_instance.api_v1_front_auth_apple_register_post(auth_login_with_apple_dto=auth_login_with_apple_dto)
        print("The response of FrontAccountApi->api_v1_front_auth_apple_register_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontAccountApi->api_v1_front_auth_apple_register_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_login_with_apple_dto** | [**AuthLoginWithAppleDto**](AuthLoginWithAppleDto.md)|  | [optional] 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_front_auth_apple_sts_v2_post**
> WpResponse api_v1_front_auth_apple_sts_v2_post(auth_apple_signed_in_user_update_dto=auth_apple_signed_in_user_update_dto)

Called by apple servers when users changed preferences in Apple portal.



### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.auth_apple_signed_in_user_update_dto import AuthAppleSignedInUserUpdateDto
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
    api_instance = wizipet_api.FrontAccountApi(api_client)
    auth_apple_signed_in_user_update_dto = wizipet_api.AuthAppleSignedInUserUpdateDto() # AuthAppleSignedInUserUpdateDto |  (optional)

    try:
        # Called by apple servers when users changed preferences in Apple portal.
        api_response = await api_instance.api_v1_front_auth_apple_sts_v2_post(auth_apple_signed_in_user_update_dto=auth_apple_signed_in_user_update_dto)
        print("The response of FrontAccountApi->api_v1_front_auth_apple_sts_v2_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontAccountApi->api_v1_front_auth_apple_sts_v2_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_apple_signed_in_user_update_dto** | [**AuthAppleSignedInUserUpdateDto**](AuthAppleSignedInUserUpdateDto.md)|  | [optional] 

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

# **api_v1_front_auth_google_login_post**
> WpResponseAuthTokensResponse api_v1_front_auth_google_login_post(auth_login_with_google_dto=auth_login_with_google_dto)

Login With Google : create access/refresh token from an Google JWT

Error codes : 
  - INVALID_CREDENTIALS: Invalid email/password pair
  - MISSING_JWT_EMAIL: Le jeton JWT n'inclut pas l'information demandée 'email'. L'inscription avec ce jeton sera impossible
  - MISSING_JWT_GOOGLE_ID: Le jeton JWT google n'inclut pas l'information demandée 'sub'. L'inscription avec ce jeton sera impossible
  - GOOGLE_EMAIL_NOT_VERIFIED: Le jeton JWT google indique que l'email n'a pas été vérifié. L'inscription avec ce jeton sera impossible
  - ACCOUNT_NOT_FOUND: 

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.auth_login_with_google_dto import AuthLoginWithGoogleDto
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
    api_instance = wizipet_api.FrontAccountApi(api_client)
    auth_login_with_google_dto = wizipet_api.AuthLoginWithGoogleDto() # AuthLoginWithGoogleDto |  (optional)

    try:
        # Login With Google : create access/refresh token from an Google JWT
        api_response = await api_instance.api_v1_front_auth_google_login_post(auth_login_with_google_dto=auth_login_with_google_dto)
        print("The response of FrontAccountApi->api_v1_front_auth_google_login_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontAccountApi->api_v1_front_auth_google_login_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_login_with_google_dto** | [**AuthLoginWithGoogleDto**](AuthLoginWithGoogleDto.md)|  | [optional] 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_front_auth_google_register_post**
> WpResponseAuthTokensResponse api_v1_front_auth_google_register_post(auth_login_with_google_dto=auth_login_with_google_dto)

Register With Google : create access/refresh token from an Google JWT

Error codes : 
  - INVALID_CREDENTIALS: Invalid email/password pair
  - MISSING_JWT_EMAIL: Le jeton JWT n'inclut pas l'information demandée 'email'. L'inscription avec ce jeton sera impossible
  - MISSING_JWT_GOOGLE_ID: Le jeton JWT google n'inclut pas l'information demandée 'sub'. L'inscription avec ce jeton sera impossible
  - GOOGLE_EMAIL_NOT_VERIFIED: Le jeton JWT google indique que l'email n'a pas été vérifié. L'inscription avec ce jeton sera impossible

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.auth_login_with_google_dto import AuthLoginWithGoogleDto
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
    api_instance = wizipet_api.FrontAccountApi(api_client)
    auth_login_with_google_dto = wizipet_api.AuthLoginWithGoogleDto() # AuthLoginWithGoogleDto |  (optional)

    try:
        # Register With Google : create access/refresh token from an Google JWT
        api_response = await api_instance.api_v1_front_auth_google_register_post(auth_login_with_google_dto=auth_login_with_google_dto)
        print("The response of FrontAccountApi->api_v1_front_auth_google_register_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontAccountApi->api_v1_front_auth_google_register_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_login_with_google_dto** | [**AuthLoginWithGoogleDto**](AuthLoginWithGoogleDto.md)|  | [optional] 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

