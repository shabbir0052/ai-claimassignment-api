# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from com_csaa_claims_ai_assignment.models.base_model_ import Model
from com_csaa_claims_ai_assignment import util


class AIResult(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, version=None, confidence_score=None, outcome=None):  # noqa: E501
        """AIResult - a model defined in OpenAPI

        :param name: The name of this AIResult.  # noqa: E501
        :type name: str
        :param version: The version of this AIResult.  # noqa: E501
        :type version: str
        :param confidence_score: The confidence_score of this AIResult.  # noqa: E501
        :type confidence_score: str
        :param outcome: The outcome of this AIResult.  # noqa: E501
        :type outcome: str
        """
        self.openapi_types = {
            'name': str,
            'version': str,
            'confidence_score': str,
            'outcome': str
        }

        self.attribute_map = {
            'name': 'name',
            'version': 'version',
            'confidence_score': 'confidenceScore',
            'outcome': 'outcome'
        }

        self._name = name
        self._version = version
        self._confidence_score = confidence_score
        self._outcome = outcome

    @classmethod
    def from_dict(cls, dikt) -> 'AIResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AIResult of this AIResult.  # noqa: E501
        :rtype: AIResult
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this AIResult.


        :return: The name of this AIResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AIResult.


        :param name: The name of this AIResult.
        :type name: str
        """

        self._name = name

    @property
    def version(self):
        """Gets the version of this AIResult.


        :return: The version of this AIResult.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this AIResult.


        :param version: The version of this AIResult.
        :type version: str
        """

        self._version = version

    @property
    def confidence_score(self):
        """Gets the confidence_score of this AIResult.


        :return: The confidence_score of this AIResult.
        :rtype: str
        """
        return self._confidence_score

    @confidence_score.setter
    def confidence_score(self, confidence_score):
        """Sets the confidence_score of this AIResult.


        :param confidence_score: The confidence_score of this AIResult.
        :type confidence_score: str
        """

        self._confidence_score = confidence_score

    @property
    def outcome(self):
        """Gets the outcome of this AIResult.


        :return: The outcome of this AIResult.
        :rtype: str
        """
        return self._outcome

    @outcome.setter
    def outcome(self, outcome):
        """Sets the outcome of this AIResult.


        :param outcome: The outcome of this AIResult.
        :type outcome: str
        """

        self._outcome = outcome
