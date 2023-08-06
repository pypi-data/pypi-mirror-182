﻿"""_4573.py

FaceGearSetModalAnalysis
"""


from typing import List

from mastapy.system_model.part_model.gears import _2481
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6813
from mastapy.system_model.analyses_and_results.system_deflections import _2702
from mastapy.system_model.analyses_and_results.modal_analyses import _4572, _4571, _4579
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_SET_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses', 'FaceGearSetModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearSetModalAnalysis',)


class FaceGearSetModalAnalysis(_4579.GearSetModalAnalysis):
    """FaceGearSetModalAnalysis

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_SET_MODAL_ANALYSIS

    def __init__(self, instance_to_wrap: 'FaceGearSetModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2481.FaceGearSet':
        """FaceGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6813.FaceGearSetLoadCase':
        """FaceGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2702.FaceGearSetSystemDeflection':
        """FaceGearSetSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def face_gears_modal_analysis(self) -> 'List[_4572.FaceGearModalAnalysis]':
        """List[FaceGearModalAnalysis]: 'FaceGearsModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceGearsModalAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def face_meshes_modal_analysis(self) -> 'List[_4571.FaceGearMeshModalAnalysis]':
        """List[FaceGearMeshModalAnalysis]: 'FaceMeshesModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceMeshesModalAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
