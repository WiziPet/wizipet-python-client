# SantesOperationItemDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**start_date** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**commentaire** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.santes_operation_item_dto import SantesOperationItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of SantesOperationItemDto from a JSON string
santes_operation_item_dto_instance = SantesOperationItemDto.from_json(json)
# print the JSON string representation of the object
print(SantesOperationItemDto.to_json())

# convert the object into a dict
santes_operation_item_dto_dict = santes_operation_item_dto_instance.to_dict()
# create an instance of SantesOperationItemDto from a dict
santes_operation_item_dto_from_dict = SantesOperationItemDto.from_dict(santes_operation_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


