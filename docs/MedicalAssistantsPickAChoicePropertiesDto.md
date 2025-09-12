# MedicalAssistantsPickAChoicePropertiesDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**option_list** | [**List[MedicalAssistantsOptionDto]**](MedicalAssistantsOptionDto.md) |  | [optional] 

## Example

```python
from wizipet_api.models.medical_assistants_pick_a_choice_properties_dto import MedicalAssistantsPickAChoicePropertiesDto

# TODO update the JSON string below
json = "{}"
# create an instance of MedicalAssistantsPickAChoicePropertiesDto from a JSON string
medical_assistants_pick_a_choice_properties_dto_instance = MedicalAssistantsPickAChoicePropertiesDto.from_json(json)
# print the JSON string representation of the object
print(MedicalAssistantsPickAChoicePropertiesDto.to_json())

# convert the object into a dict
medical_assistants_pick_a_choice_properties_dto_dict = medical_assistants_pick_a_choice_properties_dto_instance.to_dict()
# create an instance of MedicalAssistantsPickAChoicePropertiesDto from a dict
medical_assistants_pick_a_choice_properties_dto_from_dict = MedicalAssistantsPickAChoicePropertiesDto.from_dict(medical_assistants_pick_a_choice_properties_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


