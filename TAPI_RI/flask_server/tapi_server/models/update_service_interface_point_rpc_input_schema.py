# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server import util


class UpdateServiceInterfacePointRPCInputSchema(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, sip_id_or_name: str=None, state: str=None):  # noqa: E501
        """UpdateServiceInterfacePointRPCInputSchema - a model defined in Swagger

        :param sip_id_or_name: The sip_id_or_name of this UpdateServiceInterfacePointRPCInputSchema.  # noqa: E501
        :type sip_id_or_name: str
        :param state: The state of this UpdateServiceInterfacePointRPCInputSchema.  # noqa: E501
        :type state: str
        """
        self.swagger_types = {
            'sip_id_or_name': str,
            'state': str
        }

        self.attribute_map = {
            'sip_id_or_name': 'sip-id-or-name',
            'state': 'state'
        }

        self._sip_id_or_name = sip_id_or_name
        self._state = state

    @classmethod
    def from_dict(cls, dikt) -> 'UpdateServiceInterfacePointRPCInputSchema':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The update-service-interface-pointRPC_input_schema of this UpdateServiceInterfacePointRPCInputSchema.  # noqa: E501
        :rtype: UpdateServiceInterfacePointRPCInputSchema
        """
        return util.deserialize_model(dikt, cls)

    @property
    def sip_id_or_name(self) -> str:
        """Gets the sip_id_or_name of this UpdateServiceInterfacePointRPCInputSchema.


        :return: The sip_id_or_name of this UpdateServiceInterfacePointRPCInputSchema.
        :rtype: str
        """
        return self._sip_id_or_name

    @sip_id_or_name.setter
    def sip_id_or_name(self, sip_id_or_name: str):
        """Sets the sip_id_or_name of this UpdateServiceInterfacePointRPCInputSchema.


        :param sip_id_or_name: The sip_id_or_name of this UpdateServiceInterfacePointRPCInputSchema.
        :type sip_id_or_name: str
        """

        self._sip_id_or_name = sip_id_or_name

    @property
    def state(self) -> str:
        """Gets the state of this UpdateServiceInterfacePointRPCInputSchema.


        :return: The state of this UpdateServiceInterfacePointRPCInputSchema.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state: str):
        """Sets the state of this UpdateServiceInterfacePointRPCInputSchema.


        :param state: The state of this UpdateServiceInterfacePointRPCInputSchema.
        :type state: str
        """

        self._state = state
