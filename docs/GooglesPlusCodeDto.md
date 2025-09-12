# GooglesPlusCodeDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**global_code** | **str** |  | [optional] 
**compound_code** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.googles_plus_code_dto import GooglesPlusCodeDto

# TODO update the JSON string below
json = "{}"
# create an instance of GooglesPlusCodeDto from a JSON string
googles_plus_code_dto_instance = GooglesPlusCodeDto.from_json(json)
# print the JSON string representation of the object
print(GooglesPlusCodeDto.to_json())

# convert the object into a dict
googles_plus_code_dto_dict = googles_plus_code_dto_instance.to_dict()
# create an instance of GooglesPlusCodeDto from a dict
googles_plus_code_dto_from_dict = GooglesPlusCodeDto.from_dict(googles_plus_code_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


