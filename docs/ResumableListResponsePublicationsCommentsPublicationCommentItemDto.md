# ResumableListResponsePublicationsCommentsPublicationCommentItemDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_more** | **bool** |  | [optional] 
**count** | **int** |  | [optional] 
**continuation_token** | **str** |  | [optional] 
**data** | [**List[PublicationsCommentsPublicationCommentItemDto]**](PublicationsCommentsPublicationCommentItemDto.md) |  | [optional] 
**is_success** | **bool** |  | [optional] 
**error_code** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.resumable_list_response_publications_comments_publication_comment_item_dto import ResumableListResponsePublicationsCommentsPublicationCommentItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of ResumableListResponsePublicationsCommentsPublicationCommentItemDto from a JSON string
resumable_list_response_publications_comments_publication_comment_item_dto_instance = ResumableListResponsePublicationsCommentsPublicationCommentItemDto.from_json(json)
# print the JSON string representation of the object
print(ResumableListResponsePublicationsCommentsPublicationCommentItemDto.to_json())

# convert the object into a dict
resumable_list_response_publications_comments_publication_comment_item_dto_dict = resumable_list_response_publications_comments_publication_comment_item_dto_instance.to_dict()
# create an instance of ResumableListResponsePublicationsCommentsPublicationCommentItemDto from a dict
resumable_list_response_publications_comments_publication_comment_item_dto_from_dict = ResumableListResponsePublicationsCommentsPublicationCommentItemDto.from_dict(resumable_list_response_publications_comments_publication_comment_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


