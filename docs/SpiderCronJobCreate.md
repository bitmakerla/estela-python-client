# SpiderCronJobCreate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_status** | **str** | Data status. | 
**cjid** | **int** | A unique integer value identifying this cron job. | [optional] [readonly] 
**name** | **str** | Unique cron job name. | [optional] [readonly] 
**cargs** | [**[SpiderJobArg]**](SpiderJobArg.md) | Cron job arguments. | [optional] 
**cenv_vars** | [**[SpiderJobEnvVar]**](SpiderJobEnvVar.md) | Cron job env variables. | [optional] 
**ctags** | [**[SpiderJobTag]**](SpiderJobTag.md) | Cron job tags. | [optional] 
**schedule** | **str** | Cron job schedule definition. | [optional] 
**unique_collection** | **bool** | True if this cron job stores its items in a unique collection. | [optional] 
**data_expiry_days** | **str** | Days before data expires. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


