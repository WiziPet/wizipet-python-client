# GroupsUpdateGroupDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ville** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**picture_id** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.groups_update_group_dto import GroupsUpdateGroupDto

# TODO update the JSON string below
json = "{}"
# create an instance of GroupsUpdateGroupDto from a JSON string
groups_update_group_dto_instance = GroupsUpdateGroupDto.from_json(json)
# print the JSON string representation of the object
print(GroupsUpdateGroupDto.to_json())

# convert the object into a dict
groups_update_group_dto_dict = groups_update_group_dto_instance.to_dict()
# create an instance of GroupsUpdateGroupDto from a dict
groups_update_group_dto_from_dict = GroupsUpdateGroupDto.from_dict(groups_update_group_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


