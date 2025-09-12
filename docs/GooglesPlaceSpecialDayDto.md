# GooglesPlaceSpecialDayDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** |  | [optional] 
**exceptional_hours** | **bool** |  | [optional] 

## Example

```python
from wizipet_api.models.googles_place_special_day_dto import GooglesPlaceSpecialDayDto

# TODO update the JSON string below
json = "{}"
# create an instance of GooglesPlaceSpecialDayDto from a JSON string
googles_place_special_day_dto_instance = GooglesPlaceSpecialDayDto.from_json(json)
# print the JSON string representation of the object
print(GooglesPlaceSpecialDayDto.to_json())

# convert the object into a dict
googles_place_special_day_dto_dict = googles_place_special_day_dto_instance.to_dict()
# create an instance of GooglesPlaceSpecialDayDto from a dict
googles_place_special_day_dto_from_dict = GooglesPlaceSpecialDayDto.from_dict(googles_place_special_day_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


