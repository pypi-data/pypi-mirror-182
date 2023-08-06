"""_7311.py

StraightBevelGearSetAdvancedSystemDeflection
"""


from typing import List

from mastapy.system_model.part_model.gears import _2500
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6891
from mastapy.gears.rating.straight_bevel import _391
from mastapy.system_model.analyses_and_results.system_deflections import _2764
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7309, _7310, _7216
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_SET_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'StraightBevelGearSetAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelGearSetAdvancedSystemDeflection',)


class StraightBevelGearSetAdvancedSystemDeflection(_7216.BevelGearSetAdvancedSystemDeflection):
    """StraightBevelGearSetAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_SET_ADVANCED_SYSTEM_DEFLECTION

    def __init__(self, instance_to_wrap: 'StraightBevelGearSetAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2500.StraightBevelGearSet':
        """StraightBevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6891.StraightBevelGearSetLoadCase':
        """StraightBevelGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating(self) -> '_391.StraightBevelGearSetRating':
        """StraightBevelGearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis(self) -> '_391.StraightBevelGearSetRating':
        """StraightBevelGearSetRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_system_deflection_results(self) -> 'List[_2764.StraightBevelGearSetSystemDeflection]':
        """List[StraightBevelGearSetSystemDeflection]: 'AssemblySystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblySystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def straight_bevel_gears_advanced_system_deflection(self) -> 'List[_7309.StraightBevelGearAdvancedSystemDeflection]':
        """List[StraightBevelGearAdvancedSystemDeflection]: 'StraightBevelGearsAdvancedSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelGearsAdvancedSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def straight_bevel_meshes_advanced_system_deflection(self) -> 'List[_7310.StraightBevelGearMeshAdvancedSystemDeflection]':
        """List[StraightBevelGearMeshAdvancedSystemDeflection]: 'StraightBevelMeshesAdvancedSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelMeshesAdvancedSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
