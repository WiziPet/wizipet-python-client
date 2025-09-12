# PenseBetesVaccinationItemDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**souche_list** | [**List[SouchesSoucheItemDto]**](SouchesSoucheItemDto.md) |  | [optional] 

## Example

```python
from wizipet_api.models.pense_betes_vaccination_item_dto import PenseBetesVaccinationItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of PenseBetesVaccinationItemDto from a JSON string
pense_betes_vaccination_item_dto_instance = PenseBetesVaccinationItemDto.from_json(json)
# print the JSON string representation of the object
print(PenseBetesVaccinationItemDto.to_json())

# convert the object into a dict
pense_betes_vaccination_item_dto_dict = pense_betes_vaccination_item_dto_instance.to_dict()
# create an instance of PenseBetesVaccinationItemDto from a dict
pense_betes_vaccination_item_dto_from_dict = PenseBetesVaccinationItemDto.from_dict(pense_betes_vaccination_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


