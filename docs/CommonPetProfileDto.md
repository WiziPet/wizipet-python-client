# CommonPetProfileDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**pet_name** | **str** |  | [optional] 
**picture_id** | **str** |  | [optional] 
**race_id** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.common_pet_profile_dto import CommonPetProfileDto

# TODO update the JSON string below
json = "{}"
# create an instance of CommonPetProfileDto from a JSON string
common_pet_profile_dto_instance = CommonPetProfileDto.from_json(json)
# print the JSON string representation of the object
print(CommonPetProfileDto.to_json())

# convert the object into a dict
common_pet_profile_dto_dict = common_pet_profile_dto_instance.to_dict()
# create an instance of CommonPetProfileDto from a dict
common_pet_profile_dto_from_dict = CommonPetProfileDto.from_dict(common_pet_profile_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


