# CartesPlaceDetailsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**place** | [**GooglesPlaceDto**](GooglesPlaceDto.md) |  | [optional] 
**sub_categories** | [**List[PlacesPlaceSubCategoryDto]**](PlacesPlaceSubCategoryDto.md) |  | [optional] 

## Example

```python
from wizipet_api.models.cartes_place_details_dto import CartesPlaceDetailsDto

# TODO update the JSON string below
json = "{}"
# create an instance of CartesPlaceDetailsDto from a JSON string
cartes_place_details_dto_instance = CartesPlaceDetailsDto.from_json(json)
# print the JSON string representation of the object
print(CartesPlaceDetailsDto.to_json())

# convert the object into a dict
cartes_place_details_dto_dict = cartes_place_details_dto_instance.to_dict()
# create an instance of CartesPlaceDetailsDto from a dict
cartes_place_details_dto_from_dict = CartesPlaceDetailsDto.from_dict(cartes_place_details_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


