# wizipet_api.FrontMedicalAssistantApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_front_profile_pet_id_santes_assistant_comportement_post**](FrontMedicalAssistantApi.md#api_v1_front_profile_pet_id_santes_assistant_comportement_post) | **POST** /api/v1/front/profile/{pet_id}/santes/assistant/comportement | 
[**api_v1_front_profile_pet_id_santes_assistant_sante_post**](FrontMedicalAssistantApi.md#api_v1_front_profile_pet_id_santes_assistant_sante_post) | **POST** /api/v1/front/profile/{pet_id}/santes/assistant/sante | 
[**api_v1_front_profile_pet_id_santes_assistant_urgence_post**](FrontMedicalAssistantApi.md#api_v1_front_profile_pet_id_santes_assistant_urgence_post) | **POST** /api/v1/front/profile/{pet_id}/santes/assistant/urgence | 


# **api_v1_front_profile_pet_id_santes_assistant_comportement_post**
> MedicalAssistantsAssistantReplyDto api_v1_front_profile_pet_id_santes_assistant_comportement_post(pet_id, medical_assistants_assistant_query_dto=medical_assistants_assistant_query_dto)



### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.medical_assistants_assistant_query_dto import MedicalAssistantsAssistantQueryDto
from wizipet_api.models.medical_assistants_assistant_reply_dto import MedicalAssistantsAssistantReplyDto
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
    api_instance = wizipet_api.FrontMedicalAssistantApi(api_client)
    pet_id = 'pet_id_example' # str | 
    medical_assistants_assistant_query_dto = wizipet_api.MedicalAssistantsAssistantQueryDto() # MedicalAssistantsAssistantQueryDto |  (optional)

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_santes_assistant_comportement_post(pet_id, medical_assistants_assistant_query_dto=medical_assistants_assistant_query_dto)
        print("The response of FrontMedicalAssistantApi->api_v1_front_profile_pet_id_santes_assistant_comportement_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontMedicalAssistantApi->api_v1_front_profile_pet_id_santes_assistant_comportement_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **str**|  | 
 **medical_assistants_assistant_query_dto** | [**MedicalAssistantsAssistantQueryDto**](MedicalAssistantsAssistantQueryDto.md)|  | [optional] 

### Return type

[**MedicalAssistantsAssistantReplyDto**](MedicalAssistantsAssistantReplyDto.md)

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_front_profile_pet_id_santes_assistant_sante_post**
> MedicalAssistantsAssistantReplyDto api_v1_front_profile_pet_id_santes_assistant_sante_post(pet_id, medical_assistants_assistant_query_dto=medical_assistants_assistant_query_dto)



### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.medical_assistants_assistant_query_dto import MedicalAssistantsAssistantQueryDto
from wizipet_api.models.medical_assistants_assistant_reply_dto import MedicalAssistantsAssistantReplyDto
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
    api_instance = wizipet_api.FrontMedicalAssistantApi(api_client)
    pet_id = 'pet_id_example' # str | 
    medical_assistants_assistant_query_dto = wizipet_api.MedicalAssistantsAssistantQueryDto() # MedicalAssistantsAssistantQueryDto |  (optional)

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_santes_assistant_sante_post(pet_id, medical_assistants_assistant_query_dto=medical_assistants_assistant_query_dto)
        print("The response of FrontMedicalAssistantApi->api_v1_front_profile_pet_id_santes_assistant_sante_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontMedicalAssistantApi->api_v1_front_profile_pet_id_santes_assistant_sante_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **str**|  | 
 **medical_assistants_assistant_query_dto** | [**MedicalAssistantsAssistantQueryDto**](MedicalAssistantsAssistantQueryDto.md)|  | [optional] 

### Return type

[**MedicalAssistantsAssistantReplyDto**](MedicalAssistantsAssistantReplyDto.md)

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_front_profile_pet_id_santes_assistant_urgence_post**
> MedicalAssistantsAssistantReplyDto api_v1_front_profile_pet_id_santes_assistant_urgence_post(pet_id, medical_assistants_assistant_query_dto=medical_assistants_assistant_query_dto)



### Example

* Bearer (JWT) Authentication (Bearer):

```python
import wizipet_api
from wizipet_api.models.medical_assistants_assistant_query_dto import MedicalAssistantsAssistantQueryDto
from wizipet_api.models.medical_assistants_assistant_reply_dto import MedicalAssistantsAssistantReplyDto
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
    api_instance = wizipet_api.FrontMedicalAssistantApi(api_client)
    pet_id = 'pet_id_example' # str | 
    medical_assistants_assistant_query_dto = wizipet_api.MedicalAssistantsAssistantQueryDto() # MedicalAssistantsAssistantQueryDto |  (optional)

    try:
        api_response = await api_instance.api_v1_front_profile_pet_id_santes_assistant_urgence_post(pet_id, medical_assistants_assistant_query_dto=medical_assistants_assistant_query_dto)
        print("The response of FrontMedicalAssistantApi->api_v1_front_profile_pet_id_santes_assistant_urgence_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FrontMedicalAssistantApi->api_v1_front_profile_pet_id_santes_assistant_urgence_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **str**|  | 
 **medical_assistants_assistant_query_dto** | [**MedicalAssistantsAssistantQueryDto**](MedicalAssistantsAssistantQueryDto.md)|  | [optional] 

### Return type

[**MedicalAssistantsAssistantReplyDto**](MedicalAssistantsAssistantReplyDto.md)

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

