# SantesSetSterilisationDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**est_sterilise** | **bool** |  | [optional] 
**var_date** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.santes_set_sterilisation_dto import SantesSetSterilisationDto

# TODO update the JSON string below
json = "{}"
# create an instance of SantesSetSterilisationDto from a JSON string
santes_set_sterilisation_dto_instance = SantesSetSterilisationDto.from_json(json)
# print the JSON string representation of the object
print(SantesSetSterilisationDto.to_json())

# convert the object into a dict
santes_set_sterilisation_dto_dict = santes_set_sterilisation_dto_instance.to_dict()
# create an instance of SantesSetSterilisationDto from a dict
santes_set_sterilisation_dto_from_dict = SantesSetSterilisationDto.from_dict(santes_set_sterilisation_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


