# PenseBetesPatchPenseBeteDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** |  | [optional] 
**commentaire** | **str** |  | [optional] 
**type** | [**PenseBetesPenseBeteTypeDto**](PenseBetesPenseBeteTypeDto.md) |  | [optional] 
**antiparasitaire_properties** | [**PenseBetesSetPenseBeteAntiparasitaireDto**](PenseBetesSetPenseBeteAntiparasitaireDto.md) |  | [optional] 
**vermifuge_properties** | [**PenseBetesSetPenseBeteVermifugeDto**](PenseBetesSetPenseBeteVermifugeDto.md) |  | [optional] 
**vaccination_properties** | [**PenseBetesSetPenseBeteVaccinationDto**](PenseBetesSetPenseBeteVaccinationDto.md) |  | [optional] 

## Example

```python
from wizipet_api.models.pense_betes_patch_pense_bete_dto import PenseBetesPatchPenseBeteDto

# TODO update the JSON string below
json = "{}"
# create an instance of PenseBetesPatchPenseBeteDto from a JSON string
pense_betes_patch_pense_bete_dto_instance = PenseBetesPatchPenseBeteDto.from_json(json)
# print the JSON string representation of the object
print(PenseBetesPatchPenseBeteDto.to_json())

# convert the object into a dict
pense_betes_patch_pense_bete_dto_dict = pense_betes_patch_pense_bete_dto_instance.to_dict()
# create an instance of PenseBetesPatchPenseBeteDto from a dict
pense_betes_patch_pense_bete_dto_from_dict = PenseBetesPatchPenseBeteDto.from_dict(pense_betes_patch_pense_bete_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


