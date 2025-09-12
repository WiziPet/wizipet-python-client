# WarnsWarnItemGroupDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**old_name** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.warns_warn_item_group_dto import WarnsWarnItemGroupDto

# TODO update the JSON string below
json = "{}"
# create an instance of WarnsWarnItemGroupDto from a JSON string
warns_warn_item_group_dto_instance = WarnsWarnItemGroupDto.from_json(json)
# print the JSON string representation of the object
print(WarnsWarnItemGroupDto.to_json())

# convert the object into a dict
warns_warn_item_group_dto_dict = warns_warn_item_group_dto_instance.to_dict()
# create an instance of WarnsWarnItemGroupDto from a dict
warns_warn_item_group_dto_from_dict = WarnsWarnItemGroupDto.from_dict(warns_warn_item_group_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


