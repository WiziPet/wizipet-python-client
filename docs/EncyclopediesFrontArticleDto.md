# EncyclopediesFrontArticleDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**categorie** | [**EncyclopediesUnifiedArticleCategorieDto**](EncyclopediesUnifiedArticleCategorieDto.md) |  | [optional] 
**description** | **str** |  | [optional] 
**image_couverture_id** | **str** |  | [optional] 
**image_couverture_credit** | **str** |  | [optional] 
**like_count** | **int** |  | [optional] 
**comment_count** | **int** |  | [optional] 
**last_edit_date** | **datetime** |  | [optional] 

## Example

```python
from wizipet_api.models.encyclopedies_front_article_dto import EncyclopediesFrontArticleDto

# TODO update the JSON string below
json = "{}"
# create an instance of EncyclopediesFrontArticleDto from a JSON string
encyclopedies_front_article_dto_instance = EncyclopediesFrontArticleDto.from_json(json)
# print the JSON string representation of the object
print(EncyclopediesFrontArticleDto.to_json())

# convert the object into a dict
encyclopedies_front_article_dto_dict = encyclopedies_front_article_dto_instance.to_dict()
# create an instance of EncyclopediesFrontArticleDto from a dict
encyclopedies_front_article_dto_from_dict = EncyclopediesFrontArticleDto.from_dict(encyclopedies_front_article_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


