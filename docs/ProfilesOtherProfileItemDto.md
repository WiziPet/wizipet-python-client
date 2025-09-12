# ProfilesOtherProfileItemDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**pet_name** | **str** |  | [optional] 
**picture_id** | **str** |  | [optional] 
**race_id** | **str** |  | [optional] 
**ville** | **str** |  | [optional] 
**connection_status** | [**ContactsConnectionStatusDto**](ContactsConnectionStatusDto.md) |  | [optional] 
**common_friend_list_overview** | [**List[GroupsPetSummaryDto]**](GroupsPetSummaryDto.md) |  | [optional] 
**common_friend_count** | **int** |  | [optional] 
**alerte_perte** | [**ProfilesAlertePerteDto**](ProfilesAlertePerteDto.md) |  | [optional] 

## Example

```python
from wizipet_api.models.profiles_other_profile_item_dto import ProfilesOtherProfileItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProfilesOtherProfileItemDto from a JSON string
profiles_other_profile_item_dto_instance = ProfilesOtherProfileItemDto.from_json(json)
# print the JSON string representation of the object
print(ProfilesOtherProfileItemDto.to_json())

# convert the object into a dict
profiles_other_profile_item_dto_dict = profiles_other_profile_item_dto_instance.to_dict()
# create an instance of ProfilesOtherProfileItemDto from a dict
profiles_other_profile_item_dto_from_dict = ProfilesOtherProfileItemDto.from_dict(profiles_other_profile_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


