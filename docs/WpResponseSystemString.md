# WpResponseSystemString


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **str** |  | [optional] 
**is_success** | **bool** |  | [optional] 
**error_code** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.wp_response_system_string import WpResponseSystemString

# TODO update the JSON string below
json = "{}"
# create an instance of WpResponseSystemString from a JSON string
wp_response_system_string_instance = WpResponseSystemString.from_json(json)
# print the JSON string representation of the object
print(WpResponseSystemString.to_json())

# convert the object into a dict
wp_response_system_string_dict = wp_response_system_string_instance.to_dict()
# create an instance of WpResponseSystemString from a dict
wp_response_system_string_from_dict = WpResponseSystemString.from_dict(wp_response_system_string_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


