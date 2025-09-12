# AuthTokensResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** |  | [optional] 
**refresh_token** | **str** |  | [optional] 
**token_type** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.auth_tokens_response import AuthTokensResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AuthTokensResponse from a JSON string
auth_tokens_response_instance = AuthTokensResponse.from_json(json)
# print the JSON string representation of the object
print(AuthTokensResponse.to_json())

# convert the object into a dict
auth_tokens_response_dict = auth_tokens_response_instance.to_dict()
# create an instance of AuthTokensResponse from a dict
auth_tokens_response_from_dict = AuthTokensResponse.from_dict(auth_tokens_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


