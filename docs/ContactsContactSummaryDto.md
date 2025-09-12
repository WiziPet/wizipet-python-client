# ContactsContactSummaryDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_status** | [**ContactsConnectionStatusDto**](ContactsConnectionStatusDto.md) |  | [optional] 
**id** | **str** |  | [optional] 
**pet_name** | **str** |  | [optional] 
**picture_id** | **str** |  | [optional] 
**race_id** | **str** |  | [optional] 
**ville** | **str** |  | [optional] 
**alerte_perte** | [**ProfilesAlertePerteDto**](ProfilesAlertePerteDto.md) |  | [optional] 

## Example

```python
from wizipet_api.models.contacts_contact_summary_dto import ContactsContactSummaryDto

# TODO update the JSON string below
json = "{}"
# create an instance of ContactsContactSummaryDto from a JSON string
contacts_contact_summary_dto_instance = ContactsContactSummaryDto.from_json(json)
# print the JSON string representation of the object
print(ContactsContactSummaryDto.to_json())

# convert the object into a dict
contacts_contact_summary_dto_dict = contacts_contact_summary_dto_instance.to_dict()
# create an instance of ContactsContactSummaryDto from a dict
contacts_contact_summary_dto_from_dict = ContactsContactSummaryDto.from_dict(contacts_contact_summary_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


