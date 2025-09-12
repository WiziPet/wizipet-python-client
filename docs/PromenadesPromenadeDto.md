# PromenadesPromenadeDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**var_date** | **datetime** |  | [optional] 
**parcours_image_id** | **str** |  | [optional] 
**distance_in_km** | **float** |  | [optional] 
**duration** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.promenades_promenade_dto import PromenadesPromenadeDto

# TODO update the JSON string below
json = "{}"
# create an instance of PromenadesPromenadeDto from a JSON string
promenades_promenade_dto_instance = PromenadesPromenadeDto.from_json(json)
# print the JSON string representation of the object
print(PromenadesPromenadeDto.to_json())

# convert the object into a dict
promenades_promenade_dto_dict = promenades_promenade_dto_instance.to_dict()
# create an instance of PromenadesPromenadeDto from a dict
promenades_promenade_dto_from_dict = PromenadesPromenadeDto.from_dict(promenades_promenade_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


