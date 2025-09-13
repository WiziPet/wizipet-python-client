# WpListResponseSantesMedicamentationItemDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SantesMedicamentationItemDto]**](SantesMedicamentationItemDto.md) |  | [optional] 
**is_success** | **bool** |  | [optional] 
**error_code** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.wp_list_response_santes_medicamentation_item_dto import WpListResponseSantesMedicamentationItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of WpListResponseSantesMedicamentationItemDto from a JSON string
wp_list_response_santes_medicamentation_item_dto_instance = WpListResponseSantesMedicamentationItemDto.from_json(json)
# print the JSON string representation of the object
print(WpListResponseSantesMedicamentationItemDto.to_json())

# convert the object into a dict
wp_list_response_santes_medicamentation_item_dto_dict = wp_list_response_santes_medicamentation_item_dto_instance.to_dict()
# create an instance of WpListResponseSantesMedicamentationItemDto from a dict
wp_list_response_santes_medicamentation_item_dto_from_dict = WpListResponseSantesMedicamentationItemDto.from_dict(wp_list_response_santes_medicamentation_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


