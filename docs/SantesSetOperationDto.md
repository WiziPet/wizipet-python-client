# SantesSetOperationDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**commentaire** | **str** |  | [optional] 
**traitements** | [**List[SantesSetTraitementDto]**](SantesSetTraitementDto.md) |  | [optional] 

## Example

```python
from wizipet_api.models.santes_set_operation_dto import SantesSetOperationDto

# TODO update the JSON string below
json = "{}"
# create an instance of SantesSetOperationDto from a JSON string
santes_set_operation_dto_instance = SantesSetOperationDto.from_json(json)
# print the JSON string representation of the object
print(SantesSetOperationDto.to_json())

# convert the object into a dict
santes_set_operation_dto_dict = santes_set_operation_dto_instance.to_dict()
# create an instance of SantesSetOperationDto from a dict
santes_set_operation_dto_from_dict = SantesSetOperationDto.from_dict(santes_set_operation_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


