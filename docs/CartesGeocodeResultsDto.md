# CartesGeocodeResultsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[GooglesGeocodeResultDto]**](GooglesGeocodeResultDto.md) |  | [optional] 

## Example

```python
from wizipet_api.models.cartes_geocode_results_dto import CartesGeocodeResultsDto

# TODO update the JSON string below
json = "{}"
# create an instance of CartesGeocodeResultsDto from a JSON string
cartes_geocode_results_dto_instance = CartesGeocodeResultsDto.from_json(json)
# print the JSON string representation of the object
print(CartesGeocodeResultsDto.to_json())

# convert the object into a dict
cartes_geocode_results_dto_dict = cartes_geocode_results_dto_instance.to_dict()
# create an instance of CartesGeocodeResultsDto from a dict
cartes_geocode_results_dto_from_dict = CartesGeocodeResultsDto.from_dict(cartes_geocode_results_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


