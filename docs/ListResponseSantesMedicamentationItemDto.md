# ListResponseSantesMedicamentationItemDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SantesMedicamentationItemDto]**](SantesMedicamentationItemDto.md) |  | [optional] 
**is_success** | **bool** |  | [optional] 
**error_code** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.list_response_santes_medicamentation_item_dto import ListResponseSantesMedicamentationItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of ListResponseSantesMedicamentationItemDto from a JSON string
list_response_santes_medicamentation_item_dto_instance = ListResponseSantesMedicamentationItemDto.from_json(json)
# print the JSON string representation of the object
print(ListResponseSantesMedicamentationItemDto.to_json())

# convert the object into a dict
list_response_santes_medicamentation_item_dto_dict = list_response_santes_medicamentation_item_dto_instance.to_dict()
# create an instance of ListResponseSantesMedicamentationItemDto from a dict
list_response_santes_medicamentation_item_dto_from_dict = ListResponseSantesMedicamentationItemDto.from_dict(list_response_santes_medicamentation_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


