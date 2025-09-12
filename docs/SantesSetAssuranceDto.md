# SantesSetAssuranceDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_id** | **str** |  | [optional] 
**company_name** | **str** |  | [optional] 
**contract** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.santes_set_assurance_dto import SantesSetAssuranceDto

# TODO update the JSON string below
json = "{}"
# create an instance of SantesSetAssuranceDto from a JSON string
santes_set_assurance_dto_instance = SantesSetAssuranceDto.from_json(json)
# print the JSON string representation of the object
print(SantesSetAssuranceDto.to_json())

# convert the object into a dict
santes_set_assurance_dto_dict = santes_set_assurance_dto_instance.to_dict()
# create an instance of SantesSetAssuranceDto from a dict
santes_set_assurance_dto_from_dict = SantesSetAssuranceDto.from_dict(santes_set_assurance_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


