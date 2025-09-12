# SantesSetInfoDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clef** | [**SantesClefInfoDto**](SantesClefInfoDto.md) |  | [optional] 
**valeur_bool** | **bool** |  | [optional] 
**valeur_date** | **str** |  | [optional] 
**valeur_int** | **int** |  | [optional] 
**valeur_aliment** | [**SantesSetAlimentDto**](SantesSetAlimentDto.md) |  | [optional] 
**valeur_nbr_repas** | [**SantesNombreRepasDto**](SantesNombreRepasDto.md) |  | [optional] 
**valeur_qte_friandise** | [**SantesQteFriandiseDto**](SantesQteFriandiseDto.md) |  | [optional] 
**valeur_qte_session_jour** | [**SantesQteSessionJourDto**](SantesQteSessionJourDto.md) |  | [optional] 
**valeur_duree_moy_session** | [**SantesDureeMoySessionDto**](SantesDureeMoySessionDto.md) |  | [optional] 
**valeur_reference_list** | **List[str]** |  | [optional] 

## Example

```python
from wizipet_api.models.santes_set_info_dto import SantesSetInfoDto

# TODO update the JSON string below
json = "{}"
# create an instance of SantesSetInfoDto from a JSON string
santes_set_info_dto_instance = SantesSetInfoDto.from_json(json)
# print the JSON string representation of the object
print(SantesSetInfoDto.to_json())

# convert the object into a dict
santes_set_info_dto_dict = santes_set_info_dto_instance.to_dict()
# create an instance of SantesSetInfoDto from a dict
santes_set_info_dto_from_dict = SantesSetInfoDto.from_dict(santes_set_info_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


