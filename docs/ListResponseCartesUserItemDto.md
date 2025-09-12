# ListResponseCartesUserItemDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CartesUserItemDto]**](CartesUserItemDto.md) |  | [optional] 
**is_success** | **bool** |  | [optional] 
**error_code** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.list_response_cartes_user_item_dto import ListResponseCartesUserItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of ListResponseCartesUserItemDto from a JSON string
list_response_cartes_user_item_dto_instance = ListResponseCartesUserItemDto.from_json(json)
# print the JSON string representation of the object
print(ListResponseCartesUserItemDto.to_json())

# convert the object into a dict
list_response_cartes_user_item_dto_dict = list_response_cartes_user_item_dto_instance.to_dict()
# create an instance of ListResponseCartesUserItemDto from a dict
list_response_cartes_user_item_dto_from_dict = ListResponseCartesUserItemDto.from_dict(list_response_cartes_user_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


