# SantesDateAlimentDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** |  | [optional] 
**aliment** | [**SantesAlimentDto**](SantesAlimentDto.md) |  | [optional] 

## Example

```python
from wizipet_api.models.santes_date_aliment_dto import SantesDateAlimentDto

# TODO update the JSON string below
json = "{}"
# create an instance of SantesDateAlimentDto from a JSON string
santes_date_aliment_dto_instance = SantesDateAlimentDto.from_json(json)
# print the JSON string representation of the object
print(SantesDateAlimentDto.to_json())

# convert the object into a dict
santes_date_aliment_dto_dict = santes_date_aliment_dto_instance.to_dict()
# create an instance of SantesDateAlimentDto from a dict
santes_date_aliment_dto_from_dict = SantesDateAlimentDto.from_dict(santes_date_aliment_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


