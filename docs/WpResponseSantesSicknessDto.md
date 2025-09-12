# WpResponseSantesSicknessDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SantesSicknessDto**](SantesSicknessDto.md) |  | [optional] 
**is_success** | **bool** |  | [optional] 
**error_code** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.wp_response_santes_sickness_dto import WpResponseSantesSicknessDto

# TODO update the JSON string below
json = "{}"
# create an instance of WpResponseSantesSicknessDto from a JSON string
wp_response_santes_sickness_dto_instance = WpResponseSantesSicknessDto.from_json(json)
# print the JSON string representation of the object
print(WpResponseSantesSicknessDto.to_json())

# convert the object into a dict
wp_response_santes_sickness_dto_dict = wp_response_santes_sickness_dto_instance.to_dict()
# create an instance of WpResponseSantesSicknessDto from a dict
wp_response_santes_sickness_dto_from_dict = WpResponseSantesSicknessDto.from_dict(wp_response_santes_sickness_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


