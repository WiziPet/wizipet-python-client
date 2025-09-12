# ListResponseDiscussionsDiscussionItemDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DiscussionsDiscussionItemDto]**](DiscussionsDiscussionItemDto.md) |  | [optional] 
**is_success** | **bool** |  | [optional] 
**error_code** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.list_response_discussions_discussion_item_dto import ListResponseDiscussionsDiscussionItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of ListResponseDiscussionsDiscussionItemDto from a JSON string
list_response_discussions_discussion_item_dto_instance = ListResponseDiscussionsDiscussionItemDto.from_json(json)
# print the JSON string representation of the object
print(ListResponseDiscussionsDiscussionItemDto.to_json())

# convert the object into a dict
list_response_discussions_discussion_item_dto_dict = list_response_discussions_discussion_item_dto_instance.to_dict()
# create an instance of ListResponseDiscussionsDiscussionItemDto from a dict
list_response_discussions_discussion_item_dto_from_dict = ListResponseDiscussionsDiscussionItemDto.from_dict(list_response_discussions_discussion_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


