# CartesListProfilesParamDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bounds** | [**GooglesBoundsDto**](GooglesBoundsDto.md) |  | [optional] 
**keywords** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.cartes_list_profiles_param_dto import CartesListProfilesParamDto

# TODO update the JSON string below
json = "{}"
# create an instance of CartesListProfilesParamDto from a JSON string
cartes_list_profiles_param_dto_instance = CartesListProfilesParamDto.from_json(json)
# print the JSON string representation of the object
print(CartesListProfilesParamDto.to_json())

# convert the object into a dict
cartes_list_profiles_param_dto_dict = cartes_list_profiles_param_dto_instance.to_dict()
# create an instance of CartesListProfilesParamDto from a dict
cartes_list_profiles_param_dto_from_dict = CartesListProfilesParamDto.from_dict(cartes_list_profiles_param_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


