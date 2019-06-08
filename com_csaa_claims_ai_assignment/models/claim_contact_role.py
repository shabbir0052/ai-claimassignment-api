# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from com_csaa_claims_ai_assignment.models.base_model_ import Model
from com_csaa_claims_ai_assignment import util


class ClaimContactRole(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, role=None, covered_party_type=None, policy_operator_type=None):  # noqa: E501
        """ClaimContactRole - a model defined in OpenAPI

        :param role: The role of this ClaimContactRole.  # noqa: E501
        :type role: str
        :param covered_party_type: The covered_party_type of this ClaimContactRole.  # noqa: E501
        :type covered_party_type: str
        :param policy_operator_type: The policy_operator_type of this ClaimContactRole.  # noqa: E501
        :type policy_operator_type: str
        """
        self.openapi_types = {
            'role': str,
            'covered_party_type': str,
            'policy_operator_type': str
        }

        self.attribute_map = {
            'role': 'role',
            'covered_party_type': 'coveredPartyType',
            'policy_operator_type': 'policyOperatorType'
        }

        self._role = role
        self._covered_party_type = covered_party_type
        self._policy_operator_type = policy_operator_type

    @classmethod
    def from_dict(cls, dikt) -> 'ClaimContactRole':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ClaimContactRole of this ClaimContactRole.  # noqa: E501
        :rtype: ClaimContactRole
        """
        return util.deserialize_model(dikt, cls)

    @property
    def role(self):
        """Gets the role of this ClaimContactRole.


        :return: The role of this ClaimContactRole.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this ClaimContactRole.


        :param role: The role of this ClaimContactRole.
        :type role: str
        """

        self._role = role

    @property
    def covered_party_type(self):
        """Gets the covered_party_type of this ClaimContactRole.


        :return: The covered_party_type of this ClaimContactRole.
        :rtype: str
        """
        return self._covered_party_type

    @covered_party_type.setter
    def covered_party_type(self, covered_party_type):
        """Sets the covered_party_type of this ClaimContactRole.


        :param covered_party_type: The covered_party_type of this ClaimContactRole.
        :type covered_party_type: str
        """

        self._covered_party_type = covered_party_type

    @property
    def policy_operator_type(self):
        """Gets the policy_operator_type of this ClaimContactRole.


        :return: The policy_operator_type of this ClaimContactRole.
        :rtype: str
        """
        return self._policy_operator_type

    @policy_operator_type.setter
    def policy_operator_type(self, policy_operator_type):
        """Sets the policy_operator_type of this ClaimContactRole.


        :param policy_operator_type: The policy_operator_type of this ClaimContactRole.
        :type policy_operator_type: str
        """

        self._policy_operator_type = policy_operator_type