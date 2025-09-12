# PlacesListExpediaHotelSearchDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bounds** | [**GooglesBoundsDto**](GooglesBoundsDto.md) |  | [optional] 
**check_in** | **datetime** |  | [optional] 
**check_out** | **datetime** |  | [optional] 
**limit** | **int** |  | [optional] 

## Example

```python
from wizipet_api.models.places_list_expedia_hotel_search_dto import PlacesListExpediaHotelSearchDto

# TODO update the JSON string below
json = "{}"
# create an instance of PlacesListExpediaHotelSearchDto from a JSON string
places_list_expedia_hotel_search_dto_instance = PlacesListExpediaHotelSearchDto.from_json(json)
# print the JSON string representation of the object
print(PlacesListExpediaHotelSearchDto.to_json())

# convert the object into a dict
places_list_expedia_hotel_search_dto_dict = places_list_expedia_hotel_search_dto_instance.to_dict()
# create an instance of PlacesListExpediaHotelSearchDto from a dict
places_list_expedia_hotel_search_dto_from_dict = PlacesListExpediaHotelSearchDto.from_dict(places_list_expedia_hotel_search_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


