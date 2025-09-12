# ProfilesAlertePerteDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** |  | [optional] 
**location** | [**GooglesLatLngLiteralDto**](GooglesLatLngLiteralDto.md) |  | [optional] 
**publication_id** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.profiles_alerte_perte_dto import ProfilesAlertePerteDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProfilesAlertePerteDto from a JSON string
profiles_alerte_perte_dto_instance = ProfilesAlertePerteDto.from_json(json)
# print the JSON string representation of the object
print(ProfilesAlertePerteDto.to_json())

# convert the object into a dict
profiles_alerte_perte_dto_dict = profiles_alerte_perte_dto_instance.to_dict()
# create an instance of ProfilesAlertePerteDto from a dict
profiles_alerte_perte_dto_from_dict = ProfilesAlertePerteDto.from_dict(profiles_alerte_perte_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


