# SantesIdentifiantDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**SantesIdentifiantTypeDto**](SantesIdentifiantTypeDto.md) |  | [optional] 
**identifiant** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.santes_identifiant_dto import SantesIdentifiantDto

# TODO update the JSON string below
json = "{}"
# create an instance of SantesIdentifiantDto from a JSON string
santes_identifiant_dto_instance = SantesIdentifiantDto.from_json(json)
# print the JSON string representation of the object
print(SantesIdentifiantDto.to_json())

# convert the object into a dict
santes_identifiant_dto_dict = santes_identifiant_dto_instance.to_dict()
# create an instance of SantesIdentifiantDto from a dict
santes_identifiant_dto_from_dict = SantesIdentifiantDto.from_dict(santes_identifiant_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


