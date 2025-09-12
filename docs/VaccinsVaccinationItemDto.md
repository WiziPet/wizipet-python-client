# VaccinsVaccinationItemDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**var_date** | **str** |  | [optional] 
**commentaire** | **str** |  | [optional] 
**vaccin_id** | **str** |  | [optional] 
**vaccin_protocol** | [**VaccinsVaccinProtocolDto**](VaccinsVaccinProtocolDto.md) |  | [optional] 

## Example

```python
from wizipet_api.models.vaccins_vaccination_item_dto import VaccinsVaccinationItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of VaccinsVaccinationItemDto from a JSON string
vaccins_vaccination_item_dto_instance = VaccinsVaccinationItemDto.from_json(json)
# print the JSON string representation of the object
print(VaccinsVaccinationItemDto.to_json())

# convert the object into a dict
vaccins_vaccination_item_dto_dict = vaccins_vaccination_item_dto_instance.to_dict()
# create an instance of VaccinsVaccinationItemDto from a dict
vaccins_vaccination_item_dto_from_dict = VaccinsVaccinationItemDto.from_dict(vaccins_vaccination_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


