# CartesUserItemDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**position** | [**GooglesLatLngLiteralDto**](GooglesLatLngLiteralDto.md) |  | [optional] 
**pet_list** | [**List[CartesPetItemDto]**](CartesPetItemDto.md) |  | [optional] 

## Example

```python
from wizipet_api.models.cartes_user_item_dto import CartesUserItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of CartesUserItemDto from a JSON string
cartes_user_item_dto_instance = CartesUserItemDto.from_json(json)
# print the JSON string representation of the object
print(CartesUserItemDto.to_json())

# convert the object into a dict
cartes_user_item_dto_dict = cartes_user_item_dto_instance.to_dict()
# create an instance of CartesUserItemDto from a dict
cartes_user_item_dto_from_dict = CartesUserItemDto.from_dict(cartes_user_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


