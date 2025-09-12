# CreateReplyDto

Généric, minimal response for a post.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.create_reply_dto import CreateReplyDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateReplyDto from a JSON string
create_reply_dto_instance = CreateReplyDto.from_json(json)
# print the JSON string representation of the object
print(CreateReplyDto.to_json())

# convert the object into a dict
create_reply_dto_dict = create_reply_dto_instance.to_dict()
# create an instance of CreateReplyDto from a dict
create_reply_dto_from_dict = CreateReplyDto.from_dict(create_reply_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


