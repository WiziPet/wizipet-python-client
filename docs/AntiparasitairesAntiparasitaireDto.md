# AntiparasitairesAntiparasitaireDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**espece** | [**ProfilesEspeceDto**](ProfilesEspeceDto.md) |  | [optional] 

## Example

```python
from wizipet_api.models.antiparasitaires_antiparasitaire_dto import AntiparasitairesAntiparasitaireDto

# TODO update the JSON string below
json = "{}"
# create an instance of AntiparasitairesAntiparasitaireDto from a JSON string
antiparasitaires_antiparasitaire_dto_instance = AntiparasitairesAntiparasitaireDto.from_json(json)
# print the JSON string representation of the object
print(AntiparasitairesAntiparasitaireDto.to_json())

# convert the object into a dict
antiparasitaires_antiparasitaire_dto_dict = antiparasitaires_antiparasitaire_dto_instance.to_dict()
# create an instance of AntiparasitairesAntiparasitaireDto from a dict
antiparasitaires_antiparasitaire_dto_from_dict = AntiparasitairesAntiparasitaireDto.from_dict(antiparasitaires_antiparasitaire_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


