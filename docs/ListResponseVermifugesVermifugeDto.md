# ListResponseVermifugesVermifugeDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[VermifugesVermifugeDto]**](VermifugesVermifugeDto.md) |  | [optional] 
**is_success** | **bool** |  | [optional] 
**error_code** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.list_response_vermifuges_vermifuge_dto import ListResponseVermifugesVermifugeDto

# TODO update the JSON string below
json = "{}"
# create an instance of ListResponseVermifugesVermifugeDto from a JSON string
list_response_vermifuges_vermifuge_dto_instance = ListResponseVermifugesVermifugeDto.from_json(json)
# print the JSON string representation of the object
print(ListResponseVermifugesVermifugeDto.to_json())

# convert the object into a dict
list_response_vermifuges_vermifuge_dto_dict = list_response_vermifuges_vermifuge_dto_instance.to_dict()
# create an instance of ListResponseVermifugesVermifugeDto from a dict
list_response_vermifuges_vermifuge_dto_from_dict = ListResponseVermifugesVermifugeDto.from_dict(list_response_vermifuges_vermifuge_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


