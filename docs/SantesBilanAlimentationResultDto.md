# SantesBilanAlimentationResultDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aer** | **int** | Apport énergétique actuel. Somme des apports énergétique de l&#39;aliment 1 et 2.  En Kcal | [optional] 
**reco_dose** | **int** | Dose recommandée.  En Kcal | [optional] 
**rpc** | **float** | Rapport protido-calorique de l&#39;aliment principal.  En g/Mcal | [optional] 
**reco_aliment_list** | [**List[SantesRecoAlimentCatalogueItemDto]**](SantesRecoAlimentCatalogueItemDto.md) | Liste des recommandation d&#39;aliment. Peut contenir 3 à 5 aliments (3 si l&#39;aliment principal &#x3D;&#x3D; recommandation 1; 4 ou 5 sinon)                Recommandation 1:  Aliment de la marque de l&#39;aliment principal et de la gamme \&quot;Obésité\&quot; ou \&quot;SurPoids\&quot; en fonction de l&#39;état de l&#39;animal.  Recommandation 2 et 3:  Aliments non utilisés actuellement et de la gamme \&quot;Obésité\&quot; ou \&quot;SurPoids\&quot; en fonction de l&#39;état de l&#39;animal. | [optional] 
**qte_friandise** | [**SantesQteFriandiseDto**](SantesQteFriandiseDto.md) |  | [optional] 
**alimentation_status** | [**SantesAlimentationStatusDto**](SantesAlimentationStatusDto.md) |  | [optional] 
**last_update** | **datetime** |  | [optional] 
**diagnostic** | **str** |  | [optional] 
**status** | [**SantesSectionStatusDto**](SantesSectionStatusDto.md) |  | [optional] 

## Example

```python
from wizipet_api.models.santes_bilan_alimentation_result_dto import SantesBilanAlimentationResultDto

# TODO update the JSON string below
json = "{}"
# create an instance of SantesBilanAlimentationResultDto from a JSON string
santes_bilan_alimentation_result_dto_instance = SantesBilanAlimentationResultDto.from_json(json)
# print the JSON string representation of the object
print(SantesBilanAlimentationResultDto.to_json())

# convert the object into a dict
santes_bilan_alimentation_result_dto_dict = santes_bilan_alimentation_result_dto_instance.to_dict()
# create an instance of SantesBilanAlimentationResultDto from a dict
santes_bilan_alimentation_result_dto_from_dict = SantesBilanAlimentationResultDto.from_dict(santes_bilan_alimentation_result_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


