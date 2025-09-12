# DiscussionsMessageDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**content** | **str** |  | [optional] 
**author** | **str** |  | [optional] 
**creation_date** | **datetime** |  | [optional] 

## Example

```python
from wizipet_api.models.discussions_message_dto import DiscussionsMessageDto

# TODO update the JSON string below
json = "{}"
# create an instance of DiscussionsMessageDto from a JSON string
discussions_message_dto_instance = DiscussionsMessageDto.from_json(json)
# print the JSON string representation of the object
print(DiscussionsMessageDto.to_json())

# convert the object into a dict
discussions_message_dto_dict = discussions_message_dto_instance.to_dict()
# create an instance of DiscussionsMessageDto from a dict
discussions_message_dto_from_dict = DiscussionsMessageDto.from_dict(discussions_message_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


