# MediasVideoDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**dash_url** | **str** |  | [optional] 
**hls_url** | **str** |  | [optional] 
**thumbnail_url** | **str** |  | [optional] 
**status** | [**MediasVideoTranscodingStatusDto**](MediasVideoTranscodingStatusDto.md) |  | [optional] 

## Example

```python
from wizipet_api.models.medias_video_dto import MediasVideoDto

# TODO update the JSON string below
json = "{}"
# create an instance of MediasVideoDto from a JSON string
medias_video_dto_instance = MediasVideoDto.from_json(json)
# print the JSON string representation of the object
print(MediasVideoDto.to_json())

# convert the object into a dict
medias_video_dto_dict = medias_video_dto_instance.to_dict()
# create an instance of MediasVideoDto from a dict
medias_video_dto_from_dict = MediasVideoDto.from_dict(medias_video_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


