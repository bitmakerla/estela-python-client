# SpiderJob

Project jobs.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spider** | **int** | Spider sid. | 
**jid** | **int** | A unique integer value identifying this job. | [optional] [readonly] 
**created** | **datetime** | Job creation date. | [optional] [readonly] 
**name** | **str** | Unique job name. | [optional] [readonly] 
**lifespan** | **float** | The elapsed seconds the spider job was running. | [optional] 
**total_response_bytes** | **int** | The total bytes received in responses. | [optional] 
**item_count** | **int** | The number of items extracted in the job. | [optional] 
**request_count** | **int** | The number of requests made by the spider job. | [optional] 
**args** | [**[SpiderJobArg]**](SpiderJobArg.md) | Job arguments. | [optional] 
**env_vars** | [**[SpiderJobEnvVar]**](SpiderJobEnvVar.md) | Job env variables. | [optional] 
**tags** | [**[SpiderJobTag]**](SpiderJobTag.md) | Job tags. | [optional] 
**job_status** | **str** | Current job status. | [optional] [readonly] 
**cronjob** | **int, none_type** | Related cron job. | [optional] 
**data_expiry_days** | **int, none_type** | Days before data is deleted. | [optional] 
**data_status** | **str** | Data status. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


