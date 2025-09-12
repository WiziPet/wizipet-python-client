# SantesSetAlimentDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**SantesAlimentTypeDto**](SantesAlimentTypeDto.md) |  | [optional] 
**custom_properties** | [**SantesSetAlimentCustomPropertiesDto**](SantesSetAlimentCustomPropertiesDto.md) |  | [optional] 
**catalogue_properties** | [**SantesSetAlimentCataloguePropertiesDto**](SantesSetAlimentCataloguePropertiesDto.md) |  | [optional] 

## Example

```python
from wizipet_api.models.santes_set_aliment_dto import SantesSetAlimentDto

# TODO update the JSON string below
json = "{}"
# create an instance of SantesSetAlimentDto from a JSON string
santes_set_aliment_dto_instance = SantesSetAlimentDto.from_json(json)
# print the JSON string representation of the object
print(SantesSetAlimentDto.to_json())

# convert the object into a dict
santes_set_aliment_dto_dict = santes_set_aliment_dto_instance.to_dict()
# create an instance of SantesSetAlimentDto from a dict
santes_set_aliment_dto_from_dict = SantesSetAlimentDto.from_dict(santes_set_aliment_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


