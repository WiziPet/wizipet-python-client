# wizipet_api.FrontNotificationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_front_notifications_delete**](FrontNotificationApi.md#api_v1_front_notifications_delete) | **DELETE** /api/v1/front/notifications | 
[**api_v1_front_notifications_helloworld_post**](FrontNotificationApi.md#api_v1_front_notifications_helloworld_post) | **POST** /api/v1/front/notifications/helloworld | 
[**api_v1_front_notifications_post**](FrontNotificationApi.md#api_v1_front_notifications_post) | **POST** /api/v1/front/notifications | 


# **api_v1_front_notifications_delete**
> WpResponse api_v1_front_notifications_delete(notifications_unregister_for_notification_request=notifications_unregister_for_notification_request)



### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.notifications_unregister_for_notification_request import NotificationsUnregisterForNotificationRequest
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
    api_instance = wizipet_api.FrontNotificationApi(api_client)
    notifications_unregister_for_notification_request = wizipet_api.NotificationsUnregisterForNotificationRequest() # NotificationsUnregisterForNotificationRequest |  (optional)

    try:
        api_response = await api_instance.api_v1_front_notifications_delete(notifications_unregister_for_notification_request=notifications_unregister_for_notification_request)
        print("The response of FrontNotificationApi->api_v1_front_notifications_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontNotificationApi->api_v1_front_notifications_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notifications_unregister_for_notification_request** | [**NotificationsUnregisterForNotificationRequest**](NotificationsUnregisterForNotificationRequest.md)|  | [optional] 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_front_notifications_helloworld_post**
> WpResponse api_v1_front_notifications_helloworld_post()



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
    api_instance = wizipet_api.FrontNotificationApi(api_client)

    try:
        api_response = await api_instance.api_v1_front_notifications_helloworld_post()
        print("The response of FrontNotificationApi->api_v1_front_notifications_helloworld_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontNotificationApi->api_v1_front_notifications_helloworld_post: %s\n" % e)
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
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_front_notifications_post**
> WpResponseSystemString api_v1_front_notifications_post(notifications_register_for_notification_request=notifications_register_for_notification_request)



### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.notifications_register_for_notification_request import NotificationsRegisterForNotificationRequest
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
    api_instance = wizipet_api.FrontNotificationApi(api_client)
    notifications_register_for_notification_request = wizipet_api.NotificationsRegisterForNotificationRequest() # NotificationsRegisterForNotificationRequest |  (optional)

    try:
        api_response = await api_instance.api_v1_front_notifications_post(notifications_register_for_notification_request=notifications_register_for_notification_request)
        print("The response of FrontNotificationApi->api_v1_front_notifications_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontNotificationApi->api_v1_front_notifications_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notifications_register_for_notification_request** | [**NotificationsRegisterForNotificationRequest**](NotificationsRegisterForNotificationRequest.md)|  | [optional] 

### Return type

[**WpResponseSystemString**](WpResponseSystemString.md)

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

