# NotificationsUnregisterForNotificationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**registration_id** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.notifications_unregister_for_notification_request import NotificationsUnregisterForNotificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationsUnregisterForNotificationRequest from a JSON string
notifications_unregister_for_notification_request_instance = NotificationsUnregisterForNotificationRequest.from_json(json)
# print the JSON string representation of the object
print(NotificationsUnregisterForNotificationRequest.to_json())

# convert the object into a dict
notifications_unregister_for_notification_request_dict = notifications_unregister_for_notification_request_instance.to_dict()
# create an instance of NotificationsUnregisterForNotificationRequest from a dict
notifications_unregister_for_notification_request_from_dict = NotificationsUnregisterForNotificationRequest.from_dict(notifications_unregister_for_notification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


