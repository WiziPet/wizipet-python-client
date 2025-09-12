# SantesHistoPoidsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**evolution_poids_g** | [**List[SantesDatePoidsDto]**](SantesDatePoidsDto.md) |  | [optional] 

## Example

```python
from wizipet_api.models.santes_histo_poids_dto import SantesHistoPoidsDto

# TODO update the JSON string below
json = "{}"
# create an instance of SantesHistoPoidsDto from a JSON string
santes_histo_poids_dto_instance = SantesHistoPoidsDto.from_json(json)
# print the JSON string representation of the object
print(SantesHistoPoidsDto.to_json())

# convert the object into a dict
santes_histo_poids_dto_dict = santes_histo_poids_dto_instance.to_dict()
# create an instance of SantesHistoPoidsDto from a dict
santes_histo_poids_dto_from_dict = SantesHistoPoidsDto.from_dict(santes_histo_poids_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


