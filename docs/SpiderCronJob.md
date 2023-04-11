# SpiderCronJob

Project Cronjobs.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spider** | **int** | Spider sid. | 
**cjid** | **int** | A unique integer value identifying this cron job. | [optional] [readonly] 
**created** | **datetime** | Cron job creation date. | [optional] [readonly] 
**name** | **str** | Unique cron job name. | [optional] [readonly] 
**cargs** | [**[SpiderJobArg]**](SpiderJobArg.md) | Cron job arguments. | [optional] 
**cenv_vars** | [**[SpiderJobEnvVar]**](SpiderJobEnvVar.md) | Cron job env variables. | [optional] 
**ctags** | [**[SpiderJobTag]**](SpiderJobTag.md) | Cron job tags. | [optional] 
**schedule** | **str** | Cron job schedule definition. | [optional] 
**status** | **str** | Cron job status. | [optional] 
**unique_collection** | **bool** | True if this cron job stores its items in a unique collection. | [optional] 
**data_status** | **str** | Data status. | [optional] 
**data_expiry_days** | **int, none_type** | Days before data is deleted. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


