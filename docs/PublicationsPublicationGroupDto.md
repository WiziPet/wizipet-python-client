# PublicationsPublicationGroupDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**picture_id** | **str** |  | [optional] 
**ville** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.publications_publication_group_dto import PublicationsPublicationGroupDto

# TODO update the JSON string below
json = "{}"
# create an instance of PublicationsPublicationGroupDto from a JSON string
publications_publication_group_dto_instance = PublicationsPublicationGroupDto.from_json(json)
# print the JSON string representation of the object
print(PublicationsPublicationGroupDto.to_json())

# convert the object into a dict
publications_publication_group_dto_dict = publications_publication_group_dto_instance.to_dict()
# create an instance of PublicationsPublicationGroupDto from a dict
publications_publication_group_dto_from_dict = PublicationsPublicationGroupDto.from_dict(publications_publication_group_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


