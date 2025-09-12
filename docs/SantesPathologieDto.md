# SantesPathologieDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**affects_dogs** | **bool** |  | [optional] 
**affects_cats** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**is_pinned** | **bool** |  | [optional] 
**type** | [**SantesPathologieTypeDto**](SantesPathologieTypeDto.md) |  | [optional] 
**is_frequent** | **bool** |  | [optional] 

## Example

```python
from wizipet_api.models.santes_pathologie_dto import SantesPathologieDto

# TODO update the JSON string below
json = "{}"
# create an instance of SantesPathologieDto from a JSON string
santes_pathologie_dto_instance = SantesPathologieDto.from_json(json)
# print the JSON string representation of the object
print(SantesPathologieDto.to_json())

# convert the object into a dict
santes_pathologie_dto_dict = santes_pathologie_dto_instance.to_dict()
# create an instance of SantesPathologieDto from a dict
santes_pathologie_dto_from_dict = SantesPathologieDto.from_dict(santes_pathologie_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


