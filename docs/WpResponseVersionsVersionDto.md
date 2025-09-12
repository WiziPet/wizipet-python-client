# WpResponseVersionsVersionDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**VersionsVersionDto**](VersionsVersionDto.md) |  | [optional] 
**is_success** | **bool** |  | [optional] 
**error_code** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.wp_response_versions_version_dto import WpResponseVersionsVersionDto

# TODO update the JSON string below
json = "{}"
# create an instance of WpResponseVersionsVersionDto from a JSON string
wp_response_versions_version_dto_instance = WpResponseVersionsVersionDto.from_json(json)
# print the JSON string representation of the object
print(WpResponseVersionsVersionDto.to_json())

# convert the object into a dict
wp_response_versions_version_dto_dict = wp_response_versions_version_dto_instance.to_dict()
# create an instance of WpResponseVersionsVersionDto from a dict
wp_response_versions_version_dto_from_dict = WpResponseVersionsVersionDto.from_dict(wp_response_versions_version_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


