# ListResponseAntiparasitairesAntiparasitaireDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AntiparasitairesAntiparasitaireDto]**](AntiparasitairesAntiparasitaireDto.md) |  | [optional] 
**is_success** | **bool** |  | [optional] 
**error_code** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.list_response_antiparasitaires_antiparasitaire_dto import ListResponseAntiparasitairesAntiparasitaireDto

# TODO update the JSON string below
json = "{}"
# create an instance of ListResponseAntiparasitairesAntiparasitaireDto from a JSON string
list_response_antiparasitaires_antiparasitaire_dto_instance = ListResponseAntiparasitairesAntiparasitaireDto.from_json(json)
# print the JSON string representation of the object
print(ListResponseAntiparasitairesAntiparasitaireDto.to_json())

# convert the object into a dict
list_response_antiparasitaires_antiparasitaire_dto_dict = list_response_antiparasitaires_antiparasitaire_dto_instance.to_dict()
# create an instance of ListResponseAntiparasitairesAntiparasitaireDto from a dict
list_response_antiparasitaires_antiparasitaire_dto_from_dict = ListResponseAntiparasitairesAntiparasitaireDto.from_dict(list_response_antiparasitaires_antiparasitaire_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


