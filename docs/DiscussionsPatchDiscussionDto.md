# DiscussionsPatchDiscussionDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**participant_id_to_add_list** | **List[str]** | Liste de PetId à ajouter. | [optional] 
**picture_id** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.discussions_patch_discussion_dto import DiscussionsPatchDiscussionDto

# TODO update the JSON string below
json = "{}"
# create an instance of DiscussionsPatchDiscussionDto from a JSON string
discussions_patch_discussion_dto_instance = DiscussionsPatchDiscussionDto.from_json(json)
# print the JSON string representation of the object
print(DiscussionsPatchDiscussionDto.to_json())

# convert the object into a dict
discussions_patch_discussion_dto_dict = discussions_patch_discussion_dto_instance.to_dict()
# create an instance of DiscussionsPatchDiscussionDto from a dict
discussions_patch_discussion_dto_from_dict = DiscussionsPatchDiscussionDto.from_dict(discussions_patch_discussion_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


