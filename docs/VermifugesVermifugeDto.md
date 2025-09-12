# VermifugesVermifugeDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**espece** | [**ProfilesEspeceDto**](ProfilesEspeceDto.md) |  | [optional] 

## Example

```python
from wizipet_api.models.vermifuges_vermifuge_dto import VermifugesVermifugeDto

# TODO update the JSON string below
json = "{}"
# create an instance of VermifugesVermifugeDto from a JSON string
vermifuges_vermifuge_dto_instance = VermifugesVermifugeDto.from_json(json)
# print the JSON string representation of the object
print(VermifugesVermifugeDto.to_json())

# convert the object into a dict
vermifuges_vermifuge_dto_dict = vermifuges_vermifuge_dto_instance.to_dict()
# create an instance of VermifugesVermifugeDto from a dict
vermifuges_vermifuge_dto_from_dict = VermifugesVermifugeDto.from_dict(vermifuges_vermifuge_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


