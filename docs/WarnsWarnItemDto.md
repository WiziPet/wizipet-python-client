# WarnsWarnItemDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | [**WarnsWarnTypeDto**](WarnsWarnTypeDto.md) |  | [optional] 
**group_properties** | [**WarnsWarnItemGroupDto**](WarnsWarnItemGroupDto.md) |  | [optional] 

## Example

```python
from wizipet_api.models.warns_warn_item_dto import WarnsWarnItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of WarnsWarnItemDto from a JSON string
warns_warn_item_dto_instance = WarnsWarnItemDto.from_json(json)
# print the JSON string representation of the object
print(WarnsWarnItemDto.to_json())

# convert the object into a dict
warns_warn_item_dto_dict = warns_warn_item_dto_instance.to_dict()
# create an instance of WarnsWarnItemDto from a dict
warns_warn_item_dto_from_dict = WarnsWarnItemDto.from_dict(warns_warn_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


