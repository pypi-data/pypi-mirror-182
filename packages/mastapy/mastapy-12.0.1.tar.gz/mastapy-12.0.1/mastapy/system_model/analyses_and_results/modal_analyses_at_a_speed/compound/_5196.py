"""_5196.py

BevelDifferentialGearCompoundModalAnalysisAtASpeed
"""


from typing import List

from mastapy.system_model.part_model.gears import _2467, _2469, _2470
from mastapy._internal import constructor, conversion
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5068
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5201
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound', 'BevelDifferentialGearCompoundModalAnalysisAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelDifferentialGearCompoundModalAnalysisAtASpeed',)


class BevelDifferentialGearCompoundModalAnalysisAtASpeed(_5201.BevelGearCompoundModalAnalysisAtASpeed):
    """BevelDifferentialGearCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED

    def __init__(self, instance_to_wrap: 'BevelDifferentialGearCompoundModalAnalysisAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2467.BevelDifferentialGear':
        """BevelDifferentialGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2467.BevelDifferentialGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to BevelDifferentialGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_5068.BevelDifferentialGearModalAnalysisAtASpeed]':
        """List[BevelDifferentialGearModalAnalysisAtASpeed]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_5068.BevelDifferentialGearModalAnalysisAtASpeed]':
        """List[BevelDifferentialGearModalAnalysisAtASpeed]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
