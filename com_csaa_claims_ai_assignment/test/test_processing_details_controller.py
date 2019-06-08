# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from com_csaa_claims_ai_assignment.models.api_processing_response import ApiProcessingResponse  # noqa: E501
from com_csaa_claims_ai_assignment.models.fault import Fault  # noqa: E501
from com_csaa_claims_ai_assignment.test import BaseTestCase


class TestProcessingDetailsController(BaseTestCase):
    """ProcessingDetailsController integration test stubs"""

    def test_get_details(self):
        """Test case for get_details

        Get the details of AI model processing for a particular claim number
        """
        query_string = [('claimNumber', 1000-00-0000)]
        headers = { 
            'Accept': 'application/json',
            'x_application_context': {
"userId": "user",
"transactionType": "realtime",
"application": "CAS",
"subSystem": "FNOL",
"address": "127.0.0.1",
"correlationId": "0f333c4c-3d35-48e8-971c-c01e74ee209a"
}
,
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/ent/csaa/v1/claims/ai-assignment',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
