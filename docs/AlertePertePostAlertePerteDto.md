# AlertePertePostAlertePerteDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**perte_date** | **str** |  | [optional] 
**image_id_list** | **List[str]** |  | [optional] 
**location** | [**GooglesLatLngLiteralDto**](GooglesLatLngLiteralDto.md) |  | [optional] 
**address** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.alerte_perte_post_alerte_perte_dto import AlertePertePostAlertePerteDto

# TODO update the JSON string below
json = "{}"
# create an instance of AlertePertePostAlertePerteDto from a JSON string
alerte_perte_post_alerte_perte_dto_instance = AlertePertePostAlertePerteDto.from_json(json)
# print the JSON string representation of the object
print(AlertePertePostAlertePerteDto.to_json())

# convert the object into a dict
alerte_perte_post_alerte_perte_dto_dict = alerte_perte_post_alerte_perte_dto_instance.to_dict()
# create an instance of AlertePertePostAlertePerteDto from a dict
alerte_perte_post_alerte_perte_dto_from_dict = AlertePertePostAlertePerteDto.from_dict(alerte_perte_post_alerte_perte_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


