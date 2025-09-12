# NotificationsRegisterForNotificationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | [optional] 
**system** | [**NotificationsNotificationSystem**](NotificationsNotificationSystem.md) |  | [optional] 

## Example

```python
from wizipet_api.models.notifications_register_for_notification_request import NotificationsRegisterForNotificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationsRegisterForNotificationRequest from a JSON string
notifications_register_for_notification_request_instance = NotificationsRegisterForNotificationRequest.from_json(json)
# print the JSON string representation of the object
print(NotificationsRegisterForNotificationRequest.to_json())

# convert the object into a dict
notifications_register_for_notification_request_dict = notifications_register_for_notification_request_instance.to_dict()
# create an instance of NotificationsRegisterForNotificationRequest from a dict
notifications_register_for_notification_request_from_dict = NotificationsRegisterForNotificationRequest.from_dict(notifications_register_for_notification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


