# WpResponseResumableListResponseEncyclopediesArticleItemDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ResumableListResponseEncyclopediesArticleItemDto**](ResumableListResponseEncyclopediesArticleItemDto.md) |  | [optional] 
**is_success** | **bool** |  | [optional] 
**error_code** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.wp_response_resumable_list_response_encyclopedies_article_item_dto import WpResponseResumableListResponseEncyclopediesArticleItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of WpResponseResumableListResponseEncyclopediesArticleItemDto from a JSON string
wp_response_resumable_list_response_encyclopedies_article_item_dto_instance = WpResponseResumableListResponseEncyclopediesArticleItemDto.from_json(json)
# print the JSON string representation of the object
print(WpResponseResumableListResponseEncyclopediesArticleItemDto.to_json())

# convert the object into a dict
wp_response_resumable_list_response_encyclopedies_article_item_dto_dict = wp_response_resumable_list_response_encyclopedies_article_item_dto_instance.to_dict()
# create an instance of WpResponseResumableListResponseEncyclopediesArticleItemDto from a dict
wp_response_resumable_list_response_encyclopedies_article_item_dto_from_dict = WpResponseResumableListResponseEncyclopediesArticleItemDto.from_dict(wp_response_resumable_list_response_encyclopedies_article_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


