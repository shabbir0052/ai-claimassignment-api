# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from com_csaa_claims_ai_assignment.models.base_model_ import Model
from com_csaa_claims_ai_assignment.models.claimant import Claimant
from com_csaa_claims_ai_assignment.models.coverage import Coverage
from com_csaa_claims_ai_assignment import util

from com_csaa_claims_ai_assignment.models.claimant import Claimant  # noqa: E501
from com_csaa_claims_ai_assignment.models.coverage import Coverage  # noqa: E501

class Exposure(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, claimant=None, claimant_type=None, coverage_sub_type=None, exposure_subro_status=None, exposure_type=None, jurisdiction_state=None, loss_party=None, primary_coverage=None, state=None, coverage=None, incident_public_id=None):  # noqa: E501
        """Exposure - a model defined in OpenAPI

        :param claimant: The claimant of this Exposure.  # noqa: E501
        :type claimant: Claimant
        :param claimant_type: The claimant_type of this Exposure.  # noqa: E501
        :type claimant_type: str
        :param coverage_sub_type: The coverage_sub_type of this Exposure.  # noqa: E501
        :type coverage_sub_type: str
        :param exposure_subro_status: The exposure_subro_status of this Exposure.  # noqa: E501
        :type exposure_subro_status: str
        :param exposure_type: The exposure_type of this Exposure.  # noqa: E501
        :type exposure_type: str
        :param jurisdiction_state: The jurisdiction_state of this Exposure.  # noqa: E501
        :type jurisdiction_state: str
        :param loss_party: The loss_party of this Exposure.  # noqa: E501
        :type loss_party: str
        :param primary_coverage: The primary_coverage of this Exposure.  # noqa: E501
        :type primary_coverage: str
        :param state: The state of this Exposure.  # noqa: E501
        :type state: str
        :param coverage: The coverage of this Exposure.  # noqa: E501
        :type coverage: Coverage
        :param incident_public_id: The incident_public_id of this Exposure.  # noqa: E501
        :type incident_public_id: str
        """
        self.openapi_types = {
            'claimant': Claimant,
            'claimant_type': str,
            'coverage_sub_type': str,
            'exposure_subro_status': str,
            'exposure_type': str,
            'jurisdiction_state': str,
            'loss_party': str,
            'primary_coverage': str,
            'state': str,
            'coverage': Coverage,
            'incident_public_id': str
        }

        self.attribute_map = {
            'claimant': 'claimant',
            'claimant_type': 'claimantType',
            'coverage_sub_type': 'coverageSubType',
            'exposure_subro_status': 'exposureSubroStatus',
            'exposure_type': 'exposureType',
            'jurisdiction_state': 'jurisdictionState',
            'loss_party': 'lossParty',
            'primary_coverage': 'primaryCoverage',
            'state': 'state',
            'coverage': 'coverage',
            'incident_public_id': 'incidentPublicId'
        }

        self._claimant = claimant
        self._claimant_type = claimant_type
        self._coverage_sub_type = coverage_sub_type
        self._exposure_subro_status = exposure_subro_status
        self._exposure_type = exposure_type
        self._jurisdiction_state = jurisdiction_state
        self._loss_party = loss_party
        self._primary_coverage = primary_coverage
        self._state = state
        self._coverage = coverage
        self._incident_public_id = incident_public_id

    @classmethod
    def from_dict(cls, dikt) -> 'Exposure':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Exposure of this Exposure.  # noqa: E501
        :rtype: Exposure
        """
        return util.deserialize_model(dikt, cls)

    @property
    def claimant(self):
        """Gets the claimant of this Exposure.


        :return: The claimant of this Exposure.
        :rtype: Claimant
        """
        return self._claimant

    @claimant.setter
    def claimant(self, claimant):
        """Sets the claimant of this Exposure.


        :param claimant: The claimant of this Exposure.
        :type claimant: Claimant
        """

        self._claimant = claimant

    @property
    def claimant_type(self):
        """Gets the claimant_type of this Exposure.


        :return: The claimant_type of this Exposure.
        :rtype: str
        """
        return self._claimant_type

    @claimant_type.setter
    def claimant_type(self, claimant_type):
        """Sets the claimant_type of this Exposure.


        :param claimant_type: The claimant_type of this Exposure.
        :type claimant_type: str
        """

        self._claimant_type = claimant_type

    @property
    def coverage_sub_type(self):
        """Gets the coverage_sub_type of this Exposure.


        :return: The coverage_sub_type of this Exposure.
        :rtype: str
        """
        return self._coverage_sub_type

    @coverage_sub_type.setter
    def coverage_sub_type(self, coverage_sub_type):
        """Sets the coverage_sub_type of this Exposure.


        :param coverage_sub_type: The coverage_sub_type of this Exposure.
        :type coverage_sub_type: str
        """

        self._coverage_sub_type = coverage_sub_type

    @property
    def exposure_subro_status(self):
        """Gets the exposure_subro_status of this Exposure.


        :return: The exposure_subro_status of this Exposure.
        :rtype: str
        """
        return self._exposure_subro_status

    @exposure_subro_status.setter
    def exposure_subro_status(self, exposure_subro_status):
        """Sets the exposure_subro_status of this Exposure.


        :param exposure_subro_status: The exposure_subro_status of this Exposure.
        :type exposure_subro_status: str
        """

        self._exposure_subro_status = exposure_subro_status

    @property
    def exposure_type(self):
        """Gets the exposure_type of this Exposure.


        :return: The exposure_type of this Exposure.
        :rtype: str
        """
        return self._exposure_type

    @exposure_type.setter
    def exposure_type(self, exposure_type):
        """Sets the exposure_type of this Exposure.


        :param exposure_type: The exposure_type of this Exposure.
        :type exposure_type: str
        """

        self._exposure_type = exposure_type

    @property
    def jurisdiction_state(self):
        """Gets the jurisdiction_state of this Exposure.


        :return: The jurisdiction_state of this Exposure.
        :rtype: str
        """
        return self._jurisdiction_state

    @jurisdiction_state.setter
    def jurisdiction_state(self, jurisdiction_state):
        """Sets the jurisdiction_state of this Exposure.


        :param jurisdiction_state: The jurisdiction_state of this Exposure.
        :type jurisdiction_state: str
        """

        self._jurisdiction_state = jurisdiction_state

    @property
    def loss_party(self):
        """Gets the loss_party of this Exposure.


        :return: The loss_party of this Exposure.
        :rtype: str
        """
        return self._loss_party

    @loss_party.setter
    def loss_party(self, loss_party):
        """Sets the loss_party of this Exposure.


        :param loss_party: The loss_party of this Exposure.
        :type loss_party: str
        """

        self._loss_party = loss_party

    @property
    def primary_coverage(self):
        """Gets the primary_coverage of this Exposure.


        :return: The primary_coverage of this Exposure.
        :rtype: str
        """
        return self._primary_coverage

    @primary_coverage.setter
    def primary_coverage(self, primary_coverage):
        """Sets the primary_coverage of this Exposure.


        :param primary_coverage: The primary_coverage of this Exposure.
        :type primary_coverage: str
        """

        self._primary_coverage = primary_coverage

    @property
    def state(self):
        """Gets the state of this Exposure.


        :return: The state of this Exposure.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Exposure.


        :param state: The state of this Exposure.
        :type state: str
        """

        self._state = state

    @property
    def coverage(self):
        """Gets the coverage of this Exposure.


        :return: The coverage of this Exposure.
        :rtype: Coverage
        """
        return self._coverage

    @coverage.setter
    def coverage(self, coverage):
        """Sets the coverage of this Exposure.


        :param coverage: The coverage of this Exposure.
        :type coverage: Coverage
        """

        self._coverage = coverage

    @property
    def incident_public_id(self):
        """Gets the incident_public_id of this Exposure.


        :return: The incident_public_id of this Exposure.
        :rtype: str
        """
        return self._incident_public_id

    @incident_public_id.setter
    def incident_public_id(self, incident_public_id):
        """Sets the incident_public_id of this Exposure.


        :param incident_public_id: The incident_public_id of this Exposure.
        :type incident_public_id: str
        """

        self._incident_public_id = incident_public_id
