# WpListResponsePenseBetesPenseBeteItemDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PenseBetesPenseBeteItemDto]**](PenseBetesPenseBeteItemDto.md) |  | [optional] 
**is_success** | **bool** |  | [optional] 
**error_code** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.wp_list_response_pense_betes_pense_bete_item_dto import WpListResponsePenseBetesPenseBeteItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of WpListResponsePenseBetesPenseBeteItemDto from a JSON string
wp_list_response_pense_betes_pense_bete_item_dto_instance = WpListResponsePenseBetesPenseBeteItemDto.from_json(json)
# print the JSON string representation of the object
print(WpListResponsePenseBetesPenseBeteItemDto.to_json())

# convert the object into a dict
wp_list_response_pense_betes_pense_bete_item_dto_dict = wp_list_response_pense_betes_pense_bete_item_dto_instance.to_dict()
# create an instance of WpListResponsePenseBetesPenseBeteItemDto from a dict
wp_list_response_pense_betes_pense_bete_item_dto_from_dict = WpListResponsePenseBetesPenseBeteItemDto.from_dict(wp_list_response_pense_betes_pense_bete_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


