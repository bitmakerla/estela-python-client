# Project


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Project&#39;s name. | 
**pid** | **str** | A UUID identifying this project. | [optional] [readonly] 
**category** | **str** | Project&#39;s category. | [optional] 
**container_image** | **str** | Path of the project&#39;s container image. | [optional] [readonly] 
**users** | [**[Permission]**](Permission.md) | Users with permissions on this project. | [optional] 
**data_status** | **str** | Data status. | [optional] 
**data_expiry_days** | **int** | Days before data is deleted. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


