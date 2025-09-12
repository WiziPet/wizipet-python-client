# AuthLoginWithAppleDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apple_jwt** | **str** |  | [optional] 
**client_id** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.auth_login_with_apple_dto import AuthLoginWithAppleDto

# TODO update the JSON string below
json = "{}"
# create an instance of AuthLoginWithAppleDto from a JSON string
auth_login_with_apple_dto_instance = AuthLoginWithAppleDto.from_json(json)
# print the JSON string representation of the object
print(AuthLoginWithAppleDto.to_json())

# convert the object into a dict
auth_login_with_apple_dto_dict = auth_login_with_apple_dto_instance.to_dict()
# create an instance of AuthLoginWithAppleDto from a dict
auth_login_with_apple_dto_from_dict = AuthLoginWithAppleDto.from_dict(auth_login_with_apple_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


