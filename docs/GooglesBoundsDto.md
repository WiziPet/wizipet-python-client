# GooglesBoundsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**northeast** | [**GooglesLatLngLiteralDto**](GooglesLatLngLiteralDto.md) |  | [optional] 
**southwest** | [**GooglesLatLngLiteralDto**](GooglesLatLngLiteralDto.md) |  | [optional] 

## Example

```python
from wizipet_api.models.googles_bounds_dto import GooglesBoundsDto

# TODO update the JSON string below
json = "{}"
# create an instance of GooglesBoundsDto from a JSON string
googles_bounds_dto_instance = GooglesBoundsDto.from_json(json)
# print the JSON string representation of the object
print(GooglesBoundsDto.to_json())

# convert the object into a dict
googles_bounds_dto_dict = googles_bounds_dto_instance.to_dict()
# create an instance of GooglesBoundsDto from a dict
googles_bounds_dto_from_dict = GooglesBoundsDto.from_dict(googles_bounds_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


