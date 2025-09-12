# AuthAppleSignedInUserUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payload** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.auth_apple_signed_in_user_update_dto import AuthAppleSignedInUserUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of AuthAppleSignedInUserUpdateDto from a JSON string
auth_apple_signed_in_user_update_dto_instance = AuthAppleSignedInUserUpdateDto.from_json(json)
# print the JSON string representation of the object
print(AuthAppleSignedInUserUpdateDto.to_json())

# convert the object into a dict
auth_apple_signed_in_user_update_dto_dict = auth_apple_signed_in_user_update_dto_instance.to_dict()
# create an instance of AuthAppleSignedInUserUpdateDto from a dict
auth_apple_signed_in_user_update_dto_from_dict = AuthAppleSignedInUserUpdateDto.from_dict(auth_apple_signed_in_user_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


