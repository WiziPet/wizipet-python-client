# SantesSetVeterinaireDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**clinic_name** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**address** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.santes_set_veterinaire_dto import SantesSetVeterinaireDto

# TODO update the JSON string below
json = "{}"
# create an instance of SantesSetVeterinaireDto from a JSON string
santes_set_veterinaire_dto_instance = SantesSetVeterinaireDto.from_json(json)
# print the JSON string representation of the object
print(SantesSetVeterinaireDto.to_json())

# convert the object into a dict
santes_set_veterinaire_dto_dict = santes_set_veterinaire_dto_instance.to_dict()
# create an instance of SantesSetVeterinaireDto from a dict
santes_set_veterinaire_dto_from_dict = SantesSetVeterinaireDto.from_dict(santes_set_veterinaire_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


