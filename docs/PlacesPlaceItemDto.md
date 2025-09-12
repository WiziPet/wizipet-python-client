# PlacesPlaceItemDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**location** | [**GooglesLatLngLiteralDto**](GooglesLatLngLiteralDto.md) |  | [optional] 
**category_list** | [**List[PlacesPlaceCategoryDto]**](PlacesPlaceCategoryDto.md) |  | [optional] 
**sub_category_list** | [**List[PlacesPlaceSubCategoryDto]**](PlacesPlaceSubCategoryDto.md) |  | [optional] 

## Example

```python
from wizipet_api.models.places_place_item_dto import PlacesPlaceItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of PlacesPlaceItemDto from a JSON string
places_place_item_dto_instance = PlacesPlaceItemDto.from_json(json)
# print the JSON string representation of the object
print(PlacesPlaceItemDto.to_json())

# convert the object into a dict
places_place_item_dto_dict = places_place_item_dto_instance.to_dict()
# create an instance of PlacesPlaceItemDto from a dict
places_place_item_dto_from_dict = PlacesPlaceItemDto.from_dict(places_place_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


