# ProfilesPatchProfileDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pet_name** | **str** |  | [optional] 
**pet_race_id** | **str** |  | [optional] 
**birthday** | **str** |  | [optional] 
**personality** | **str** |  | [optional] 
**ville** | **str** |  | [optional] 
**picture_id** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.profiles_patch_profile_dto import ProfilesPatchProfileDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProfilesPatchProfileDto from a JSON string
profiles_patch_profile_dto_instance = ProfilesPatchProfileDto.from_json(json)
# print the JSON string representation of the object
print(ProfilesPatchProfileDto.to_json())

# convert the object into a dict
profiles_patch_profile_dto_dict = profiles_patch_profile_dto_instance.to_dict()
# create an instance of ProfilesPatchProfileDto from a dict
profiles_patch_profile_dto_from_dict = ProfilesPatchProfileDto.from_dict(profiles_patch_profile_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


