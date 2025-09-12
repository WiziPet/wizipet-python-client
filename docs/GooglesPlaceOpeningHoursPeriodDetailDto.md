# GooglesPlaceOpeningHoursPeriodDetailDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day** | **int** |  | [optional] 
**time** | **str** |  | [optional] 
**var_date** | **str** |  | [optional] 
**truncated** | **bool** |  | [optional] 

## Example

```python
from wizipet_api.models.googles_place_opening_hours_period_detail_dto import GooglesPlaceOpeningHoursPeriodDetailDto

# TODO update the JSON string below
json = "{}"
# create an instance of GooglesPlaceOpeningHoursPeriodDetailDto from a JSON string
googles_place_opening_hours_period_detail_dto_instance = GooglesPlaceOpeningHoursPeriodDetailDto.from_json(json)
# print the JSON string representation of the object
print(GooglesPlaceOpeningHoursPeriodDetailDto.to_json())

# convert the object into a dict
googles_place_opening_hours_period_detail_dto_dict = googles_place_opening_hours_period_detail_dto_instance.to_dict()
# create an instance of GooglesPlaceOpeningHoursPeriodDetailDto from a dict
googles_place_opening_hours_period_detail_dto_from_dict = GooglesPlaceOpeningHoursPeriodDetailDto.from_dict(googles_place_opening_hours_period_detail_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


