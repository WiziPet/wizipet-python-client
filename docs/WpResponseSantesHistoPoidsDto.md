# WpResponseSantesHistoPoidsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SantesHistoPoidsDto**](SantesHistoPoidsDto.md) |  | [optional] 
**is_success** | **bool** |  | [optional] 
**error_code** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.wp_response_santes_histo_poids_dto import WpResponseSantesHistoPoidsDto

# TODO update the JSON string below
json = "{}"
# create an instance of WpResponseSantesHistoPoidsDto from a JSON string
wp_response_santes_histo_poids_dto_instance = WpResponseSantesHistoPoidsDto.from_json(json)
# print the JSON string representation of the object
print(WpResponseSantesHistoPoidsDto.to_json())

# convert the object into a dict
wp_response_santes_histo_poids_dto_dict = wp_response_santes_histo_poids_dto_instance.to_dict()
# create an instance of WpResponseSantesHistoPoidsDto from a dict
wp_response_santes_histo_poids_dto_from_dict = WpResponseSantesHistoPoidsDto.from_dict(wp_response_santes_histo_poids_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


