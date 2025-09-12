# CartesPutPositionDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | [**GooglesLatLngLiteralDto**](GooglesLatLngLiteralDto.md) |  | [optional] 

## Example

```python
from wizipet_api.models.cartes_put_position_dto import CartesPutPositionDto

# TODO update the JSON string below
json = "{}"
# create an instance of CartesPutPositionDto from a JSON string
cartes_put_position_dto_instance = CartesPutPositionDto.from_json(json)
# print the JSON string representation of the object
print(CartesPutPositionDto.to_json())

# convert the object into a dict
cartes_put_position_dto_dict = cartes_put_position_dto_instance.to_dict()
# create an instance of CartesPutPositionDto from a dict
cartes_put_position_dto_from_dict = CartesPutPositionDto.from_dict(cartes_put_position_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


