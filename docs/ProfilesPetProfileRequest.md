# ProfilesPetProfileRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pet_name** | **str** |  | [optional] 
**ville** | **str** |  | [optional] 
**personality** | **str** |  | [optional] 
**pet_race_id** | **str** |  | [optional] 
**picture_id** | **str** |  | [optional] 
**gender** | [**ProfilesGenderDto**](ProfilesGenderDto.md) |  | [optional] 
**birthday** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.profiles_pet_profile_request import ProfilesPetProfileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProfilesPetProfileRequest from a JSON string
profiles_pet_profile_request_instance = ProfilesPetProfileRequest.from_json(json)
# print the JSON string representation of the object
print(ProfilesPetProfileRequest.to_json())

# convert the object into a dict
profiles_pet_profile_request_dict = profiles_pet_profile_request_instance.to_dict()
# create an instance of ProfilesPetProfileRequest from a dict
profiles_pet_profile_request_from_dict = ProfilesPetProfileRequest.from_dict(profiles_pet_profile_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


