# WpResponsePenseBetesPenseBeteDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PenseBetesPenseBeteDto**](PenseBetesPenseBeteDto.md) |  | [optional] 
**is_success** | **bool** |  | [optional] 
**error_code** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.wp_response_pense_betes_pense_bete_dto import WpResponsePenseBetesPenseBeteDto

# TODO update the JSON string below
json = "{}"
# create an instance of WpResponsePenseBetesPenseBeteDto from a JSON string
wp_response_pense_betes_pense_bete_dto_instance = WpResponsePenseBetesPenseBeteDto.from_json(json)
# print the JSON string representation of the object
print(WpResponsePenseBetesPenseBeteDto.to_json())

# convert the object into a dict
wp_response_pense_betes_pense_bete_dto_dict = wp_response_pense_betes_pense_bete_dto_instance.to_dict()
# create an instance of WpResponsePenseBetesPenseBeteDto from a dict
wp_response_pense_betes_pense_bete_dto_from_dict = WpResponsePenseBetesPenseBeteDto.from_dict(wp_response_pense_betes_pense_bete_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


