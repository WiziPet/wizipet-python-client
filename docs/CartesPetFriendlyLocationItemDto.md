# CartesPetFriendlyLocationItemDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**CartesPetFriendlyLocationTypeDto**](CartesPetFriendlyLocationTypeDto.md) |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**location** | [**GooglesLatLngLiteralDto**](GooglesLatLngLiteralDto.md) |  | [optional] 
**category_list** | [**List[PlacesPlaceCategoryDto]**](PlacesPlaceCategoryDto.md) |  | [optional] 
**sub_category_list** | [**List[PlacesPlaceSubCategoryDto]**](PlacesPlaceSubCategoryDto.md) |  | [optional] 

## Example

```python
from wizipet_api.models.cartes_pet_friendly_location_item_dto import CartesPetFriendlyLocationItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of CartesPetFriendlyLocationItemDto from a JSON string
cartes_pet_friendly_location_item_dto_instance = CartesPetFriendlyLocationItemDto.from_json(json)
# print the JSON string representation of the object
print(CartesPetFriendlyLocationItemDto.to_json())

# convert the object into a dict
cartes_pet_friendly_location_item_dto_dict = cartes_pet_friendly_location_item_dto_instance.to_dict()
# create an instance of CartesPetFriendlyLocationItemDto from a dict
cartes_pet_friendly_location_item_dto_from_dict = CartesPetFriendlyLocationItemDto.from_dict(cartes_pet_friendly_location_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


