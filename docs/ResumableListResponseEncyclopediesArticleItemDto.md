# ResumableListResponseEncyclopediesArticleItemDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_more** | **bool** |  | [optional] 
**count** | **int** |  | [optional] 
**continuation_token** | **str** |  | [optional] 
**data** | [**List[EncyclopediesArticleItemDto]**](EncyclopediesArticleItemDto.md) |  | [optional] 
**is_success** | **bool** |  | [optional] 
**error_code** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.resumable_list_response_encyclopedies_article_item_dto import ResumableListResponseEncyclopediesArticleItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of ResumableListResponseEncyclopediesArticleItemDto from a JSON string
resumable_list_response_encyclopedies_article_item_dto_instance = ResumableListResponseEncyclopediesArticleItemDto.from_json(json)
# print the JSON string representation of the object
print(ResumableListResponseEncyclopediesArticleItemDto.to_json())

# convert the object into a dict
resumable_list_response_encyclopedies_article_item_dto_dict = resumable_list_response_encyclopedies_article_item_dto_instance.to_dict()
# create an instance of ResumableListResponseEncyclopediesArticleItemDto from a dict
resumable_list_response_encyclopedies_article_item_dto_from_dict = ResumableListResponseEncyclopediesArticleItemDto.from_dict(resumable_list_response_encyclopedies_article_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


