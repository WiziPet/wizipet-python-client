# SantesPorteeDto

Portée

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**petits_count** | **int** |  | [optional] 
**date_mise_bas** | **str** |  | [optional] 
**date_fin_lactation** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.santes_portee_dto import SantesPorteeDto

# TODO update the JSON string below
json = "{}"
# create an instance of SantesPorteeDto from a JSON string
santes_portee_dto_instance = SantesPorteeDto.from_json(json)
# print the JSON string representation of the object
print(SantesPorteeDto.to_json())

# convert the object into a dict
santes_portee_dto_dict = santes_portee_dto_instance.to_dict()
# create an instance of SantesPorteeDto from a dict
santes_portee_dto_from_dict = SantesPorteeDto.from_dict(santes_portee_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


