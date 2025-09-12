# ProfilesDiscussionParticipantDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**pet_name** | **str** |  | [optional] 
**race_id** | **str** |  | [optional] 
**picture_id** | **str** |  | [optional] 
**alerte_perte** | [**ProfilesAlertePerteDto**](ProfilesAlertePerteDto.md) |  | [optional] 

## Example

```python
from wizipet_api.models.profiles_discussion_participant_dto import ProfilesDiscussionParticipantDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProfilesDiscussionParticipantDto from a JSON string
profiles_discussion_participant_dto_instance = ProfilesDiscussionParticipantDto.from_json(json)
# print the JSON string representation of the object
print(ProfilesDiscussionParticipantDto.to_json())

# convert the object into a dict
profiles_discussion_participant_dto_dict = profiles_discussion_participant_dto_instance.to_dict()
# create an instance of ProfilesDiscussionParticipantDto from a dict
profiles_discussion_participant_dto_from_dict = ProfilesDiscussionParticipantDto.from_dict(profiles_discussion_participant_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


