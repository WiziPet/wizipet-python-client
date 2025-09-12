# WpResponseAuthMeDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AuthMeDto**](AuthMeDto.md) |  | [optional] 
**is_success** | **bool** |  | [optional] 
**error_code** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.wp_response_auth_me_dto import WpResponseAuthMeDto

# TODO update the JSON string below
json = "{}"
# create an instance of WpResponseAuthMeDto from a JSON string
wp_response_auth_me_dto_instance = WpResponseAuthMeDto.from_json(json)
# print the JSON string representation of the object
print(WpResponseAuthMeDto.to_json())

# convert the object into a dict
wp_response_auth_me_dto_dict = wp_response_auth_me_dto_instance.to_dict()
# create an instance of WpResponseAuthMeDto from a dict
wp_response_auth_me_dto_from_dict = WpResponseAuthMeDto.from_dict(wp_response_auth_me_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


