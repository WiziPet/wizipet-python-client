# PublicationsPublicationItemDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**group** | [**PublicationsPublicationGroupDto**](PublicationsPublicationGroupDto.md) |  | [optional] 
**author** | [**CommonPetProfileDto**](CommonPetProfileDto.md) |  | [optional] 
**publication_date** | **datetime** |  | [optional] 
**body** | **str** |  | [optional] 
**like_count** | **int** |  | [optional] 
**comment_count** | **int** |  | [optional] 
**share_count** | **int** |  | [optional] 
**image_id_list** | **List[str]** |  | [optional] 
**video_list** | [**List[MediasVideoDto]**](MediasVideoDto.md) |  | [optional] 
**type** | [**PublicationsPublicationTypeDto**](PublicationsPublicationTypeDto.md) |  | [optional] 
**is_actif_challenge** | **bool** |  | [optional] 
**challenge_start_date** | **datetime** |  | [optional] 
**challenge_end_date** | **datetime** |  | [optional] 
**challenge_title** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.publications_publication_item_dto import PublicationsPublicationItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of PublicationsPublicationItemDto from a JSON string
publications_publication_item_dto_instance = PublicationsPublicationItemDto.from_json(json)
# print the JSON string representation of the object
print(PublicationsPublicationItemDto.to_json())

# convert the object into a dict
publications_publication_item_dto_dict = publications_publication_item_dto_instance.to_dict()
# create an instance of PublicationsPublicationItemDto from a dict
publications_publication_item_dto_from_dict = PublicationsPublicationItemDto.from_dict(publications_publication_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


