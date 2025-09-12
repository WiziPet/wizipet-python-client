# CommonCommentsArticleCommentItemDto


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
from wizipet_api.models.common_comments_article_comment_item_dto import CommonCommentsArticleCommentItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of CommonCommentsArticleCommentItemDto from a JSON string
common_comments_article_comment_item_dto_instance = CommonCommentsArticleCommentItemDto.from_json(json)
# print the JSON string representation of the object
print(CommonCommentsArticleCommentItemDto.to_json())

# convert the object into a dict
common_comments_article_comment_item_dto_dict = common_comments_article_comment_item_dto_instance.to_dict()
# create an instance of CommonCommentsArticleCommentItemDto from a dict
common_comments_article_comment_item_dto_from_dict = CommonCommentsArticleCommentItemDto.from_dict(common_comments_article_comment_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


