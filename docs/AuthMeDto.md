# AuthMeDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | [optional] 
**shared_position_allowed** | **bool** |  | [optional] 
**sponsored_content_allowed** | **bool** |  | [optional] 
**analytics_allowed** | **bool** |  | [optional] 
**email** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.auth_me_dto import AuthMeDto

# TODO update the JSON string below
json = "{}"
# create an instance of AuthMeDto from a JSON string
auth_me_dto_instance = AuthMeDto.from_json(json)
# print the JSON string representation of the object
print(AuthMeDto.to_json())

# convert the object into a dict
auth_me_dto_dict = auth_me_dto_instance.to_dict()
# create an instance of AuthMeDto from a dict
auth_me_dto_from_dict = AuthMeDto.from_dict(auth_me_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


