# CommonListPetLikesDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id_list** | **List[str]** |  | [optional] 

## Example

```python
from wizipet_api.models.common_list_pet_likes_dto import CommonListPetLikesDto

# TODO update the JSON string below
json = "{}"
# create an instance of CommonListPetLikesDto from a JSON string
common_list_pet_likes_dto_instance = CommonListPetLikesDto.from_json(json)
# print the JSON string representation of the object
print(CommonListPetLikesDto.to_json())

# convert the object into a dict
common_list_pet_likes_dto_dict = common_list_pet_likes_dto_instance.to_dict()
# create an instance of CommonListPetLikesDto from a dict
common_list_pet_likes_dto_from_dict = CommonListPetLikesDto.from_dict(common_list_pet_likes_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


