# ResumableListResponseDiscussionsMessageDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_more** | **bool** |  | [optional] 
**count** | **int** |  | [optional] 
**continuation_token** | **str** |  | [optional] 
**data** | [**List[DiscussionsMessageDto]**](DiscussionsMessageDto.md) |  | [optional] 
**is_success** | **bool** |  | [optional] 
**error_code** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.resumable_list_response_discussions_message_dto import ResumableListResponseDiscussionsMessageDto

# TODO update the JSON string below
json = "{}"
# create an instance of ResumableListResponseDiscussionsMessageDto from a JSON string
resumable_list_response_discussions_message_dto_instance = ResumableListResponseDiscussionsMessageDto.from_json(json)
# print the JSON string representation of the object
print(ResumableListResponseDiscussionsMessageDto.to_json())

# convert the object into a dict
resumable_list_response_discussions_message_dto_dict = resumable_list_response_discussions_message_dto_instance.to_dict()
# create an instance of ResumableListResponseDiscussionsMessageDto from a dict
resumable_list_response_discussions_message_dto_from_dict = ResumableListResponseDiscussionsMessageDto.from_dict(resumable_list_response_discussions_message_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


