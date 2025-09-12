# SantesSterilisationDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**est_sterilise** | **bool** |  | [optional] 
**var_date** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.santes_sterilisation_dto import SantesSterilisationDto

# TODO update the JSON string below
json = "{}"
# create an instance of SantesSterilisationDto from a JSON string
santes_sterilisation_dto_instance = SantesSterilisationDto.from_json(json)
# print the JSON string representation of the object
print(SantesSterilisationDto.to_json())

# convert the object into a dict
santes_sterilisation_dto_dict = santes_sterilisation_dto_instance.to_dict()
# create an instance of SantesSterilisationDto from a dict
santes_sterilisation_dto_from_dict = SantesSterilisationDto.from_dict(santes_sterilisation_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


