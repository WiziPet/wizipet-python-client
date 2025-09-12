# SantesDatePoidsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** |  | [optional] 
**poids_g** | **int** |  | [optional] 

## Example

```python
from wizipet_api.models.santes_date_poids_dto import SantesDatePoidsDto

# TODO update the JSON string below
json = "{}"
# create an instance of SantesDatePoidsDto from a JSON string
santes_date_poids_dto_instance = SantesDatePoidsDto.from_json(json)
# print the JSON string representation of the object
print(SantesDatePoidsDto.to_json())

# convert the object into a dict
santes_date_poids_dto_dict = santes_date_poids_dto_instance.to_dict()
# create an instance of SantesDatePoidsDto from a dict
santes_date_poids_dto_from_dict = SantesDatePoidsDto.from_dict(santes_date_poids_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


