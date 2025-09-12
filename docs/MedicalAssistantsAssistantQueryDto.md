# MedicalAssistantsAssistantQueryDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** |  | [optional] 
**option_id** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.medical_assistants_assistant_query_dto import MedicalAssistantsAssistantQueryDto

# TODO update the JSON string below
json = "{}"
# create an instance of MedicalAssistantsAssistantQueryDto from a JSON string
medical_assistants_assistant_query_dto_instance = MedicalAssistantsAssistantQueryDto.from_json(json)
# print the JSON string representation of the object
print(MedicalAssistantsAssistantQueryDto.to_json())

# convert the object into a dict
medical_assistants_assistant_query_dto_dict = medical_assistants_assistant_query_dto_instance.to_dict()
# create an instance of MedicalAssistantsAssistantQueryDto from a dict
medical_assistants_assistant_query_dto_from_dict = MedicalAssistantsAssistantQueryDto.from_dict(medical_assistants_assistant_query_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


