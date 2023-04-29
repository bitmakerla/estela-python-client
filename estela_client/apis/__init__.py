# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from estela_client.api.auth_api import AuthApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from estela_client.api.auth_api import AuthApi
from estela_client.api.deploys_api import DeploysApi
from estela_client.api.projects_api import ProjectsApi
from estela_client.api.spider_cronjobs_api import SpiderCronjobsApi
from estela_client.api.spider_jobs_api import SpiderJobsApi
from estela_client.api.spiders_api import SpidersApi
