# ProfilesMyProfileItemDto


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
**friend_count** | **int** |  | [optional] 
**group_count** | **int** |  | [optional] 
**profile_creation_order** | **int** |  | [optional] 
**alerte_perte** | [**ProfilesAlertePerteDto**](ProfilesAlertePerteDto.md) |  | [optional] 

## Example

```python
from wizipet_api.models.profiles_my_profile_item_dto import ProfilesMyProfileItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProfilesMyProfileItemDto from a JSON string
profiles_my_profile_item_dto_instance = ProfilesMyProfileItemDto.from_json(json)
# print the JSON string representation of the object
print(ProfilesMyProfileItemDto.to_json())

# convert the object into a dict
profiles_my_profile_item_dto_dict = profiles_my_profile_item_dto_instance.to_dict()
# create an instance of ProfilesMyProfileItemDto from a dict
profiles_my_profile_item_dto_from_dict = ProfilesMyProfileItemDto.from_dict(profiles_my_profile_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


