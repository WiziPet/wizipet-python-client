# SantesMessagesInternesOtherProfileItemMessageInterneDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**pet_name** | **str** |  | [optional] 
**picture_id** | **str** |  | [optional] 
**race_id** | **str** |  | [optional] 
**alerte_perte** | [**ProfilesAlertePerteDto**](ProfilesAlertePerteDto.md) |  | [optional] 

## Example

```python
from wizipet_api.models.santes_messages_internes_other_profile_item_message_interne_dto import SantesMessagesInternesOtherProfileItemMessageInterneDto

# TODO update the JSON string below
json = "{}"
# create an instance of SantesMessagesInternesOtherProfileItemMessageInterneDto from a JSON string
santes_messages_internes_other_profile_item_message_interne_dto_instance = SantesMessagesInternesOtherProfileItemMessageInterneDto.from_json(json)
# print the JSON string representation of the object
print(SantesMessagesInternesOtherProfileItemMessageInterneDto.to_json())

# convert the object into a dict
santes_messages_internes_other_profile_item_message_interne_dto_dict = santes_messages_internes_other_profile_item_message_interne_dto_instance.to_dict()
# create an instance of SantesMessagesInternesOtherProfileItemMessageInterneDto from a dict
santes_messages_internes_other_profile_item_message_interne_dto_from_dict = SantesMessagesInternesOtherProfileItemMessageInterneDto.from_dict(santes_messages_internes_other_profile_item_message_interne_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


