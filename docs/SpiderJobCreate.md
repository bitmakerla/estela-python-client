# SpiderJobCreate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_status** | **str** | Data status. | 
**jid** | **int** | A unique integer value identifying this job. | [optional] [readonly] 
**name** | **str** | Unique job name. | [optional] [readonly] 
**args** | [**[SpiderJobArg]**](SpiderJobArg.md) | Job arguments. | [optional] 
**env_vars** | [**[SpiderJobEnvVar]**](SpiderJobEnvVar.md) | Job env variables. | [optional] 
**tags** | [**[SpiderJobTag]**](SpiderJobTag.md) | Job tags. | [optional] 
**job_status** | **str** | Current job status. | [optional] [readonly] 
**cronjob** | **int, none_type** | Related cron job. | [optional] 
**data_expiry_days** | **int** | Days before data expires. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


