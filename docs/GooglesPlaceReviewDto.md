# GooglesPlaceReviewDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author_name** | **str** |  | [optional] 
**rating** | **float** |  | [optional] 
**relative_time_description** | **str** |  | [optional] 
**time** | **int** |  | [optional] 
**author_url** | **str** |  | [optional] 
**language** | **str** |  | [optional] 
**original_language** | **str** |  | [optional] 
**profile_photo_url** | **str** |  | [optional] 
**text** | **str** |  | [optional] 
**translated** | **bool** |  | [optional] 

## Example

```python
from wizipet_api.models.googles_place_review_dto import GooglesPlaceReviewDto

# TODO update the JSON string below
json = "{}"
# create an instance of GooglesPlaceReviewDto from a JSON string
googles_place_review_dto_instance = GooglesPlaceReviewDto.from_json(json)
# print the JSON string representation of the object
print(GooglesPlaceReviewDto.to_json())

# convert the object into a dict
googles_place_review_dto_dict = googles_place_review_dto_instance.to_dict()
# create an instance of GooglesPlaceReviewDto from a dict
googles_place_review_dto_from_dict = GooglesPlaceReviewDto.from_dict(googles_place_review_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


