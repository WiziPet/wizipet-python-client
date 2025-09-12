# WpResponseSantesOperationDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SantesOperationDto**](SantesOperationDto.md) |  | [optional] 
**is_success** | **bool** |  | [optional] 
**error_code** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.wp_response_santes_operation_dto import WpResponseSantesOperationDto

# TODO update the JSON string below
json = "{}"
# create an instance of WpResponseSantesOperationDto from a JSON string
wp_response_santes_operation_dto_instance = WpResponseSantesOperationDto.from_json(json)
# print the JSON string representation of the object
print(WpResponseSantesOperationDto.to_json())

# convert the object into a dict
wp_response_santes_operation_dto_dict = wp_response_santes_operation_dto_instance.to_dict()
# create an instance of WpResponseSantesOperationDto from a dict
wp_response_santes_operation_dto_from_dict = WpResponseSantesOperationDto.from_dict(wp_response_santes_operation_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


