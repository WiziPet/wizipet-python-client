# WpResponseCartesPositionDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CartesPositionDto**](CartesPositionDto.md) |  | [optional] 
**is_success** | **bool** |  | [optional] 
**error_code** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.wp_response_cartes_position_dto import WpResponseCartesPositionDto

# TODO update the JSON string below
json = "{}"
# create an instance of WpResponseCartesPositionDto from a JSON string
wp_response_cartes_position_dto_instance = WpResponseCartesPositionDto.from_json(json)
# print the JSON string representation of the object
print(WpResponseCartesPositionDto.to_json())

# convert the object into a dict
wp_response_cartes_position_dto_dict = wp_response_cartes_position_dto_instance.to_dict()
# create an instance of WpResponseCartesPositionDto from a dict
wp_response_cartes_position_dto_from_dict = WpResponseCartesPositionDto.from_dict(wp_response_cartes_position_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


