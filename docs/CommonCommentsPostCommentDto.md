# CommonCommentsPostCommentDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.common_comments_post_comment_dto import CommonCommentsPostCommentDto

# TODO update the JSON string below
json = "{}"
# create an instance of CommonCommentsPostCommentDto from a JSON string
common_comments_post_comment_dto_instance = CommonCommentsPostCommentDto.from_json(json)
# print the JSON string representation of the object
print(CommonCommentsPostCommentDto.to_json())

# convert the object into a dict
common_comments_post_comment_dto_dict = common_comments_post_comment_dto_instance.to_dict()
# create an instance of CommonCommentsPostCommentDto from a dict
common_comments_post_comment_dto_from_dict = CommonCommentsPostCommentDto.from_dict(common_comments_post_comment_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


