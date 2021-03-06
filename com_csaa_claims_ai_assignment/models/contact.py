# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from com_csaa_claims_ai_assignment.models.base_model_ import Model
from com_csaa_claims_ai_assignment.models.claim_contact_role import ClaimContactRole
from com_csaa_claims_ai_assignment import util

from com_csaa_claims_ai_assignment.models.claim_contact_role import ClaimContactRole  # noqa: E501

class Contact(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, public_id=None, first_name=None, last_name=None, ssn_tax_id_present=None, claim_contact_role=None):  # noqa: E501
        """Contact - a model defined in OpenAPI

        :param public_id: The public_id of this Contact.  # noqa: E501
        :type public_id: str
        :param first_name: The first_name of this Contact.  # noqa: E501
        :type first_name: str
        :param last_name: The last_name of this Contact.  # noqa: E501
        :type last_name: str
        :param ssn_tax_id_present: The ssn_tax_id_present of this Contact.  # noqa: E501
        :type ssn_tax_id_present: str
        :param claim_contact_role: The claim_contact_role of this Contact.  # noqa: E501
        :type claim_contact_role: List[ClaimContactRole]
        """
        self.openapi_types = {
            'public_id': str,
            'first_name': str,
            'last_name': str,
            'ssn_tax_id_present': str,
            'claim_contact_role': List[ClaimContactRole]
        }

        self.attribute_map = {
            'public_id': 'publicId',
            'first_name': 'firstName',
            'last_name': 'lastName',
            'ssn_tax_id_present': 'ssnTaxIDPresent',
            'claim_contact_role': 'claimContactRole'
        }

        self._public_id = public_id
        self._first_name = first_name
        self._last_name = last_name
        self._ssn_tax_id_present = ssn_tax_id_present
        self._claim_contact_role = claim_contact_role

    @classmethod
    def from_dict(cls, dikt) -> 'Contact':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Contact of this Contact.  # noqa: E501
        :rtype: Contact
        """
        return util.deserialize_model(dikt, cls)

    @property
    def public_id(self):
        """Gets the public_id of this Contact.


        :return: The public_id of this Contact.
        :rtype: str
        """
        return self._public_id

    @public_id.setter
    def public_id(self, public_id):
        """Sets the public_id of this Contact.


        :param public_id: The public_id of this Contact.
        :type public_id: str
        """

        self._public_id = public_id

    @property
    def first_name(self):
        """Gets the first_name of this Contact.


        :return: The first_name of this Contact.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this Contact.


        :param first_name: The first_name of this Contact.
        :type first_name: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this Contact.


        :return: The last_name of this Contact.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this Contact.


        :param last_name: The last_name of this Contact.
        :type last_name: str
        """

        self._last_name = last_name

    @property
    def ssn_tax_id_present(self):
        """Gets the ssn_tax_id_present of this Contact.


        :return: The ssn_tax_id_present of this Contact.
        :rtype: str
        """
        return self._ssn_tax_id_present

    @ssn_tax_id_present.setter
    def ssn_tax_id_present(self, ssn_tax_id_present):
        """Sets the ssn_tax_id_present of this Contact.


        :param ssn_tax_id_present: The ssn_tax_id_present of this Contact.
        :type ssn_tax_id_present: str
        """

        self._ssn_tax_id_present = ssn_tax_id_present

    @property
    def claim_contact_role(self):
        """Gets the claim_contact_role of this Contact.


        :return: The claim_contact_role of this Contact.
        :rtype: List[ClaimContactRole]
        """
        return self._claim_contact_role

    @claim_contact_role.setter
    def claim_contact_role(self, claim_contact_role):
        """Sets the claim_contact_role of this Contact.


        :param claim_contact_role: The claim_contact_role of this Contact.
        :type claim_contact_role: List[ClaimContactRole]
        """

        self._claim_contact_role = claim_contact_role
