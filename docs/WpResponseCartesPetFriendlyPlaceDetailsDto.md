# WpResponseCartesPetFriendlyPlaceDetailsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CartesPetFriendlyPlaceDetailsDto**](CartesPetFriendlyPlaceDetailsDto.md) |  | [optional] 
**is_success** | **bool** |  | [optional] 
**error_code** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.wp_response_cartes_pet_friendly_place_details_dto import WpResponseCartesPetFriendlyPlaceDetailsDto

# TODO update the JSON string below
json = "{}"
# create an instance of WpResponseCartesPetFriendlyPlaceDetailsDto from a JSON string
wp_response_cartes_pet_friendly_place_details_dto_instance = WpResponseCartesPetFriendlyPlaceDetailsDto.from_json(json)
# print the JSON string representation of the object
print(WpResponseCartesPetFriendlyPlaceDetailsDto.to_json())

# convert the object into a dict
wp_response_cartes_pet_friendly_place_details_dto_dict = wp_response_cartes_pet_friendly_place_details_dto_instance.to_dict()
# create an instance of WpResponseCartesPetFriendlyPlaceDetailsDto from a dict
wp_response_cartes_pet_friendly_place_details_dto_from_dict = WpResponseCartesPetFriendlyPlaceDetailsDto.from_dict(wp_response_cartes_pet_friendly_place_details_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


