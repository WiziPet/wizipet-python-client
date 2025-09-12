# SantesMessagesInternesMessageInterneItemDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | [**SantesMessagesInternesMessageInterneTypeDto**](SantesMessagesInternesMessageInterneTypeDto.md) |  | [optional] 
**var_date** | **str** |  | [optional] 
**encyclopedie_article_id** | **str** |  | [optional] 
**alerte_perte_animal** | [**SantesMessagesInternesAlertePerteAnimalDto**](SantesMessagesInternesAlertePerteAnimalDto.md) |  | [optional] 

## Example

```python
from wizipet_api.models.santes_messages_internes_message_interne_item_dto import SantesMessagesInternesMessageInterneItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of SantesMessagesInternesMessageInterneItemDto from a JSON string
santes_messages_internes_message_interne_item_dto_instance = SantesMessagesInternesMessageInterneItemDto.from_json(json)
# print the JSON string representation of the object
print(SantesMessagesInternesMessageInterneItemDto.to_json())

# convert the object into a dict
santes_messages_internes_message_interne_item_dto_dict = santes_messages_internes_message_interne_item_dto_instance.to_dict()
# create an instance of SantesMessagesInternesMessageInterneItemDto from a dict
santes_messages_internes_message_interne_item_dto_from_dict = SantesMessagesInternesMessageInterneItemDto.from_dict(santes_messages_internes_message_interne_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


