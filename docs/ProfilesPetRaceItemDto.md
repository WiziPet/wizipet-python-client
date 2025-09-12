# ProfilesPetRaceItemDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**espece** | [**ProfilesEspeceDto**](ProfilesEspeceDto.md) |  | [optional] 
**age_adulte_mois** | **int** |  | [optional] 
**age_senior_mois** | **int** |  | [optional] 
**poid_debut_gramme** | **int** |  | [optional] 
**poid_fin_gramme** | **int** |  | [optional] 
**taille** | [**ProfilesTailleRaceDto**](ProfilesTailleRaceDto.md) |  | [optional] 
**coef_energetique** | **float** |  | [optional] 

## Example

```python
from wizipet_api.models.profiles_pet_race_item_dto import ProfilesPetRaceItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProfilesPetRaceItemDto from a JSON string
profiles_pet_race_item_dto_instance = ProfilesPetRaceItemDto.from_json(json)
# print the JSON string representation of the object
print(ProfilesPetRaceItemDto.to_json())

# convert the object into a dict
profiles_pet_race_item_dto_dict = profiles_pet_race_item_dto_instance.to_dict()
# create an instance of ProfilesPetRaceItemDto from a dict
profiles_pet_race_item_dto_from_dict = ProfilesPetRaceItemDto.from_dict(profiles_pet_race_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


