# WpResponseProfilesMyProfilesListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ProfilesMyProfilesListDto**](ProfilesMyProfilesListDto.md) |  | [optional] 
**is_success** | **bool** |  | [optional] 
**error_code** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.wp_response_profiles_my_profiles_list_dto import WpResponseProfilesMyProfilesListDto

# TODO update the JSON string below
json = "{}"
# create an instance of WpResponseProfilesMyProfilesListDto from a JSON string
wp_response_profiles_my_profiles_list_dto_instance = WpResponseProfilesMyProfilesListDto.from_json(json)
# print the JSON string representation of the object
print(WpResponseProfilesMyProfilesListDto.to_json())

# convert the object into a dict
wp_response_profiles_my_profiles_list_dto_dict = wp_response_profiles_my_profiles_list_dto_instance.to_dict()
# create an instance of WpResponseProfilesMyProfilesListDto from a dict
wp_response_profiles_my_profiles_list_dto_from_dict = WpResponseProfilesMyProfilesListDto.from_dict(wp_response_profiles_my_profiles_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


