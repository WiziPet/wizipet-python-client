# SantesSetPhysioDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**birthday** | **str** |  | [optional] 
**portee_list** | [**List[SantesPorteeDto]**](SantesPorteeDto.md) |  | [optional] 

## Example

```python
from wizipet_api.models.santes_set_physio_dto import SantesSetPhysioDto

# TODO update the JSON string below
json = "{}"
# create an instance of SantesSetPhysioDto from a JSON string
santes_set_physio_dto_instance = SantesSetPhysioDto.from_json(json)
# print the JSON string representation of the object
print(SantesSetPhysioDto.to_json())

# convert the object into a dict
santes_set_physio_dto_dict = santes_set_physio_dto_instance.to_dict()
# create an instance of SantesSetPhysioDto from a dict
santes_set_physio_dto_from_dict = SantesSetPhysioDto.from_dict(santes_set_physio_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


