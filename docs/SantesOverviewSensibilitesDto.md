# SantesOverviewSensibilitesDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**valeur_reference_list** | **List[str]** |  | [optional] 

## Example

```python
from wizipet_api.models.santes_overview_sensibilites_dto import SantesOverviewSensibilitesDto

# TODO update the JSON string below
json = "{}"
# create an instance of SantesOverviewSensibilitesDto from a JSON string
santes_overview_sensibilites_dto_instance = SantesOverviewSensibilitesDto.from_json(json)
# print the JSON string representation of the object
print(SantesOverviewSensibilitesDto.to_json())

# convert the object into a dict
santes_overview_sensibilites_dto_dict = santes_overview_sensibilites_dto_instance.to_dict()
# create an instance of SantesOverviewSensibilitesDto from a dict
santes_overview_sensibilites_dto_from_dict = SantesOverviewSensibilitesDto.from_dict(santes_overview_sensibilites_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


