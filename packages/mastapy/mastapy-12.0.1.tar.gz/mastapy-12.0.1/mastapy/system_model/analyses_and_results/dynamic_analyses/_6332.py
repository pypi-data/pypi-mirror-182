﻿"""_6332.py

WormGearSetDynamicAnalysis
"""


from typing import List

from mastapy.system_model.part_model.gears import _2504
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6911
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6330, _6331, _6267
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_SET_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses', 'WormGearSetDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearSetDynamicAnalysis',)


class WormGearSetDynamicAnalysis(_6267.GearSetDynamicAnalysis):
    """WormGearSetDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_SET_DYNAMIC_ANALYSIS

    def __init__(self, instance_to_wrap: 'WormGearSetDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2504.WormGearSet':
        """WormGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6911.WormGearSetLoadCase':
        """WormGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def worm_gears_dynamic_analysis(self) -> 'List[_6330.WormGearDynamicAnalysis]':
        """List[WormGearDynamicAnalysis]: 'WormGearsDynamicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormGearsDynamicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def worm_meshes_dynamic_analysis(self) -> 'List[_6331.WormGearMeshDynamicAnalysis]':
        """List[WormGearMeshDynamicAnalysis]: 'WormMeshesDynamicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormMeshesDynamicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
