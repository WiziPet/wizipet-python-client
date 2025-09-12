# GooglesPlaceEditorialSummaryDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | **str** |  | [optional] 
**overview** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.googles_place_editorial_summary_dto import GooglesPlaceEditorialSummaryDto

# TODO update the JSON string below
json = "{}"
# create an instance of GooglesPlaceEditorialSummaryDto from a JSON string
googles_place_editorial_summary_dto_instance = GooglesPlaceEditorialSummaryDto.from_json(json)
# print the JSON string representation of the object
print(GooglesPlaceEditorialSummaryDto.to_json())

# convert the object into a dict
googles_place_editorial_summary_dto_dict = googles_place_editorial_summary_dto_instance.to_dict()
# create an instance of GooglesPlaceEditorialSummaryDto from a dict
googles_place_editorial_summary_dto_from_dict = GooglesPlaceEditorialSummaryDto.from_dict(googles_place_editorial_summary_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


