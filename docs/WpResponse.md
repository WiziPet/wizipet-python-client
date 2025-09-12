# WpResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] 
**error_code** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.wp_response import WpResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WpResponse from a JSON string
wp_response_instance = WpResponse.from_json(json)
# print the JSON string representation of the object
print(WpResponse.to_json())

# convert the object into a dict
wp_response_dict = wp_response_instance.to_dict()
# create an instance of WpResponse from a dict
wp_response_from_dict = WpResponse.from_dict(wp_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


