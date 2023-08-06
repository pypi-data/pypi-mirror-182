"""_4258.py

BoltedJointParametricStudyTool
"""


from typing import List

from mastapy.system_model.part_model import _2396
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6758
from mastapy.system_model.analyses_and_results.system_deflections import _2656
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4355
from mastapy._internal.python_net import python_net_import

_BOLTED_JOINT_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'BoltedJointParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('BoltedJointParametricStudyTool',)


class BoltedJointParametricStudyTool(_4355.SpecialisedAssemblyParametricStudyTool):
    """BoltedJointParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _BOLTED_JOINT_PARAMETRIC_STUDY_TOOL

    def __init__(self, instance_to_wrap: 'BoltedJointParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2396.BoltedJoint':
        """BoltedJoint: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6758.BoltedJointLoadCase':
        """BoltedJointLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_system_deflection_results(self) -> 'List[_2656.BoltedJointSystemDeflection]':
        """List[BoltedJointSystemDeflection]: 'AssemblySystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblySystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
