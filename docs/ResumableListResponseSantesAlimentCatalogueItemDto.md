# ResumableListResponseSantesAlimentCatalogueItemDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_more** | **bool** |  | [optional] 
**count** | **int** |  | [optional] 
**continuation_token** | **str** |  | [optional] 
**data** | [**List[SantesAlimentCatalogueItemDto]**](SantesAlimentCatalogueItemDto.md) |  | [optional] 
**is_success** | **bool** |  | [optional] 
**error_code** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.resumable_list_response_santes_aliment_catalogue_item_dto import ResumableListResponseSantesAlimentCatalogueItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of ResumableListResponseSantesAlimentCatalogueItemDto from a JSON string
resumable_list_response_santes_aliment_catalogue_item_dto_instance = ResumableListResponseSantesAlimentCatalogueItemDto.from_json(json)
# print the JSON string representation of the object
print(ResumableListResponseSantesAlimentCatalogueItemDto.to_json())

# convert the object into a dict
resumable_list_response_santes_aliment_catalogue_item_dto_dict = resumable_list_response_santes_aliment_catalogue_item_dto_instance.to_dict()
# create an instance of ResumableListResponseSantesAlimentCatalogueItemDto from a dict
resumable_list_response_santes_aliment_catalogue_item_dto_from_dict = ResumableListResponseSantesAlimentCatalogueItemDto.from_dict(resumable_list_response_santes_aliment_catalogue_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


