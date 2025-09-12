# SantesBilanSectionResultDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**diagnostic** | **str** |  | [optional] 
**status** | [**SantesSectionStatusDto**](SantesSectionStatusDto.md) |  | [optional] 

## Example

```python
from wizipet_api.models.santes_bilan_section_result_dto import SantesBilanSectionResultDto

# TODO update the JSON string below
json = "{}"
# create an instance of SantesBilanSectionResultDto from a JSON string
santes_bilan_section_result_dto_instance = SantesBilanSectionResultDto.from_json(json)
# print the JSON string representation of the object
print(SantesBilanSectionResultDto.to_json())

# convert the object into a dict
santes_bilan_section_result_dto_dict = santes_bilan_section_result_dto_instance.to_dict()
# create an instance of SantesBilanSectionResultDto from a dict
santes_bilan_section_result_dto_from_dict = SantesBilanSectionResultDto.from_dict(santes_bilan_section_result_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


