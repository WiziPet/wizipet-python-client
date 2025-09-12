# PenseBetesPenseBeteDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | [**PenseBetesPenseBeteTypeDto**](PenseBetesPenseBeteTypeDto.md) |  | [optional] 
**var_date** | **str** |  | [optional] 
**commentaire** | **str** |  | [optional] 
**antiparasitaire_properties** | [**PenseBetesAntiparasitaireDto**](PenseBetesAntiparasitaireDto.md) |  | [optional] 
**vermifuge_properties** | [**PenseBetesVermifugeDto**](PenseBetesVermifugeDto.md) |  | [optional] 
**vaccination_properties** | [**PenseBetesVaccinationDto**](PenseBetesVaccinationDto.md) |  | [optional] 

## Example

```python
from wizipet_api.models.pense_betes_pense_bete_dto import PenseBetesPenseBeteDto

# TODO update the JSON string below
json = "{}"
# create an instance of PenseBetesPenseBeteDto from a JSON string
pense_betes_pense_bete_dto_instance = PenseBetesPenseBeteDto.from_json(json)
# print the JSON string representation of the object
print(PenseBetesPenseBeteDto.to_json())

# convert the object into a dict
pense_betes_pense_bete_dto_dict = pense_betes_pense_bete_dto_instance.to_dict()
# create an instance of PenseBetesPenseBeteDto from a dict
pense_betes_pense_bete_dto_from_dict = PenseBetesPenseBeteDto.from_dict(pense_betes_pense_bete_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


