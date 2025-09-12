# AdvertisementsAdItemDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**image_id** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.advertisements_ad_item_dto import AdvertisementsAdItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of AdvertisementsAdItemDto from a JSON string
advertisements_ad_item_dto_instance = AdvertisementsAdItemDto.from_json(json)
# print the JSON string representation of the object
print(AdvertisementsAdItemDto.to_json())

# convert the object into a dict
advertisements_ad_item_dto_dict = advertisements_ad_item_dto_instance.to_dict()
# create an instance of AdvertisementsAdItemDto from a dict
advertisements_ad_item_dto_from_dict = AdvertisementsAdItemDto.from_dict(advertisements_ad_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


