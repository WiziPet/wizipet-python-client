# WpListResponsePlacesAnimauteLocalPageItemDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PlacesAnimauteLocalPageItemDto]**](PlacesAnimauteLocalPageItemDto.md) |  | [optional] 
**is_success** | **bool** |  | [optional] 
**error_code** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.wp_list_response_places_animaute_local_page_item_dto import WpListResponsePlacesAnimauteLocalPageItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of WpListResponsePlacesAnimauteLocalPageItemDto from a JSON string
wp_list_response_places_animaute_local_page_item_dto_instance = WpListResponsePlacesAnimauteLocalPageItemDto.from_json(json)
# print the JSON string representation of the object
print(WpListResponsePlacesAnimauteLocalPageItemDto.to_json())

# convert the object into a dict
wp_list_response_places_animaute_local_page_item_dto_dict = wp_list_response_places_animaute_local_page_item_dto_instance.to_dict()
# create an instance of WpListResponsePlacesAnimauteLocalPageItemDto from a dict
wp_list_response_places_animaute_local_page_item_dto_from_dict = WpListResponsePlacesAnimauteLocalPageItemDto.from_dict(wp_list_response_places_animaute_local_page_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


