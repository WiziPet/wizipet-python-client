# SantesAlimentCatalogueItemDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**picture_id** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.santes_aliment_catalogue_item_dto import SantesAlimentCatalogueItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of SantesAlimentCatalogueItemDto from a JSON string
santes_aliment_catalogue_item_dto_instance = SantesAlimentCatalogueItemDto.from_json(json)
# print the JSON string representation of the object
print(SantesAlimentCatalogueItemDto.to_json())

# convert the object into a dict
santes_aliment_catalogue_item_dto_dict = santes_aliment_catalogue_item_dto_instance.to_dict()
# create an instance of SantesAlimentCatalogueItemDto from a dict
santes_aliment_catalogue_item_dto_from_dict = SantesAlimentCatalogueItemDto.from_dict(santes_aliment_catalogue_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


