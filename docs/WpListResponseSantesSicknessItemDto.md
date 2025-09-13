# WpListResponseSantesSicknessItemDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SantesSicknessItemDto]**](SantesSicknessItemDto.md) |  | [optional] 
**is_success** | **bool** |  | [optional] 
**error_code** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.wp_list_response_santes_sickness_item_dto import WpListResponseSantesSicknessItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of WpListResponseSantesSicknessItemDto from a JSON string
wp_list_response_santes_sickness_item_dto_instance = WpListResponseSantesSicknessItemDto.from_json(json)
# print the JSON string representation of the object
print(WpListResponseSantesSicknessItemDto.to_json())

# convert the object into a dict
wp_list_response_santes_sickness_item_dto_dict = wp_list_response_santes_sickness_item_dto_instance.to_dict()
# create an instance of WpListResponseSantesSicknessItemDto from a dict
wp_list_response_santes_sickness_item_dto_from_dict = WpListResponseSantesSicknessItemDto.from_dict(wp_list_response_santes_sickness_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


