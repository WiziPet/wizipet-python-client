# DiscussionsPostMessageDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.discussions_post_message_dto import DiscussionsPostMessageDto

# TODO update the JSON string below
json = "{}"
# create an instance of DiscussionsPostMessageDto from a JSON string
discussions_post_message_dto_instance = DiscussionsPostMessageDto.from_json(json)
# print the JSON string representation of the object
print(DiscussionsPostMessageDto.to_json())

# convert the object into a dict
discussions_post_message_dto_dict = discussions_post_message_dto_instance.to_dict()
# create an instance of DiscussionsPostMessageDto from a dict
discussions_post_message_dto_from_dict = DiscussionsPostMessageDto.from_dict(discussions_post_message_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


