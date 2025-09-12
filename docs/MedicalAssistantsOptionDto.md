# MedicalAssistantsOptionDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**option_id** | **str** |  | [optional] 
**label** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.medical_assistants_option_dto import MedicalAssistantsOptionDto

# TODO update the JSON string below
json = "{}"
# create an instance of MedicalAssistantsOptionDto from a JSON string
medical_assistants_option_dto_instance = MedicalAssistantsOptionDto.from_json(json)
# print the JSON string representation of the object
print(MedicalAssistantsOptionDto.to_json())

# convert the object into a dict
medical_assistants_option_dto_dict = medical_assistants_option_dto_instance.to_dict()
# create an instance of MedicalAssistantsOptionDto from a dict
medical_assistants_option_dto_from_dict = MedicalAssistantsOptionDto.from_dict(medical_assistants_option_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


