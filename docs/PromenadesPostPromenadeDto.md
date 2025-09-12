# PromenadesPostPromenadeDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**promenade_path** | [**List[GooglesLatLngLiteralDto]**](GooglesLatLngLiteralDto.md) |  | [optional] 
**start_time** | **datetime** |  | [optional] 
**duration** | **str** |  | [optional] 
**distance_in_km** | **float** |  | [optional] 

## Example

```python
from wizipet_api.models.promenades_post_promenade_dto import PromenadesPostPromenadeDto

# TODO update the JSON string below
json = "{}"
# create an instance of PromenadesPostPromenadeDto from a JSON string
promenades_post_promenade_dto_instance = PromenadesPostPromenadeDto.from_json(json)
# print the JSON string representation of the object
print(PromenadesPostPromenadeDto.to_json())

# convert the object into a dict
promenades_post_promenade_dto_dict = promenades_post_promenade_dto_instance.to_dict()
# create an instance of PromenadesPostPromenadeDto from a dict
promenades_post_promenade_dto_from_dict = PromenadesPostPromenadeDto.from_dict(promenades_post_promenade_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


