# CartesPetItemDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**image_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**race_id** | **str** |  | [optional] 
**alerte_perte** | [**CartesCartePerteDto**](CartesCartePerteDto.md) |  | [optional] 

## Example

```python
from wizipet_api.models.cartes_pet_item_dto import CartesPetItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of CartesPetItemDto from a JSON string
cartes_pet_item_dto_instance = CartesPetItemDto.from_json(json)
# print the JSON string representation of the object
print(CartesPetItemDto.to_json())

# convert the object into a dict
cartes_pet_item_dto_dict = cartes_pet_item_dto_instance.to_dict()
# create an instance of CartesPetItemDto from a dict
cartes_pet_item_dto_from_dict = CartesPetItemDto.from_dict(cartes_pet_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


