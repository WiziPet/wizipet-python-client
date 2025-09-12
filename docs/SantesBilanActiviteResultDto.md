# SantesBilanActiviteResultDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reco_qte_session_jour** | [**SantesQteSessionJourDto**](SantesQteSessionJourDto.md) |  | [optional] 
**reco_duree_moy_session** | [**SantesDureeMoySessionDto**](SantesDureeMoySessionDto.md) |  | [optional] 
**diagnostic** | **str** |  | [optional] 
**status** | [**SantesSectionStatusDto**](SantesSectionStatusDto.md) |  | [optional] 

## Example

```python
from wizipet_api.models.santes_bilan_activite_result_dto import SantesBilanActiviteResultDto

# TODO update the JSON string below
json = "{}"
# create an instance of SantesBilanActiviteResultDto from a JSON string
santes_bilan_activite_result_dto_instance = SantesBilanActiviteResultDto.from_json(json)
# print the JSON string representation of the object
print(SantesBilanActiviteResultDto.to_json())

# convert the object into a dict
santes_bilan_activite_result_dto_dict = santes_bilan_activite_result_dto_instance.to_dict()
# create an instance of SantesBilanActiviteResultDto from a dict
santes_bilan_activite_result_dto_from_dict = SantesBilanActiviteResultDto.from_dict(santes_bilan_activite_result_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


