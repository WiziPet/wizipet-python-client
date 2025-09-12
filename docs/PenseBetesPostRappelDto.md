# PenseBetesPostRappelDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** |  | [optional] 
**commentaire** | **str** |  | [optional] 

## Example

```python
from wizipet_api.models.pense_betes_post_rappel_dto import PenseBetesPostRappelDto

# TODO update the JSON string below
json = "{}"
# create an instance of PenseBetesPostRappelDto from a JSON string
pense_betes_post_rappel_dto_instance = PenseBetesPostRappelDto.from_json(json)
# print the JSON string representation of the object
print(PenseBetesPostRappelDto.to_json())

# convert the object into a dict
pense_betes_post_rappel_dto_dict = pense_betes_post_rappel_dto_instance.to_dict()
# create an instance of PenseBetesPostRappelDto from a dict
pense_betes_post_rappel_dto_from_dict = PenseBetesPostRappelDto.from_dict(pense_betes_post_rappel_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


