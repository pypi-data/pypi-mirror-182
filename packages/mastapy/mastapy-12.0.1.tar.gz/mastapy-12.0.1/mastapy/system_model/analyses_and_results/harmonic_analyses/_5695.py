﻿"""_5695.py

GuideDxfModelHarmonicAnalysis
"""


from mastapy.system_model.part_model import _2408
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6823
from mastapy.system_model.analyses_and_results.system_deflections import _2709
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5642
from mastapy._internal.python_net import python_net_import

_GUIDE_DXF_MODEL_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'GuideDxfModelHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('GuideDxfModelHarmonicAnalysis',)


class GuideDxfModelHarmonicAnalysis(_5642.ComponentHarmonicAnalysis):
    """GuideDxfModelHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _GUIDE_DXF_MODEL_HARMONIC_ANALYSIS

    def __init__(self, instance_to_wrap: 'GuideDxfModelHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2408.GuideDxfModel':
        """GuideDxfModel: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6823.GuideDxfModelLoadCase':
        """GuideDxfModelLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2709.GuideDxfModelSystemDeflection':
        """GuideDxfModelSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
