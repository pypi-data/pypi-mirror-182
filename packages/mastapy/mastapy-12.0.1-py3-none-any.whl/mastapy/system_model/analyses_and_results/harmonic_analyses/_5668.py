﻿"""_5668.py

DatumHarmonicAnalysis
"""


from mastapy.system_model.part_model import _2401
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6796
from mastapy.system_model.analyses_and_results.system_deflections import _2698
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5642
from mastapy._internal.python_net import python_net_import

_DATUM_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'DatumHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('DatumHarmonicAnalysis',)


class DatumHarmonicAnalysis(_5642.ComponentHarmonicAnalysis):
    """DatumHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _DATUM_HARMONIC_ANALYSIS

    def __init__(self, instance_to_wrap: 'DatumHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2401.Datum':
        """Datum: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6796.DatumLoadCase':
        """DatumLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2698.DatumSystemDeflection':
        """DatumSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
