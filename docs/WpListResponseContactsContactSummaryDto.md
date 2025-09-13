# WpListResponseContactsContactSummaryDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ContactsContactSummaryDto]**](ContactsContactSummaryDto.md) |  | [optional] 
**is_success** | **bool** |  | [optional] 
**error_code** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.wp_list_response_contacts_contact_summary_dto import WpListResponseContactsContactSummaryDto

# TODO update the JSON string below
json = "{}"
# create an instance of WpListResponseContactsContactSummaryDto from a JSON string
wp_list_response_contacts_contact_summary_dto_instance = WpListResponseContactsContactSummaryDto.from_json(json)
# print the JSON string representation of the object
print(WpListResponseContactsContactSummaryDto.to_json())

# convert the object into a dict
wp_list_response_contacts_contact_summary_dto_dict = wp_list_response_contacts_contact_summary_dto_instance.to_dict()
# create an instance of WpListResponseContactsContactSummaryDto from a dict
wp_list_response_contacts_contact_summary_dto_from_dict = WpListResponseContactsContactSummaryDto.from_dict(wp_list_response_contacts_contact_summary_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


