# estela_client.SpiderJobsApi

All URIs are relative to *http://127.0.0.1:8000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_projects_spiders_jobs_create**](SpiderJobsApi.md#api_projects_spiders_jobs_create) | **POST** /api/projects/{pid}/spiders/{sid}/jobs | 
[**api_projects_spiders_jobs_data_delete**](SpiderJobsApi.md#api_projects_spiders_jobs_data_delete) | **POST** /api/projects/{pid}/spiders/{sid}/jobs/{jid}/data/delete | 
[**api_projects_spiders_jobs_data_list**](SpiderJobsApi.md#api_projects_spiders_jobs_data_list) | **GET** /api/projects/{pid}/spiders/{sid}/jobs/{jid}/data | 
[**api_projects_spiders_jobs_list**](SpiderJobsApi.md#api_projects_spiders_jobs_list) | **GET** /api/projects/{pid}/spiders/{sid}/jobs | 
[**api_projects_spiders_jobs_partial_update**](SpiderJobsApi.md#api_projects_spiders_jobs_partial_update) | **PATCH** /api/projects/{pid}/spiders/{sid}/jobs/{jid} | 
[**api_projects_spiders_jobs_read**](SpiderJobsApi.md#api_projects_spiders_jobs_read) | **GET** /api/projects/{pid}/spiders/{sid}/jobs/{jid} | 
[**api_projects_spiders_jobs_update**](SpiderJobsApi.md#api_projects_spiders_jobs_update) | **PUT** /api/projects/{pid}/spiders/{sid}/jobs/{jid} | 


# **api_projects_spiders_jobs_create**
> SpiderJobCreate api_projects_spiders_jobs_create(pid, sid, data)



### Example

* Basic Authentication (Basic):

```python
import time
import estela_client
from estela_client.api import spider_jobs_api
from estela_client.model.spider_job_create import SpiderJobCreate
from pprint import pprint
# Defining the host is optional and defaults to http://127.0.0.1:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = estela_client.Configuration(
    host = "http://127.0.0.1:8000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = estela_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with estela_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spider_jobs_api.SpiderJobsApi(api_client)
    pid = "pid_example" # str | 
    sid = "sid_example" # str | 
    data = SpiderJobCreate(
        args=[
            SpiderJobArg(
                name="name_example",
                value="value_example",
            ),
        ],
        env_vars=[
            SpiderJobEnvVar(
                name="name_example",
                value="value_example",
                masked=True,
            ),
        ],
        tags=[
            SpiderJobTag(
                name="name_example",
            ),
        ],
        cronjob=1,
        data_expiry_days=1,
        data_status="data_status_example",
    ) # SpiderJobCreate | 
    _async = True # bool | True if this job is async. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_projects_spiders_jobs_create(pid, sid, data)
        pprint(api_response)
    except estela_client.ApiException as e:
        print("Exception when calling SpiderJobsApi->api_projects_spiders_jobs_create: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_projects_spiders_jobs_create(pid, sid, data, _async=_async)
        pprint(api_response)
    except estela_client.ApiException as e:
        print("Exception when calling SpiderJobsApi->api_projects_spiders_jobs_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid** | **str**|  |
 **sid** | **str**|  |
 **data** | [**SpiderJobCreate**](SpiderJobCreate.md)|  |
 **_async** | **bool**| True if this job is async. | [optional]

### Return type

[**SpiderJobCreate**](SpiderJobCreate.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_projects_spiders_jobs_data_delete**
> DeleteJobData api_projects_spiders_jobs_data_delete(jid, pid, sid, type)



### Example

* Basic Authentication (Basic):

```python
import time
import estela_client
from estela_client.api import spider_jobs_api
from estela_client.model.delete_job_data import DeleteJobData
from pprint import pprint
# Defining the host is optional and defaults to http://127.0.0.1:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = estela_client.Configuration(
    host = "http://127.0.0.1:8000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = estela_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with estela_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spider_jobs_api.SpiderJobsApi(api_client)
    jid = "jid_example" # str | 
    pid = "pid_example" # str | 
    sid = "sid_example" # str | 
    type = "type_example" # str | Spider job data type.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_projects_spiders_jobs_data_delete(jid, pid, sid, type)
        pprint(api_response)
    except estela_client.ApiException as e:
        print("Exception when calling SpiderJobsApi->api_projects_spiders_jobs_data_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jid** | **str**|  |
 **pid** | **str**|  |
 **sid** | **str**|  |
 **type** | **str**| Spider job data type. |

### Return type

[**DeleteJobData**](DeleteJobData.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_projects_spiders_jobs_data_list**
> InlineResponse2006 api_projects_spiders_jobs_data_list(jid, pid, sid)



### Example

* Basic Authentication (Basic):

```python
import time
import estela_client
from estela_client.api import spider_jobs_api
from estela_client.model.inline_response2006 import InlineResponse2006
from pprint import pprint
# Defining the host is optional and defaults to http://127.0.0.1:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = estela_client.Configuration(
    host = "http://127.0.0.1:8000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = estela_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with estela_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spider_jobs_api.SpiderJobsApi(api_client)
    jid = "jid_example" # str | 
    pid = "pid_example" # str | 
    sid = "sid_example" # str | 
    page = 1 # int | A page number within the paginated result set. (optional)
    page_size = 1 # int | Number of results to return per page. (optional)
    type = "type_example" # str | Spider job data type. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_projects_spiders_jobs_data_list(jid, pid, sid)
        pprint(api_response)
    except estela_client.ApiException as e:
        print("Exception when calling SpiderJobsApi->api_projects_spiders_jobs_data_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_projects_spiders_jobs_data_list(jid, pid, sid, page=page, page_size=page_size, type=type)
        pprint(api_response)
    except estela_client.ApiException as e:
        print("Exception when calling SpiderJobsApi->api_projects_spiders_jobs_data_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jid** | **str**|  |
 **pid** | **str**|  |
 **sid** | **str**|  |
 **page** | **int**| A page number within the paginated result set. | [optional]
 **page_size** | **int**| Number of results to return per page. | [optional]
 **type** | **str**| Spider job data type. | [optional]

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_projects_spiders_jobs_list**
> InlineResponse2005 api_projects_spiders_jobs_list(pid, sid)



### Example

* Basic Authentication (Basic):

```python
import time
import estela_client
from estela_client.api import spider_jobs_api
from estela_client.model.inline_response2005 import InlineResponse2005
from pprint import pprint
# Defining the host is optional and defaults to http://127.0.0.1:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = estela_client.Configuration(
    host = "http://127.0.0.1:8000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = estela_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with estela_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spider_jobs_api.SpiderJobsApi(api_client)
    pid = "pid_example" # str | 
    sid = "sid_example" # str | 
    cronjob = 3.14 # float | Related cron job. (optional)
    status = "status_example" # str | Job status. (optional)
    tag = "tag_example" # str | Job tag. (optional)
    page = 1 # int | A page number within the paginated result set. (optional)
    page_size = 1 # int | Number of results to return per page. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_projects_spiders_jobs_list(pid, sid)
        pprint(api_response)
    except estela_client.ApiException as e:
        print("Exception when calling SpiderJobsApi->api_projects_spiders_jobs_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_projects_spiders_jobs_list(pid, sid, cronjob=cronjob, status=status, tag=tag, page=page, page_size=page_size)
        pprint(api_response)
    except estela_client.ApiException as e:
        print("Exception when calling SpiderJobsApi->api_projects_spiders_jobs_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid** | **str**|  |
 **sid** | **str**|  |
 **cronjob** | **float**| Related cron job. | [optional]
 **status** | **str**| Job status. | [optional]
 **tag** | **str**| Job tag. | [optional]
 **page** | **int**| A page number within the paginated result set. | [optional]
 **page_size** | **int**| Number of results to return per page. | [optional]

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_projects_spiders_jobs_partial_update**
> SpiderJob api_projects_spiders_jobs_partial_update(jid, pid, sid, data)



### Example

* Basic Authentication (Basic):

```python
import time
import estela_client
from estela_client.api import spider_jobs_api
from estela_client.model.spider_job import SpiderJob
from pprint import pprint
# Defining the host is optional and defaults to http://127.0.0.1:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = estela_client.Configuration(
    host = "http://127.0.0.1:8000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = estela_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with estela_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spider_jobs_api.SpiderJobsApi(api_client)
    jid = 1 # int | A unique integer value identifying this job.
    pid = "pid_example" # str | 
    sid = "sid_example" # str | 
    data = SpiderJob(
        spider=1,
        lifespan=3.14,
        total_response_bytes=0,
        item_count=0,
        request_count=0,
        args=[
            SpiderJobArg(
                name="name_example",
                value="value_example",
            ),
        ],
        env_vars=[
            SpiderJobEnvVar(
                name="name_example",
                value="value_example",
                masked=True,
            ),
        ],
        tags=[
            SpiderJobTag(
                name="name_example",
            ),
        ],
        cronjob=1,
        data_expiry_days=0,
        data_status="PERSISTENT",
    ) # SpiderJob | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_projects_spiders_jobs_partial_update(jid, pid, sid, data)
        pprint(api_response)
    except estela_client.ApiException as e:
        print("Exception when calling SpiderJobsApi->api_projects_spiders_jobs_partial_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jid** | **int**| A unique integer value identifying this job. |
 **pid** | **str**|  |
 **sid** | **str**|  |
 **data** | [**SpiderJob**](SpiderJob.md)|  |

### Return type

[**SpiderJob**](SpiderJob.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_projects_spiders_jobs_read**
> SpiderJob api_projects_spiders_jobs_read(jid, pid, sid)



### Example

* Basic Authentication (Basic):

```python
import time
import estela_client
from estela_client.api import spider_jobs_api
from estela_client.model.spider_job import SpiderJob
from pprint import pprint
# Defining the host is optional and defaults to http://127.0.0.1:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = estela_client.Configuration(
    host = "http://127.0.0.1:8000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = estela_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with estela_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spider_jobs_api.SpiderJobsApi(api_client)
    jid = 1 # int | A unique integer value identifying this job.
    pid = "pid_example" # str | 
    sid = "sid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_projects_spiders_jobs_read(jid, pid, sid)
        pprint(api_response)
    except estela_client.ApiException as e:
        print("Exception when calling SpiderJobsApi->api_projects_spiders_jobs_read: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jid** | **int**| A unique integer value identifying this job. |
 **pid** | **str**|  |
 **sid** | **str**|  |

### Return type

[**SpiderJob**](SpiderJob.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_projects_spiders_jobs_update**
> SpiderJobUpdate api_projects_spiders_jobs_update(jid, pid, sid, data)



### Example

* Basic Authentication (Basic):

```python
import time
import estela_client
from estela_client.api import spider_jobs_api
from estela_client.model.spider_job_update import SpiderJobUpdate
from pprint import pprint
# Defining the host is optional and defaults to http://127.0.0.1:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = estela_client.Configuration(
    host = "http://127.0.0.1:8000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = estela_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with estela_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spider_jobs_api.SpiderJobsApi(api_client)
    jid = 1 # int | A unique integer value identifying this job.
    pid = "pid_example" # str | 
    sid = "sid_example" # str | 
    data = SpiderJobUpdate(
        status="IN_QUEUE",
        lifespan=3.14,
        total_response_bytes=0,
        item_count=0,
        request_count=0,
        data_status="PERSISTENT",
        data_expiry_days=0,
    ) # SpiderJobUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_projects_spiders_jobs_update(jid, pid, sid, data)
        pprint(api_response)
    except estela_client.ApiException as e:
        print("Exception when calling SpiderJobsApi->api_projects_spiders_jobs_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jid** | **int**| A unique integer value identifying this job. |
 **pid** | **str**|  |
 **sid** | **str**|  |
 **data** | [**SpiderJobUpdate**](SpiderJobUpdate.md)|  |

### Return type

[**SpiderJobUpdate**](SpiderJobUpdate.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

