# SantesBilanDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**physio** | [**SantesBilanSectionResultDto**](SantesBilanSectionResultDto.md) |  | [optional] 
**poids** | [**SantesBilanPoidsResultDto**](SantesBilanPoidsResultDto.md) |  | [optional] 
**alimentation** | [**SantesBilanAlimentationResultDto**](SantesBilanAlimentationResultDto.md) |  | [optional] 
**activite** | [**SantesBilanActiviteResultDto**](SantesBilanActiviteResultDto.md) |  | [optional] 
**sante** | [**SantesBilanSectionResultDto**](SantesBilanSectionResultDto.md) |  | [optional] 

## Example

```python
from wizipet_api.models.santes_bilan_dto import SantesBilanDto

# TODO update the JSON string below
json = "{}"
# create an instance of SantesBilanDto from a JSON string
santes_bilan_dto_instance = SantesBilanDto.from_json(json)
# print the JSON string representation of the object
print(SantesBilanDto.to_json())

# convert the object into a dict
santes_bilan_dto_dict = santes_bilan_dto_instance.to_dict()
# create an instance of SantesBilanDto from a dict
santes_bilan_dto_from_dict = SantesBilanDto.from_dict(santes_bilan_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


