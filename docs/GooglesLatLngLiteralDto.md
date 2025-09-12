# GooglesLatLngLiteralDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lat** | **float** |  | [optional] 
**lng** | **float** |  | [optional] 

## Example

```python
from wizipet_api.models.googles_lat_lng_literal_dto import GooglesLatLngLiteralDto

# TODO update the JSON string below
json = "{}"
# create an instance of GooglesLatLngLiteralDto from a JSON string
googles_lat_lng_literal_dto_instance = GooglesLatLngLiteralDto.from_json(json)
# print the JSON string representation of the object
print(GooglesLatLngLiteralDto.to_json())

# convert the object into a dict
googles_lat_lng_literal_dto_dict = googles_lat_lng_literal_dto_instance.to_dict()
# create an instance of GooglesLatLngLiteralDto from a dict
googles_lat_lng_literal_dto_from_dict = GooglesLatLngLiteralDto.from_dict(googles_lat_lng_literal_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


