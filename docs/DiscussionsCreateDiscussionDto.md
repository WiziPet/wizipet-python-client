# DiscussionsCreateDiscussionDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**participant_id_list** | **List[str]** | Liste de PetId. | [optional] 
**picture_id** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.discussions_create_discussion_dto import DiscussionsCreateDiscussionDto

# TODO update the JSON string below
json = "{}"
# create an instance of DiscussionsCreateDiscussionDto from a JSON string
discussions_create_discussion_dto_instance = DiscussionsCreateDiscussionDto.from_json(json)
# print the JSON string representation of the object
print(DiscussionsCreateDiscussionDto.to_json())

# convert the object into a dict
discussions_create_discussion_dto_dict = discussions_create_discussion_dto_instance.to_dict()
# create an instance of DiscussionsCreateDiscussionDto from a dict
discussions_create_discussion_dto_from_dict = DiscussionsCreateDiscussionDto.from_dict(discussions_create_discussion_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


