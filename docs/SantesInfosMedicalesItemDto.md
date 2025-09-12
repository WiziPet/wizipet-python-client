# SantesInfosMedicalesItemDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | [**SantesInfosMedicalesCategoryDto**](SantesInfosMedicalesCategoryDto.md) |  | [optional] 
**last_item_start_date** | **str** |  | [optional] 
**last_item_name** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.santes_infos_medicales_item_dto import SantesInfosMedicalesItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of SantesInfosMedicalesItemDto from a JSON string
santes_infos_medicales_item_dto_instance = SantesInfosMedicalesItemDto.from_json(json)
# print the JSON string representation of the object
print(SantesInfosMedicalesItemDto.to_json())

# convert the object into a dict
santes_infos_medicales_item_dto_dict = santes_infos_medicales_item_dto_instance.to_dict()
# create an instance of SantesInfosMedicalesItemDto from a dict
santes_infos_medicales_item_dto_from_dict = SantesInfosMedicalesItemDto.from_dict(santes_infos_medicales_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


