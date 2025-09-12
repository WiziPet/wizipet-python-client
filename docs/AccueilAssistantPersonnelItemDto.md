# AccueilAssistantPersonnelItemDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**AccueilAssistantPersonnelTypeDto**](AccueilAssistantPersonnelTypeDto.md) |  | [optional] 
**pensebete_properties** | [**PenseBetesPenseBeteItemDto**](PenseBetesPenseBeteItemDto.md) |  | [optional] 
**message_interne_properties** | [**SantesMessagesInternesMessageInterneItemDto**](SantesMessagesInternesMessageInterneItemDto.md) |  | [optional] 

## Example

```python
from wizipet_api.models.accueil_assistant_personnel_item_dto import AccueilAssistantPersonnelItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of AccueilAssistantPersonnelItemDto from a JSON string
accueil_assistant_personnel_item_dto_instance = AccueilAssistantPersonnelItemDto.from_json(json)
# print the JSON string representation of the object
print(AccueilAssistantPersonnelItemDto.to_json())

# convert the object into a dict
accueil_assistant_personnel_item_dto_dict = accueil_assistant_personnel_item_dto_instance.to_dict()
# create an instance of AccueilAssistantPersonnelItemDto from a dict
accueil_assistant_personnel_item_dto_from_dict = AccueilAssistantPersonnelItemDto.from_dict(accueil_assistant_personnel_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


