# CartesCartePerteDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location** | [**GooglesLatLngLiteralDto**](GooglesLatLngLiteralDto.md) |  | [optional] 

## Example

```python
from wizipet_api.models.cartes_carte_perte_dto import CartesCartePerteDto

# TODO update the JSON string below
json = "{}"
# create an instance of CartesCartePerteDto from a JSON string
cartes_carte_perte_dto_instance = CartesCartePerteDto.from_json(json)
# print the JSON string representation of the object
print(CartesCartePerteDto.to_json())

# convert the object into a dict
cartes_carte_perte_dto_dict = cartes_carte_perte_dto_instance.to_dict()
# create an instance of CartesCartePerteDto from a dict
cartes_carte_perte_dto_from_dict = CartesCartePerteDto.from_dict(cartes_carte_perte_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


