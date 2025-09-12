# SantesSetSicknessDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_actif** | **bool** |  | [optional] 
**start_date** | **str** |  | [optional] 
**pathologie_id** | **str** |  | [optional] 
**commentaire** | **str** |  | [optional] 
**traitements** | [**List[SantesSetTraitementDto]**](SantesSetTraitementDto.md) |  | [optional] 

## Example

```python
from wizipet_api.models.santes_set_sickness_dto import SantesSetSicknessDto

# TODO update the JSON string below
json = "{}"
# create an instance of SantesSetSicknessDto from a JSON string
santes_set_sickness_dto_instance = SantesSetSicknessDto.from_json(json)
# print the JSON string representation of the object
print(SantesSetSicknessDto.to_json())

# convert the object into a dict
santes_set_sickness_dto_dict = santes_set_sickness_dto_instance.to_dict()
# create an instance of SantesSetSicknessDto from a dict
santes_set_sickness_dto_from_dict = SantesSetSicknessDto.from_dict(santes_set_sickness_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


