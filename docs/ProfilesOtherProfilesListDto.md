# ProfilesOtherProfilesListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id_extra** | [**ProfilesGroupIdExtraDto**](ProfilesGroupIdExtraDto.md) |  | [optional] 
**has_more** | **bool** |  | [optional] 
**count** | **int** |  | [optional] 
**continuation_token** | **str** |  | [optional] 
**data** | [**List[ProfilesOtherProfileItemDto]**](ProfilesOtherProfileItemDto.md) |  | [optional] 
**is_success** | **bool** |  | [optional] 
**error_code** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.profiles_other_profiles_list_dto import ProfilesOtherProfilesListDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProfilesOtherProfilesListDto from a JSON string
profiles_other_profiles_list_dto_instance = ProfilesOtherProfilesListDto.from_json(json)
# print the JSON string representation of the object
print(ProfilesOtherProfilesListDto.to_json())

# convert the object into a dict
profiles_other_profiles_list_dto_dict = profiles_other_profiles_list_dto_instance.to_dict()
# create an instance of ProfilesOtherProfilesListDto from a dict
profiles_other_profiles_list_dto_from_dict = ProfilesOtherProfilesListDto.from_dict(profiles_other_profiles_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


