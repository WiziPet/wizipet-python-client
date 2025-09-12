# SantesSicknessItemDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**is_actif** | **bool** |  | [optional] 
**start_date** | **str** |  | [optional] 
**pathologie_id** | **str** |  | [optional] 
**commentaire** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.santes_sickness_item_dto import SantesSicknessItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of SantesSicknessItemDto from a JSON string
santes_sickness_item_dto_instance = SantesSicknessItemDto.from_json(json)
# print the JSON string representation of the object
print(SantesSicknessItemDto.to_json())

# convert the object into a dict
santes_sickness_item_dto_dict = santes_sickness_item_dto_instance.to_dict()
# create an instance of SantesSicknessItemDto from a dict
santes_sickness_item_dto_from_dict = SantesSicknessItemDto.from_dict(santes_sickness_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


