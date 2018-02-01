# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.admin_state_pac import AdminStatePac  # noqa: F401,E501
from tapi_server.models.capacity_pac import CapacityPac  # noqa: F401,E501
from tapi_server.models.local_class import LocalClass  # noqa: F401,E501
from tapi_server.models.name_and_value import NameAndValue  # noqa: F401,E501
from tapi_server import util


class ConnectivityServiceEndPoint(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, local_id: str=None, name: List[NameAndValue]=None, administrative_state: str=None, operational_state: str=None, lifecycle_state: str=None, layer_protocol_name: str=None, service_interface_point: str=None, capacity: CapacityPac=None, direction: str=None, role: str=None, protection_role: str=None):  # noqa: E501
        """ConnectivityServiceEndPoint - a model defined in Swagger

        :param local_id: The local_id of this ConnectivityServiceEndPoint.  # noqa: E501
        :type local_id: str
        :param name: The name of this ConnectivityServiceEndPoint.  # noqa: E501
        :type name: List[NameAndValue]
        :param administrative_state: The administrative_state of this ConnectivityServiceEndPoint.  # noqa: E501
        :type administrative_state: str
        :param operational_state: The operational_state of this ConnectivityServiceEndPoint.  # noqa: E501
        :type operational_state: str
        :param lifecycle_state: The lifecycle_state of this ConnectivityServiceEndPoint.  # noqa: E501
        :type lifecycle_state: str
        :param layer_protocol_name: The layer_protocol_name of this ConnectivityServiceEndPoint.  # noqa: E501
        :type layer_protocol_name: str
        :param service_interface_point: The service_interface_point of this ConnectivityServiceEndPoint.  # noqa: E501
        :type service_interface_point: str
        :param capacity: The capacity of this ConnectivityServiceEndPoint.  # noqa: E501
        :type capacity: CapacityPac
        :param direction: The direction of this ConnectivityServiceEndPoint.  # noqa: E501
        :type direction: str
        :param role: The role of this ConnectivityServiceEndPoint.  # noqa: E501
        :type role: str
        :param protection_role: The protection_role of this ConnectivityServiceEndPoint.  # noqa: E501
        :type protection_role: str
        """
        self.swagger_types = {
            'local_id': str,
            'name': List[NameAndValue],
            'administrative_state': str,
            'operational_state': str,
            'lifecycle_state': str,
            'layer_protocol_name': str,
            'service_interface_point': str,
            'capacity': CapacityPac,
            'direction': str,
            'role': str,
            'protection_role': str
        }

        self.attribute_map = {
            'local_id': 'local-id',
            'name': 'name',
            'administrative_state': 'administrative-state',
            'operational_state': 'operational-state',
            'lifecycle_state': 'lifecycle-state',
            'layer_protocol_name': 'layer-protocol-name',
            'service_interface_point': 'service-interface-point',
            'capacity': 'capacity',
            'direction': 'direction',
            'role': 'role',
            'protection_role': 'protection-role'
        }

        self._local_id = local_id
        self._name = name
        self._administrative_state = administrative_state
        self._operational_state = operational_state
        self._lifecycle_state = lifecycle_state
        self._layer_protocol_name = layer_protocol_name
        self._service_interface_point = service_interface_point
        self._capacity = capacity
        self._direction = direction
        self._role = role
        self._protection_role = protection_role

    @classmethod
    def from_dict(cls, dikt) -> 'ConnectivityServiceEndPoint':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The connectivity-service-end-point of this ConnectivityServiceEndPoint.  # noqa: E501
        :rtype: ConnectivityServiceEndPoint
        """
        return util.deserialize_model(dikt, cls)

    @property
    def local_id(self) -> str:
        """Gets the local_id of this ConnectivityServiceEndPoint.


        :return: The local_id of this ConnectivityServiceEndPoint.
        :rtype: str
        """
        return self._local_id

    @local_id.setter
    def local_id(self, local_id: str):
        """Sets the local_id of this ConnectivityServiceEndPoint.


        :param local_id: The local_id of this ConnectivityServiceEndPoint.
        :type local_id: str
        """

        self._local_id = local_id

    @property
    def name(self) -> List[NameAndValue]:
        """Gets the name of this ConnectivityServiceEndPoint.

        List of names. A property of an entity with a value that is unique in some namespace but may change during the life of the entity. A name carries no semantics with respect to the purpose of the entity.  # noqa: E501

        :return: The name of this ConnectivityServiceEndPoint.
        :rtype: List[NameAndValue]
        """
        return self._name

    @name.setter
    def name(self, name: List[NameAndValue]):
        """Sets the name of this ConnectivityServiceEndPoint.

        List of names. A property of an entity with a value that is unique in some namespace but may change during the life of the entity. A name carries no semantics with respect to the purpose of the entity.  # noqa: E501

        :param name: The name of this ConnectivityServiceEndPoint.
        :type name: List[NameAndValue]
        """

        self._name = name

    @property
    def administrative_state(self) -> str:
        """Gets the administrative_state of this ConnectivityServiceEndPoint.


        :return: The administrative_state of this ConnectivityServiceEndPoint.
        :rtype: str
        """
        return self._administrative_state

    @administrative_state.setter
    def administrative_state(self, administrative_state: str):
        """Sets the administrative_state of this ConnectivityServiceEndPoint.


        :param administrative_state: The administrative_state of this ConnectivityServiceEndPoint.
        :type administrative_state: str
        """
        allowed_values = ["LOCKED", "UNLOCKED"]  # noqa: E501
        if administrative_state not in allowed_values:
            raise ValueError(
                "Invalid value for `administrative_state` ({0}), must be one of {1}"
                .format(administrative_state, allowed_values)
            )

        self._administrative_state = administrative_state

    @property
    def operational_state(self) -> str:
        """Gets the operational_state of this ConnectivityServiceEndPoint.


        :return: The operational_state of this ConnectivityServiceEndPoint.
        :rtype: str
        """
        return self._operational_state

    @operational_state.setter
    def operational_state(self, operational_state: str):
        """Sets the operational_state of this ConnectivityServiceEndPoint.


        :param operational_state: The operational_state of this ConnectivityServiceEndPoint.
        :type operational_state: str
        """
        allowed_values = ["DISABLED", "ENABLED"]  # noqa: E501
        if operational_state not in allowed_values:
            raise ValueError(
                "Invalid value for `operational_state` ({0}), must be one of {1}"
                .format(operational_state, allowed_values)
            )

        self._operational_state = operational_state

    @property
    def lifecycle_state(self) -> str:
        """Gets the lifecycle_state of this ConnectivityServiceEndPoint.


        :return: The lifecycle_state of this ConnectivityServiceEndPoint.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state: str):
        """Sets the lifecycle_state of this ConnectivityServiceEndPoint.


        :param lifecycle_state: The lifecycle_state of this ConnectivityServiceEndPoint.
        :type lifecycle_state: str
        """
        allowed_values = ["PLANNED", "POTENTIAL_AVAILABLE", "POTENTIAL_BUSY", "INSTALLED", "PENDING_REMOVAL"]  # noqa: E501
        if lifecycle_state not in allowed_values:
            raise ValueError(
                "Invalid value for `lifecycle_state` ({0}), must be one of {1}"
                .format(lifecycle_state, allowed_values)
            )

        self._lifecycle_state = lifecycle_state

    @property
    def layer_protocol_name(self) -> str:
        """Gets the layer_protocol_name of this ConnectivityServiceEndPoint.


        :return: The layer_protocol_name of this ConnectivityServiceEndPoint.
        :rtype: str
        """
        return self._layer_protocol_name

    @layer_protocol_name.setter
    def layer_protocol_name(self, layer_protocol_name: str):
        """Sets the layer_protocol_name of this ConnectivityServiceEndPoint.


        :param layer_protocol_name: The layer_protocol_name of this ConnectivityServiceEndPoint.
        :type layer_protocol_name: str
        """
        allowed_values = ["OTSiA", "OCH", "OTU", "ODU", "ETH", "ETY"]  # noqa: E501
        if layer_protocol_name not in allowed_values:
            raise ValueError(
                "Invalid value for `layer_protocol_name` ({0}), must be one of {1}"
                .format(layer_protocol_name, allowed_values)
            )

        self._layer_protocol_name = layer_protocol_name

    @property
    def service_interface_point(self) -> str:
        """Gets the service_interface_point of this ConnectivityServiceEndPoint.


        :return: The service_interface_point of this ConnectivityServiceEndPoint.
        :rtype: str
        """
        return self._service_interface_point

    @service_interface_point.setter
    def service_interface_point(self, service_interface_point: str):
        """Sets the service_interface_point of this ConnectivityServiceEndPoint.


        :param service_interface_point: The service_interface_point of this ConnectivityServiceEndPoint.
        :type service_interface_point: str
        """

        self._service_interface_point = service_interface_point

    @property
    def capacity(self) -> CapacityPac:
        """Gets the capacity of this ConnectivityServiceEndPoint.


        :return: The capacity of this ConnectivityServiceEndPoint.
        :rtype: CapacityPac
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity: CapacityPac):
        """Sets the capacity of this ConnectivityServiceEndPoint.


        :param capacity: The capacity of this ConnectivityServiceEndPoint.
        :type capacity: CapacityPac
        """

        self._capacity = capacity

    @property
    def direction(self) -> str:
        """Gets the direction of this ConnectivityServiceEndPoint.

        The orientation of defined flow at the EndPoint.  # noqa: E501

        :return: The direction of this ConnectivityServiceEndPoint.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction: str):
        """Sets the direction of this ConnectivityServiceEndPoint.

        The orientation of defined flow at the EndPoint.  # noqa: E501

        :param direction: The direction of this ConnectivityServiceEndPoint.
        :type direction: str
        """
        allowed_values = ["BIDIRECTIONAL", "INPUT", "OUTPUT", "UNIDENTIFIED_OR_UNKNOWN"]  # noqa: E501
        if direction not in allowed_values:
            raise ValueError(
                "Invalid value for `direction` ({0}), must be one of {1}"
                .format(direction, allowed_values)
            )

        self._direction = direction

    @property
    def role(self) -> str:
        """Gets the role of this ConnectivityServiceEndPoint.

        Each EP of the FC has a role (e.g., working, protection, protected, symmetric, hub, spoke, leaf, root)  in the context of the FC with respect to the FC function.   # noqa: E501

        :return: The role of this ConnectivityServiceEndPoint.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role: str):
        """Sets the role of this ConnectivityServiceEndPoint.

        Each EP of the FC has a role (e.g., working, protection, protected, symmetric, hub, spoke, leaf, root)  in the context of the FC with respect to the FC function.   # noqa: E501

        :param role: The role of this ConnectivityServiceEndPoint.
        :type role: str
        """
        allowed_values = ["SYMMETRIC", "ROOT", "LEAF", "TRUNK", "UNKNOWN"]  # noqa: E501
        if role not in allowed_values:
            raise ValueError(
                "Invalid value for `role` ({0}), must be one of {1}"
                .format(role, allowed_values)
            )

        self._role = role

    @property
    def protection_role(self) -> str:
        """Gets the protection_role of this ConnectivityServiceEndPoint.

        To specify the protection role of this Port when create or update ConnectivityService.  # noqa: E501

        :return: The protection_role of this ConnectivityServiceEndPoint.
        :rtype: str
        """
        return self._protection_role

    @protection_role.setter
    def protection_role(self, protection_role: str):
        """Sets the protection_role of this ConnectivityServiceEndPoint.

        To specify the protection role of this Port when create or update ConnectivityService.  # noqa: E501

        :param protection_role: The protection_role of this ConnectivityServiceEndPoint.
        :type protection_role: str
        """
        allowed_values = ["WORK", "PROTECT", "PROTECTED", "NA", "WORK_RESTORE", "PROTECT_RESTORE"]  # noqa: E501
        if protection_role not in allowed_values:
            raise ValueError(
                "Invalid value for `protection_role` ({0}), must be one of {1}"
                .format(protection_role, allowed_values)
            )

        self._protection_role = protection_role