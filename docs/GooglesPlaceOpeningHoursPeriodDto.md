# GooglesPlaceOpeningHoursPeriodDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**open** | [**GooglesPlaceOpeningHoursPeriodDetailDto**](GooglesPlaceOpeningHoursPeriodDetailDto.md) |  | [optional] 
**close** | [**GooglesPlaceOpeningHoursPeriodDetailDto**](GooglesPlaceOpeningHoursPeriodDetailDto.md) |  | [optional] 

## Example

```python
from wizipet_api.models.googles_place_opening_hours_period_dto import GooglesPlaceOpeningHoursPeriodDto

# TODO update the JSON string below
json = "{}"
# create an instance of GooglesPlaceOpeningHoursPeriodDto from a JSON string
googles_place_opening_hours_period_dto_instance = GooglesPlaceOpeningHoursPeriodDto.from_json(json)
# print the JSON string representation of the object
print(GooglesPlaceOpeningHoursPeriodDto.to_json())

# convert the object into a dict
googles_place_opening_hours_period_dto_dict = googles_place_opening_hours_period_dto_instance.to_dict()
# create an instance of GooglesPlaceOpeningHoursPeriodDto from a dict
googles_place_opening_hours_period_dto_from_dict = GooglesPlaceOpeningHoursPeriodDto.from_dict(googles_place_opening_hours_period_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


