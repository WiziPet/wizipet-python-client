# SantesBilanPoidsResultDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**poids_actuel_g** | **int** |  | [optional] 
**poids_a_perdre_g** | **int** |  | [optional] 
**poids_cible_g** | **int** |  | [optional] 
**poids_state** | [**SantesPoidsStateDto**](SantesPoidsStateDto.md) |  | [optional] 
**reco_duree_semaine** | **int** | En Semaine | [optional] 
**reco_rythme_g_semaine** | **int** | En g/semaine | [optional] 
**diagnostic** | **str** |  | [optional] 
**status** | [**SantesSectionStatusDto**](SantesSectionStatusDto.md) |  | [optional] 

## Example

```python
from wizipet_api.models.santes_bilan_poids_result_dto import SantesBilanPoidsResultDto

# TODO update the JSON string below
json = "{}"
# create an instance of SantesBilanPoidsResultDto from a JSON string
santes_bilan_poids_result_dto_instance = SantesBilanPoidsResultDto.from_json(json)
# print the JSON string representation of the object
print(SantesBilanPoidsResultDto.to_json())

# convert the object into a dict
santes_bilan_poids_result_dto_dict = santes_bilan_poids_result_dto_instance.to_dict()
# create an instance of SantesBilanPoidsResultDto from a dict
santes_bilan_poids_result_dto_from_dict = SantesBilanPoidsResultDto.from_dict(santes_bilan_poids_result_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


