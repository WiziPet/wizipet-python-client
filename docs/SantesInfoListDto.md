# SantesInfoListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info_list** | [**List[SantesInfoDto]**](SantesInfoDto.md) |  | [optional] 

## Example

```python
from wizipet_api.models.santes_info_list_dto import SantesInfoListDto

# TODO update the JSON string below
json = "{}"
# create an instance of SantesInfoListDto from a JSON string
santes_info_list_dto_instance = SantesInfoListDto.from_json(json)
# print the JSON string representation of the object
print(SantesInfoListDto.to_json())

# convert the object into a dict
santes_info_list_dto_dict = santes_info_list_dto_instance.to_dict()
# create an instance of SantesInfoListDto from a dict
santes_info_list_dto_from_dict = SantesInfoListDto.from_dict(santes_info_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


