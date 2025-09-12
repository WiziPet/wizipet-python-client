# SantesHistoAlimentationDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**evolution_aliment_principal** | [**List[SantesDateAlimentDto]**](SantesDateAlimentDto.md) |  | [optional] 
**evolution_aliment_secondaire** | [**List[SantesDateAlimentDto]**](SantesDateAlimentDto.md) |  | [optional] 

## Example

```python
from wizipet_api.models.santes_histo_alimentation_dto import SantesHistoAlimentationDto

# TODO update the JSON string below
json = "{}"
# create an instance of SantesHistoAlimentationDto from a JSON string
santes_histo_alimentation_dto_instance = SantesHistoAlimentationDto.from_json(json)
# print the JSON string representation of the object
print(SantesHistoAlimentationDto.to_json())

# convert the object into a dict
santes_histo_alimentation_dto_dict = santes_histo_alimentation_dto_instance.to_dict()
# create an instance of SantesHistoAlimentationDto from a dict
santes_histo_alimentation_dto_from_dict = SantesHistoAlimentationDto.from_dict(santes_histo_alimentation_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


