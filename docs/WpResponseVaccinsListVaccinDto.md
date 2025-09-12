# WpResponseVaccinsListVaccinDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**VaccinsListVaccinDto**](VaccinsListVaccinDto.md) |  | [optional] 
**is_success** | **bool** |  | [optional] 
**error_code** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.wp_response_vaccins_list_vaccin_dto import WpResponseVaccinsListVaccinDto

# TODO update the JSON string below
json = "{}"
# create an instance of WpResponseVaccinsListVaccinDto from a JSON string
wp_response_vaccins_list_vaccin_dto_instance = WpResponseVaccinsListVaccinDto.from_json(json)
# print the JSON string representation of the object
print(WpResponseVaccinsListVaccinDto.to_json())

# convert the object into a dict
wp_response_vaccins_list_vaccin_dto_dict = wp_response_vaccins_list_vaccin_dto_instance.to_dict()
# create an instance of WpResponseVaccinsListVaccinDto from a dict
wp_response_vaccins_list_vaccin_dto_from_dict = WpResponseVaccinsListVaccinDto.from_dict(wp_response_vaccins_list_vaccin_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


