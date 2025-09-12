# GooglesPlaceDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_components** | [**List[GooglesAddressComponentDto]**](GooglesAddressComponentDto.md) |  | [optional] 
**adr_address** | **str** |  | [optional] 
**business_status** | **str** |  | [optional] 
**curbside_pickup** | **bool** |  | [optional] 
**current_opening_hours** | [**GooglesPlaceOpeningHoursDto**](GooglesPlaceOpeningHoursDto.md) |  | [optional] 
**delivery** | **bool** |  | [optional] 
**dine_in** | **bool** |  | [optional] 
**editorial_summary** | [**GooglesPlaceEditorialSummaryDto**](GooglesPlaceEditorialSummaryDto.md) |  | [optional] 
**formatted_address** | **str** |  | [optional] 
**formatted_phone_number** | **str** |  | [optional] 
**geometry** | [**GooglesGeometryDto**](GooglesGeometryDto.md) |  | [optional] 
**icon** | **str** |  | [optional] 
**icon_background_color** | **str** |  | [optional] 
**icon_mask_base_uri** | **str** |  | [optional] 
**international_phone_number** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**opening_hours** | [**GooglesPlaceOpeningHoursDto**](GooglesPlaceOpeningHoursDto.md) |  | [optional] 
**photos** | [**List[GooglesPlacePhotoDto]**](GooglesPlacePhotoDto.md) |  | [optional] 
**place_id** | **str** |  | [optional] 
**plus_code** | [**GooglesPlusCodeDto**](GooglesPlusCodeDto.md) |  | [optional] 
**price_level** | **int** |  | [optional] 
**rating** | **float** |  | [optional] 
**reservable** | **bool** |  | [optional] 
**reviews** | [**List[GooglesPlaceReviewDto]**](GooglesPlaceReviewDto.md) |  | [optional] 
**secondary_opening_hours** | [**List[GooglesPlaceOpeningHoursDto]**](GooglesPlaceOpeningHoursDto.md) |  | [optional] 
**serves_beer** | **bool** |  | [optional] 
**serves_breakfast** | **bool** |  | [optional] 
**serves_brunch** | **bool** |  | [optional] 
**serves_dinner** | **bool** |  | [optional] 
**serves_lunch** | **bool** |  | [optional] 
**serves_vegetarian_food** | **bool** |  | [optional] 
**serves_wine** | **bool** |  | [optional] 
**takeout** | **bool** |  | [optional] 
**types** | **List[str]** |  | [optional] 
**url** | **str** |  | [optional] 
**user_ratings_total** | **int** |  | [optional] 
**utc_offset** | **int** |  | [optional] 
**vicinity** | **str** |  | [optional] 
**website** | **str** |  | [optional] 
**wheelchair_accessible_entrance** | **bool** |  | [optional] 

## Example

```python
from wizipet_api.models.googles_place_dto import GooglesPlaceDto

# TODO update the JSON string below
json = "{}"
# create an instance of GooglesPlaceDto from a JSON string
googles_place_dto_instance = GooglesPlaceDto.from_json(json)
# print the JSON string representation of the object
print(GooglesPlaceDto.to_json())

# convert the object into a dict
googles_place_dto_dict = googles_place_dto_instance.to_dict()
# create an instance of GooglesPlaceDto from a dict
googles_place_dto_from_dict = GooglesPlaceDto.from_dict(googles_place_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


