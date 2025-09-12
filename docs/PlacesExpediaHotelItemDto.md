# PlacesExpediaHotelItemDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | Lien vers le détail de l&#39;hotel | [optional] 
**image_url** | **str** | Image de preview | [optional] 
**promotion_text** | **str** | Contenu du badge promotionnel | [optional] 
**final_price** | **float** | Prix final, réduction déduite | [optional] 
**currency** | **str** | Euro par défaut (EUR), ignorable atm | [optional] 
**strike_out_price** | **float** | Prix sans réduction | [optional] 
**distance_in_km** | **float** | Distance en km (à partir du centre de la bounding box) | [optional] 
**star_rating** | **int** | Classement de 1 à 5 étoiles | [optional] 
**guest_rating_count** | **int** | Nombre d&#39;avis utilisateurs | [optional] 
**guest_rating** | **float** | Note des utilisateurs hotels.com de 0 à 10 | [optional] 
**type** | [**CartesPetFriendlyLocationTypeDto**](CartesPetFriendlyLocationTypeDto.md) |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**location** | [**GooglesLatLngLiteralDto**](GooglesLatLngLiteralDto.md) |  | [optional] 
**category_list** | [**List[PlacesPlaceCategoryDto]**](PlacesPlaceCategoryDto.md) |  | [optional] 
**sub_category_list** | [**List[PlacesPlaceSubCategoryDto]**](PlacesPlaceSubCategoryDto.md) |  | [optional] 

## Example

```python
from wizipet_api.models.places_expedia_hotel_item_dto import PlacesExpediaHotelItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of PlacesExpediaHotelItemDto from a JSON string
places_expedia_hotel_item_dto_instance = PlacesExpediaHotelItemDto.from_json(json)
# print the JSON string representation of the object
print(PlacesExpediaHotelItemDto.to_json())

# convert the object into a dict
places_expedia_hotel_item_dto_dict = places_expedia_hotel_item_dto_instance.to_dict()
# create an instance of PlacesExpediaHotelItemDto from a dict
places_expedia_hotel_item_dto_from_dict = PlacesExpediaHotelItemDto.from_dict(places_expedia_hotel_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


