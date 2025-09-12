# ListResponseWarnsWarnItemDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[WarnsWarnItemDto]**](WarnsWarnItemDto.md) |  | [optional] 
**is_success** | **bool** |  | [optional] 
**error_code** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.list_response_warns_warn_item_dto import ListResponseWarnsWarnItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of ListResponseWarnsWarnItemDto from a JSON string
list_response_warns_warn_item_dto_instance = ListResponseWarnsWarnItemDto.from_json(json)
# print the JSON string representation of the object
print(ListResponseWarnsWarnItemDto.to_json())

# convert the object into a dict
list_response_warns_warn_item_dto_dict = list_response_warns_warn_item_dto_instance.to_dict()
# create an instance of ListResponseWarnsWarnItemDto from a dict
list_response_warns_warn_item_dto_from_dict = ListResponseWarnsWarnItemDto.from_dict(list_response_warns_warn_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


