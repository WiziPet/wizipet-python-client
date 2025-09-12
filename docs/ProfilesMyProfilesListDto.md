# ProfilesMyProfilesListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_list** | [**List[ProfilesMyProfileItemDto]**](ProfilesMyProfileItemDto.md) |  | [optional] 

## Example

```python
from wizipet_api.models.profiles_my_profiles_list_dto import ProfilesMyProfilesListDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProfilesMyProfilesListDto from a JSON string
profiles_my_profiles_list_dto_instance = ProfilesMyProfilesListDto.from_json(json)
# print the JSON string representation of the object
print(ProfilesMyProfilesListDto.to_json())

# convert the object into a dict
profiles_my_profiles_list_dto_dict = profiles_my_profiles_list_dto_instance.to_dict()
# create an instance of ProfilesMyProfilesListDto from a dict
profiles_my_profiles_list_dto_from_dict = ProfilesMyProfilesListDto.from_dict(profiles_my_profiles_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


