# DiscussionsDiscussionItemDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**picture_id** | **str** |  | [optional] 
**participant_count** | **int** |  | [optional] 
**creation_date** | **datetime** |  | [optional] 
**last_message** | [**DiscussionsMessageSummaryDto**](DiscussionsMessageSummaryDto.md) |  | [optional] 
**last_read_message_creation_date** | **datetime** |  | [optional] 
**random_participant** | [**ProfilesDiscussionParticipantDto**](ProfilesDiscussionParticipantDto.md) |  | [optional] 

## Example

```python
from wizipet_api.models.discussions_discussion_item_dto import DiscussionsDiscussionItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of DiscussionsDiscussionItemDto from a JSON string
discussions_discussion_item_dto_instance = DiscussionsDiscussionItemDto.from_json(json)
# print the JSON string representation of the object
print(DiscussionsDiscussionItemDto.to_json())

# convert the object into a dict
discussions_discussion_item_dto_dict = discussions_discussion_item_dto_instance.to_dict()
# create an instance of DiscussionsDiscussionItemDto from a dict
discussions_discussion_item_dto_from_dict = DiscussionsDiscussionItemDto.from_dict(discussions_discussion_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


