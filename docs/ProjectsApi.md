# estela_client.ProjectsApi

All URIs are relative to *http://127.0.0.1:8000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_projects_create**](ProjectsApi.md#api_projects_create) | **POST** /api/projects | 
[**api_projects_cronjobs**](ProjectsApi.md#api_projects_cronjobs) | **GET** /api/projects/{pid}/cronjobs | 
[**api_projects_current_usage**](ProjectsApi.md#api_projects_current_usage) | **GET** /api/projects/{pid}/current_usage | 
[**api_projects_delete**](ProjectsApi.md#api_projects_delete) | **DELETE** /api/projects/{pid} | 
[**api_projects_jobs**](ProjectsApi.md#api_projects_jobs) | **GET** /api/projects/{pid}/jobs | 
[**api_projects_list**](ProjectsApi.md#api_projects_list) | **GET** /api/projects | 
[**api_projects_partial_update**](ProjectsApi.md#api_projects_partial_update) | **PATCH** /api/projects/{pid} | 
[**api_projects_read**](ProjectsApi.md#api_projects_read) | **GET** /api/projects/{pid} | 
[**api_projects_update**](ProjectsApi.md#api_projects_update) | **PUT** /api/projects/{pid} | 
[**api_projects_usage**](ProjectsApi.md#api_projects_usage) | **GET** /api/projects/{pid}/usage | 


# **api_projects_create**
> Project api_projects_create(data)



### Example

* Basic Authentication (Basic):

```python
import time
import estela_client
from estela_client.api import projects_api
from estela_client.model.project import Project
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
    api_instance = projects_api.ProjectsApi(api_client)
    data = Project(
        name="name_example",
        category="NOT ESPECIFIED",
        users=[
            Permission(
                user=UserDetail(
                    username="A",
                    email="email_example",
                ),
                permission="OWNER",
            ),
        ],
        data_status="PERSISTENT",
        data_expiry_days=0,
    ) # Project | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_projects_create(data)
        pprint(api_response)
    except estela_client.ApiException as e:
        print("Exception when calling ProjectsApi->api_projects_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Project**](Project.md)|  |

### Return type

[**Project**](Project.md)

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

# **api_projects_cronjobs**
> ProjectCronJob api_projects_cronjobs(pid)



### Example

* Basic Authentication (Basic):

```python
import time
import estela_client
from estela_client.api import projects_api
from estela_client.model.project_cron_job import ProjectCronJob
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
    api_instance = projects_api.ProjectsApi(api_client)
    pid = "pid_example" # str | A UUID identifying this project.
    page = 3.14 # float | A page number within the paginated result set. (optional)
    page_size = 3.14 # float | Number of results to return per page. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_projects_cronjobs(pid)
        pprint(api_response)
    except estela_client.ApiException as e:
        print("Exception when calling ProjectsApi->api_projects_cronjobs: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_projects_cronjobs(pid, page=page, page_size=page_size)
        pprint(api_response)
    except estela_client.ApiException as e:
        print("Exception when calling ProjectsApi->api_projects_cronjobs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid** | **str**| A UUID identifying this project. |
 **page** | **float**| A page number within the paginated result set. | [optional]
 **page_size** | **float**| Number of results to return per page. | [optional]

### Return type

[**ProjectCronJob**](ProjectCronJob.md)

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

# **api_projects_current_usage**
> ProjectUsage api_projects_current_usage(pid)



### Example

* Basic Authentication (Basic):

```python
import time
import estela_client
from estela_client.api import projects_api
from estela_client.model.project_usage import ProjectUsage
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
    api_instance = projects_api.ProjectsApi(api_client)
    pid = "pid_example" # str | A UUID identifying this project.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_projects_current_usage(pid)
        pprint(api_response)
    except estela_client.ApiException as e:
        print("Exception when calling ProjectsApi->api_projects_current_usage: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid** | **str**| A UUID identifying this project. |

### Return type

[**ProjectUsage**](ProjectUsage.md)

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

# **api_projects_delete**
> api_projects_delete(pid)



### Example

* Basic Authentication (Basic):

```python
import time
import estela_client
from estela_client.api import projects_api
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
    api_instance = projects_api.ProjectsApi(api_client)
    pid = "pid_example" # str | A UUID identifying this project.

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_projects_delete(pid)
    except estela_client.ApiException as e:
        print("Exception when calling ProjectsApi->api_projects_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid** | **str**| A UUID identifying this project. |

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
**204** | Project deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_projects_jobs**
> ProjectJob api_projects_jobs(pid)



### Example

* Basic Authentication (Basic):

```python
import time
import estela_client
from estela_client.api import projects_api
from estela_client.model.project_job import ProjectJob
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
    api_instance = projects_api.ProjectsApi(api_client)
    pid = "pid_example" # str | A UUID identifying this project.
    page = 3.14 # float | A page number within the paginated result set. (optional)
    page_size = 3.14 # float | Number of results to return per page. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_projects_jobs(pid)
        pprint(api_response)
    except estela_client.ApiException as e:
        print("Exception when calling ProjectsApi->api_projects_jobs: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_projects_jobs(pid, page=page, page_size=page_size)
        pprint(api_response)
    except estela_client.ApiException as e:
        print("Exception when calling ProjectsApi->api_projects_jobs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid** | **str**| A UUID identifying this project. |
 **page** | **float**| A page number within the paginated result set. | [optional]
 **page_size** | **float**| Number of results to return per page. | [optional]

### Return type

[**ProjectJob**](ProjectJob.md)

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

# **api_projects_list**
> InlineResponse2001 api_projects_list()



### Example

* Basic Authentication (Basic):

```python
import time
import estela_client
from estela_client.api import projects_api
from estela_client.model.inline_response2001 import InlineResponse2001
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
    api_instance = projects_api.ProjectsApi(api_client)
    page = 1 # int | A page number within the paginated result set. (optional)
    page_size = 1 # int | Number of results to return per page. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_projects_list(page=page, page_size=page_size)
        pprint(api_response)
    except estela_client.ApiException as e:
        print("Exception when calling ProjectsApi->api_projects_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional]
 **page_size** | **int**| Number of results to return per page. | [optional]

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

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

# **api_projects_partial_update**
> Project api_projects_partial_update(pid, data)



### Example

* Basic Authentication (Basic):

```python
import time
import estela_client
from estela_client.api import projects_api
from estela_client.model.project import Project
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
    api_instance = projects_api.ProjectsApi(api_client)
    pid = "pid_example" # str | A UUID identifying this project.
    data = Project(
        name="name_example",
        category="NOT ESPECIFIED",
        users=[
            Permission(
                user=UserDetail(
                    username="A",
                    email="email_example",
                ),
                permission="OWNER",
            ),
        ],
        data_status="PERSISTENT",
        data_expiry_days=0,
    ) # Project | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_projects_partial_update(pid, data)
        pprint(api_response)
    except estela_client.ApiException as e:
        print("Exception when calling ProjectsApi->api_projects_partial_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid** | **str**| A UUID identifying this project. |
 **data** | [**Project**](Project.md)|  |

### Return type

[**Project**](Project.md)

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

# **api_projects_read**
> Project api_projects_read(pid)



### Example

* Basic Authentication (Basic):

```python
import time
import estela_client
from estela_client.api import projects_api
from estela_client.model.project import Project
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
    api_instance = projects_api.ProjectsApi(api_client)
    pid = "pid_example" # str | A UUID identifying this project.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_projects_read(pid)
        pprint(api_response)
    except estela_client.ApiException as e:
        print("Exception when calling ProjectsApi->api_projects_read: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid** | **str**| A UUID identifying this project. |

### Return type

[**Project**](Project.md)

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

# **api_projects_update**
> ProjectUpdate api_projects_update(pid, data)



### Example

* Basic Authentication (Basic):

```python
import time
import estela_client
from estela_client.api import projects_api
from estela_client.model.project_update import ProjectUpdate
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
    api_instance = projects_api.ProjectsApi(api_client)
    pid = "pid_example" # str | A UUID identifying this project.
    data = ProjectUpdate(
        name="name_example",
        users=[
            UserDetail(
                username="A",
                email="email_example",
            ),
        ],
        email="email_example",
        action="remove",
        permission="ADMIN",
        data_status="PERSISTENT",
        data_expiry_days=1,
    ) # ProjectUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_projects_update(pid, data)
        pprint(api_response)
    except estela_client.ApiException as e:
        print("Exception when calling ProjectsApi->api_projects_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid** | **str**| A UUID identifying this project. |
 **data** | [**ProjectUpdate**](ProjectUpdate.md)|  |

### Return type

[**ProjectUpdate**](ProjectUpdate.md)

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

# **api_projects_usage**
> [UsageRecord] api_projects_usage(pid)



### Example

* Basic Authentication (Basic):

```python
import time
import estela_client
from estela_client.api import projects_api
from estela_client.model.usage_record import UsageRecord
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
    api_instance = projects_api.ProjectsApi(api_client)
    pid = "pid_example" # str | A UUID identifying this project.
    start_date = "start_date_example" # str | Start of date range. (optional)
    end_date = "end_date_example" # str | End of date range. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_projects_usage(pid)
        pprint(api_response)
    except estela_client.ApiException as e:
        print("Exception when calling ProjectsApi->api_projects_usage: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_projects_usage(pid, start_date=start_date, end_date=end_date)
        pprint(api_response)
    except estela_client.ApiException as e:
        print("Exception when calling ProjectsApi->api_projects_usage: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid** | **str**| A UUID identifying this project. |
 **start_date** | **str**| Start of date range. | [optional]
 **end_date** | **str**| End of date range. | [optional]

### Return type

[**[UsageRecord]**](UsageRecord.md)

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

