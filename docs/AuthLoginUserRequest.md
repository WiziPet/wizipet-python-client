# AuthLoginUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**client_id** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 
**password** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.auth_login_user_request import AuthLoginUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuthLoginUserRequest from a JSON string
auth_login_user_request_instance = AuthLoginUserRequest.from_json(json)
# print the JSON string representation of the object
print(AuthLoginUserRequest.to_json())

# convert the object into a dict
auth_login_user_request_dict = auth_login_user_request_instance.to_dict()
# create an instance of AuthLoginUserRequest from a dict
auth_login_user_request_from_dict = AuthLoginUserRequest.from_dict(auth_login_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


