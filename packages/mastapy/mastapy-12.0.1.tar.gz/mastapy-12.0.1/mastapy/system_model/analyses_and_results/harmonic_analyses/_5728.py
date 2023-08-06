"""_5728.py

PowerLoadHarmonicAnalysis
"""


from mastapy.system_model.part_model import _2425
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6866
from mastapy.system_model.analyses_and_results.system_deflections import _2739
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5767
from mastapy._internal.python_net import python_net_import

_POWER_LOAD_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'PowerLoadHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('PowerLoadHarmonicAnalysis',)


class PowerLoadHarmonicAnalysis(_5767.VirtualComponentHarmonicAnalysis):
    """PowerLoadHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _POWER_LOAD_HARMONIC_ANALYSIS

    def __init__(self, instance_to_wrap: 'PowerLoadHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2425.PowerLoad':
        """PowerLoad: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6866.PowerLoadLoadCase':
        """PowerLoadLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2739.PowerLoadSystemDeflection':
        """PowerLoadSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
