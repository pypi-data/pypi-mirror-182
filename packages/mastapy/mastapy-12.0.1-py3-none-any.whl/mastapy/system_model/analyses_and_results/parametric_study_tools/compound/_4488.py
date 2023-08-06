﻿"""_4488.py

SpringDamperCompoundParametricStudyTool
"""


from typing import List

from mastapy.system_model.part_model.couplings import _2552
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4361
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4423
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound', 'SpringDamperCompoundParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('SpringDamperCompoundParametricStudyTool',)


class SpringDamperCompoundParametricStudyTool(_4423.CouplingCompoundParametricStudyTool):
    """SpringDamperCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_COMPOUND_PARAMETRIC_STUDY_TOOL

    def __init__(self, instance_to_wrap: 'SpringDamperCompoundParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2552.SpringDamper':
        """SpringDamper: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2552.SpringDamper':
        """SpringDamper: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_4361.SpringDamperParametricStudyTool]':
        """List[SpringDamperParametricStudyTool]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_4361.SpringDamperParametricStudyTool]':
        """List[SpringDamperParametricStudyTool]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
