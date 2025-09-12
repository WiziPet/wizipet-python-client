# EncyclopediesArticleItemDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**image_couverture_id** | **str** |  | [optional] 
**short_description** | **str** |  | [optional] 
**categorie** | [**EncyclopediesUnifiedArticleCategorieDto**](EncyclopediesUnifiedArticleCategorieDto.md) |  | [optional] 
**like_count** | **int** |  | [optional] 
**comment_count** | **int** |  | [optional] 
**last_edit_date** | **datetime** |  | [optional] 

## Example

```python
from wizipet_api.models.encyclopedies_article_item_dto import EncyclopediesArticleItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of EncyclopediesArticleItemDto from a JSON string
encyclopedies_article_item_dto_instance = EncyclopediesArticleItemDto.from_json(json)
# print the JSON string representation of the object
print(EncyclopediesArticleItemDto.to_json())

# convert the object into a dict
encyclopedies_article_item_dto_dict = encyclopedies_article_item_dto_instance.to_dict()
# create an instance of EncyclopediesArticleItemDto from a dict
encyclopedies_article_item_dto_from_dict = EncyclopediesArticleItemDto.from_dict(encyclopedies_article_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


