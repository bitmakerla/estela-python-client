# estela_client.DeploysApi

All URIs are relative to *http://127.0.0.1:8000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_projects_deploys_create**](DeploysApi.md#api_projects_deploys_create) | **POST** /api/projects/{pid}/deploys | 
[**api_projects_deploys_delete**](DeploysApi.md#api_projects_deploys_delete) | **DELETE** /api/projects/{pid}/deploys/{did} | 
[**api_projects_deploys_list**](DeploysApi.md#api_projects_deploys_list) | **GET** /api/projects/{pid}/deploys | 
[**api_projects_deploys_partial_update**](DeploysApi.md#api_projects_deploys_partial_update) | **PATCH** /api/projects/{pid}/deploys/{did} | 
[**api_projects_deploys_read**](DeploysApi.md#api_projects_deploys_read) | **GET** /api/projects/{pid}/deploys/{did} | 
[**api_projects_deploys_update**](DeploysApi.md#api_projects_deploys_update) | **PUT** /api/projects/{pid}/deploys/{did} | 


# **api_projects_deploys_create**
> DeployCreate api_projects_deploys_create(pid, data)



### Example

* Basic Authentication (Basic):

```python
import time
import estela_client
from estela_client.api import deploys_api
from estela_client.model.deploy_create import DeployCreate
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
    api_instance = deploys_api.DeploysApi(api_client)
    pid = "pid_example" # str | 
    data = DeployCreate(
        status="SUCCESS",
    ) # DeployCreate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_projects_deploys_create(pid, data)
        pprint(api_response)
    except estela_client.ApiException as e:
        print("Exception when calling DeploysApi->api_projects_deploys_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid** | **str**|  |
 **data** | [**DeployCreate**](DeployCreate.md)|  |

### Return type

[**DeployCreate**](DeployCreate.md)

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

# **api_projects_deploys_delete**
> api_projects_deploys_delete(did, pid)



### Example

* Basic Authentication (Basic):

```python
import time
import estela_client
from estela_client.api import deploys_api
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
    api_instance = deploys_api.DeploysApi(api_client)
    did = 1 # int | A unique integer value identifying this deploy.
    pid = "pid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_projects_deploys_delete(did, pid)
    except estela_client.ApiException as e:
        print("Exception when calling DeploysApi->api_projects_deploys_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **int**| A unique integer value identifying this deploy. |
 **pid** | **str**|  |

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
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_projects_deploys_list**
> InlineResponse2002 api_projects_deploys_list(pid)



### Example

* Basic Authentication (Basic):

```python
import time
import estela_client
from estela_client.api import deploys_api
from estela_client.model.inline_response2002 import InlineResponse2002
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
    api_instance = deploys_api.DeploysApi(api_client)
    pid = "pid_example" # str | 
    page = 1 # int | A page number within the paginated result set. (optional)
    page_size = 1 # int | Number of results to return per page. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_projects_deploys_list(pid)
        pprint(api_response)
    except estela_client.ApiException as e:
        print("Exception when calling DeploysApi->api_projects_deploys_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_projects_deploys_list(pid, page=page, page_size=page_size)
        pprint(api_response)
    except estela_client.ApiException as e:
        print("Exception when calling DeploysApi->api_projects_deploys_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid** | **str**|  |
 **page** | **int**| A page number within the paginated result set. | [optional]
 **page_size** | **int**| Number of results to return per page. | [optional]

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

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

# **api_projects_deploys_partial_update**
> Deploy api_projects_deploys_partial_update(did, pid, data)



### Example

* Basic Authentication (Basic):

```python
import time
import estela_client
from estela_client.api import deploys_api
from estela_client.model.deploy import Deploy
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
    api_instance = deploys_api.DeploysApi(api_client)
    did = 1 # int | A unique integer value identifying this deploy.
    pid = "pid_example" # str | 
    data = Deploy(
        project="project_example",
        user=UserDetail(
            username="A",
            email="email_example",
        ),
        status="SUCCESS",
        spiders=[
            Spider(
                name="name_example",
                project="project_example",
                data_status="PERSISTENT",
                data_expiry_days=0,
            ),
        ],
    ) # Deploy | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_projects_deploys_partial_update(did, pid, data)
        pprint(api_response)
    except estela_client.ApiException as e:
        print("Exception when calling DeploysApi->api_projects_deploys_partial_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **int**| A unique integer value identifying this deploy. |
 **pid** | **str**|  |
 **data** | [**Deploy**](Deploy.md)|  |

### Return type

[**Deploy**](Deploy.md)

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

# **api_projects_deploys_read**
> Deploy api_projects_deploys_read(did, pid)



### Example

* Basic Authentication (Basic):

```python
import time
import estela_client
from estela_client.api import deploys_api
from estela_client.model.deploy import Deploy
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
    api_instance = deploys_api.DeploysApi(api_client)
    did = 1 # int | A unique integer value identifying this deploy.
    pid = "pid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_projects_deploys_read(did, pid)
        pprint(api_response)
    except estela_client.ApiException as e:
        print("Exception when calling DeploysApi->api_projects_deploys_read: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **int**| A unique integer value identifying this deploy. |
 **pid** | **str**|  |

### Return type

[**Deploy**](Deploy.md)

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

# **api_projects_deploys_update**
> DeployUpdate api_projects_deploys_update(did, pid, data)



### Example

* Basic Authentication (Basic):

```python
import time
import estela_client
from estela_client.api import deploys_api
from estela_client.model.deploy_update import DeployUpdate
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
    api_instance = deploys_api.DeploysApi(api_client)
    did = 1 # int | A unique integer value identifying this deploy.
    pid = "pid_example" # str | 
    data = DeployUpdate(
        status="SUCCESS",
        spiders_names=[
            "spiders_names_example",
        ],
    ) # DeployUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_projects_deploys_update(did, pid, data)
        pprint(api_response)
    except estela_client.ApiException as e:
        print("Exception when calling DeploysApi->api_projects_deploys_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **int**| A unique integer value identifying this deploy. |
 **pid** | **str**|  |
 **data** | [**DeployUpdate**](DeployUpdate.md)|  |

### Return type

[**DeployUpdate**](DeployUpdate.md)

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

