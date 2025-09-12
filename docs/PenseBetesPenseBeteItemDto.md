# PenseBetesPenseBeteItemDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | [**PenseBetesPenseBeteTypeDto**](PenseBetesPenseBeteTypeDto.md) |  | [optional] 
**var_date** | **str** |  | [optional] 
**commentaire** | **str** |  | [optional] 
**operation_properties** | [**PenseBetesOperationItemDto**](PenseBetesOperationItemDto.md) |  | [optional] 
**sickness_properties** | [**PenseBetesSicknessItemDto**](PenseBetesSicknessItemDto.md) |  | [optional] 
**vaccination_properties** | [**PenseBetesVaccinationItemDto**](PenseBetesVaccinationItemDto.md) |  | [optional] 

## Example

```python
from wizipet_api.models.pense_betes_pense_bete_item_dto import PenseBetesPenseBeteItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of PenseBetesPenseBeteItemDto from a JSON string
pense_betes_pense_bete_item_dto_instance = PenseBetesPenseBeteItemDto.from_json(json)
# print the JSON string representation of the object
print(PenseBetesPenseBeteItemDto.to_json())

# convert the object into a dict
pense_betes_pense_bete_item_dto_dict = pense_betes_pense_bete_item_dto_instance.to_dict()
# create an instance of PenseBetesPenseBeteItemDto from a dict
pense_betes_pense_bete_item_dto_from_dict = PenseBetesPenseBeteItemDto.from_dict(pense_betes_pense_bete_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


