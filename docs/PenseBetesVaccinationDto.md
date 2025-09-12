# PenseBetesVaccinationDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**souche_list** | [**List[SouchesSoucheItemDto]**](SouchesSoucheItemDto.md) |  | [optional] 
**vaccin_id_list** | **List[str]** |  | [optional] 

## Example

```python
from wizipet_api.models.pense_betes_vaccination_dto import PenseBetesVaccinationDto

# TODO update the JSON string below
json = "{}"
# create an instance of PenseBetesVaccinationDto from a JSON string
pense_betes_vaccination_dto_instance = PenseBetesVaccinationDto.from_json(json)
# print the JSON string representation of the object
print(PenseBetesVaccinationDto.to_json())

# convert the object into a dict
pense_betes_vaccination_dto_dict = pense_betes_vaccination_dto_instance.to_dict()
# create an instance of PenseBetesVaccinationDto from a dict
pense_betes_vaccination_dto_from_dict = PenseBetesVaccinationDto.from_dict(pense_betes_vaccination_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


