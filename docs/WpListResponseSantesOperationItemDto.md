# WpListResponseSantesOperationItemDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SantesOperationItemDto]**](SantesOperationItemDto.md) |  | [optional] 
**is_success** | **bool** |  | [optional] 
**error_code** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.wp_list_response_santes_operation_item_dto import WpListResponseSantesOperationItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of WpListResponseSantesOperationItemDto from a JSON string
wp_list_response_santes_operation_item_dto_instance = WpListResponseSantesOperationItemDto.from_json(json)
# print the JSON string representation of the object
print(WpListResponseSantesOperationItemDto.to_json())

# convert the object into a dict
wp_list_response_santes_operation_item_dto_dict = wp_list_response_santes_operation_item_dto_instance.to_dict()
# create an instance of WpListResponseSantesOperationItemDto from a dict
wp_list_response_santes_operation_item_dto_from_dict = WpListResponseSantesOperationItemDto.from_dict(wp_list_response_santes_operation_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


