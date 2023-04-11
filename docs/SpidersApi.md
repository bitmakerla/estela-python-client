# estela_client.SpidersApi

All URIs are relative to *http://127.0.0.1:8000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_projects_spiders_list**](SpidersApi.md#api_projects_spiders_list) | **GET** /api/projects/{pid}/spiders | 
[**api_projects_spiders_partial_update**](SpidersApi.md#api_projects_spiders_partial_update) | **PATCH** /api/projects/{pid}/spiders/{sid} | 
[**api_projects_spiders_read**](SpidersApi.md#api_projects_spiders_read) | **GET** /api/projects/{pid}/spiders/{sid} | 
[**api_projects_spiders_update**](SpidersApi.md#api_projects_spiders_update) | **PUT** /api/projects/{pid}/spiders/{sid} | 


# **api_projects_spiders_list**
> InlineResponse2003 api_projects_spiders_list(pid)



### Example

* Basic Authentication (Basic):

```python
import time
import estela_client
from estela_client.api import spiders_api
from estela_client.model.inline_response2003 import InlineResponse2003
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
    api_instance = spiders_api.SpidersApi(api_client)
    pid = "pid_example" # str | 
    page = 1 # int | A page number within the paginated result set. (optional)
    page_size = 1 # int | Number of results to return per page. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_projects_spiders_list(pid)
        pprint(api_response)
    except estela_client.ApiException as e:
        print("Exception when calling SpidersApi->api_projects_spiders_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_projects_spiders_list(pid, page=page, page_size=page_size)
        pprint(api_response)
    except estela_client.ApiException as e:
        print("Exception when calling SpidersApi->api_projects_spiders_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid** | **str**|  |
 **page** | **int**| A page number within the paginated result set. | [optional]
 **page_size** | **int**| Number of results to return per page. | [optional]

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

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

# **api_projects_spiders_partial_update**
> Spider api_projects_spiders_partial_update(pid, sid, data)



### Example

* Basic Authentication (Basic):

```python
import time
import estela_client
from estela_client.api import spiders_api
from estela_client.model.spider import Spider
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
    api_instance = spiders_api.SpidersApi(api_client)
    pid = "pid_example" # str | 
    sid = 1 # int | A unique integer value identifying this spider.
    data = Spider(
        name="name_example",
        project="project_example",
        data_status="PERSISTENT",
        data_expiry_days=0,
    ) # Spider | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_projects_spiders_partial_update(pid, sid, data)
        pprint(api_response)
    except estela_client.ApiException as e:
        print("Exception when calling SpidersApi->api_projects_spiders_partial_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid** | **str**|  |
 **sid** | **int**| A unique integer value identifying this spider. |
 **data** | [**Spider**](Spider.md)|  |

### Return type

[**Spider**](Spider.md)

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

# **api_projects_spiders_read**
> Spider api_projects_spiders_read(pid, sid)



### Example

* Basic Authentication (Basic):

```python
import time
import estela_client
from estela_client.api import spiders_api
from estela_client.model.spider import Spider
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
    api_instance = spiders_api.SpidersApi(api_client)
    pid = "pid_example" # str | 
    sid = 1 # int | A unique integer value identifying this spider.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_projects_spiders_read(pid, sid)
        pprint(api_response)
    except estela_client.ApiException as e:
        print("Exception when calling SpidersApi->api_projects_spiders_read: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid** | **str**|  |
 **sid** | **int**| A unique integer value identifying this spider. |

### Return type

[**Spider**](Spider.md)

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

# **api_projects_spiders_update**
> SpiderUpdate api_projects_spiders_update(pid, sid, data)



### Example

* Basic Authentication (Basic):

```python
import time
import estela_client
from estela_client.api import spiders_api
from estela_client.model.spider_update import SpiderUpdate
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
    api_instance = spiders_api.SpidersApi(api_client)
    pid = "pid_example" # str | 
    sid = 1 # int | A unique integer value identifying this spider.
    data = SpiderUpdate(
        name="name_example",
        data_status="PERSISTENT",
        data_expiry_days=1,
    ) # SpiderUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_projects_spiders_update(pid, sid, data)
        pprint(api_response)
    except estela_client.ApiException as e:
        print("Exception when calling SpidersApi->api_projects_spiders_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid** | **str**|  |
 **sid** | **int**| A unique integer value identifying this spider. |
 **data** | [**SpiderUpdate**](SpiderUpdate.md)|  |

### Return type

[**SpiderUpdate**](SpiderUpdate.md)

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

