# PlacesAnimauteLocalPageItemDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**location** | [**GooglesLatLngLiteralDto**](GooglesLatLngLiteralDto.md) |  | [optional] 
**category_list** | [**List[PlacesPlaceCategoryDto]**](PlacesPlaceCategoryDto.md) |  | [optional] 
**sub_category_list** | [**List[PlacesPlaceSubCategoryDto]**](PlacesPlaceSubCategoryDto.md) |  | [optional] 

## Example

```python
from wizipet_api.models.places_animaute_local_page_item_dto import PlacesAnimauteLocalPageItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of PlacesAnimauteLocalPageItemDto from a JSON string
places_animaute_local_page_item_dto_instance = PlacesAnimauteLocalPageItemDto.from_json(json)
# print the JSON string representation of the object
print(PlacesAnimauteLocalPageItemDto.to_json())

# convert the object into a dict
places_animaute_local_page_item_dto_dict = places_animaute_local_page_item_dto_instance.to_dict()
# create an instance of PlacesAnimauteLocalPageItemDto from a dict
places_animaute_local_page_item_dto_from_dict = PlacesAnimauteLocalPageItemDto.from_dict(places_animaute_local_page_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


