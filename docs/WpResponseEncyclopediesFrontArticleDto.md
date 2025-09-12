# WpResponseEncyclopediesFrontArticleDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**EncyclopediesFrontArticleDto**](EncyclopediesFrontArticleDto.md) |  | [optional] 
**is_success** | **bool** |  | [optional] 
**error_code** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.wp_response_encyclopedies_front_article_dto import WpResponseEncyclopediesFrontArticleDto

# TODO update the JSON string below
json = "{}"
# create an instance of WpResponseEncyclopediesFrontArticleDto from a JSON string
wp_response_encyclopedies_front_article_dto_instance = WpResponseEncyclopediesFrontArticleDto.from_json(json)
# print the JSON string representation of the object
print(WpResponseEncyclopediesFrontArticleDto.to_json())

# convert the object into a dict
wp_response_encyclopedies_front_article_dto_dict = wp_response_encyclopedies_front_article_dto_instance.to_dict()
# create an instance of WpResponseEncyclopediesFrontArticleDto from a dict
wp_response_encyclopedies_front_article_dto_from_dict = WpResponseEncyclopediesFrontArticleDto.from_dict(wp_response_encyclopedies_front_article_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


