"""_6271.py

HypoidGearSetDynamicAnalysis
"""


from typing import List

from mastapy.system_model.part_model.gears import _2487
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6834
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6269, _6270, _6212
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_SET_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses', 'HypoidGearSetDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('HypoidGearSetDynamicAnalysis',)


class HypoidGearSetDynamicAnalysis(_6212.AGMAGleasonConicalGearSetDynamicAnalysis):
    """HypoidGearSetDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_SET_DYNAMIC_ANALYSIS

    def __init__(self, instance_to_wrap: 'HypoidGearSetDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2487.HypoidGearSet':
        """HypoidGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6834.HypoidGearSetLoadCase':
        """HypoidGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def hypoid_gears_dynamic_analysis(self) -> 'List[_6269.HypoidGearDynamicAnalysis]':
        """List[HypoidGearDynamicAnalysis]: 'HypoidGearsDynamicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HypoidGearsDynamicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def hypoid_meshes_dynamic_analysis(self) -> 'List[_6270.HypoidGearMeshDynamicAnalysis]':
        """List[HypoidGearMeshDynamicAnalysis]: 'HypoidMeshesDynamicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HypoidMeshesDynamicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
