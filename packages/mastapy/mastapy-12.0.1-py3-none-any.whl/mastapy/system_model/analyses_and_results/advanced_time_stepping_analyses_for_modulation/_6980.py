﻿"""_6980.py

CycloidalDiscAdvancedTimeSteppingAnalysisForModulation
"""


from mastapy.system_model.part_model.cycloidal import _2521
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6786
from mastapy.system_model.analyses_and_results.system_deflections import _2685
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6933
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation', 'CycloidalDiscAdvancedTimeSteppingAnalysisForModulation')


__docformat__ = 'restructuredtext en'
__all__ = ('CycloidalDiscAdvancedTimeSteppingAnalysisForModulation',)


class CycloidalDiscAdvancedTimeSteppingAnalysisForModulation(_6933.AbstractShaftAdvancedTimeSteppingAnalysisForModulation):
    """CycloidalDiscAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    def __init__(self, instance_to_wrap: 'CycloidalDiscAdvancedTimeSteppingAnalysisForModulation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2521.CycloidalDisc':
        """CycloidalDisc: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6786.CycloidalDiscLoadCase':
        """CycloidalDiscLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2685.CycloidalDiscSystemDeflection':
        """CycloidalDiscSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
