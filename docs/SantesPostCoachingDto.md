# SantesPostCoachingDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aliment_principal** | [**SantesPostCoachingAlimentDto**](SantesPostCoachingAlimentDto.md) |  | [optional] 
**aliment_secondaire** | [**SantesPostCoachingAlimentDto**](SantesPostCoachingAlimentDto.md) |  | [optional] 

## Example

```python
from wizipet_api.models.santes_post_coaching_dto import SantesPostCoachingDto

# TODO update the JSON string below
json = "{}"
# create an instance of SantesPostCoachingDto from a JSON string
santes_post_coaching_dto_instance = SantesPostCoachingDto.from_json(json)
# print the JSON string representation of the object
print(SantesPostCoachingDto.to_json())

# convert the object into a dict
santes_post_coaching_dto_dict = santes_post_coaching_dto_instance.to_dict()
# create an instance of SantesPostCoachingDto from a dict
santes_post_coaching_dto_from_dict = SantesPostCoachingDto.from_dict(santes_post_coaching_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


