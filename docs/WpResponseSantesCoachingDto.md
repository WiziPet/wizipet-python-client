# WpResponseSantesCoachingDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SantesCoachingDto**](SantesCoachingDto.md) |  | [optional] 
**is_success** | **bool** |  | [optional] 
**error_code** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.wp_response_santes_coaching_dto import WpResponseSantesCoachingDto

# TODO update the JSON string below
json = "{}"
# create an instance of WpResponseSantesCoachingDto from a JSON string
wp_response_santes_coaching_dto_instance = WpResponseSantesCoachingDto.from_json(json)
# print the JSON string representation of the object
print(WpResponseSantesCoachingDto.to_json())

# convert the object into a dict
wp_response_santes_coaching_dto_dict = wp_response_santes_coaching_dto_instance.to_dict()
# create an instance of WpResponseSantesCoachingDto from a dict
wp_response_santes_coaching_dto_from_dict = WpResponseSantesCoachingDto.from_dict(wp_response_santes_coaching_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


