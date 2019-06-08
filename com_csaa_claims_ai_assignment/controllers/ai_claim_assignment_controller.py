import connexion
import six

from com_csaa_claims_ai_assignment.models.claim import Claim  # noqa: E501
from com_csaa_claims_ai_assignment.models.fault import Fault  # noqa: E501
from com_csaa_claims_ai_assignment.models.response import Response  # noqa: E501
from com_csaa_claims_ai_assignment import util


def postassign(claim_number, x_application_context, claim):  # noqa: E501
    """AI API to determine claim eligible for STP

    AI API to determine claim eligible for STP # noqa: E501

    :param claim_number: Claim Number
    :type claim_number: str
    :param x_application_context: 
    :type x_application_context: str
    :param claim: 
    :type claim: dict | bytes

    :rtype: Response
    """
    if connexion.request.is_json:
        claim = Claim.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
