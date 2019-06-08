# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from com_csaa_claims_ai_assignment.models.claim import Claim  # noqa: E501
from com_csaa_claims_ai_assignment.models.fault import Fault  # noqa: E501
from com_csaa_claims_ai_assignment.models.response import Response  # noqa: E501
from com_csaa_claims_ai_assignment.test import BaseTestCase


class TestAIClaimAssignmentController(BaseTestCase):
    """AIClaimAssignmentController integration test stubs"""

    def test_postassign(self):
        """Test case for postassign

        AI API to determine claim eligible for STP
        """
        claim = "{\r\n      \"catastropheNumber\": \"074\",\r\n      \"claimNumber\": \"1000-00-0000\",\r\n      \"coverageInQuestion\": \"false\",\r\n      \"description\": \"collision\",\r\n      \"faultRating\": \"0\",\r\n      \"howReported\": \"phone\",\r\n      \"incidentReport\": \"false\",\r\n      \"liabilityCode\": \"C_AAA\",\r\n      \"lossCause\": \"parkedCollision_AAA\",\r\n      \"reportedByType\": \"self\",\r\n      \"subrogationStatus\": \"notpursuing_AAA\",\r\n      \"lossLocation\": {\r\n        \"publicId\": \"cc:34435468\",\r\n        \"postalCode\": \"95815-2625\",\r\n        \"state\": \"CA\"\r\n      },\r\n      \"contacts\": [\r\n        {\r\n          \"publicId\": \"cc:123456\",\r\n          \"firstName\": \"John\",\r\n          \"lastName\": \"Doe\",\r\n          \"ssnTaxIDPresent\": \"Yes\",\r\n          \"claimContactRole\": [\r\n            {\r\n              \"role\": \"reporter\",\r\n              \"coveredPartyType\": \"insured_AAA\",\r\n              \"policyOperatorType\": \"rated_AAA\"\r\n            },\r\n            {\r\n              \"role\": \"insured\",\r\n              \"coveredPartyType\": \"\",\r\n              \"policyOperatorType\": \"rated_AAA\"\r\n            }\r\n          ]\r\n        }\r\n      ],\r\n      \"exposures\": [\r\n        {\r\n          \"claimant\": {\r\n            \"publicId\": \"cc:2343559009\",\r\n            \"driverInsuredRelation\": \"self\",\r\n            \"injured\": \"Yes\",\r\n            \"isEmployee\": \"Yes\",\r\n            \"occupation\": \"licensed physician\",\r\n            \"subType\": \"Person\",\r\n            \"taxStatus\": \"activenoexmpt_AAA\"\r\n          },\r\n          \"claimantType\": \"insured\",\r\n          \"coverageSubType\": \"PACollisionCov\",\r\n          \"exposureSubroStatus\": \"notpursuing_AAA\",\r\n          \"exposureType\": \"VehicleDamage\",\r\n          \"jurisdictionState\": \"CA\",\r\n          \"lossParty\": \"insured\",\r\n          \"primaryCoverage\": \"PACollisionCov\",\r\n          \"state\": \"draft\",\r\n          \"coverage\": {\r\n            \"deductible\": \"250.00 usd\",\r\n            \"rentalDailyLimit\": \"\",\r\n            \"type\": \"PACollisionCov\",\r\n            \"zeroGlassDeduct\": \"\"\r\n          },\r\n          \"incidentPublicId\": \"cc:45657567\"\r\n        },\r\n        {\r\n          \"claimant\": {\r\n            \"publicId\": \"cc:2343556876\",\r\n            \"driverInsuredRelation\": \"self\",\r\n            \"injured\": \"Yes\",\r\n            \"isEmployee\": \"Yes\",\r\n            \"occupation\": \"licensed physician\",\r\n            \"subType\": \"Person\",\r\n            \"taxStatus\": \"activenoexmpt_AAA\"\r\n          },\r\n          \"claimantType\": \"insured\",\r\n          \"coverageSubType\": \"PARentalCov\",\r\n          \"state\": \"draft\",\r\n          \"coverage\": {\r\n            \"deductible\": \"350.00 usd\",\r\n            \"rentalDailyLimit\": \"\",\r\n            \"type\": \"PARentalCov\",\r\n            \"zeroGlassDeduct\": \"\"\r\n          },\r\n          \"incidentPublicId\": \"cc:45657567\"\r\n        }\r\n      ],\r\n      \"incidents\": [\r\n        {\r\n          \"publicid\": \"cc:45657567\",\r\n          \"subtype\": \"VehicleIncident\",\r\n          \"childSeat\": \"Yes\",\r\n          \"vehicleLossParty\": \"insured\",\r\n          \"driverRelation\": \"self\",\r\n          \"insFurthInvest\": \"false\",\r\n          \"totalLoss\": \"true\",\r\n          \"totalLossPoints\": \"0\",\r\n          \"incidentVehicle\": {\r\n            \"publicid\": \"cc:78797865\",\r\n            \"color\": \"red\",\r\n            \"licensePlate\": \"1C223GS56\",\r\n            \"make\": \"Chevrolet\",\r\n            \"mileage\": \"50000\",\r\n            \"model\": \"Impala\",\r\n            \"style\": \"passengercar\",\r\n            \"symbol\": \"35\",\r\n            \"ubi\": \"No\",\r\n            \"year\": \"2013\"\r\n          },\r\n          \"vehicleAge10years\": \"false\",\r\n          \"vehicleAge5years\": \"true\",\r\n          \"vehicleOperable\": \"true\",\r\n          \"vehicleParked\": \"false\",\r\n          \"vehicleType\": \"owned\"\r\n        },\r\n        {\r\n          \"publicid\": \"cc:45657589\",\r\n          \"subtype\": \"VehicleIncident\",\r\n          \"childSeat\": \"No\",\r\n          \"vehicleLossParty\": \"third_party\",\r\n          \"driverRelation\": \"other\",\r\n          \"insFurthInvest\": \"false\",\r\n          \"totalLoss\": \"false\",\r\n          \"totalLossPoints\": \"0\",\r\n          \"incidentVehicle\": {\r\n            \"publicid\": \"cc:787978698\",\r\n            \"color\": \"white\",\r\n            \"licensePlate\": \"1AB43GS56\",\r\n            \"make\": \"Honda\",\r\n            \"mileage\": \"4000\",\r\n            \"model\": \"Civic\",\r\n            \"style\": \"passengercar\",\r\n            \"symbol\": \"35\",\r\n            \"ubi\": \"No\",\r\n            \"year\": \"2013\"\r\n          },\r\n          \"vehicleAge10years\": \"false\",\r\n          \"vehicleAge5years\": \"true\",\r\n          \"vehicleOperable\": \"true\",\r\n          \"vehicleParked\": \"false\",\r\n          \"vehicleType\": \"owned\"\r\n        },\r\n        {\r\n          \"publicid\": \"cc:456574567\",\r\n          \"subtype\": \"FixedPropertyIncident\"\r\n        },\r\n        {\r\n          \"publicid\": \"cc:4565769890\",\r\n          \"subtype\": \"InjuryIncident\"\r\n        }\r\n      ]\r\n    }"
        query_string = [('claimNumber', 1000-00-0000)]
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
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
            method='POST',
            headers=headers,
            data=json.dumps(claim),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
