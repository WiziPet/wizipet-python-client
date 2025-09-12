# ListResponseSantesHistoriqueDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SantesHistoriqueDto]**](SantesHistoriqueDto.md) |  | [optional] 
**is_success** | **bool** |  | [optional] 
**error_code** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.list_response_santes_historique_dto import ListResponseSantesHistoriqueDto

# TODO update the JSON string below
json = "{}"
# create an instance of ListResponseSantesHistoriqueDto from a JSON string
list_response_santes_historique_dto_instance = ListResponseSantesHistoriqueDto.from_json(json)
# print the JSON string representation of the object
print(ListResponseSantesHistoriqueDto.to_json())

# convert the object into a dict
list_response_santes_historique_dto_dict = list_response_santes_historique_dto_instance.to_dict()
# create an instance of ListResponseSantesHistoriqueDto from a dict
list_response_santes_historique_dto_from_dict = ListResponseSantesHistoriqueDto.from_dict(list_response_santes_historique_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


