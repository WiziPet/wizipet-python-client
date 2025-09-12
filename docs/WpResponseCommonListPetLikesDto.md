# WpResponseCommonListPetLikesDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CommonListPetLikesDto**](CommonListPetLikesDto.md) |  | [optional] 
**is_success** | **bool** |  | [optional] 
**error_code** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.wp_response_common_list_pet_likes_dto import WpResponseCommonListPetLikesDto

# TODO update the JSON string below
json = "{}"
# create an instance of WpResponseCommonListPetLikesDto from a JSON string
wp_response_common_list_pet_likes_dto_instance = WpResponseCommonListPetLikesDto.from_json(json)
# print the JSON string representation of the object
print(WpResponseCommonListPetLikesDto.to_json())

# convert the object into a dict
wp_response_common_list_pet_likes_dto_dict = wp_response_common_list_pet_likes_dto_instance.to_dict()
# create an instance of WpResponseCommonListPetLikesDto from a dict
wp_response_common_list_pet_likes_dto_from_dict = WpResponseCommonListPetLikesDto.from_dict(wp_response_common_list_pet_likes_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


