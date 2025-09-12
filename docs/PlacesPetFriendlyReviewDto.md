# PlacesPetFriendlyReviewDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pet_id** | **str** |  | [optional] 
**race_id** | **str** |  | [optional] 
**media_id** | **str** |  | [optional] 
**pet_name** | **str** |  | [optional] 
**review_count** | **int** |  | [optional] [default to 1]
**rating** | **float** |  | [optional] 
**created_date** | **datetime** |  | [optional] 

## Example

```python
from wizipet_api.models.places_pet_friendly_review_dto import PlacesPetFriendlyReviewDto

# TODO update the JSON string below
json = "{}"
# create an instance of PlacesPetFriendlyReviewDto from a JSON string
places_pet_friendly_review_dto_instance = PlacesPetFriendlyReviewDto.from_json(json)
# print the JSON string representation of the object
print(PlacesPetFriendlyReviewDto.to_json())

# convert the object into a dict
places_pet_friendly_review_dto_dict = places_pet_friendly_review_dto_instance.to_dict()
# create an instance of PlacesPetFriendlyReviewDto from a dict
places_pet_friendly_review_dto_from_dict = PlacesPetFriendlyReviewDto.from_dict(places_pet_friendly_review_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


