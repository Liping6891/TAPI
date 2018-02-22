# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.name_and_value import NameAndValue  # noqa: F401,E501
from tapi_server.models.resilience_constraint import ResilienceConstraint  # noqa: F401,E501
from tapi_server.models.resilience_type import ResilienceType  # noqa: F401,E501
from tapi_server.models.resource_spec import ResourceSpec  # noqa: F401,E501
from tapi_server.models.switch import Switch  # noqa: F401,E501
from tapi_server import util


class SwitchControl(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, uuid: str=None, name: List[NameAndValue]=None, resilience_type: ResilienceType=None, restoration_coordinate_type: str=None, restore_priority: str=None, reversion_mode: str=None, wait_to_revert_time: str=None, hold_off_time: str=None, is_lock_out: bool=None, is_frozen: bool=None, is_coordinated_switching_both_ends: bool=None, max_switch_times: str=None, layer_protocol: str=None, sub_switch_control: List[str]=None, switch: List[Switch]=None):  # noqa: E501
        """SwitchControl - a model defined in Swagger

        :param uuid: The uuid of this SwitchControl.  # noqa: E501
        :type uuid: str
        :param name: The name of this SwitchControl.  # noqa: E501
        :type name: List[NameAndValue]
        :param resilience_type: The resilience_type of this SwitchControl.  # noqa: E501
        :type resilience_type: ResilienceType
        :param restoration_coordinate_type: The restoration_coordinate_type of this SwitchControl.  # noqa: E501
        :type restoration_coordinate_type: str
        :param restore_priority: The restore_priority of this SwitchControl.  # noqa: E501
        :type restore_priority: str
        :param reversion_mode: The reversion_mode of this SwitchControl.  # noqa: E501
        :type reversion_mode: str
        :param wait_to_revert_time: The wait_to_revert_time of this SwitchControl.  # noqa: E501
        :type wait_to_revert_time: str
        :param hold_off_time: The hold_off_time of this SwitchControl.  # noqa: E501
        :type hold_off_time: str
        :param is_lock_out: The is_lock_out of this SwitchControl.  # noqa: E501
        :type is_lock_out: bool
        :param is_frozen: The is_frozen of this SwitchControl.  # noqa: E501
        :type is_frozen: bool
        :param is_coordinated_switching_both_ends: The is_coordinated_switching_both_ends of this SwitchControl.  # noqa: E501
        :type is_coordinated_switching_both_ends: bool
        :param max_switch_times: The max_switch_times of this SwitchControl.  # noqa: E501
        :type max_switch_times: str
        :param layer_protocol: The layer_protocol of this SwitchControl.  # noqa: E501
        :type layer_protocol: str
        :param sub_switch_control: The sub_switch_control of this SwitchControl.  # noqa: E501
        :type sub_switch_control: List[str]
        :param switch: The switch of this SwitchControl.  # noqa: E501
        :type switch: List[Switch]
        """
        self.swagger_types = {
            'uuid': str,
            'name': List[NameAndValue],
            'resilience_type': ResilienceType,
            'restoration_coordinate_type': str,
            'restore_priority': str,
            'reversion_mode': str,
            'wait_to_revert_time': str,
            'hold_off_time': str,
            'is_lock_out': bool,
            'is_frozen': bool,
            'is_coordinated_switching_both_ends': bool,
            'max_switch_times': str,
            'layer_protocol': str,
            'sub_switch_control': List[str],
            'switch': List[Switch]
        }

        self.attribute_map = {
            'uuid': 'uuid',
            'name': 'name',
            'resilience_type': 'resilience-type',
            'restoration_coordinate_type': 'restoration-coordinate-type',
            'restore_priority': 'restore-priority',
            'reversion_mode': 'reversion-mode',
            'wait_to_revert_time': 'wait-to-revert-time',
            'hold_off_time': 'hold-off-time',
            'is_lock_out': 'is-lock-out',
            'is_frozen': 'is-frozen',
            'is_coordinated_switching_both_ends': 'is-coordinated-switching-both-ends',
            'max_switch_times': 'max-switch-times',
            'layer_protocol': 'layer-protocol',
            'sub_switch_control': 'sub-switch-control',
            'switch': 'switch'
        }

        self._uuid = uuid
        self._name = name
        self._resilience_type = resilience_type
        self._restoration_coordinate_type = restoration_coordinate_type
        self._restore_priority = restore_priority
        self._reversion_mode = reversion_mode
        self._wait_to_revert_time = wait_to_revert_time
        self._hold_off_time = hold_off_time
        self._is_lock_out = is_lock_out
        self._is_frozen = is_frozen
        self._is_coordinated_switching_both_ends = is_coordinated_switching_both_ends
        self._max_switch_times = max_switch_times
        self._layer_protocol = layer_protocol
        self._sub_switch_control = sub_switch_control
        self._switch = switch

    @classmethod
    def from_dict(cls, dikt) -> 'SwitchControl':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The switch-control of this SwitchControl.  # noqa: E501
        :rtype: SwitchControl
        """
        return util.deserialize_model(dikt, cls)

    @property
    def uuid(self) -> str:
        """Gets the uuid of this SwitchControl.

        UUID: An identifier that is universally unique within an identifier space, where the identifier space is itself globally unique, and immutable. An UUID carries no semantics with respect to the purpose or state of the entity. UUID here uses string representation as defined in RFC 4122.  The canonical representation uses lowercase characters. Pattern: [0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-' + '[0-9a-fA-F]{4}-[0-9a-fA-F]{12}  Example of a UUID in string representation: f81d4fae-7dec-11d0-a765-00a0c91e6bf6  # noqa: E501

        :return: The uuid of this SwitchControl.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid: str):
        """Sets the uuid of this SwitchControl.

        UUID: An identifier that is universally unique within an identifier space, where the identifier space is itself globally unique, and immutable. An UUID carries no semantics with respect to the purpose or state of the entity. UUID here uses string representation as defined in RFC 4122.  The canonical representation uses lowercase characters. Pattern: [0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-' + '[0-9a-fA-F]{4}-[0-9a-fA-F]{12}  Example of a UUID in string representation: f81d4fae-7dec-11d0-a765-00a0c91e6bf6  # noqa: E501

        :param uuid: The uuid of this SwitchControl.
        :type uuid: str
        """

        self._uuid = uuid

    @property
    def name(self) -> List[NameAndValue]:
        """Gets the name of this SwitchControl.

        List of names. A property of an entity with a value that is unique in some namespace but may change during the life of the entity. A name carries no semantics with respect to the purpose of the entity.  # noqa: E501

        :return: The name of this SwitchControl.
        :rtype: List[NameAndValue]
        """
        return self._name

    @name.setter
    def name(self, name: List[NameAndValue]):
        """Sets the name of this SwitchControl.

        List of names. A property of an entity with a value that is unique in some namespace but may change during the life of the entity. A name carries no semantics with respect to the purpose of the entity.  # noqa: E501

        :param name: The name of this SwitchControl.
        :type name: List[NameAndValue]
        """

        self._name = name

    @property
    def resilience_type(self) -> ResilienceType:
        """Gets the resilience_type of this SwitchControl.


        :return: The resilience_type of this SwitchControl.
        :rtype: ResilienceType
        """
        return self._resilience_type

    @resilience_type.setter
    def resilience_type(self, resilience_type: ResilienceType):
        """Sets the resilience_type of this SwitchControl.


        :param resilience_type: The resilience_type of this SwitchControl.
        :type resilience_type: ResilienceType
        """

        self._resilience_type = resilience_type

    @property
    def restoration_coordinate_type(self) -> str:
        """Gets the restoration_coordinate_type of this SwitchControl.

         The coordination mechanism between multi-layers.  # noqa: E501

        :return: The restoration_coordinate_type of this SwitchControl.
        :rtype: str
        """
        return self._restoration_coordinate_type

    @restoration_coordinate_type.setter
    def restoration_coordinate_type(self, restoration_coordinate_type: str):
        """Sets the restoration_coordinate_type of this SwitchControl.

         The coordination mechanism between multi-layers.  # noqa: E501

        :param restoration_coordinate_type: The restoration_coordinate_type of this SwitchControl.
        :type restoration_coordinate_type: str
        """
        allowed_values = ["NO_COORDINATE", "HOLD_OFF_TIME", "WAIT_FOR_NOTIFICATION"]  # noqa: E501
        if restoration_coordinate_type not in allowed_values:
            raise ValueError(
                "Invalid value for `restoration_coordinate_type` ({0}), must be one of {1}"
                .format(restoration_coordinate_type, allowed_values)
            )

        self._restoration_coordinate_type = restoration_coordinate_type

    @property
    def restore_priority(self) -> str:
        """Gets the restore_priority of this SwitchControl.


        :return: The restore_priority of this SwitchControl.
        :rtype: str
        """
        return self._restore_priority

    @restore_priority.setter
    def restore_priority(self, restore_priority: str):
        """Sets the restore_priority of this SwitchControl.


        :param restore_priority: The restore_priority of this SwitchControl.
        :type restore_priority: str
        """

        self._restore_priority = restore_priority

    @property
    def reversion_mode(self) -> str:
        """Gets the reversion_mode of this SwitchControl.

        Indcates whether the protection scheme is revertive or non-revertive.  # noqa: E501

        :return: The reversion_mode of this SwitchControl.
        :rtype: str
        """
        return self._reversion_mode

    @reversion_mode.setter
    def reversion_mode(self, reversion_mode: str):
        """Sets the reversion_mode of this SwitchControl.

        Indcates whether the protection scheme is revertive or non-revertive.  # noqa: E501

        :param reversion_mode: The reversion_mode of this SwitchControl.
        :type reversion_mode: str
        """
        allowed_values = ["REVERTIVE", "NON-REVERTIVE"]  # noqa: E501
        if reversion_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `reversion_mode` ({0}), must be one of {1}"
                .format(reversion_mode, allowed_values)
            )

        self._reversion_mode = reversion_mode

    @property
    def wait_to_revert_time(self) -> str:
        """Gets the wait_to_revert_time of this SwitchControl.

        If the protection system is revertive, this attribute specifies the time, in minutes, to wait after a fault clears on a higher priority (preferred) resource before reverting to the preferred resource.  # noqa: E501

        :return: The wait_to_revert_time of this SwitchControl.
        :rtype: str
        """
        return self._wait_to_revert_time

    @wait_to_revert_time.setter
    def wait_to_revert_time(self, wait_to_revert_time: str):
        """Sets the wait_to_revert_time of this SwitchControl.

        If the protection system is revertive, this attribute specifies the time, in minutes, to wait after a fault clears on a higher priority (preferred) resource before reverting to the preferred resource.  # noqa: E501

        :param wait_to_revert_time: The wait_to_revert_time of this SwitchControl.
        :type wait_to_revert_time: str
        """

        self._wait_to_revert_time = wait_to_revert_time

    @property
    def hold_off_time(self) -> str:
        """Gets the hold_off_time of this SwitchControl.

        This attribute indicates the time, in milliseconds, between declaration of signal degrade or signal fail, and the initialization of the protection switching algorithm.  # noqa: E501

        :return: The hold_off_time of this SwitchControl.
        :rtype: str
        """
        return self._hold_off_time

    @hold_off_time.setter
    def hold_off_time(self, hold_off_time: str):
        """Sets the hold_off_time of this SwitchControl.

        This attribute indicates the time, in milliseconds, between declaration of signal degrade or signal fail, and the initialization of the protection switching algorithm.  # noqa: E501

        :param hold_off_time: The hold_off_time of this SwitchControl.
        :type hold_off_time: str
        """

        self._hold_off_time = hold_off_time

    @property
    def is_lock_out(self) -> bool:
        """Gets the is_lock_out of this SwitchControl.

        The resource is configured to temporarily not be available for use in the protection scheme(s) it is part of. This overrides all other protection control states including forced. If the item is locked out then it cannot be used under any circumstances. Note: Only relevant when part of a protection scheme.  # noqa: E501

        :return: The is_lock_out of this SwitchControl.
        :rtype: bool
        """
        return self._is_lock_out

    @is_lock_out.setter
    def is_lock_out(self, is_lock_out: bool):
        """Sets the is_lock_out of this SwitchControl.

        The resource is configured to temporarily not be available for use in the protection scheme(s) it is part of. This overrides all other protection control states including forced. If the item is locked out then it cannot be used under any circumstances. Note: Only relevant when part of a protection scheme.  # noqa: E501

        :param is_lock_out: The is_lock_out of this SwitchControl.
        :type is_lock_out: bool
        """

        self._is_lock_out = is_lock_out

    @property
    def is_frozen(self) -> bool:
        """Gets the is_frozen of this SwitchControl.

        Temporarily prevents any switch action to be taken and, as such, freezes the current state.  Until the freeze is cleared, additional near-end external commands are rejected and fault condition changes and received APS messages are ignored. All administrative controls of any aspect of protection are rejected.  # noqa: E501

        :return: The is_frozen of this SwitchControl.
        :rtype: bool
        """
        return self._is_frozen

    @is_frozen.setter
    def is_frozen(self, is_frozen: bool):
        """Sets the is_frozen of this SwitchControl.

        Temporarily prevents any switch action to be taken and, as such, freezes the current state.  Until the freeze is cleared, additional near-end external commands are rejected and fault condition changes and received APS messages are ignored. All administrative controls of any aspect of protection are rejected.  # noqa: E501

        :param is_frozen: The is_frozen of this SwitchControl.
        :type is_frozen: bool
        """

        self._is_frozen = is_frozen

    @property
    def is_coordinated_switching_both_ends(self) -> bool:
        """Gets the is_coordinated_switching_both_ends of this SwitchControl.

        Is operating such that switching at both ends of each flow acorss the FC is coordinated at both ingress and egress ends.  # noqa: E501

        :return: The is_coordinated_switching_both_ends of this SwitchControl.
        :rtype: bool
        """
        return self._is_coordinated_switching_both_ends

    @is_coordinated_switching_both_ends.setter
    def is_coordinated_switching_both_ends(self, is_coordinated_switching_both_ends: bool):
        """Sets the is_coordinated_switching_both_ends of this SwitchControl.

        Is operating such that switching at both ends of each flow acorss the FC is coordinated at both ingress and egress ends.  # noqa: E501

        :param is_coordinated_switching_both_ends: The is_coordinated_switching_both_ends of this SwitchControl.
        :type is_coordinated_switching_both_ends: bool
        """

        self._is_coordinated_switching_both_ends = is_coordinated_switching_both_ends

    @property
    def max_switch_times(self) -> str:
        """Gets the max_switch_times of this SwitchControl.

        Used to limit the maximum swtich times. When work fault disappears , and traffic return to the original work path, switch counter reset.  # noqa: E501

        :return: The max_switch_times of this SwitchControl.
        :rtype: str
        """
        return self._max_switch_times

    @max_switch_times.setter
    def max_switch_times(self, max_switch_times: str):
        """Sets the max_switch_times of this SwitchControl.

        Used to limit the maximum swtich times. When work fault disappears , and traffic return to the original work path, switch counter reset.  # noqa: E501

        :param max_switch_times: The max_switch_times of this SwitchControl.
        :type max_switch_times: str
        """

        self._max_switch_times = max_switch_times

    @property
    def layer_protocol(self) -> str:
        """Gets the layer_protocol of this SwitchControl.

        Indicate which layer this resilience parameters package configured for.  # noqa: E501

        :return: The layer_protocol of this SwitchControl.
        :rtype: str
        """
        return self._layer_protocol

    @layer_protocol.setter
    def layer_protocol(self, layer_protocol: str):
        """Sets the layer_protocol of this SwitchControl.

        Indicate which layer this resilience parameters package configured for.  # noqa: E501

        :param layer_protocol: The layer_protocol of this SwitchControl.
        :type layer_protocol: str
        """
        allowed_values = ["OTSiA", "OCH", "OTU", "ODU", "ETH", "ETY", "DSR"]  # noqa: E501
        if layer_protocol not in allowed_values:
            raise ValueError(
                "Invalid value for `layer_protocol` ({0}), must be one of {1}"
                .format(layer_protocol, allowed_values)
            )

        self._layer_protocol = layer_protocol

    @property
    def sub_switch_control(self) -> List[str]:
        """Gets the sub_switch_control of this SwitchControl.


        :return: The sub_switch_control of this SwitchControl.
        :rtype: List[str]
        """
        return self._sub_switch_control

    @sub_switch_control.setter
    def sub_switch_control(self, sub_switch_control: List[str]):
        """Sets the sub_switch_control of this SwitchControl.


        :param sub_switch_control: The sub_switch_control of this SwitchControl.
        :type sub_switch_control: List[str]
        """

        self._sub_switch_control = sub_switch_control

    @property
    def switch(self) -> List[Switch]:
        """Gets the switch of this SwitchControl.


        :return: The switch of this SwitchControl.
        :rtype: List[Switch]
        """
        return self._switch

    @switch.setter
    def switch(self, switch: List[Switch]):
        """Sets the switch of this SwitchControl.


        :param switch: The switch of this SwitchControl.
        :type switch: List[Switch]
        """

        self._switch = switch
