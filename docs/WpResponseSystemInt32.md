# WpResponseSystemInt32


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **int** |  | [optional] 
**is_success** | **bool** |  | [optional] 
**error_code** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.wp_response_system_int32 import WpResponseSystemInt32

# TODO update the JSON string below
json = "{}"
# create an instance of WpResponseSystemInt32 from a JSON string
wp_response_system_int32_instance = WpResponseSystemInt32.from_json(json)
# print the JSON string representation of the object
print(WpResponseSystemInt32.to_json())

# convert the object into a dict
wp_response_system_int32_dict = wp_response_system_int32_instance.to_dict()
# create an instance of WpResponseSystemInt32 from a dict
wp_response_system_int32_from_dict = WpResponseSystemInt32.from_dict(wp_response_system_int32_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


