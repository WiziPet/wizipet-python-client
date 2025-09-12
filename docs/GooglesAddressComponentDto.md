# GooglesAddressComponentDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**long_name** | **str** |  | [optional] 
**short_name** | **str** |  | [optional] 
**types** | **List[str]** |  | [optional] 

## Example

```python
from wizipet_api.models.googles_address_component_dto import GooglesAddressComponentDto

# TODO update the JSON string below
json = "{}"
# create an instance of GooglesAddressComponentDto from a JSON string
googles_address_component_dto_instance = GooglesAddressComponentDto.from_json(json)
# print the JSON string representation of the object
print(GooglesAddressComponentDto.to_json())

# convert the object into a dict
googles_address_component_dto_dict = googles_address_component_dto_instance.to_dict()
# create an instance of GooglesAddressComponentDto from a dict
googles_address_component_dto_from_dict = GooglesAddressComponentDto.from_dict(googles_address_component_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


