# ProfilesOtherProfileDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**owner_id** | **str** |  | [optional] 
**pet_name** | **str** |  | [optional] 
**personality** | **str** |  | [optional] 
**race_id** | **str** |  | [optional] 
**picture_id** | **str** |  | [optional] 
**gender** | [**ProfilesGenderDto**](ProfilesGenderDto.md) |  | [optional] 
**birthday** | **str** |  | [optional] 
**ville** | **str** |  | [optional] 
**connection_status** | [**ContactsConnectionStatusDto**](ContactsConnectionStatusDto.md) |  | [optional] 
**friend_count** | **int** |  | [optional] 
**alerte_perte** | [**ProfilesAlertePerteDto**](ProfilesAlertePerteDto.md) |  | [optional] 
**is_ignored** | **bool** |  | [optional] 

## Example

```python
from wizipet_api.models.profiles_other_profile_dto import ProfilesOtherProfileDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProfilesOtherProfileDto from a JSON string
profiles_other_profile_dto_instance = ProfilesOtherProfileDto.from_json(json)
# print the JSON string representation of the object
print(ProfilesOtherProfileDto.to_json())

# convert the object into a dict
profiles_other_profile_dto_dict = profiles_other_profile_dto_instance.to_dict()
# create an instance of ProfilesOtherProfileDto from a dict
profiles_other_profile_dto_from_dict = ProfilesOtherProfileDto.from_dict(profiles_other_profile_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


