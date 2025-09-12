# WpResponseCreateReplyDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CreateReplyDto**](CreateReplyDto.md) |  | [optional] 
**is_success** | **bool** |  | [optional] 
**error_code** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.wp_response_create_reply_dto import WpResponseCreateReplyDto

# TODO update the JSON string below
json = "{}"
# create an instance of WpResponseCreateReplyDto from a JSON string
wp_response_create_reply_dto_instance = WpResponseCreateReplyDto.from_json(json)
# print the JSON string representation of the object
print(WpResponseCreateReplyDto.to_json())

# convert the object into a dict
wp_response_create_reply_dto_dict = wp_response_create_reply_dto_instance.to_dict()
# create an instance of WpResponseCreateReplyDto from a dict
wp_response_create_reply_dto_from_dict = WpResponseCreateReplyDto.from_dict(wp_response_create_reply_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


