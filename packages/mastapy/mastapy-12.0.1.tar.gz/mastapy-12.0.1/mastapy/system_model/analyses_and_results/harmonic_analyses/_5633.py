﻿"""_5633.py

BevelGearMeshHarmonicAnalysis
"""


from mastapy.system_model.connections_and_sockets.gears import (
    _2256, _2254, _2276, _2278,
    _2280, _2284
)
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.system_deflections import (
    _2653, _2648, _2754, _2760,
    _2763, _2786
)
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5621
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MESH_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'BevelGearMeshHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelGearMeshHarmonicAnalysis',)


class BevelGearMeshHarmonicAnalysis(_5621.AGMAGleasonConicalGearMeshHarmonicAnalysis):
    """BevelGearMeshHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MESH_HARMONIC_ANALYSIS

    def __init__(self, instance_to_wrap: 'BevelGearMeshHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2256.BevelGearMesh':
        """BevelGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        if _2256.BevelGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to BevelGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design_of_type_bevel_differential_gear_mesh(self) -> '_2254.BevelDifferentialGearMesh':
        """BevelDifferentialGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        if _2254.BevelDifferentialGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to BevelDifferentialGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design_of_type_spiral_bevel_gear_mesh(self) -> '_2276.SpiralBevelGearMesh':
        """SpiralBevelGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        if _2276.SpiralBevelGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to SpiralBevelGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design_of_type_straight_bevel_diff_gear_mesh(self) -> '_2278.StraightBevelDiffGearMesh':
        """StraightBevelDiffGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        if _2278.StraightBevelDiffGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to StraightBevelDiffGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design_of_type_straight_bevel_gear_mesh(self) -> '_2280.StraightBevelGearMesh':
        """StraightBevelGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        if _2280.StraightBevelGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to StraightBevelGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design_of_type_zerol_bevel_gear_mesh(self) -> '_2284.ZerolBevelGearMesh':
        """ZerolBevelGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        if _2284.ZerolBevelGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to ZerolBevelGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2653.BevelGearMeshSystemDeflection':
        """BevelGearMeshSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2653.BevelGearMeshSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to BevelGearMeshSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_bevel_differential_gear_mesh_system_deflection(self) -> '_2648.BevelDifferentialGearMeshSystemDeflection':
        """BevelDifferentialGearMeshSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2648.BevelDifferentialGearMeshSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to BevelDifferentialGearMeshSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_spiral_bevel_gear_mesh_system_deflection(self) -> '_2754.SpiralBevelGearMeshSystemDeflection':
        """SpiralBevelGearMeshSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2754.SpiralBevelGearMeshSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to SpiralBevelGearMeshSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_straight_bevel_diff_gear_mesh_system_deflection(self) -> '_2760.StraightBevelDiffGearMeshSystemDeflection':
        """StraightBevelDiffGearMeshSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2760.StraightBevelDiffGearMeshSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to StraightBevelDiffGearMeshSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_straight_bevel_gear_mesh_system_deflection(self) -> '_2763.StraightBevelGearMeshSystemDeflection':
        """StraightBevelGearMeshSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2763.StraightBevelGearMeshSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to StraightBevelGearMeshSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_zerol_bevel_gear_mesh_system_deflection(self) -> '_2786.ZerolBevelGearMeshSystemDeflection':
        """ZerolBevelGearMeshSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2786.ZerolBevelGearMeshSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to ZerolBevelGearMeshSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
