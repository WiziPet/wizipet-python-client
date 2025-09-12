# SantesOverviewPhysioDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stade** | [**SantesStadePhysioDto**](SantesStadePhysioDto.md) |  | [optional] 

## Example

```python
from wizipet_api.models.santes_overview_physio_dto import SantesOverviewPhysioDto

# TODO update the JSON string below
json = "{}"
# create an instance of SantesOverviewPhysioDto from a JSON string
santes_overview_physio_dto_instance = SantesOverviewPhysioDto.from_json(json)
# print the JSON string representation of the object
print(SantesOverviewPhysioDto.to_json())

# convert the object into a dict
santes_overview_physio_dto_dict = santes_overview_physio_dto_instance.to_dict()
# create an instance of SantesOverviewPhysioDto from a dict
santes_overview_physio_dto_from_dict = SantesOverviewPhysioDto.from_dict(santes_overview_physio_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


