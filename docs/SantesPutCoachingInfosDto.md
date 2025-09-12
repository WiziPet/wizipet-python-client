# SantesPutCoachingInfosDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clef** | [**SantesCoachingInfoClefDto**](SantesCoachingInfoClefDto.md) |  | [optional] 
**int_value** | **int** |  | [optional] 

## Example

```python
from wizipet_api.models.santes_put_coaching_infos_dto import SantesPutCoachingInfosDto

# TODO update the JSON string below
json = "{}"
# create an instance of SantesPutCoachingInfosDto from a JSON string
santes_put_coaching_infos_dto_instance = SantesPutCoachingInfosDto.from_json(json)
# print the JSON string representation of the object
print(SantesPutCoachingInfosDto.to_json())

# convert the object into a dict
santes_put_coaching_infos_dto_dict = santes_put_coaching_infos_dto_instance.to_dict()
# create an instance of SantesPutCoachingInfosDto from a dict
santes_put_coaching_infos_dto_from_dict = SantesPutCoachingInfosDto.from_dict(santes_put_coaching_infos_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


