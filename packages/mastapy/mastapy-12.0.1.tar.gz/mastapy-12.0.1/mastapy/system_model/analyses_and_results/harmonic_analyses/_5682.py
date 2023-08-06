"""_5682.py

FaceGearHarmonicAnalysis
"""


from mastapy.system_model.part_model.gears import _2480
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6811
from mastapy.system_model.analyses_and_results.system_deflections import _2703
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5688
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'FaceGearHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearHarmonicAnalysis',)


class FaceGearHarmonicAnalysis(_5688.GearHarmonicAnalysis):
    """FaceGearHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_HARMONIC_ANALYSIS

    def __init__(self, instance_to_wrap: 'FaceGearHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2480.FaceGear':
        """FaceGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6811.FaceGearLoadCase':
        """FaceGearLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2703.FaceGearSystemDeflection':
        """FaceGearSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
