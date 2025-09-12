# CartesPositionDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | [**GooglesLatLngLiteralDto**](GooglesLatLngLiteralDto.md) |  | [optional] 

## Example

```python
from wizipet_api.models.cartes_position_dto import CartesPositionDto

# TODO update the JSON string below
json = "{}"
# create an instance of CartesPositionDto from a JSON string
cartes_position_dto_instance = CartesPositionDto.from_json(json)
# print the JSON string representation of the object
print(CartesPositionDto.to_json())

# convert the object into a dict
cartes_position_dto_dict = cartes_position_dto_instance.to_dict()
# create an instance of CartesPositionDto from a dict
cartes_position_dto_from_dict = CartesPositionDto.from_dict(cartes_position_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


