# AuthRefreshTokenRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**refresh_token** | **str** |  | [optional] 
**client_id** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.auth_refresh_token_request import AuthRefreshTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuthRefreshTokenRequest from a JSON string
auth_refresh_token_request_instance = AuthRefreshTokenRequest.from_json(json)
# print the JSON string representation of the object
print(AuthRefreshTokenRequest.to_json())

# convert the object into a dict
auth_refresh_token_request_dict = auth_refresh_token_request_instance.to_dict()
# create an instance of AuthRefreshTokenRequest from a dict
auth_refresh_token_request_from_dict = AuthRefreshTokenRequest.from_dict(auth_refresh_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


