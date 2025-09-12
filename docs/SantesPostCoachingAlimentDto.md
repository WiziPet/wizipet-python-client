# SantesPostCoachingAlimentDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aliment_id** | **str** |  | [optional] 
**ration_g** | **int** |  | [optional] 

## Example

```python
from wizipet_api.models.santes_post_coaching_aliment_dto import SantesPostCoachingAlimentDto

# TODO update the JSON string below
json = "{}"
# create an instance of SantesPostCoachingAlimentDto from a JSON string
santes_post_coaching_aliment_dto_instance = SantesPostCoachingAlimentDto.from_json(json)
# print the JSON string representation of the object
print(SantesPostCoachingAlimentDto.to_json())

# convert the object into a dict
santes_post_coaching_aliment_dto_dict = santes_post_coaching_aliment_dto_instance.to_dict()
# create an instance of SantesPostCoachingAlimentDto from a dict
santes_post_coaching_aliment_dto_from_dict = SantesPostCoachingAlimentDto.from_dict(santes_post_coaching_aliment_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


