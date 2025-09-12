# AuthPatchPasswordDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**old_password** | **str** |  | [optional] 
**new_password** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.auth_patch_password_dto import AuthPatchPasswordDto

# TODO update the JSON string below
json = "{}"
# create an instance of AuthPatchPasswordDto from a JSON string
auth_patch_password_dto_instance = AuthPatchPasswordDto.from_json(json)
# print the JSON string representation of the object
print(AuthPatchPasswordDto.to_json())

# convert the object into a dict
auth_patch_password_dto_dict = auth_patch_password_dto_instance.to_dict()
# create an instance of AuthPatchPasswordDto from a dict
auth_patch_password_dto_from_dict = AuthPatchPasswordDto.from_dict(auth_patch_password_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


