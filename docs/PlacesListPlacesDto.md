# PlacesListPlacesDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bounds** | [**GooglesBoundsDto**](GooglesBoundsDto.md) |  | [optional] 
**sub_categories** | [**List[PlacesPlaceSubCategoryDto]**](PlacesPlaceSubCategoryDto.md) |  | [optional] 
**keywords** | **str** |  | [optional] 
**continuation_token** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.places_list_places_dto import PlacesListPlacesDto

# TODO update the JSON string below
json = "{}"
# create an instance of PlacesListPlacesDto from a JSON string
places_list_places_dto_instance = PlacesListPlacesDto.from_json(json)
# print the JSON string representation of the object
print(PlacesListPlacesDto.to_json())

# convert the object into a dict
places_list_places_dto_dict = places_list_places_dto_instance.to_dict()
# create an instance of PlacesListPlacesDto from a dict
places_list_places_dto_from_dict = PlacesListPlacesDto.from_dict(places_list_places_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


