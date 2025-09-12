# CommonItemLikeDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **str** |  | [optional] 
**liked** | **bool** |  | [optional] 

## Example

```python
from wizipet_api.models.common_item_like_dto import CommonItemLikeDto

# TODO update the JSON string below
json = "{}"
# create an instance of CommonItemLikeDto from a JSON string
common_item_like_dto_instance = CommonItemLikeDto.from_json(json)
# print the JSON string representation of the object
print(CommonItemLikeDto.to_json())

# convert the object into a dict
common_item_like_dto_dict = common_item_like_dto_instance.to_dict()
# create an instance of CommonItemLikeDto from a dict
common_item_like_dto_from_dict = CommonItemLikeDto.from_dict(common_item_like_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


