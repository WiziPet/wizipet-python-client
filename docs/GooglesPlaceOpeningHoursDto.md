# GooglesPlaceOpeningHoursDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**open_now** | **bool** |  | [optional] 
**periods** | [**List[GooglesPlaceOpeningHoursPeriodDto]**](GooglesPlaceOpeningHoursPeriodDto.md) |  | [optional] 
**special_days** | [**List[GooglesPlaceSpecialDayDto]**](GooglesPlaceSpecialDayDto.md) |  | [optional] 
**types** | **List[str]** |  | [optional] 
**weekday_text** | **List[str]** |  | [optional] 

## Example

```python
from wizipet_api.models.googles_place_opening_hours_dto import GooglesPlaceOpeningHoursDto

# TODO update the JSON string below
json = "{}"
# create an instance of GooglesPlaceOpeningHoursDto from a JSON string
googles_place_opening_hours_dto_instance = GooglesPlaceOpeningHoursDto.from_json(json)
# print the JSON string representation of the object
print(GooglesPlaceOpeningHoursDto.to_json())

# convert the object into a dict
googles_place_opening_hours_dto_dict = googles_place_opening_hours_dto_instance.to_dict()
# create an instance of GooglesPlaceOpeningHoursDto from a dict
googles_place_opening_hours_dto_from_dict = GooglesPlaceOpeningHoursDto.from_dict(googles_place_opening_hours_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


