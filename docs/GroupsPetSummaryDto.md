# GroupsPetSummaryDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**picture_id** | **str** |  | [optional] 
**race_id** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.groups_pet_summary_dto import GroupsPetSummaryDto

# TODO update the JSON string below
json = "{}"
# create an instance of GroupsPetSummaryDto from a JSON string
groups_pet_summary_dto_instance = GroupsPetSummaryDto.from_json(json)
# print the JSON string representation of the object
print(GroupsPetSummaryDto.to_json())

# convert the object into a dict
groups_pet_summary_dto_dict = groups_pet_summary_dto_instance.to_dict()
# create an instance of GroupsPetSummaryDto from a dict
groups_pet_summary_dto_from_dict = GroupsPetSummaryDto.from_dict(groups_pet_summary_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


