import connexion
import six

from com_csaa_claims_ai_assignment.models.api_processing_response import ApiProcessingResponse  # noqa: E501
from com_csaa_claims_ai_assignment.models.fault import Fault  # noqa: E501
from com_csaa_claims_ai_assignment import util


def get_details(claim_number, x_application_context):  # noqa: E501
    """Get the details of AI model processing for a particular claim number

    Get the details of AI model processing for a particular claim number # noqa: E501

    :param claim_number: Claim Number
    :type claim_number: str
    :param x_application_context: 
    :type x_application_context: str

    :rtype: ApiProcessingResponse
    """
    return 'do some magic!'
