# ListResponsePlacesExpediaHotelItemDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PlacesExpediaHotelItemDto]**](PlacesExpediaHotelItemDto.md) |  | [optional] 
**is_success** | **bool** |  | [optional] 
**error_code** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.list_response_places_expedia_hotel_item_dto import ListResponsePlacesExpediaHotelItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of ListResponsePlacesExpediaHotelItemDto from a JSON string
list_response_places_expedia_hotel_item_dto_instance = ListResponsePlacesExpediaHotelItemDto.from_json(json)
# print the JSON string representation of the object
print(ListResponsePlacesExpediaHotelItemDto.to_json())

# convert the object into a dict
list_response_places_expedia_hotel_item_dto_dict = list_response_places_expedia_hotel_item_dto_instance.to_dict()
# create an instance of ListResponsePlacesExpediaHotelItemDto from a dict
list_response_places_expedia_hotel_item_dto_from_dict = ListResponsePlacesExpediaHotelItemDto.from_dict(list_response_places_expedia_hotel_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


