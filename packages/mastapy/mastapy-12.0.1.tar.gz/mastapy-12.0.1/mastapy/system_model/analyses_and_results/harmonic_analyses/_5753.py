"""_5753.py

StraightBevelGearMeshHarmonicAnalysis
"""


from mastapy.system_model.connections_and_sockets.gears import _2280
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6890
from mastapy.system_model.analyses_and_results.system_deflections import _2763
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5633
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_MESH_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'StraightBevelGearMeshHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelGearMeshHarmonicAnalysis',)


class StraightBevelGearMeshHarmonicAnalysis(_5633.BevelGearMeshHarmonicAnalysis):
    """StraightBevelGearMeshHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_MESH_HARMONIC_ANALYSIS

    def __init__(self, instance_to_wrap: 'StraightBevelGearMeshHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2280.StraightBevelGearMesh':
        """StraightBevelGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6890.StraightBevelGearMeshLoadCase':
        """StraightBevelGearMeshLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2763.StraightBevelGearMeshSystemDeflection':
        """StraightBevelGearMeshSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
