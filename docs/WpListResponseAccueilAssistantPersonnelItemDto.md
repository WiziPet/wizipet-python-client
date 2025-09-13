# WpListResponseAccueilAssistantPersonnelItemDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AccueilAssistantPersonnelItemDto]**](AccueilAssistantPersonnelItemDto.md) |  | [optional] 
**is_success** | **bool** |  | [optional] 
**error_code** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.wp_list_response_accueil_assistant_personnel_item_dto import WpListResponseAccueilAssistantPersonnelItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of WpListResponseAccueilAssistantPersonnelItemDto from a JSON string
wp_list_response_accueil_assistant_personnel_item_dto_instance = WpListResponseAccueilAssistantPersonnelItemDto.from_json(json)
# print the JSON string representation of the object
print(WpListResponseAccueilAssistantPersonnelItemDto.to_json())

# convert the object into a dict
wp_list_response_accueil_assistant_personnel_item_dto_dict = wp_list_response_accueil_assistant_personnel_item_dto_instance.to_dict()
# create an instance of WpListResponseAccueilAssistantPersonnelItemDto from a dict
wp_list_response_accueil_assistant_personnel_item_dto_from_dict = WpListResponseAccueilAssistantPersonnelItemDto.from_dict(wp_list_response_accueil_assistant_personnel_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


