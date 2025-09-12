# DiscussionsMessageSummaryDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** |  | [optional] 
**creation_date** | **datetime** |  | [optional] 

## Example

```python
from wizipet_api.models.discussions_message_summary_dto import DiscussionsMessageSummaryDto

# TODO update the JSON string below
json = "{}"
# create an instance of DiscussionsMessageSummaryDto from a JSON string
discussions_message_summary_dto_instance = DiscussionsMessageSummaryDto.from_json(json)
# print the JSON string representation of the object
print(DiscussionsMessageSummaryDto.to_json())

# convert the object into a dict
discussions_message_summary_dto_dict = discussions_message_summary_dto_instance.to_dict()
# create an instance of DiscussionsMessageSummaryDto from a dict
discussions_message_summary_dto_from_dict = DiscussionsMessageSummaryDto.from_dict(discussions_message_summary_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


