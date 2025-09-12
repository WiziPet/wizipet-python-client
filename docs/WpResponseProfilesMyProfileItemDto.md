# WpResponseProfilesMyProfileItemDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ProfilesMyProfileItemDto**](ProfilesMyProfileItemDto.md) |  | [optional] 
**is_success** | **bool** |  | [optional] 
**error_code** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.wp_response_profiles_my_profile_item_dto import WpResponseProfilesMyProfileItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of WpResponseProfilesMyProfileItemDto from a JSON string
wp_response_profiles_my_profile_item_dto_instance = WpResponseProfilesMyProfileItemDto.from_json(json)
# print the JSON string representation of the object
print(WpResponseProfilesMyProfileItemDto.to_json())

# convert the object into a dict
wp_response_profiles_my_profile_item_dto_dict = wp_response_profiles_my_profile_item_dto_instance.to_dict()
# create an instance of WpResponseProfilesMyProfileItemDto from a dict
wp_response_profiles_my_profile_item_dto_from_dict = WpResponseProfilesMyProfileItemDto.from_dict(wp_response_profiles_my_profile_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


