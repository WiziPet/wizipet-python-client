# SantesOperationDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**var_date** | **str** |  | [optional] 
**commentaire** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**traitements** | [**List[SantesTraitementDto]**](SantesTraitementDto.md) |  | [optional] 

## Example

```python
from wizipet_api.models.santes_operation_dto import SantesOperationDto

# TODO update the JSON string below
json = "{}"
# create an instance of SantesOperationDto from a JSON string
santes_operation_dto_instance = SantesOperationDto.from_json(json)
# print the JSON string representation of the object
print(SantesOperationDto.to_json())

# convert the object into a dict
santes_operation_dto_dict = santes_operation_dto_instance.to_dict()
# create an instance of SantesOperationDto from a dict
santes_operation_dto_from_dict = SantesOperationDto.from_dict(santes_operation_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


