# SantesRecoAlimentCatalogueItemDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aliment_catalogue_item** | [**SantesAlimentCatalogueItemDto**](SantesAlimentCatalogueItemDto.md) |  | [optional] 
**reco_ration_100be_g** | **int** |  | [optional] 
**reco_ration_80be_g** | **int** |  | [optional] 
**type** | [**SantesRecoAlimentTypeDto**](SantesRecoAlimentTypeDto.md) |  | [optional] 
**nbr_repas** | [**SantesNombreRepasDto**](SantesNombreRepasDto.md) |  | [optional] 

## Example

```python
from wizipet_api.models.santes_reco_aliment_catalogue_item_dto import SantesRecoAlimentCatalogueItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of SantesRecoAlimentCatalogueItemDto from a JSON string
santes_reco_aliment_catalogue_item_dto_instance = SantesRecoAlimentCatalogueItemDto.from_json(json)
# print the JSON string representation of the object
print(SantesRecoAlimentCatalogueItemDto.to_json())

# convert the object into a dict
santes_reco_aliment_catalogue_item_dto_dict = santes_reco_aliment_catalogue_item_dto_instance.to_dict()
# create an instance of SantesRecoAlimentCatalogueItemDto from a dict
santes_reco_aliment_catalogue_item_dto_from_dict = SantesRecoAlimentCatalogueItemDto.from_dict(santes_reco_aliment_catalogue_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


