# VaccinsListVaccinDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vaccin_list** | [**List[VaccinsVaccinDto]**](VaccinsVaccinDto.md) |  | [optional] 

## Example

```python
from wizipet_api.models.vaccins_list_vaccin_dto import VaccinsListVaccinDto

# TODO update the JSON string below
json = "{}"
# create an instance of VaccinsListVaccinDto from a JSON string
vaccins_list_vaccin_dto_instance = VaccinsListVaccinDto.from_json(json)
# print the JSON string representation of the object
print(VaccinsListVaccinDto.to_json())

# convert the object into a dict
vaccins_list_vaccin_dto_dict = vaccins_list_vaccin_dto_instance.to_dict()
# create an instance of VaccinsListVaccinDto from a dict
vaccins_list_vaccin_dto_from_dict = VaccinsListVaccinDto.from_dict(vaccins_list_vaccin_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


