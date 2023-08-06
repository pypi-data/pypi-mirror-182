﻿"""_2558.py

SynchroniserSleeve
"""


from mastapy._internal import constructor
from mastapy.system_model.part_model.couplings import _2557
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_SLEEVE = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'SynchroniserSleeve')


__docformat__ = 'restructuredtext en'
__all__ = ('SynchroniserSleeve',)


class SynchroniserSleeve(_2557.SynchroniserPart):
    """SynchroniserSleeve

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_SLEEVE

    def __init__(self, instance_to_wrap: 'SynchroniserSleeve.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def hub_bore(self) -> 'float':
        """float: 'HubBore' is the original name of this property."""

        temp = self.wrapped.HubBore

        if temp is None:
            return 0.0

        return temp

    @hub_bore.setter
    def hub_bore(self, value: 'float'):
        self.wrapped.HubBore = float(value) if value else 0.0

    @property
    def hub_height(self) -> 'float':
        """float: 'HubHeight' is the original name of this property."""

        temp = self.wrapped.HubHeight

        if temp is None:
            return 0.0

        return temp

    @hub_height.setter
    def hub_height(self, value: 'float'):
        self.wrapped.HubHeight = float(value) if value else 0.0

    @property
    def hub_width(self) -> 'float':
        """float: 'HubWidth' is the original name of this property."""

        temp = self.wrapped.HubWidth

        if temp is None:
            return 0.0

        return temp

    @hub_width.setter
    def hub_width(self, value: 'float'):
        self.wrapped.HubWidth = float(value) if value else 0.0

    @property
    def sleeve_outer_diameter(self) -> 'float':
        """float: 'SleeveOuterDiameter' is the original name of this property."""

        temp = self.wrapped.SleeveOuterDiameter

        if temp is None:
            return 0.0

        return temp

    @sleeve_outer_diameter.setter
    def sleeve_outer_diameter(self, value: 'float'):
        self.wrapped.SleeveOuterDiameter = float(value) if value else 0.0

    @property
    def sleeve_selection_height(self) -> 'float':
        """float: 'SleeveSelectionHeight' is the original name of this property."""

        temp = self.wrapped.SleeveSelectionHeight

        if temp is None:
            return 0.0

        return temp

    @sleeve_selection_height.setter
    def sleeve_selection_height(self, value: 'float'):
        self.wrapped.SleeveSelectionHeight = float(value) if value else 0.0

    @property
    def sleeve_selection_width(self) -> 'float':
        """float: 'SleeveSelectionWidth' is the original name of this property."""

        temp = self.wrapped.SleeveSelectionWidth

        if temp is None:
            return 0.0

        return temp

    @sleeve_selection_width.setter
    def sleeve_selection_width(self, value: 'float'):
        self.wrapped.SleeveSelectionWidth = float(value) if value else 0.0

    @property
    def sleeve_width(self) -> 'float':
        """float: 'SleeveWidth' is the original name of this property."""

        temp = self.wrapped.SleeveWidth

        if temp is None:
            return 0.0

        return temp

    @sleeve_width.setter
    def sleeve_width(self, value: 'float'):
        self.wrapped.SleeveWidth = float(value) if value else 0.0
