# GroupsCreateGroupDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**ville** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**picture_id** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.groups_create_group_dto import GroupsCreateGroupDto

# TODO update the JSON string below
json = "{}"
# create an instance of GroupsCreateGroupDto from a JSON string
groups_create_group_dto_instance = GroupsCreateGroupDto.from_json(json)
# print the JSON string representation of the object
print(GroupsCreateGroupDto.to_json())

# convert the object into a dict
groups_create_group_dto_dict = groups_create_group_dto_instance.to_dict()
# create an instance of GroupsCreateGroupDto from a dict
groups_create_group_dto_from_dict = GroupsCreateGroupDto.from_dict(groups_create_group_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


