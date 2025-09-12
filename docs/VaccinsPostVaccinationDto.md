# VaccinsPostVaccinationDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** |  | [optional] 
**commentaire** | **str** |  | [optional] 
**vaccin_id_list** | **List[str]** |  | [optional] 
**vaccin_protocol** | [**VaccinsVaccinProtocolDto**](VaccinsVaccinProtocolDto.md) |  | [optional] 

## Example

```python
from wizipet_api.models.vaccins_post_vaccination_dto import VaccinsPostVaccinationDto

# TODO update the JSON string below
json = "{}"
# create an instance of VaccinsPostVaccinationDto from a JSON string
vaccins_post_vaccination_dto_instance = VaccinsPostVaccinationDto.from_json(json)
# print the JSON string representation of the object
print(VaccinsPostVaccinationDto.to_json())

# convert the object into a dict
vaccins_post_vaccination_dto_dict = vaccins_post_vaccination_dto_instance.to_dict()
# create an instance of VaccinsPostVaccinationDto from a dict
vaccins_post_vaccination_dto_from_dict = VaccinsPostVaccinationDto.from_dict(vaccins_post_vaccination_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


