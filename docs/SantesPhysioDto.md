# SantesPhysioDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**birthday** | **str** |  | [optional] 
**portee_list** | [**List[SantesPorteeDto]**](SantesPorteeDto.md) |  | [optional] 

## Example

```python
from wizipet_api.models.santes_physio_dto import SantesPhysioDto

# TODO update the JSON string below
json = "{}"
# create an instance of SantesPhysioDto from a JSON string
santes_physio_dto_instance = SantesPhysioDto.from_json(json)
# print the JSON string representation of the object
print(SantesPhysioDto.to_json())

# convert the object into a dict
santes_physio_dto_dict = santes_physio_dto_instance.to_dict()
# create an instance of SantesPhysioDto from a dict
santes_physio_dto_from_dict = SantesPhysioDto.from_dict(santes_physio_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


