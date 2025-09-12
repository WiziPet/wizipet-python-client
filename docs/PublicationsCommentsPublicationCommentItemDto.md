# PublicationsCommentsPublicationCommentItemDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**author** | [**CommonPetProfileDto**](CommonPetProfileDto.md) |  | [optional] 
**var_date** | **datetime** |  | [optional] 
**body** | **str** |  | [optional] 
**like_count** | **int** |  | [optional] 

## Example

```python
from wizipet_api.models.publications_comments_publication_comment_item_dto import PublicationsCommentsPublicationCommentItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of PublicationsCommentsPublicationCommentItemDto from a JSON string
publications_comments_publication_comment_item_dto_instance = PublicationsCommentsPublicationCommentItemDto.from_json(json)
# print the JSON string representation of the object
print(PublicationsCommentsPublicationCommentItemDto.to_json())

# convert the object into a dict
publications_comments_publication_comment_item_dto_dict = publications_comments_publication_comment_item_dto_instance.to_dict()
# create an instance of PublicationsCommentsPublicationCommentItemDto from a dict
publications_comments_publication_comment_item_dto_from_dict = PublicationsCommentsPublicationCommentItemDto.from_dict(publications_comments_publication_comment_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


