# PlacesListPlacesFromBoundsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bounds** | [**GooglesBoundsDto**](GooglesBoundsDto.md) |  | [optional] 
**is_hebergement** | **bool** |  | [optional] 

## Example

```python
from wizipet_api.models.places_list_places_from_bounds_dto import PlacesListPlacesFromBoundsDto

# TODO update the JSON string below
json = "{}"
# create an instance of PlacesListPlacesFromBoundsDto from a JSON string
places_list_places_from_bounds_dto_instance = PlacesListPlacesFromBoundsDto.from_json(json)
# print the JSON string representation of the object
print(PlacesListPlacesFromBoundsDto.to_json())

# convert the object into a dict
places_list_places_from_bounds_dto_dict = places_list_places_from_bounds_dto_instance.to_dict()
# create an instance of PlacesListPlacesFromBoundsDto from a dict
places_list_places_from_bounds_dto_from_dict = PlacesListPlacesFromBoundsDto.from_dict(places_list_places_from_bounds_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


