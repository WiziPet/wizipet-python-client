# SantesAlimentDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | [**SantesAlimentTypeDto**](SantesAlimentTypeDto.md) |  | [optional] 
**name** | **str** |  | [optional] 
**proteine_brutes_percent** | **float** |  | [optional] 
**matiere_grasse_percent** | **float** |  | [optional] 
**cellulose_brutes_percent** | **float** |  | [optional] 
**cendres_brutes_percent** | **float** |  | [optional] 
**humidite_percent** | **float** |  | [optional] 
**catalogue_properties** | [**SantesAlimentCataloguePropertiesDto**](SantesAlimentCataloguePropertiesDto.md) |  | [optional] 

## Example

```python
from wizipet_api.models.santes_aliment_dto import SantesAlimentDto

# TODO update the JSON string below
json = "{}"
# create an instance of SantesAlimentDto from a JSON string
santes_aliment_dto_instance = SantesAlimentDto.from_json(json)
# print the JSON string representation of the object
print(SantesAlimentDto.to_json())

# convert the object into a dict
santes_aliment_dto_dict = santes_aliment_dto_instance.to_dict()
# create an instance of SantesAlimentDto from a dict
santes_aliment_dto_from_dict = SantesAlimentDto.from_dict(santes_aliment_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


