# WpResponseSantesVeterinaireDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SantesVeterinaireDto**](SantesVeterinaireDto.md) |  | [optional] 
**is_success** | **bool** |  | [optional] 
**error_code** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.wp_response_santes_veterinaire_dto import WpResponseSantesVeterinaireDto

# TODO update the JSON string below
json = "{}"
# create an instance of WpResponseSantesVeterinaireDto from a JSON string
wp_response_santes_veterinaire_dto_instance = WpResponseSantesVeterinaireDto.from_json(json)
# print the JSON string representation of the object
print(WpResponseSantesVeterinaireDto.to_json())

# convert the object into a dict
wp_response_santes_veterinaire_dto_dict = wp_response_santes_veterinaire_dto_instance.to_dict()
# create an instance of WpResponseSantesVeterinaireDto from a dict
wp_response_santes_veterinaire_dto_from_dict = WpResponseSantesVeterinaireDto.from_dict(wp_response_santes_veterinaire_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


