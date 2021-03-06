# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from com_csaa_claims_ai_assignment.models.base_model_ import Model
from com_csaa_claims_ai_assignment.models.vehicle import Vehicle
from com_csaa_claims_ai_assignment import util

from com_csaa_claims_ai_assignment.models.vehicle import Vehicle  # noqa: E501

class Incident(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, publicid=None, subtype=None, child_seat=None, vehicle_loss_party=None, driver_relation=None, ins_furth_invest=None, total_loss=None, total_loss_points=None, incident_vehicle=None, vehicle_age10years=None, vehicle_age5years=None, vehicle_operable=None, vehicle_parked=None, vehicle_type=None):  # noqa: E501
        """Incident - a model defined in OpenAPI

        :param publicid: The publicid of this Incident.  # noqa: E501
        :type publicid: str
        :param subtype: The subtype of this Incident.  # noqa: E501
        :type subtype: str
        :param child_seat: The child_seat of this Incident.  # noqa: E501
        :type child_seat: str
        :param vehicle_loss_party: The vehicle_loss_party of this Incident.  # noqa: E501
        :type vehicle_loss_party: str
        :param driver_relation: The driver_relation of this Incident.  # noqa: E501
        :type driver_relation: str
        :param ins_furth_invest: The ins_furth_invest of this Incident.  # noqa: E501
        :type ins_furth_invest: str
        :param total_loss: The total_loss of this Incident.  # noqa: E501
        :type total_loss: str
        :param total_loss_points: The total_loss_points of this Incident.  # noqa: E501
        :type total_loss_points: str
        :param incident_vehicle: The incident_vehicle of this Incident.  # noqa: E501
        :type incident_vehicle: Vehicle
        :param vehicle_age10years: The vehicle_age10years of this Incident.  # noqa: E501
        :type vehicle_age10years: str
        :param vehicle_age5years: The vehicle_age5years of this Incident.  # noqa: E501
        :type vehicle_age5years: str
        :param vehicle_operable: The vehicle_operable of this Incident.  # noqa: E501
        :type vehicle_operable: str
        :param vehicle_parked: The vehicle_parked of this Incident.  # noqa: E501
        :type vehicle_parked: str
        :param vehicle_type: The vehicle_type of this Incident.  # noqa: E501
        :type vehicle_type: str
        """
        self.openapi_types = {
            'publicid': str,
            'subtype': str,
            'child_seat': str,
            'vehicle_loss_party': str,
            'driver_relation': str,
            'ins_furth_invest': str,
            'total_loss': str,
            'total_loss_points': str,
            'incident_vehicle': Vehicle,
            'vehicle_age10years': str,
            'vehicle_age5years': str,
            'vehicle_operable': str,
            'vehicle_parked': str,
            'vehicle_type': str
        }

        self.attribute_map = {
            'publicid': 'publicid',
            'subtype': 'subtype',
            'child_seat': 'childSeat',
            'vehicle_loss_party': 'vehicleLossParty',
            'driver_relation': 'driverRelation',
            'ins_furth_invest': 'insFurthInvest',
            'total_loss': 'totalLoss',
            'total_loss_points': 'totalLossPoints',
            'incident_vehicle': 'incidentVehicle',
            'vehicle_age10years': 'vehicleAge10years',
            'vehicle_age5years': 'vehicleAge5years',
            'vehicle_operable': 'vehicleOperable',
            'vehicle_parked': 'vehicleParked',
            'vehicle_type': 'vehicleType'
        }

        self._publicid = publicid
        self._subtype = subtype
        self._child_seat = child_seat
        self._vehicle_loss_party = vehicle_loss_party
        self._driver_relation = driver_relation
        self._ins_furth_invest = ins_furth_invest
        self._total_loss = total_loss
        self._total_loss_points = total_loss_points
        self._incident_vehicle = incident_vehicle
        self._vehicle_age10years = vehicle_age10years
        self._vehicle_age5years = vehicle_age5years
        self._vehicle_operable = vehicle_operable
        self._vehicle_parked = vehicle_parked
        self._vehicle_type = vehicle_type

    @classmethod
    def from_dict(cls, dikt) -> 'Incident':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Incident of this Incident.  # noqa: E501
        :rtype: Incident
        """
        return util.deserialize_model(dikt, cls)

    @property
    def publicid(self):
        """Gets the publicid of this Incident.


        :return: The publicid of this Incident.
        :rtype: str
        """
        return self._publicid

    @publicid.setter
    def publicid(self, publicid):
        """Sets the publicid of this Incident.


        :param publicid: The publicid of this Incident.
        :type publicid: str
        """

        self._publicid = publicid

    @property
    def subtype(self):
        """Gets the subtype of this Incident.


        :return: The subtype of this Incident.
        :rtype: str
        """
        return self._subtype

    @subtype.setter
    def subtype(self, subtype):
        """Sets the subtype of this Incident.


        :param subtype: The subtype of this Incident.
        :type subtype: str
        """

        self._subtype = subtype

    @property
    def child_seat(self):
        """Gets the child_seat of this Incident.


        :return: The child_seat of this Incident.
        :rtype: str
        """
        return self._child_seat

    @child_seat.setter
    def child_seat(self, child_seat):
        """Sets the child_seat of this Incident.


        :param child_seat: The child_seat of this Incident.
        :type child_seat: str
        """

        self._child_seat = child_seat

    @property
    def vehicle_loss_party(self):
        """Gets the vehicle_loss_party of this Incident.


        :return: The vehicle_loss_party of this Incident.
        :rtype: str
        """
        return self._vehicle_loss_party

    @vehicle_loss_party.setter
    def vehicle_loss_party(self, vehicle_loss_party):
        """Sets the vehicle_loss_party of this Incident.


        :param vehicle_loss_party: The vehicle_loss_party of this Incident.
        :type vehicle_loss_party: str
        """

        self._vehicle_loss_party = vehicle_loss_party

    @property
    def driver_relation(self):
        """Gets the driver_relation of this Incident.


        :return: The driver_relation of this Incident.
        :rtype: str
        """
        return self._driver_relation

    @driver_relation.setter
    def driver_relation(self, driver_relation):
        """Sets the driver_relation of this Incident.


        :param driver_relation: The driver_relation of this Incident.
        :type driver_relation: str
        """

        self._driver_relation = driver_relation

    @property
    def ins_furth_invest(self):
        """Gets the ins_furth_invest of this Incident.


        :return: The ins_furth_invest of this Incident.
        :rtype: str
        """
        return self._ins_furth_invest

    @ins_furth_invest.setter
    def ins_furth_invest(self, ins_furth_invest):
        """Sets the ins_furth_invest of this Incident.


        :param ins_furth_invest: The ins_furth_invest of this Incident.
        :type ins_furth_invest: str
        """

        self._ins_furth_invest = ins_furth_invest

    @property
    def total_loss(self):
        """Gets the total_loss of this Incident.


        :return: The total_loss of this Incident.
        :rtype: str
        """
        return self._total_loss

    @total_loss.setter
    def total_loss(self, total_loss):
        """Sets the total_loss of this Incident.


        :param total_loss: The total_loss of this Incident.
        :type total_loss: str
        """

        self._total_loss = total_loss

    @property
    def total_loss_points(self):
        """Gets the total_loss_points of this Incident.


        :return: The total_loss_points of this Incident.
        :rtype: str
        """
        return self._total_loss_points

    @total_loss_points.setter
    def total_loss_points(self, total_loss_points):
        """Sets the total_loss_points of this Incident.


        :param total_loss_points: The total_loss_points of this Incident.
        :type total_loss_points: str
        """

        self._total_loss_points = total_loss_points

    @property
    def incident_vehicle(self):
        """Gets the incident_vehicle of this Incident.


        :return: The incident_vehicle of this Incident.
        :rtype: Vehicle
        """
        return self._incident_vehicle

    @incident_vehicle.setter
    def incident_vehicle(self, incident_vehicle):
        """Sets the incident_vehicle of this Incident.


        :param incident_vehicle: The incident_vehicle of this Incident.
        :type incident_vehicle: Vehicle
        """

        self._incident_vehicle = incident_vehicle

    @property
    def vehicle_age10years(self):
        """Gets the vehicle_age10years of this Incident.


        :return: The vehicle_age10years of this Incident.
        :rtype: str
        """
        return self._vehicle_age10years

    @vehicle_age10years.setter
    def vehicle_age10years(self, vehicle_age10years):
        """Sets the vehicle_age10years of this Incident.


        :param vehicle_age10years: The vehicle_age10years of this Incident.
        :type vehicle_age10years: str
        """

        self._vehicle_age10years = vehicle_age10years

    @property
    def vehicle_age5years(self):
        """Gets the vehicle_age5years of this Incident.


        :return: The vehicle_age5years of this Incident.
        :rtype: str
        """
        return self._vehicle_age5years

    @vehicle_age5years.setter
    def vehicle_age5years(self, vehicle_age5years):
        """Sets the vehicle_age5years of this Incident.


        :param vehicle_age5years: The vehicle_age5years of this Incident.
        :type vehicle_age5years: str
        """

        self._vehicle_age5years = vehicle_age5years

    @property
    def vehicle_operable(self):
        """Gets the vehicle_operable of this Incident.


        :return: The vehicle_operable of this Incident.
        :rtype: str
        """
        return self._vehicle_operable

    @vehicle_operable.setter
    def vehicle_operable(self, vehicle_operable):
        """Sets the vehicle_operable of this Incident.


        :param vehicle_operable: The vehicle_operable of this Incident.
        :type vehicle_operable: str
        """

        self._vehicle_operable = vehicle_operable

    @property
    def vehicle_parked(self):
        """Gets the vehicle_parked of this Incident.


        :return: The vehicle_parked of this Incident.
        :rtype: str
        """
        return self._vehicle_parked

    @vehicle_parked.setter
    def vehicle_parked(self, vehicle_parked):
        """Sets the vehicle_parked of this Incident.


        :param vehicle_parked: The vehicle_parked of this Incident.
        :type vehicle_parked: str
        """

        self._vehicle_parked = vehicle_parked

    @property
    def vehicle_type(self):
        """Gets the vehicle_type of this Incident.


        :return: The vehicle_type of this Incident.
        :rtype: str
        """
        return self._vehicle_type

    @vehicle_type.setter
    def vehicle_type(self, vehicle_type):
        """Sets the vehicle_type of this Incident.


        :param vehicle_type: The vehicle_type of this Incident.
        :type vehicle_type: str
        """

        self._vehicle_type = vehicle_type
