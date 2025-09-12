# ListResponseGroupsGroupItemDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[GroupsGroupItemDto]**](GroupsGroupItemDto.md) |  | [optional] 
**is_success** | **bool** |  | [optional] 
**error_code** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.list_response_groups_group_item_dto import ListResponseGroupsGroupItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of ListResponseGroupsGroupItemDto from a JSON string
list_response_groups_group_item_dto_instance = ListResponseGroupsGroupItemDto.from_json(json)
# print the JSON string representation of the object
print(ListResponseGroupsGroupItemDto.to_json())

# convert the object into a dict
list_response_groups_group_item_dto_dict = list_response_groups_group_item_dto_instance.to_dict()
# create an instance of ListResponseGroupsGroupItemDto from a dict
list_response_groups_group_item_dto_from_dict = ListResponseGroupsGroupItemDto.from_dict(list_response_groups_group_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


