# CartesPostPetFriendlyLocationParamDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**type** | [**CartesPetFriendlyLocationTypeDto**](CartesPetFriendlyLocationTypeDto.md) |  | [optional] 
**image_id_list** | **List[str]** |  | [optional] 
**always_opened** | **bool** |  | [optional] 
**dog_off_leash** | **bool** |  | [optional] 
**water_available** | **bool** |  | [optional] 
**location** | [**GooglesLatLngLiteralDto**](GooglesLatLngLiteralDto.md) |  | [optional] 
**address** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**star_rating** | **float** |  | [optional] 
**commentaire** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.cartes_post_pet_friendly_location_param_dto import CartesPostPetFriendlyLocationParamDto

# TODO update the JSON string below
json = "{}"
# create an instance of CartesPostPetFriendlyLocationParamDto from a JSON string
cartes_post_pet_friendly_location_param_dto_instance = CartesPostPetFriendlyLocationParamDto.from_json(json)
# print the JSON string representation of the object
print(CartesPostPetFriendlyLocationParamDto.to_json())

# convert the object into a dict
cartes_post_pet_friendly_location_param_dto_dict = cartes_post_pet_friendly_location_param_dto_instance.to_dict()
# create an instance of CartesPostPetFriendlyLocationParamDto from a dict
cartes_post_pet_friendly_location_param_dto_from_dict = CartesPostPetFriendlyLocationParamDto.from_dict(cartes_post_pet_friendly_location_param_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


