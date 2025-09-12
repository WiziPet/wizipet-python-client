# WpResponseSantesInfoListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SantesInfoListDto**](SantesInfoListDto.md) |  | [optional] 
**is_success** | **bool** |  | [optional] 
**error_code** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.wp_response_santes_info_list_dto import WpResponseSantesInfoListDto

# TODO update the JSON string below
json = "{}"
# create an instance of WpResponseSantesInfoListDto from a JSON string
wp_response_santes_info_list_dto_instance = WpResponseSantesInfoListDto.from_json(json)
# print the JSON string representation of the object
print(WpResponseSantesInfoListDto.to_json())

# convert the object into a dict
wp_response_santes_info_list_dto_dict = wp_response_santes_info_list_dto_instance.to_dict()
# create an instance of WpResponseSantesInfoListDto from a dict
wp_response_santes_info_list_dto_from_dict = WpResponseSantesInfoListDto.from_dict(wp_response_santes_info_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


