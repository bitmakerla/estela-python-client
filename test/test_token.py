"""
    estela API v1.0 Documentation

    estela API Swagger Specification  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import estela_client
from estela_client.model.user_detail import UserDetail
globals()['UserDetail'] = UserDetail
from estela_client.model.token import Token


class TestToken(unittest.TestCase):
    """Token unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testToken(self):
        """Test Token"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Token()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()