# SantesSetIdentifiantDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifiant** | **str** |  | [optional] 
**type** | [**SantesIdentifiantTypeDto**](SantesIdentifiantTypeDto.md) |  | [optional] 

## Example

```python
from wizipet_api.models.santes_set_identifiant_dto import SantesSetIdentifiantDto

# TODO update the JSON string below
json = "{}"
# create an instance of SantesSetIdentifiantDto from a JSON string
santes_set_identifiant_dto_instance = SantesSetIdentifiantDto.from_json(json)
# print the JSON string representation of the object
print(SantesSetIdentifiantDto.to_json())

# convert the object into a dict
santes_set_identifiant_dto_dict = santes_set_identifiant_dto_instance.to_dict()
# create an instance of SantesSetIdentifiantDto from a dict
santes_set_identifiant_dto_from_dict = SantesSetIdentifiantDto.from_dict(santes_set_identifiant_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


