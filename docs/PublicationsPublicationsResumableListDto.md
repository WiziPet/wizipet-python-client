# PublicationsPublicationsResumableListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_more** | **bool** |  | [optional] 
**count** | **int** |  | [optional] 
**continuation_token** | **str** |  | [optional] 
**has_active_challenges** | **bool** |  | [optional] 
**data** | [**List[PublicationsPublicationItemDto]**](PublicationsPublicationItemDto.md) |  | [optional] 
**is_success** | **bool** |  | [optional] 
**error_code** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.publications_publications_resumable_list_dto import PublicationsPublicationsResumableListDto

# TODO update the JSON string below
json = "{}"
# create an instance of PublicationsPublicationsResumableListDto from a JSON string
publications_publications_resumable_list_dto_instance = PublicationsPublicationsResumableListDto.from_json(json)
# print the JSON string representation of the object
print(PublicationsPublicationsResumableListDto.to_json())

# convert the object into a dict
publications_publications_resumable_list_dto_dict = publications_publications_resumable_list_dto_instance.to_dict()
# create an instance of PublicationsPublicationsResumableListDto from a dict
publications_publications_resumable_list_dto_from_dict = PublicationsPublicationsResumableListDto.from_dict(publications_publications_resumable_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


