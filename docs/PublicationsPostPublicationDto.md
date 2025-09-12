# PublicationsPostPublicationDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** |  | [optional] 
**image_id_list** | **List[str]** |  | [optional] 
**video_id_list** | **List[str]** |  | [optional] 
**group_id** | **str** |  | [optional] 
**is_challenge_publication** | **bool** |  | [optional] 

## Example

```python
from wizipet_api.models.publications_post_publication_dto import PublicationsPostPublicationDto

# TODO update the JSON string below
json = "{}"
# create an instance of PublicationsPostPublicationDto from a JSON string
publications_post_publication_dto_instance = PublicationsPostPublicationDto.from_json(json)
# print the JSON string representation of the object
print(PublicationsPostPublicationDto.to_json())

# convert the object into a dict
publications_post_publication_dto_dict = publications_post_publication_dto_instance.to_dict()
# create an instance of PublicationsPostPublicationDto from a dict
publications_post_publication_dto_from_dict = PublicationsPostPublicationDto.from_dict(publications_post_publication_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


