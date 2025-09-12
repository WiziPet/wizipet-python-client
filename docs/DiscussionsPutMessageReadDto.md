# DiscussionsPutMessageReadDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_read_message_creation_date** | **datetime** |  | [optional] 

## Example

```python
from wizipet_api.models.discussions_put_message_read_dto import DiscussionsPutMessageReadDto

# TODO update the JSON string below
json = "{}"
# create an instance of DiscussionsPutMessageReadDto from a JSON string
discussions_put_message_read_dto_instance = DiscussionsPutMessageReadDto.from_json(json)
# print the JSON string representation of the object
print(DiscussionsPutMessageReadDto.to_json())

# convert the object into a dict
discussions_put_message_read_dto_dict = discussions_put_message_read_dto_instance.to_dict()
# create an instance of DiscussionsPutMessageReadDto from a dict
discussions_put_message_read_dto_from_dict = DiscussionsPutMessageReadDto.from_dict(discussions_put_message_read_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


