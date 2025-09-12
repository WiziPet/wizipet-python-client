# DiscussionsDiscussionDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**picture_id** | **str** |  | [optional] 
**participant_list** | [**List[ProfilesDiscussionParticipantDto]**](ProfilesDiscussionParticipantDto.md) |  | [optional] 
**creation_date** | **datetime** |  | [optional] 
**last_message_date** | **datetime** |  | [optional] 
**random_participant** | [**ProfilesDiscussionParticipantDto**](ProfilesDiscussionParticipantDto.md) |  | [optional] 

## Example

```python
from wizipet_api.models.discussions_discussion_dto import DiscussionsDiscussionDto

# TODO update the JSON string below
json = "{}"
# create an instance of DiscussionsDiscussionDto from a JSON string
discussions_discussion_dto_instance = DiscussionsDiscussionDto.from_json(json)
# print the JSON string representation of the object
print(DiscussionsDiscussionDto.to_json())

# convert the object into a dict
discussions_discussion_dto_dict = discussions_discussion_dto_instance.to_dict()
# create an instance of DiscussionsDiscussionDto from a dict
discussions_discussion_dto_from_dict = DiscussionsDiscussionDto.from_dict(discussions_discussion_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


