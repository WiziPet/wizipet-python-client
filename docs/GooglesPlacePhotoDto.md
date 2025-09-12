# GooglesPlacePhotoDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**height** | **int** |  | [optional] 
**html_attributions** | **List[str]** |  | [optional] 
**photo_reference** | **str** |  | [optional] 
**width** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.googles_place_photo_dto import GooglesPlacePhotoDto

# TODO update the JSON string below
json = "{}"
# create an instance of GooglesPlacePhotoDto from a JSON string
googles_place_photo_dto_instance = GooglesPlacePhotoDto.from_json(json)
# print the JSON string representation of the object
print(GooglesPlacePhotoDto.to_json())

# convert the object into a dict
googles_place_photo_dto_dict = googles_place_photo_dto_instance.to_dict()
# create an instance of GooglesPlacePhotoDto from a dict
googles_place_photo_dto_from_dict = GooglesPlacePhotoDto.from_dict(googles_place_photo_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


