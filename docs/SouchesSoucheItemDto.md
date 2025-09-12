# SouchesSoucheItemDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.souches_souche_item_dto import SouchesSoucheItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of SouchesSoucheItemDto from a JSON string
souches_souche_item_dto_instance = SouchesSoucheItemDto.from_json(json)
# print the JSON string representation of the object
print(SouchesSoucheItemDto.to_json())

# convert the object into a dict
souches_souche_item_dto_dict = souches_souche_item_dto_instance.to_dict()
# create an instance of SouchesSoucheItemDto from a dict
souches_souche_item_dto_from_dict = SouchesSoucheItemDto.from_dict(souches_souche_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


