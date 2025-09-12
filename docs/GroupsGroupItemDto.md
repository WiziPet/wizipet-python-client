# GroupsGroupItemDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**ville** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**picture_id** | **str** |  | [optional] 
**is_author** | **bool** |  | [optional] 
**is_subscribed** | **bool** |  | [optional] 
**is_highlighted** | **bool** |  | [optional] 
**member_count** | **int** |  | [optional] 
**member_list_overview** | [**List[GroupsPetSummaryDto]**](GroupsPetSummaryDto.md) |  | [optional] 

## Example

```python
from wizipet_api.models.groups_group_item_dto import GroupsGroupItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of GroupsGroupItemDto from a JSON string
groups_group_item_dto_instance = GroupsGroupItemDto.from_json(json)
# print the JSON string representation of the object
print(GroupsGroupItemDto.to_json())

# convert the object into a dict
groups_group_item_dto_dict = groups_group_item_dto_instance.to_dict()
# create an instance of GroupsGroupItemDto from a dict
groups_group_item_dto_from_dict = GroupsGroupItemDto.from_dict(groups_group_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


