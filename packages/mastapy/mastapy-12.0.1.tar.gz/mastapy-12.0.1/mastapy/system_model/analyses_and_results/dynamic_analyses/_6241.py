"""_6241.py

ConnectionDynamicAnalysis
"""


from mastapy.system_model.connections_and_sockets import (
    _2225, _2218, _2221, _2222,
    _2226, _2234, _2240, _2245,
    _2248
)
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.connections_and_sockets.gears import (
    _2252, _2254, _2256, _2258,
    _2260, _2262, _2264, _2266,
    _2268, _2271, _2272, _2273,
    _2276, _2278, _2280, _2282,
    _2284
)
from mastapy.system_model.connections_and_sockets.cycloidal import _2288, _2291, _2294
from mastapy.system_model.connections_and_sockets.couplings import (
    _2295, _2297, _2299, _2301,
    _2303, _2305
)
from mastapy.system_model.analyses_and_results.dynamic_analyses import _2578
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2982
from mastapy.system_model.analyses_and_results.stability_analyses import _2582
from mastapy.system_model.analyses_and_results.modal_analyses import _2581
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4849
from mastapy.system_model.analyses_and_results.harmonic_analyses import _2580
from mastapy.system_model.analyses_and_results.analysis_cases import _7465
from mastapy._internal.python_net import python_net_import

_CONNECTION_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses', 'ConnectionDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ConnectionDynamicAnalysis',)


class ConnectionDynamicAnalysis(_7465.ConnectionFEAnalysis):
    """ConnectionDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _CONNECTION_DYNAMIC_ANALYSIS

    def __init__(self, instance_to_wrap: 'ConnectionDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2225.Connection':
        """Connection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2225.Connection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to Connection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_abstract_shaft_to_mountable_component_connection(self) -> '_2218.AbstractShaftToMountableComponentConnection':
        """AbstractShaftToMountableComponentConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2218.AbstractShaftToMountableComponentConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to AbstractShaftToMountableComponentConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_belt_connection(self) -> '_2221.BeltConnection':
        """BeltConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2221.BeltConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to BeltConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_coaxial_connection(self) -> '_2222.CoaxialConnection':
        """CoaxialConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2222.CoaxialConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to CoaxialConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_cvt_belt_connection(self) -> '_2226.CVTBeltConnection':
        """CVTBeltConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2226.CVTBeltConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to CVTBeltConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_inter_mountable_component_connection(self) -> '_2234.InterMountableComponentConnection':
        """InterMountableComponentConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2234.InterMountableComponentConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to InterMountableComponentConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_planetary_connection(self) -> '_2240.PlanetaryConnection':
        """PlanetaryConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2240.PlanetaryConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to PlanetaryConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_rolling_ring_connection(self) -> '_2245.RollingRingConnection':
        """RollingRingConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2245.RollingRingConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to RollingRingConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_shaft_to_mountable_component_connection(self) -> '_2248.ShaftToMountableComponentConnection':
        """ShaftToMountableComponentConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2248.ShaftToMountableComponentConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to ShaftToMountableComponentConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_agma_gleason_conical_gear_mesh(self) -> '_2252.AGMAGleasonConicalGearMesh':
        """AGMAGleasonConicalGearMesh: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2252.AGMAGleasonConicalGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to AGMAGleasonConicalGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_bevel_differential_gear_mesh(self) -> '_2254.BevelDifferentialGearMesh':
        """BevelDifferentialGearMesh: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2254.BevelDifferentialGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to BevelDifferentialGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_bevel_gear_mesh(self) -> '_2256.BevelGearMesh':
        """BevelGearMesh: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2256.BevelGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to BevelGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_concept_gear_mesh(self) -> '_2258.ConceptGearMesh':
        """ConceptGearMesh: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2258.ConceptGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to ConceptGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_conical_gear_mesh(self) -> '_2260.ConicalGearMesh':
        """ConicalGearMesh: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2260.ConicalGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to ConicalGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_cylindrical_gear_mesh(self) -> '_2262.CylindricalGearMesh':
        """CylindricalGearMesh: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2262.CylindricalGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to CylindricalGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_face_gear_mesh(self) -> '_2264.FaceGearMesh':
        """FaceGearMesh: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2264.FaceGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to FaceGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_gear_mesh(self) -> '_2266.GearMesh':
        """GearMesh: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2266.GearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to GearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_hypoid_gear_mesh(self) -> '_2268.HypoidGearMesh':
        """HypoidGearMesh: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2268.HypoidGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to HypoidGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_klingelnberg_cyclo_palloid_conical_gear_mesh(self) -> '_2271.KlingelnbergCycloPalloidConicalGearMesh':
        """KlingelnbergCycloPalloidConicalGearMesh: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2271.KlingelnbergCycloPalloidConicalGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to KlingelnbergCycloPalloidConicalGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_klingelnberg_cyclo_palloid_hypoid_gear_mesh(self) -> '_2272.KlingelnbergCycloPalloidHypoidGearMesh':
        """KlingelnbergCycloPalloidHypoidGearMesh: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2272.KlingelnbergCycloPalloidHypoidGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to KlingelnbergCycloPalloidHypoidGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(self) -> '_2273.KlingelnbergCycloPalloidSpiralBevelGearMesh':
        """KlingelnbergCycloPalloidSpiralBevelGearMesh: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2273.KlingelnbergCycloPalloidSpiralBevelGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to KlingelnbergCycloPalloidSpiralBevelGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_spiral_bevel_gear_mesh(self) -> '_2276.SpiralBevelGearMesh':
        """SpiralBevelGearMesh: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2276.SpiralBevelGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to SpiralBevelGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_straight_bevel_diff_gear_mesh(self) -> '_2278.StraightBevelDiffGearMesh':
        """StraightBevelDiffGearMesh: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2278.StraightBevelDiffGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to StraightBevelDiffGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_straight_bevel_gear_mesh(self) -> '_2280.StraightBevelGearMesh':
        """StraightBevelGearMesh: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2280.StraightBevelGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to StraightBevelGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_worm_gear_mesh(self) -> '_2282.WormGearMesh':
        """WormGearMesh: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2282.WormGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to WormGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_zerol_bevel_gear_mesh(self) -> '_2284.ZerolBevelGearMesh':
        """ZerolBevelGearMesh: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2284.ZerolBevelGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to ZerolBevelGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_cycloidal_disc_central_bearing_connection(self) -> '_2288.CycloidalDiscCentralBearingConnection':
        """CycloidalDiscCentralBearingConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2288.CycloidalDiscCentralBearingConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to CycloidalDiscCentralBearingConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_cycloidal_disc_planetary_bearing_connection(self) -> '_2291.CycloidalDiscPlanetaryBearingConnection':
        """CycloidalDiscPlanetaryBearingConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2291.CycloidalDiscPlanetaryBearingConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to CycloidalDiscPlanetaryBearingConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_ring_pins_to_disc_connection(self) -> '_2294.RingPinsToDiscConnection':
        """RingPinsToDiscConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2294.RingPinsToDiscConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to RingPinsToDiscConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_clutch_connection(self) -> '_2295.ClutchConnection':
        """ClutchConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2295.ClutchConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to ClutchConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_concept_coupling_connection(self) -> '_2297.ConceptCouplingConnection':
        """ConceptCouplingConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2297.ConceptCouplingConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to ConceptCouplingConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_coupling_connection(self) -> '_2299.CouplingConnection':
        """CouplingConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2299.CouplingConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to CouplingConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_part_to_part_shear_coupling_connection(self) -> '_2301.PartToPartShearCouplingConnection':
        """PartToPartShearCouplingConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2301.PartToPartShearCouplingConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to PartToPartShearCouplingConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_spring_damper_connection(self) -> '_2303.SpringDamperConnection':
        """SpringDamperConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2303.SpringDamperConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to SpringDamperConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_torque_converter_connection(self) -> '_2305.TorqueConverterConnection':
        """TorqueConverterConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2305.TorqueConverterConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to TorqueConverterConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design(self) -> '_2225.Connection':
        """Connection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        if _2225.Connection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to Connection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design_of_type_abstract_shaft_to_mountable_component_connection(self) -> '_2218.AbstractShaftToMountableComponentConnection':
        """AbstractShaftToMountableComponentConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        if _2218.AbstractShaftToMountableComponentConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to AbstractShaftToMountableComponentConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design_of_type_belt_connection(self) -> '_2221.BeltConnection':
        """BeltConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        if _2221.BeltConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to BeltConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design_of_type_coaxial_connection(self) -> '_2222.CoaxialConnection':
        """CoaxialConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        if _2222.CoaxialConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to CoaxialConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design_of_type_cvt_belt_connection(self) -> '_2226.CVTBeltConnection':
        """CVTBeltConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        if _2226.CVTBeltConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to CVTBeltConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design_of_type_inter_mountable_component_connection(self) -> '_2234.InterMountableComponentConnection':
        """InterMountableComponentConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        if _2234.InterMountableComponentConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to InterMountableComponentConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design_of_type_planetary_connection(self) -> '_2240.PlanetaryConnection':
        """PlanetaryConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        if _2240.PlanetaryConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to PlanetaryConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design_of_type_rolling_ring_connection(self) -> '_2245.RollingRingConnection':
        """RollingRingConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        if _2245.RollingRingConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to RollingRingConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design_of_type_shaft_to_mountable_component_connection(self) -> '_2248.ShaftToMountableComponentConnection':
        """ShaftToMountableComponentConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        if _2248.ShaftToMountableComponentConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to ShaftToMountableComponentConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design_of_type_agma_gleason_conical_gear_mesh(self) -> '_2252.AGMAGleasonConicalGearMesh':
        """AGMAGleasonConicalGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        if _2252.AGMAGleasonConicalGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to AGMAGleasonConicalGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

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
    def connection_design_of_type_bevel_gear_mesh(self) -> '_2256.BevelGearMesh':
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
    def connection_design_of_type_concept_gear_mesh(self) -> '_2258.ConceptGearMesh':
        """ConceptGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        if _2258.ConceptGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to ConceptGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design_of_type_conical_gear_mesh(self) -> '_2260.ConicalGearMesh':
        """ConicalGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        if _2260.ConicalGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to ConicalGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design_of_type_cylindrical_gear_mesh(self) -> '_2262.CylindricalGearMesh':
        """CylindricalGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        if _2262.CylindricalGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to CylindricalGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design_of_type_face_gear_mesh(self) -> '_2264.FaceGearMesh':
        """FaceGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        if _2264.FaceGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to FaceGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design_of_type_gear_mesh(self) -> '_2266.GearMesh':
        """GearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        if _2266.GearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to GearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design_of_type_hypoid_gear_mesh(self) -> '_2268.HypoidGearMesh':
        """HypoidGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        if _2268.HypoidGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to HypoidGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design_of_type_klingelnberg_cyclo_palloid_conical_gear_mesh(self) -> '_2271.KlingelnbergCycloPalloidConicalGearMesh':
        """KlingelnbergCycloPalloidConicalGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        if _2271.KlingelnbergCycloPalloidConicalGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to KlingelnbergCycloPalloidConicalGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design_of_type_klingelnberg_cyclo_palloid_hypoid_gear_mesh(self) -> '_2272.KlingelnbergCycloPalloidHypoidGearMesh':
        """KlingelnbergCycloPalloidHypoidGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        if _2272.KlingelnbergCycloPalloidHypoidGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to KlingelnbergCycloPalloidHypoidGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(self) -> '_2273.KlingelnbergCycloPalloidSpiralBevelGearMesh':
        """KlingelnbergCycloPalloidSpiralBevelGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        if _2273.KlingelnbergCycloPalloidSpiralBevelGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to KlingelnbergCycloPalloidSpiralBevelGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

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
    def connection_design_of_type_worm_gear_mesh(self) -> '_2282.WormGearMesh':
        """WormGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        if _2282.WormGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to WormGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

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
    def connection_design_of_type_cycloidal_disc_central_bearing_connection(self) -> '_2288.CycloidalDiscCentralBearingConnection':
        """CycloidalDiscCentralBearingConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        if _2288.CycloidalDiscCentralBearingConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to CycloidalDiscCentralBearingConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design_of_type_cycloidal_disc_planetary_bearing_connection(self) -> '_2291.CycloidalDiscPlanetaryBearingConnection':
        """CycloidalDiscPlanetaryBearingConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        if _2291.CycloidalDiscPlanetaryBearingConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to CycloidalDiscPlanetaryBearingConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design_of_type_ring_pins_to_disc_connection(self) -> '_2294.RingPinsToDiscConnection':
        """RingPinsToDiscConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        if _2294.RingPinsToDiscConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to RingPinsToDiscConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design_of_type_clutch_connection(self) -> '_2295.ClutchConnection':
        """ClutchConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        if _2295.ClutchConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to ClutchConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design_of_type_concept_coupling_connection(self) -> '_2297.ConceptCouplingConnection':
        """ConceptCouplingConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        if _2297.ConceptCouplingConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to ConceptCouplingConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design_of_type_coupling_connection(self) -> '_2299.CouplingConnection':
        """CouplingConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        if _2299.CouplingConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to CouplingConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design_of_type_part_to_part_shear_coupling_connection(self) -> '_2301.PartToPartShearCouplingConnection':
        """PartToPartShearCouplingConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        if _2301.PartToPartShearCouplingConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to PartToPartShearCouplingConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design_of_type_spring_damper_connection(self) -> '_2303.SpringDamperConnection':
        """SpringDamperConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        if _2303.SpringDamperConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to SpringDamperConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design_of_type_torque_converter_connection(self) -> '_2305.TorqueConverterConnection':
        """TorqueConverterConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        if _2305.TorqueConverterConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to TorqueConverterConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def dynamic_analysis(self) -> '_2578.DynamicAnalysis':
        """DynamicAnalysis: 'DynamicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DynamicAnalysis

        if temp is None:
            return None

        if _2578.DynamicAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast dynamic_analysis to DynamicAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
