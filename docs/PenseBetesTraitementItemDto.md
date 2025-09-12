# PenseBetesTraitementItemDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**start_date** | **str** |  | [optional] 
**end_date** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.pense_betes_traitement_item_dto import PenseBetesTraitementItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of PenseBetesTraitementItemDto from a JSON string
pense_betes_traitement_item_dto_instance = PenseBetesTraitementItemDto.from_json(json)
# print the JSON string representation of the object
print(PenseBetesTraitementItemDto.to_json())

# convert the object into a dict
pense_betes_traitement_item_dto_dict = pense_betes_traitement_item_dto_instance.to_dict()
# create an instance of PenseBetesTraitementItemDto from a dict
pense_betes_traitement_item_dto_from_dict = PenseBetesTraitementItemDto.from_dict(pense_betes_traitement_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


