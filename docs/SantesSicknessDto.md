# SantesSicknessDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**is_actif** | **bool** |  | [optional] 
**start_date** | **str** |  | [optional] 
**pathologie_id** | **str** |  | [optional] 
**commentaire** | **str** |  | [optional] 
**traitements** | [**List[SantesTraitementDto]**](SantesTraitementDto.md) |  | [optional] 

## Example

```python
from wizipet_api.models.santes_sickness_dto import SantesSicknessDto

# TODO update the JSON string below
json = "{}"
# create an instance of SantesSicknessDto from a JSON string
santes_sickness_dto_instance = SantesSicknessDto.from_json(json)
# print the JSON string representation of the object
print(SantesSicknessDto.to_json())

# convert the object into a dict
santes_sickness_dto_dict = santes_sickness_dto_instance.to_dict()
# create an instance of SantesSicknessDto from a dict
santes_sickness_dto_from_dict = SantesSicknessDto.from_dict(santes_sickness_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


