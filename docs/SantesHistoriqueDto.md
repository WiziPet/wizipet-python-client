# SantesHistoriqueDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** |  | [optional] 
**value** | **float** |  | [optional] 

## Example

```python
from wizipet_api.models.santes_historique_dto import SantesHistoriqueDto

# TODO update the JSON string below
json = "{}"
# create an instance of SantesHistoriqueDto from a JSON string
santes_historique_dto_instance = SantesHistoriqueDto.from_json(json)
# print the JSON string representation of the object
print(SantesHistoriqueDto.to_json())

# convert the object into a dict
santes_historique_dto_dict = santes_historique_dto_instance.to_dict()
# create an instance of SantesHistoriqueDto from a dict
santes_historique_dto_from_dict = SantesHistoriqueDto.from_dict(santes_historique_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


