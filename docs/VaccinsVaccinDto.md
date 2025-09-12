# VaccinsVaccinDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**espece** | [**ProfilesEspeceDto**](ProfilesEspeceDto.md) |  | [optional] 
**souches** | [**List[SouchesSoucheItemDto]**](SouchesSoucheItemDto.md) |  | [optional] 

## Example

```python
from wizipet_api.models.vaccins_vaccin_dto import VaccinsVaccinDto

# TODO update the JSON string below
json = "{}"
# create an instance of VaccinsVaccinDto from a JSON string
vaccins_vaccin_dto_instance = VaccinsVaccinDto.from_json(json)
# print the JSON string representation of the object
print(VaccinsVaccinDto.to_json())

# convert the object into a dict
vaccins_vaccin_dto_dict = vaccins_vaccin_dto_instance.to_dict()
# create an instance of VaccinsVaccinDto from a dict
vaccins_vaccin_dto_from_dict = VaccinsVaccinDto.from_dict(vaccins_vaccin_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


