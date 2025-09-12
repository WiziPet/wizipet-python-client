# SantesCoachingDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | [**SantesCoachingStateDto**](SantesCoachingStateDto.md) |  | [optional] 
**diagnostic** | **str** | Phrase de diagnostic du coaching en cours. | [optional] 
**poids_a_perdre_g** | **int** |  | [optional] 
**poids_debut_g** | **int** |  | [optional] 
**poids_cible_g** | **int** |  | [optional] 
**pourcentage_avancement** | **int** |  | [optional] 
**poids_avancement_g** | **int** |  | [optional] 
**start_date** | **str** |  | [optional] 
**end_date** | **str** |  | [optional] 
**aliment_principal** | [**SantesCoachingRecoAlimentDto**](SantesCoachingRecoAlimentDto.md) |  | [optional] 
**aliment_secondaire** | [**SantesCoachingRecoAlimentDto**](SantesCoachingRecoAlimentDto.md) |  | [optional] 
**reco_qte_session_jour** | [**SantesQteSessionJourDto**](SantesQteSessionJourDto.md) |  | [optional] 
**reco_duree_moy_session** | [**SantesDureeMoySessionDto**](SantesDureeMoySessionDto.md) |  | [optional] 
**poids_saisies_count** | **int** |  | [optional] 
**ration_principale_saisies_count** | **int** |  | [optional] 
**ration_principale_saisie_gramme** | **int** |  | [optional] 
**duree_session_saisies_count** | **int** |  | [optional] 
**duree_session_saisie** | **int** |  | [optional] 
**ration_secondaire_saisies_count** | **int** |  | [optional] 
**ration_secondaire_saisie_gramme** | **int** |  | [optional] 
**rythme_conseille_semaine_gramme** | **int** |  | [optional] 
**rythme_reel_semaine_gramme** | **int** |  | [optional] 
**last_pesee_date** | **str** |  | [optional] 
**duree_semaines** | **int** |  | [optional] 
**duree_jours** | **int** |  | [optional] 
**nbr_weekly_pesee** | **int** |  | [optional] 
**nbr_ration_quantite** | **int** |  | [optional] 
**nbr_activity_session** | **int** |  | [optional] 
**nbr_weekly_pesee_is_success** | **bool** |  | [optional] 
**nbr_ration_quantite_is_success** | **bool** |  | [optional] 
**nbr_activity_session_is_success** | **bool** |  | [optional] 

## Example

```python
from wizipet_api.models.santes_coaching_dto import SantesCoachingDto

# TODO update the JSON string below
json = "{}"
# create an instance of SantesCoachingDto from a JSON string
santes_coaching_dto_instance = SantesCoachingDto.from_json(json)
# print the JSON string representation of the object
print(SantesCoachingDto.to_json())

# convert the object into a dict
santes_coaching_dto_dict = santes_coaching_dto_instance.to_dict()
# create an instance of SantesCoachingDto from a dict
santes_coaching_dto_from_dict = SantesCoachingDto.from_dict(santes_coaching_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


