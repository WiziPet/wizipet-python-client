# SantesTraitementDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**start_date** | **str** |  | [optional] 
**end_date** | **str** |  | [optional] 
**dose** | **str** |  | [optional] 
**rythme** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.santes_traitement_dto import SantesTraitementDto

# TODO update the JSON string below
json = "{}"
# create an instance of SantesTraitementDto from a JSON string
santes_traitement_dto_instance = SantesTraitementDto.from_json(json)
# print the JSON string representation of the object
print(SantesTraitementDto.to_json())

# convert the object into a dict
santes_traitement_dto_dict = santes_traitement_dto_instance.to_dict()
# create an instance of SantesTraitementDto from a dict
santes_traitement_dto_from_dict = SantesTraitementDto.from_dict(santes_traitement_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


