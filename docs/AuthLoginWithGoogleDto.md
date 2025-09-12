# AuthLoginWithGoogleDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**google_id_token_jwt** | **str** |  | [optional] 
**client_id** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.auth_login_with_google_dto import AuthLoginWithGoogleDto

# TODO update the JSON string below
json = "{}"
# create an instance of AuthLoginWithGoogleDto from a JSON string
auth_login_with_google_dto_instance = AuthLoginWithGoogleDto.from_json(json)
# print the JSON string representation of the object
print(AuthLoginWithGoogleDto.to_json())

# convert the object into a dict
auth_login_with_google_dto_dict = auth_login_with_google_dto_instance.to_dict()
# create an instance of AuthLoginWithGoogleDto from a dict
auth_login_with_google_dto_from_dict = AuthLoginWithGoogleDto.from_dict(auth_login_with_google_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


