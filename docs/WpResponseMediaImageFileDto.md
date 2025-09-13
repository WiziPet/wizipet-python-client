# WpResponseMediaImageFileDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**MediaImageFileDto**](MediaImageFileDto.md) |  | [optional] 
**is_success** | **bool** |  | [optional] 
**error_code** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.wp_response_media_image_file_dto import WpResponseMediaImageFileDto

# TODO update the JSON string below
json = "{}"
# create an instance of WpResponseMediaImageFileDto from a JSON string
wp_response_media_image_file_dto_instance = WpResponseMediaImageFileDto.from_json(json)
# print the JSON string representation of the object
print(WpResponseMediaImageFileDto.to_json())

# convert the object into a dict
wp_response_media_image_file_dto_dict = wp_response_media_image_file_dto_instance.to_dict()
# create an instance of WpResponseMediaImageFileDto from a dict
wp_response_media_image_file_dto_from_dict = WpResponseMediaImageFileDto.from_dict(wp_response_media_image_file_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


