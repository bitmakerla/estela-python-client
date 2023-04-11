# estela_client.AuthApi

All URIs are relative to *http://127.0.0.1:8000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_account_change_password_change**](AuthApi.md#api_account_change_password_change) | **PATCH** /api/account/changePassword/change | 
[**api_account_reset_password_confirm**](AuthApi.md#api_account_reset_password_confirm) | **PATCH** /api/account/resetPassword/confirm | 
[**api_account_reset_password_request**](AuthApi.md#api_account_reset_password_request) | **POST** /api/account/resetPassword/request | 
[**api_account_reset_password_validate**](AuthApi.md#api_account_reset_password_validate) | **GET** /api/account/resetPassword/validate | 
[**api_auth_activate**](AuthApi.md#api_auth_activate) | **GET** /api/auth/activate | 
[**api_auth_login**](AuthApi.md#api_auth_login) | **POST** /api/auth/login | 
[**api_auth_profile_create**](AuthApi.md#api_auth_profile_create) | **POST** /api/auth/profile | 
[**api_auth_profile_delete**](AuthApi.md#api_auth_profile_delete) | **DELETE** /api/auth/profile/{username} | 
[**api_auth_profile_list**](AuthApi.md#api_auth_profile_list) | **GET** /api/auth/profile | 
[**api_auth_profile_partial_update**](AuthApi.md#api_auth_profile_partial_update) | **PATCH** /api/auth/profile/{username} | 
[**api_auth_profile_read**](AuthApi.md#api_auth_profile_read) | **GET** /api/auth/profile/{username} | 
[**api_auth_profile_update**](AuthApi.md#api_auth_profile_update) | **PUT** /api/auth/profile/{username} | 
[**api_auth_register**](AuthApi.md#api_auth_register) | **POST** /api/auth/register | 


# **api_account_change_password_change**
> Token api_account_change_password_change(data)



### Example

* Basic Authentication (Basic):

```python
import time
import estela_client
from estela_client.api import auth_api
from estela_client.model.change_password import ChangePassword
from estela_client.model.token import Token
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
    api_instance = auth_api.AuthApi(api_client)
    data = ChangePassword(
        new_password="new_password_example",
        confirm_new_password="confirm_new_password_example",
        old_password="old_password_example",
    ) # ChangePassword | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_account_change_password_change(data)
        pprint(api_response)
    except estela_client.ApiException as e:
        print("Exception when calling AuthApi->api_account_change_password_change: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ChangePassword**](ChangePassword.md)|  |

### Return type

[**Token**](Token.md)

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

# **api_account_reset_password_confirm**
> Token api_account_reset_password_confirm(token, pair, data)



### Example

* Basic Authentication (Basic):

```python
import time
import estela_client
from estela_client.api import auth_api
from estela_client.model.token import Token
from estela_client.model.reset_password_confirm import ResetPasswordConfirm
from estela_client.model.inline_response401 import InlineResponse401
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
    api_instance = auth_api.AuthApi(api_client)
    token = "token_example" # str | Token
    pair = "pair_example" # str | Pair
    data = ResetPasswordConfirm(
        new_password="new_password_example",
        confirm_new_password="confirm_new_password_example",
    ) # ResetPasswordConfirm | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_account_reset_password_confirm(token, pair, data)
        pprint(api_response)
    except estela_client.ApiException as e:
        print("Exception when calling AuthApi->api_account_reset_password_confirm: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Token |
 **pair** | **str**| Pair |
 **data** | [**ResetPasswordConfirm**](ResetPasswordConfirm.md)|  |

### Return type

[**Token**](Token.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**401** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_account_reset_password_request**
> Token api_account_reset_password_request(data)



### Example

* Basic Authentication (Basic):

```python
import time
import estela_client
from estela_client.api import auth_api
from estela_client.model.reset_password_request import ResetPasswordRequest
from estela_client.model.token import Token
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
    api_instance = auth_api.AuthApi(api_client)
    data = ResetPasswordRequest(
        email="email_example",
    ) # ResetPasswordRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_account_reset_password_request(data)
        pprint(api_response)
    except estela_client.ApiException as e:
        print("Exception when calling AuthApi->api_account_reset_password_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ResetPasswordRequest**](ResetPasswordRequest.md)|  |

### Return type

[**Token**](Token.md)

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

# **api_account_reset_password_validate**
> InlineResponse200 api_account_reset_password_validate(token, pair)



### Example

* Basic Authentication (Basic):

```python
import time
import estela_client
from estela_client.api import auth_api
from estela_client.model.inline_response200 import InlineResponse200
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
    api_instance = auth_api.AuthApi(api_client)
    token = "token_example" # str | Token
    pair = "pair_example" # str | Pair

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_account_reset_password_validate(token, pair)
        pprint(api_response)
    except estela_client.ApiException as e:
        print("Exception when calling AuthApi->api_account_reset_password_validate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Token |
 **pair** | **str**| Pair |

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_auth_activate**
> [AuthToken] api_auth_activate()



### Example

* Basic Authentication (Basic):

```python
import time
import estela_client
from estela_client.api import auth_api
from estela_client.model.auth_token import AuthToken
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
    api_instance = auth_api.AuthApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.api_auth_activate()
        pprint(api_response)
    except estela_client.ApiException as e:
        print("Exception when calling AuthApi->api_auth_activate: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[AuthToken]**](AuthToken.md)

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

# **api_auth_login**
> Token api_auth_login(data)



### Example

* Basic Authentication (Basic):

```python
import time
import estela_client
from estela_client.api import auth_api
from estela_client.model.token import Token
from estela_client.model.auth_token import AuthToken
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
    api_instance = auth_api.AuthApi(api_client)
    data = AuthToken(
        username="username_example",
        password="password_example",
    ) # AuthToken | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_auth_login(data)
        pprint(api_response)
    except estela_client.ApiException as e:
        print("Exception when calling AuthApi->api_auth_login: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**AuthToken**](AuthToken.md)|  |

### Return type

[**Token**](Token.md)

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

# **api_auth_profile_create**
> UserProfile api_auth_profile_create(data)



### Example

* Basic Authentication (Basic):

```python
import time
import estela_client
from estela_client.api import auth_api
from estela_client.model.user_profile import UserProfile
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
    api_instance = auth_api.AuthApi(api_client)
    data = UserProfile(
        username="username_example",
        email="email_example",
        password="password_example",
    ) # UserProfile | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_auth_profile_create(data)
        pprint(api_response)
    except estela_client.ApiException as e:
        print("Exception when calling AuthApi->api_auth_profile_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**UserProfile**](UserProfile.md)|  |

### Return type

[**UserProfile**](UserProfile.md)

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

# **api_auth_profile_delete**
> api_auth_profile_delete(username)



### Example

* Basic Authentication (Basic):

```python
import time
import estela_client
from estela_client.api import auth_api
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
    api_instance = auth_api.AuthApi(api_client)
    username = "A" # str | Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_auth_profile_delete(username)
    except estela_client.ApiException as e:
        print("Exception when calling AuthApi->api_auth_profile_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. |

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

# **api_auth_profile_list**
> [UserProfile] api_auth_profile_list()



### Example

* Basic Authentication (Basic):

```python
import time
import estela_client
from estela_client.api import auth_api
from estela_client.model.user_profile import UserProfile
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
    api_instance = auth_api.AuthApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.api_auth_profile_list()
        pprint(api_response)
    except estela_client.ApiException as e:
        print("Exception when calling AuthApi->api_auth_profile_list: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[UserProfile]**](UserProfile.md)

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

# **api_auth_profile_partial_update**
> UserProfile api_auth_profile_partial_update(username, data)



### Example

* Basic Authentication (Basic):

```python
import time
import estela_client
from estela_client.api import auth_api
from estela_client.model.user_profile import UserProfile
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
    api_instance = auth_api.AuthApi(api_client)
    username = "A" # str | Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.
    data = UserProfile(
        username="username_example",
        email="email_example",
        password="password_example",
    ) # UserProfile | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_auth_profile_partial_update(username, data)
        pprint(api_response)
    except estela_client.ApiException as e:
        print("Exception when calling AuthApi->api_auth_profile_partial_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. |
 **data** | [**UserProfile**](UserProfile.md)|  |

### Return type

[**UserProfile**](UserProfile.md)

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

# **api_auth_profile_read**
> UserProfile api_auth_profile_read(username)



### Example

* Basic Authentication (Basic):

```python
import time
import estela_client
from estela_client.api import auth_api
from estela_client.model.user_profile import UserProfile
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
    api_instance = auth_api.AuthApi(api_client)
    username = "A" # str | Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_auth_profile_read(username)
        pprint(api_response)
    except estela_client.ApiException as e:
        print("Exception when calling AuthApi->api_auth_profile_read: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. |

### Return type

[**UserProfile**](UserProfile.md)

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

# **api_auth_profile_update**
> UserProfile api_auth_profile_update(username, data)



### Example

* Basic Authentication (Basic):

```python
import time
import estela_client
from estela_client.api import auth_api
from estela_client.model.user_profile import UserProfile
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
    api_instance = auth_api.AuthApi(api_client)
    username = "A" # str | Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.
    data = UserProfile(
        username="username_example",
        email="email_example",
        password="password_example",
    ) # UserProfile | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_auth_profile_update(username, data)
        pprint(api_response)
    except estela_client.ApiException as e:
        print("Exception when calling AuthApi->api_auth_profile_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. |
 **data** | [**UserProfile**](UserProfile.md)|  |

### Return type

[**UserProfile**](UserProfile.md)

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

# **api_auth_register**
> Token api_auth_register(data)



### Example

* Basic Authentication (Basic):

```python
import time
import estela_client
from estela_client.api import auth_api
from estela_client.model.user import User
from estela_client.model.token import Token
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
    api_instance = auth_api.AuthApi(api_client)
    data = User(
        email="email_example",
        username="A",
        password="password_example",
    ) # User | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_auth_register(data)
        pprint(api_response)
    except estela_client.ApiException as e:
        print("Exception when calling AuthApi->api_auth_register: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**User**](User.md)|  |

### Return type

[**Token**](Token.md)

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

