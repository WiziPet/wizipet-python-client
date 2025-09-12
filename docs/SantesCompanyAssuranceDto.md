# SantesCompanyAssuranceDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**image_id** | **str** |  | [optional] 
**is_partenaire** | **bool** |  | [optional] 
**index** | **int** |  | [optional] 

## Example

```python
from wizipet_api.models.santes_company_assurance_dto import SantesCompanyAssuranceDto

# TODO update the JSON string below
json = "{}"
# create an instance of SantesCompanyAssuranceDto from a JSON string
santes_company_assurance_dto_instance = SantesCompanyAssuranceDto.from_json(json)
# print the JSON string representation of the object
print(SantesCompanyAssuranceDto.to_json())

# convert the object into a dict
santes_company_assurance_dto_dict = santes_company_assurance_dto_instance.to_dict()
# create an instance of SantesCompanyAssuranceDto from a dict
santes_company_assurance_dto_from_dict = SantesCompanyAssuranceDto.from_dict(santes_company_assurance_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


