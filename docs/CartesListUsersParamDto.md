# CartesListUsersParamDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bounds** | [**GooglesBoundsDto**](GooglesBoundsDto.md) |  | [optional] 
**keywords** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.cartes_list_users_param_dto import CartesListUsersParamDto

# TODO update the JSON string below
json = "{}"
# create an instance of CartesListUsersParamDto from a JSON string
cartes_list_users_param_dto_instance = CartesListUsersParamDto.from_json(json)
# print the JSON string representation of the object
print(CartesListUsersParamDto.to_json())

# convert the object into a dict
cartes_list_users_param_dto_dict = cartes_list_users_param_dto_instance.to_dict()
# create an instance of CartesListUsersParamDto from a dict
cartes_list_users_param_dto_from_dict = CartesListUsersParamDto.from_dict(cartes_list_users_param_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


