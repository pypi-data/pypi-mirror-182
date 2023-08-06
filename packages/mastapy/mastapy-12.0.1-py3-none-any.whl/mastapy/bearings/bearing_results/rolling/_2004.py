﻿"""_2004.py

LoadedTaperRollerBearingElement
"""


from mastapy._internal import constructor
from mastapy.bearings.bearing_results.rolling import _1984
from mastapy._internal.python_net import python_net_import

_LOADED_TAPER_ROLLER_BEARING_ELEMENT = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'LoadedTaperRollerBearingElement')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedTaperRollerBearingElement',)


class LoadedTaperRollerBearingElement(_1984.LoadedNonBarrelRollerElement):
    """LoadedTaperRollerBearingElement

    This is a mastapy class.
    """

    TYPE = _LOADED_TAPER_ROLLER_BEARING_ELEMENT

    def __init__(self, instance_to_wrap: 'LoadedTaperRollerBearingElement.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def height_of_rib_roller_contact_above_race(self) -> 'float':
        """float: 'HeightOfRibRollerContactAboveRace' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HeightOfRibRollerContactAboveRace

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_rib_stress(self) -> 'float':
        """float: 'MaximumRibStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumRibStress

        if temp is None:
            return 0.0

        return temp
