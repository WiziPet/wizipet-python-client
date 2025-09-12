# MedicalAssistantsDefinitiveAnswerPropertiesDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**diagnostic** | **str** |  | [optional] 
**recommendation** | **str** |  | [optional] 
**niveau_urgence** | **int** |  | [optional] 

## Example

```python
from wizipet_api.models.medical_assistants_definitive_answer_properties_dto import MedicalAssistantsDefinitiveAnswerPropertiesDto

# TODO update the JSON string below
json = "{}"
# create an instance of MedicalAssistantsDefinitiveAnswerPropertiesDto from a JSON string
medical_assistants_definitive_answer_properties_dto_instance = MedicalAssistantsDefinitiveAnswerPropertiesDto.from_json(json)
# print the JSON string representation of the object
print(MedicalAssistantsDefinitiveAnswerPropertiesDto.to_json())

# convert the object into a dict
medical_assistants_definitive_answer_properties_dto_dict = medical_assistants_definitive_answer_properties_dto_instance.to_dict()
# create an instance of MedicalAssistantsDefinitiveAnswerPropertiesDto from a dict
medical_assistants_definitive_answer_properties_dto_from_dict = MedicalAssistantsDefinitiveAnswerPropertiesDto.from_dict(medical_assistants_definitive_answer_properties_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


