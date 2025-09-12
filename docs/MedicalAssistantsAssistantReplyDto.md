# MedicalAssistantsAssistantReplyDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**MedicalAssistantsReplyTypeDto**](MedicalAssistantsReplyTypeDto.md) |  | [optional] 
**pick_a_choice_properties** | [**MedicalAssistantsPickAChoicePropertiesDto**](MedicalAssistantsPickAChoicePropertiesDto.md) |  | [optional] 
**definive_answer_properties** | [**MedicalAssistantsDefinitiveAnswerPropertiesDto**](MedicalAssistantsDefinitiveAnswerPropertiesDto.md) |  | [optional] 

## Example

```python
from wizipet_api.models.medical_assistants_assistant_reply_dto import MedicalAssistantsAssistantReplyDto

# TODO update the JSON string below
json = "{}"
# create an instance of MedicalAssistantsAssistantReplyDto from a JSON string
medical_assistants_assistant_reply_dto_instance = MedicalAssistantsAssistantReplyDto.from_json(json)
# print the JSON string representation of the object
print(MedicalAssistantsAssistantReplyDto.to_json())

# convert the object into a dict
medical_assistants_assistant_reply_dto_dict = medical_assistants_assistant_reply_dto_instance.to_dict()
# create an instance of MedicalAssistantsAssistantReplyDto from a dict
medical_assistants_assistant_reply_dto_from_dict = MedicalAssistantsAssistantReplyDto.from_dict(medical_assistants_assistant_reply_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


