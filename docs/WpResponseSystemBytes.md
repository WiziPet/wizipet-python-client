# WpResponseSystemBytes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **bytearray** |  | [optional] 
**is_success** | **bool** |  | [optional] 
**error_code** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.wp_response_system_bytes import WpResponseSystemBytes

# TODO update the JSON string below
json = "{}"
# create an instance of WpResponseSystemBytes from a JSON string
wp_response_system_bytes_instance = WpResponseSystemBytes.from_json(json)
# print the JSON string representation of the object
print(WpResponseSystemBytes.to_json())

# convert the object into a dict
wp_response_system_bytes_dict = wp_response_system_bytes_instance.to_dict()
# create an instance of WpResponseSystemBytes from a dict
wp_response_system_bytes_from_dict = WpResponseSystemBytes.from_dict(wp_response_system_bytes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


