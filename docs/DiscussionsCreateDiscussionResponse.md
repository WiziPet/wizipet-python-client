# DiscussionsCreateDiscussionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duo_discussion_already_exists** | **bool** |  | [optional] 
**data** | [**DiscussionsDiscussionDto**](DiscussionsDiscussionDto.md) |  | [optional] 
**is_success** | **bool** |  | [optional] 
**error_code** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.discussions_create_discussion_response import DiscussionsCreateDiscussionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DiscussionsCreateDiscussionResponse from a JSON string
discussions_create_discussion_response_instance = DiscussionsCreateDiscussionResponse.from_json(json)
# print the JSON string representation of the object
print(DiscussionsCreateDiscussionResponse.to_json())

# convert the object into a dict
discussions_create_discussion_response_dict = discussions_create_discussion_response_instance.to_dict()
# create an instance of DiscussionsCreateDiscussionResponse from a dict
discussions_create_discussion_response_from_dict = DiscussionsCreateDiscussionResponse.from_dict(discussions_create_discussion_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


