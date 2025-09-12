# SantesSetAlimentCustomPropertiesDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**proteine_brutes_percent** | **float** |  | [optional] 
**matiere_grasse_percent** | **float** |  | [optional] 
**cellulose_brutes_percent** | **float** |  | [optional] 
**cendres_brutes_percent** | **float** |  | [optional] 
**humidite_percent** | **float** |  | [optional] 

## Example

```python
from wizipet_api.models.santes_set_aliment_custom_properties_dto import SantesSetAlimentCustomPropertiesDto

# TODO update the JSON string below
json = "{}"
# create an instance of SantesSetAlimentCustomPropertiesDto from a JSON string
santes_set_aliment_custom_properties_dto_instance = SantesSetAlimentCustomPropertiesDto.from_json(json)
# print the JSON string representation of the object
print(SantesSetAlimentCustomPropertiesDto.to_json())

# convert the object into a dict
santes_set_aliment_custom_properties_dto_dict = santes_set_aliment_custom_properties_dto_instance.to_dict()
# create an instance of SantesSetAlimentCustomPropertiesDto from a dict
santes_set_aliment_custom_properties_dto_from_dict = SantesSetAlimentCustomPropertiesDto.from_dict(santes_set_aliment_custom_properties_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


