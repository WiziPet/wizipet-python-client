# SantesInfoDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clef** | [**SantesClefInfoDto**](SantesClefInfoDto.md) |  | [optional] 
**valeur_bool** | **bool** |  | [optional] 
**valeur_date** | **str** |  | [optional] 
**valeur_int** | **int** |  | [optional] 
**valeur_aliment** | [**SantesAlimentDto**](SantesAlimentDto.md) |  | [optional] 
**valeur_nbr_repas** | [**SantesNombreRepasDto**](SantesNombreRepasDto.md) |  | [optional] 
**valeur_qte_friandise** | [**SantesQteFriandiseDto**](SantesQteFriandiseDto.md) |  | [optional] 
**valeur_qte_session_jour** | [**SantesQteSessionJourDto**](SantesQteSessionJourDto.md) |  | [optional] 
**valeur_duree_moy_session** | [**SantesDureeMoySessionDto**](SantesDureeMoySessionDto.md) |  | [optional] 
**valeur_reference_list** | **List[str]** |  | [optional] 

## Example

```python
from wizipet_api.models.santes_info_dto import SantesInfoDto

# TODO update the JSON string below
json = "{}"
# create an instance of SantesInfoDto from a JSON string
santes_info_dto_instance = SantesInfoDto.from_json(json)
# print the JSON string representation of the object
print(SantesInfoDto.to_json())

# convert the object into a dict
santes_info_dto_dict = santes_info_dto_instance.to_dict()
# create an instance of SantesInfoDto from a dict
santes_info_dto_from_dict = SantesInfoDto.from_dict(santes_info_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


