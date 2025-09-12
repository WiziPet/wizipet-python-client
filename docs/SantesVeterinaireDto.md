# SantesVeterinaireDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**clinic_name** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**address** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.santes_veterinaire_dto import SantesVeterinaireDto

# TODO update the JSON string below
json = "{}"
# create an instance of SantesVeterinaireDto from a JSON string
santes_veterinaire_dto_instance = SantesVeterinaireDto.from_json(json)
# print the JSON string representation of the object
print(SantesVeterinaireDto.to_json())

# convert the object into a dict
santes_veterinaire_dto_dict = santes_veterinaire_dto_instance.to_dict()
# create an instance of SantesVeterinaireDto from a dict
santes_veterinaire_dto_from_dict = SantesVeterinaireDto.from_dict(santes_veterinaire_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


