# SantesSetMedicamentationDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** |  | [optional] 
**commentaire** | **str** |  | [optional] 
**produit_id** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.santes_set_medicamentation_dto import SantesSetMedicamentationDto

# TODO update the JSON string below
json = "{}"
# create an instance of SantesSetMedicamentationDto from a JSON string
santes_set_medicamentation_dto_instance = SantesSetMedicamentationDto.from_json(json)
# print the JSON string representation of the object
print(SantesSetMedicamentationDto.to_json())

# convert the object into a dict
santes_set_medicamentation_dto_dict = santes_set_medicamentation_dto_instance.to_dict()
# create an instance of SantesSetMedicamentationDto from a dict
santes_set_medicamentation_dto_from_dict = SantesSetMedicamentationDto.from_dict(santes_set_medicamentation_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


