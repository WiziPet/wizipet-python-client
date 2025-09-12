# WpResponsePromenadesPromenadeDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PromenadesPromenadeDto**](PromenadesPromenadeDto.md) |  | [optional] 
**is_success** | **bool** |  | [optional] 
**error_code** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.wp_response_promenades_promenade_dto import WpResponsePromenadesPromenadeDto

# TODO update the JSON string below
json = "{}"
# create an instance of WpResponsePromenadesPromenadeDto from a JSON string
wp_response_promenades_promenade_dto_instance = WpResponsePromenadesPromenadeDto.from_json(json)
# print the JSON string representation of the object
print(WpResponsePromenadesPromenadeDto.to_json())

# convert the object into a dict
wp_response_promenades_promenade_dto_dict = wp_response_promenades_promenade_dto_instance.to_dict()
# create an instance of WpResponsePromenadesPromenadeDto from a dict
wp_response_promenades_promenade_dto_from_dict = WpResponsePromenadesPromenadeDto.from_dict(wp_response_promenades_promenade_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


