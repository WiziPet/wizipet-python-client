# PenseBetesSicknessItemDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**traitement_list** | [**List[PenseBetesTraitementItemDto]**](PenseBetesTraitementItemDto.md) |  | [optional] 

## Example

```python
from wizipet_api.models.pense_betes_sickness_item_dto import PenseBetesSicknessItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of PenseBetesSicknessItemDto from a JSON string
pense_betes_sickness_item_dto_instance = PenseBetesSicknessItemDto.from_json(json)
# print the JSON string representation of the object
print(PenseBetesSicknessItemDto.to_json())

# convert the object into a dict
pense_betes_sickness_item_dto_dict = pense_betes_sickness_item_dto_instance.to_dict()
# create an instance of PenseBetesSicknessItemDto from a dict
pense_betes_sickness_item_dto_from_dict = PenseBetesSicknessItemDto.from_dict(pense_betes_sickness_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


