# GroupsGroupDto


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
**creation_date** | **datetime** |  | [optional] 

## Example

```python
from wizipet_api.models.groups_group_dto import GroupsGroupDto

# TODO update the JSON string below
json = "{}"
# create an instance of GroupsGroupDto from a JSON string
groups_group_dto_instance = GroupsGroupDto.from_json(json)
# print the JSON string representation of the object
print(GroupsGroupDto.to_json())

# convert the object into a dict
groups_group_dto_dict = groups_group_dto_instance.to_dict()
# create an instance of GroupsGroupDto from a dict
groups_group_dto_from_dict = GroupsGroupDto.from_dict(groups_group_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


