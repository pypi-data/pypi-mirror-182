﻿"""_3740.py

ConceptGearSetStabilityAnalysis
"""


from typing import List

from mastapy.system_model.part_model.gears import _2474
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6770
from mastapy.system_model.analyses_and_results.stability_analyses import _3741, _3739, _3770
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_SET_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses', 'ConceptGearSetStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptGearSetStabilityAnalysis',)


class ConceptGearSetStabilityAnalysis(_3770.GearSetStabilityAnalysis):
    """ConceptGearSetStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_SET_STABILITY_ANALYSIS

    def __init__(self, instance_to_wrap: 'ConceptGearSetStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2474.ConceptGearSet':
        """ConceptGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6770.ConceptGearSetLoadCase':
        """ConceptGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def concept_gears_stability_analysis(self) -> 'List[_3741.ConceptGearStabilityAnalysis]':
        """List[ConceptGearStabilityAnalysis]: 'ConceptGearsStabilityAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConceptGearsStabilityAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def concept_meshes_stability_analysis(self) -> 'List[_3739.ConceptGearMeshStabilityAnalysis]':
        """List[ConceptGearMeshStabilityAnalysis]: 'ConceptMeshesStabilityAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConceptMeshesStabilityAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
