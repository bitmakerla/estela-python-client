# estela_client.SpiderCronjobsApi

All URIs are relative to *http://127.0.0.1:8000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_projects_spiders_cronjobs_create**](SpiderCronjobsApi.md#api_projects_spiders_cronjobs_create) | **POST** /api/projects/{pid}/spiders/{sid}/cronjobs | 
[**api_projects_spiders_cronjobs_delete**](SpiderCronjobsApi.md#api_projects_spiders_cronjobs_delete) | **DELETE** /api/projects/{pid}/spiders/{sid}/cronjobs/{cjid} | 
[**api_projects_spiders_cronjobs_list**](SpiderCronjobsApi.md#api_projects_spiders_cronjobs_list) | **GET** /api/projects/{pid}/spiders/{sid}/cronjobs | 
[**api_projects_spiders_cronjobs_partial_update**](SpiderCronjobsApi.md#api_projects_spiders_cronjobs_partial_update) | **PATCH** /api/projects/{pid}/spiders/{sid}/cronjobs/{cjid} | 
[**api_projects_spiders_cronjobs_read**](SpiderCronjobsApi.md#api_projects_spiders_cronjobs_read) | **GET** /api/projects/{pid}/spiders/{sid}/cronjobs/{cjid} | 
[**api_projects_spiders_cronjobs_run_once**](SpiderCronjobsApi.md#api_projects_spiders_cronjobs_run_once) | **GET** /api/projects/{pid}/spiders/{sid}/cronjobs/{cjid}/run_once | 
[**api_projects_spiders_cronjobs_update**](SpiderCronjobsApi.md#api_projects_spiders_cronjobs_update) | **PUT** /api/projects/{pid}/spiders/{sid}/cronjobs/{cjid} | 


# **api_projects_spiders_cronjobs_create**
> SpiderCronJobCreate api_projects_spiders_cronjobs_create(pid, sid, data)



### Example

* Basic Authentication (Basic):

```python
import time
import estela_client
from estela_client.api import spider_cronjobs_api
from estela_client.model.spider_cron_job_create import SpiderCronJobCreate
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
    api_instance = spider_cronjobs_api.SpiderCronjobsApi(api_client)
    pid = "pid_example" # str | 
    sid = "sid_example" # str | 
    data = SpiderCronJobCreate(
        cargs=[
            SpiderJobArg(
                name="name_example",
                value="value_example",
            ),
        ],
        cenv_vars=[
            SpiderJobEnvVar(
                name="name_example",
                value="value_example",
                masked=True,
            ),
        ],
        ctags=[
            SpiderJobTag(
                name="name_example",
            ),
        ],
        schedule="schedule_example",
        unique_collection=True,
        data_expiry_days="data_expiry_days_example",
        data_status="data_status_example",
    ) # SpiderCronJobCreate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_projects_spiders_cronjobs_create(pid, sid, data)
        pprint(api_response)
    except estela_client.ApiException as e:
        print("Exception when calling SpiderCronjobsApi->api_projects_spiders_cronjobs_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid** | **str**|  |
 **sid** | **str**|  |
 **data** | [**SpiderCronJobCreate**](SpiderCronJobCreate.md)|  |

### Return type

[**SpiderCronJobCreate**](SpiderCronJobCreate.md)

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

# **api_projects_spiders_cronjobs_delete**
> api_projects_spiders_cronjobs_delete(cjid, pid, sid)



### Example

* Basic Authentication (Basic):

```python
import time
import estela_client
from estela_client.api import spider_cronjobs_api
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
    api_instance = spider_cronjobs_api.SpiderCronjobsApi(api_client)
    cjid = 1 # int | A unique integer value identifying this cron job.
    pid = "pid_example" # str | 
    sid = "sid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_projects_spiders_cronjobs_delete(cjid, pid, sid)
    except estela_client.ApiException as e:
        print("Exception when calling SpiderCronjobsApi->api_projects_spiders_cronjobs_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cjid** | **int**| A unique integer value identifying this cron job. |
 **pid** | **str**|  |
 **sid** | **str**|  |

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Cronjob deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_projects_spiders_cronjobs_list**
> InlineResponse2004 api_projects_spiders_cronjobs_list(pid, sid)



### Example

* Basic Authentication (Basic):

```python
import time
import estela_client
from estela_client.api import spider_cronjobs_api
from estela_client.model.inline_response2004 import InlineResponse2004
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
    api_instance = spider_cronjobs_api.SpiderCronjobsApi(api_client)
    pid = "pid_example" # str | 
    sid = "sid_example" # str | 
    tag = "tag_example" # str | Cron job tag. (optional)
    page = 1 # int | A page number within the paginated result set. (optional)
    page_size = 1 # int | Number of results to return per page. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_projects_spiders_cronjobs_list(pid, sid)
        pprint(api_response)
    except estela_client.ApiException as e:
        print("Exception when calling SpiderCronjobsApi->api_projects_spiders_cronjobs_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_projects_spiders_cronjobs_list(pid, sid, tag=tag, page=page, page_size=page_size)
        pprint(api_response)
    except estela_client.ApiException as e:
        print("Exception when calling SpiderCronjobsApi->api_projects_spiders_cronjobs_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid** | **str**|  |
 **sid** | **str**|  |
 **tag** | **str**| Cron job tag. | [optional]
 **page** | **int**| A page number within the paginated result set. | [optional]
 **page_size** | **int**| Number of results to return per page. | [optional]

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

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

# **api_projects_spiders_cronjobs_partial_update**
> SpiderCronJob api_projects_spiders_cronjobs_partial_update(cjid, pid, sid, data)



### Example

* Basic Authentication (Basic):

```python
import time
import estela_client
from estela_client.api import spider_cronjobs_api
from estela_client.model.spider_cron_job import SpiderCronJob
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
    api_instance = spider_cronjobs_api.SpiderCronjobsApi(api_client)
    cjid = 1 # int | A unique integer value identifying this cron job.
    pid = "pid_example" # str | 
    sid = "sid_example" # str | 
    data = SpiderCronJob(
        spider=1,
        cargs=[
            SpiderJobArg(
                name="name_example",
                value="value_example",
            ),
        ],
        cenv_vars=[
            SpiderJobEnvVar(
                name="name_example",
                value="value_example",
                masked=True,
            ),
        ],
        ctags=[
            SpiderJobTag(
                name="name_example",
            ),
        ],
        schedule="schedule_example",
        status="ACTIVE",
        unique_collection=True,
        data_status="PERSISTENT",
        data_expiry_days=0,
    ) # SpiderCronJob | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_projects_spiders_cronjobs_partial_update(cjid, pid, sid, data)
        pprint(api_response)
    except estela_client.ApiException as e:
        print("Exception when calling SpiderCronjobsApi->api_projects_spiders_cronjobs_partial_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cjid** | **int**| A unique integer value identifying this cron job. |
 **pid** | **str**|  |
 **sid** | **str**|  |
 **data** | [**SpiderCronJob**](SpiderCronJob.md)|  |

### Return type

[**SpiderCronJob**](SpiderCronJob.md)

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

# **api_projects_spiders_cronjobs_read**
> SpiderCronJob api_projects_spiders_cronjobs_read(cjid, pid, sid)



### Example

* Basic Authentication (Basic):

```python
import time
import estela_client
from estela_client.api import spider_cronjobs_api
from estela_client.model.spider_cron_job import SpiderCronJob
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
    api_instance = spider_cronjobs_api.SpiderCronjobsApi(api_client)
    cjid = 1 # int | A unique integer value identifying this cron job.
    pid = "pid_example" # str | 
    sid = "sid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_projects_spiders_cronjobs_read(cjid, pid, sid)
        pprint(api_response)
    except estela_client.ApiException as e:
        print("Exception when calling SpiderCronjobsApi->api_projects_spiders_cronjobs_read: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cjid** | **int**| A unique integer value identifying this cron job. |
 **pid** | **str**|  |
 **sid** | **str**|  |

### Return type

[**SpiderCronJob**](SpiderCronJob.md)

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

# **api_projects_spiders_cronjobs_run_once**
> SpiderCronJob api_projects_spiders_cronjobs_run_once(cjid, pid, sid)



### Example

* Basic Authentication (Basic):

```python
import time
import estela_client
from estela_client.api import spider_cronjobs_api
from estela_client.model.spider_cron_job import SpiderCronJob
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
    api_instance = spider_cronjobs_api.SpiderCronjobsApi(api_client)
    cjid = 1 # int | A unique integer value identifying this cron job.
    pid = "pid_example" # str | 
    sid = "sid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_projects_spiders_cronjobs_run_once(cjid, pid, sid)
        pprint(api_response)
    except estela_client.ApiException as e:
        print("Exception when calling SpiderCronjobsApi->api_projects_spiders_cronjobs_run_once: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cjid** | **int**| A unique integer value identifying this cron job. |
 **pid** | **str**|  |
 **sid** | **str**|  |

### Return type

[**SpiderCronJob**](SpiderCronJob.md)

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

# **api_projects_spiders_cronjobs_update**
> SpiderCronJobUpdate api_projects_spiders_cronjobs_update(cjid, pid, sid, data)



### Example

* Basic Authentication (Basic):

```python
import time
import estela_client
from estela_client.api import spider_cronjobs_api
from estela_client.model.spider_cron_job_update import SpiderCronJobUpdate
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
    api_instance = spider_cronjobs_api.SpiderCronjobsApi(api_client)
    cjid = 1 # int | A unique integer value identifying this cron job.
    pid = "pid_example" # str | 
    sid = "sid_example" # str | 
    data = SpiderCronJobUpdate(
        status="ACTIVE",
        schedule="schedule_example",
        unique_collection=True,
        data_status="PERSISTENT",
        data_expiry_days=0,
    ) # SpiderCronJobUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_projects_spiders_cronjobs_update(cjid, pid, sid, data)
        pprint(api_response)
    except estela_client.ApiException as e:
        print("Exception when calling SpiderCronjobsApi->api_projects_spiders_cronjobs_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cjid** | **int**| A unique integer value identifying this cron job. |
 **pid** | **str**|  |
 **sid** | **str**|  |
 **data** | [**SpiderCronJobUpdate**](SpiderCronJobUpdate.md)|  |

### Return type

[**SpiderCronJobUpdate**](SpiderCronJobUpdate.md)

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

