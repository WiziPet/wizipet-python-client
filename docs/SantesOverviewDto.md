# SantesOverviewDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**physio** | [**SantesOverviewPhysioDto**](SantesOverviewPhysioDto.md) |  | [optional] 
**sterilisation** | [**SantesSterilisationDto**](SantesSterilisationDto.md) |  | [optional] 
**sensibilites** | [**SantesOverviewSensibilitesDto**](SantesOverviewSensibilitesDto.md) |  | [optional] 
**identifiant** | [**SantesIdentifiantDto**](SantesIdentifiantDto.md) |  | [optional] 
**veterinaire** | [**SantesVeterinaireDto**](SantesVeterinaireDto.md) |  | [optional] 
**assurance** | [**SantesAssuranceDto**](SantesAssuranceDto.md) |  | [optional] 

## Example

```python
from wizipet_api.models.santes_overview_dto import SantesOverviewDto

# TODO update the JSON string below
json = "{}"
# create an instance of SantesOverviewDto from a JSON string
santes_overview_dto_instance = SantesOverviewDto.from_json(json)
# print the JSON string representation of the object
print(SantesOverviewDto.to_json())

# convert the object into a dict
santes_overview_dto_dict = santes_overview_dto_instance.to_dict()
# create an instance of SantesOverviewDto from a dict
santes_overview_dto_from_dict = SantesOverviewDto.from_dict(santes_overview_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


