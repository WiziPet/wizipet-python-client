# ListResponseSantesSicknessItemDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SantesSicknessItemDto]**](SantesSicknessItemDto.md) |  | [optional] 
**is_success** | **bool** |  | [optional] 
**error_code** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.list_response_santes_sickness_item_dto import ListResponseSantesSicknessItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of ListResponseSantesSicknessItemDto from a JSON string
list_response_santes_sickness_item_dto_instance = ListResponseSantesSicknessItemDto.from_json(json)
# print the JSON string representation of the object
print(ListResponseSantesSicknessItemDto.to_json())

# convert the object into a dict
list_response_santes_sickness_item_dto_dict = list_response_santes_sickness_item_dto_instance.to_dict()
# create an instance of ListResponseSantesSicknessItemDto from a dict
list_response_santes_sickness_item_dto_from_dict = ListResponseSantesSicknessItemDto.from_dict(list_response_santes_sickness_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


