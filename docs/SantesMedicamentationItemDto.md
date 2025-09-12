# SantesMedicamentationItemDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**var_date** | **str** |  | [optional] 
**commentaire** | **str** |  | [optional] 
**antiparasitaire_id** | **str** |  | [optional] 
**vermifuge_id** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.santes_medicamentation_item_dto import SantesMedicamentationItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of SantesMedicamentationItemDto from a JSON string
santes_medicamentation_item_dto_instance = SantesMedicamentationItemDto.from_json(json)
# print the JSON string representation of the object
print(SantesMedicamentationItemDto.to_json())

# convert the object into a dict
santes_medicamentation_item_dto_dict = santes_medicamentation_item_dto_instance.to_dict()
# create an instance of SantesMedicamentationItemDto from a dict
santes_medicamentation_item_dto_from_dict = SantesMedicamentationItemDto.from_dict(santes_medicamentation_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


