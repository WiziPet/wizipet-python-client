# AuthRegisterUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**client_id** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 
**password** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.auth_register_user_request import AuthRegisterUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuthRegisterUserRequest from a JSON string
auth_register_user_request_instance = AuthRegisterUserRequest.from_json(json)
# print the JSON string representation of the object
print(AuthRegisterUserRequest.to_json())

# convert the object into a dict
auth_register_user_request_dict = auth_register_user_request_instance.to_dict()
# create an instance of AuthRegisterUserRequest from a dict
auth_register_user_request_from_dict = AuthRegisterUserRequest.from_dict(auth_register_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


