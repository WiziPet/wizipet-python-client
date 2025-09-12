# CartesPetFriendlyPlaceDetailsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**author_id** | **str** |  | [optional] 
**last_update_author_id** | **str** |  | [optional] 
**last_update_author_race_id** | **str** |  | [optional] 
**last_update_author_image_id** | **str** |  | [optional] 
**last_update_author_name** | **str** |  | [optional] 
**race_id** | **str** |  | [optional] 
**author_image_id** | **str** |  | [optional] 
**author_name** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | [**CartesPetFriendlyLocationTypeDto**](CartesPetFriendlyLocationTypeDto.md) |  | [optional] 
**image_id_list** | **List[str]** |  | [optional] 
**always_opened** | **bool** |  | [optional] 
**dog_off_leash** | **bool** |  | [optional] 
**water_available** | **bool** |  | [optional] 
**location** | [**GooglesLatLngLiteralDto**](GooglesLatLngLiteralDto.md) |  | [optional] 
**address** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**rating** | **float** |  | [optional] 
**rating_count** | **int** |  | [optional] 
**last_reviews** | [**List[PlacesPetFriendlyReviewDto]**](PlacesPetFriendlyReviewDto.md) |  | [optional] 
**commentaire** | **str** |  | [optional] 
**creation_date** | **datetime** |  | [optional] 
**updated_date** | **datetime** |  | [optional] 

## Example

```python
from wizipet_api.models.cartes_pet_friendly_place_details_dto import CartesPetFriendlyPlaceDetailsDto

# TODO update the JSON string below
json = "{}"
# create an instance of CartesPetFriendlyPlaceDetailsDto from a JSON string
cartes_pet_friendly_place_details_dto_instance = CartesPetFriendlyPlaceDetailsDto.from_json(json)
# print the JSON string representation of the object
print(CartesPetFriendlyPlaceDetailsDto.to_json())

# convert the object into a dict
cartes_pet_friendly_place_details_dto_dict = cartes_pet_friendly_place_details_dto_instance.to_dict()
# create an instance of CartesPetFriendlyPlaceDetailsDto from a dict
cartes_pet_friendly_place_details_dto_from_dict = CartesPetFriendlyPlaceDetailsDto.from_dict(cartes_pet_friendly_place_details_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


