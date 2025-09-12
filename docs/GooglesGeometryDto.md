# GooglesGeometryDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location** | [**GooglesLatLngLiteralDto**](GooglesLatLngLiteralDto.md) |  | [optional] 
**viewport** | [**GooglesBoundsDto**](GooglesBoundsDto.md) |  | [optional] 

## Example

```python
from wizipet_api.models.googles_geometry_dto import GooglesGeometryDto

# TODO update the JSON string below
json = "{}"
# create an instance of GooglesGeometryDto from a JSON string
googles_geometry_dto_instance = GooglesGeometryDto.from_json(json)
# print the JSON string representation of the object
print(GooglesGeometryDto.to_json())

# convert the object into a dict
googles_geometry_dto_dict = googles_geometry_dto_instance.to_dict()
# create an instance of GooglesGeometryDto from a dict
googles_geometry_dto_from_dict = GooglesGeometryDto.from_dict(googles_geometry_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


