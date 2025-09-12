# GooglesGeocodeResultDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**formatted_address** | **str** |  | [optional] 
**geometry** | [**GooglesGeometryDto**](GooglesGeometryDto.md) |  | [optional] 

## Example

```python
from wizipet_api.models.googles_geocode_result_dto import GooglesGeocodeResultDto

# TODO update the JSON string below
json = "{}"
# create an instance of GooglesGeocodeResultDto from a JSON string
googles_geocode_result_dto_instance = GooglesGeocodeResultDto.from_json(json)
# print the JSON string representation of the object
print(GooglesGeocodeResultDto.to_json())

# convert the object into a dict
googles_geocode_result_dto_dict = googles_geocode_result_dto_instance.to_dict()
# create an instance of GooglesGeocodeResultDto from a dict
googles_geocode_result_dto_from_dict = GooglesGeocodeResultDto.from_dict(googles_geocode_result_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


