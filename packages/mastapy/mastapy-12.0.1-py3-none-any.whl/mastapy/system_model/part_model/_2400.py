"""_2400.py

Connector
"""


from typing import Optional

from mastapy.system_model.part_model import (
    _2389, _2397, _2398, _2417
)
from mastapy._internal import constructor
from mastapy.system_model.part_model.shaft_model import _2435
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.part_model.cycloidal import _2521
from mastapy.system_model.connections_and_sockets import (
    _2225, _2218, _2221, _2222,
    _2226, _2234, _2240, _2245,
    _2248, _2229, _2219, _2220,
    _2227, _2232, _2233, _2235,
    _2236, _2237, _2238, _2239,
    _2241, _2242, _2243, _2246,
    _2247
)
from mastapy.system_model.connections_and_sockets.gears import (
    _2252, _2254, _2256, _2258,
    _2260, _2262, _2264, _2266,
    _2268, _2271, _2272, _2273,
    _2276, _2278, _2280, _2282,
    _2284, _2263
)
from mastapy.system_model.connections_and_sockets.cycloidal import (
    _2288, _2291, _2294, _2286,
    _2287, _2289, _2290, _2292,
    _2293
)
from mastapy.system_model.connections_and_sockets.couplings import (
    _2295, _2297, _2299, _2301,
    _2303, _2305, _2296, _2298,
    _2300, _2302, _2304, _2306,
    _2307
)
from mastapy._internal.python_net import python_net_import

_CONNECTOR = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'Connector')


__docformat__ = 'restructuredtext en'
__all__ = ('Connector',)


class Connector(_2417.MountableComponent):
    """Connector

    This is a mastapy class.
    """

    TYPE = _CONNECTOR

    def __init__(self, instance_to_wrap: 'Connector.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def outer_component(self) -> '_2389.AbstractShaft':
        """AbstractShaft: 'OuterComponent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterComponent

        if temp is None:
            return None

        if _2389.AbstractShaft.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast outer_component to AbstractShaft. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_component_of_type_shaft(self) -> '_2435.Shaft':
        """Shaft: 'OuterComponent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterComponent

        if temp is None:
            return None

        if _2435.Shaft.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast outer_component to Shaft. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_component_of_type_cycloidal_disc(self) -> '_2521.CycloidalDisc':
        """CycloidalDisc: 'OuterComponent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterComponent

        if temp is None:
            return None

        if _2521.CycloidalDisc.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast outer_component to CycloidalDisc. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_connection(self) -> '_2225.Connection':
        """Connection: 'OuterConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterConnection

        if temp is None:
            return None

        if _2225.Connection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast outer_connection to Connection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_connection_of_type_abstract_shaft_to_mountable_component_connection(self) -> '_2218.AbstractShaftToMountableComponentConnection':
        """AbstractShaftToMountableComponentConnection: 'OuterConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterConnection

        if temp is None:
            return None

        if _2218.AbstractShaftToMountableComponentConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast outer_connection to AbstractShaftToMountableComponentConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_connection_of_type_belt_connection(self) -> '_2221.BeltConnection':
        """BeltConnection: 'OuterConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterConnection

        if temp is None:
            return None

        if _2221.BeltConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast outer_connection to BeltConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_connection_of_type_coaxial_connection(self) -> '_2222.CoaxialConnection':
        """CoaxialConnection: 'OuterConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterConnection

        if temp is None:
            return None

        if _2222.CoaxialConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast outer_connection to CoaxialConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_connection_of_type_cvt_belt_connection(self) -> '_2226.CVTBeltConnection':
        """CVTBeltConnection: 'OuterConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterConnection

        if temp is None:
            return None

        if _2226.CVTBeltConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast outer_connection to CVTBeltConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_connection_of_type_inter_mountable_component_connection(self) -> '_2234.InterMountableComponentConnection':
        """InterMountableComponentConnection: 'OuterConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterConnection

        if temp is None:
            return None

        if _2234.InterMountableComponentConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast outer_connection to InterMountableComponentConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_connection_of_type_planetary_connection(self) -> '_2240.PlanetaryConnection':
        """PlanetaryConnection: 'OuterConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterConnection

        if temp is None:
            return None

        if _2240.PlanetaryConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast outer_connection to PlanetaryConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_connection_of_type_rolling_ring_connection(self) -> '_2245.RollingRingConnection':
        """RollingRingConnection: 'OuterConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterConnection

        if temp is None:
            return None

        if _2245.RollingRingConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast outer_connection to RollingRingConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_connection_of_type_shaft_to_mountable_component_connection(self) -> '_2248.ShaftToMountableComponentConnection':
        """ShaftToMountableComponentConnection: 'OuterConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterConnection

        if temp is None:
            return None

        if _2248.ShaftToMountableComponentConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast outer_connection to ShaftToMountableComponentConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_connection_of_type_agma_gleason_conical_gear_mesh(self) -> '_2252.AGMAGleasonConicalGearMesh':
        """AGMAGleasonConicalGearMesh: 'OuterConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterConnection

        if temp is None:
            return None

        if _2252.AGMAGleasonConicalGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast outer_connection to AGMAGleasonConicalGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_connection_of_type_bevel_differential_gear_mesh(self) -> '_2254.BevelDifferentialGearMesh':
        """BevelDifferentialGearMesh: 'OuterConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterConnection

        if temp is None:
            return None

        if _2254.BevelDifferentialGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast outer_connection to BevelDifferentialGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_connection_of_type_bevel_gear_mesh(self) -> '_2256.BevelGearMesh':
        """BevelGearMesh: 'OuterConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterConnection

        if temp is None:
            return None

        if _2256.BevelGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast outer_connection to BevelGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_connection_of_type_concept_gear_mesh(self) -> '_2258.ConceptGearMesh':
        """ConceptGearMesh: 'OuterConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterConnection

        if temp is None:
            return None

        if _2258.ConceptGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast outer_connection to ConceptGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_connection_of_type_conical_gear_mesh(self) -> '_2260.ConicalGearMesh':
        """ConicalGearMesh: 'OuterConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterConnection

        if temp is None:
            return None

        if _2260.ConicalGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast outer_connection to ConicalGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_connection_of_type_cylindrical_gear_mesh(self) -> '_2262.CylindricalGearMesh':
        """CylindricalGearMesh: 'OuterConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterConnection

        if temp is None:
            return None

        if _2262.CylindricalGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast outer_connection to CylindricalGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_connection_of_type_face_gear_mesh(self) -> '_2264.FaceGearMesh':
        """FaceGearMesh: 'OuterConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterConnection

        if temp is None:
            return None

        if _2264.FaceGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast outer_connection to FaceGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_connection_of_type_gear_mesh(self) -> '_2266.GearMesh':
        """GearMesh: 'OuterConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterConnection

        if temp is None:
            return None

        if _2266.GearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast outer_connection to GearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_connection_of_type_hypoid_gear_mesh(self) -> '_2268.HypoidGearMesh':
        """HypoidGearMesh: 'OuterConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterConnection

        if temp is None:
            return None

        if _2268.HypoidGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast outer_connection to HypoidGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_connection_of_type_klingelnberg_cyclo_palloid_conical_gear_mesh(self) -> '_2271.KlingelnbergCycloPalloidConicalGearMesh':
        """KlingelnbergCycloPalloidConicalGearMesh: 'OuterConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterConnection

        if temp is None:
            return None

        if _2271.KlingelnbergCycloPalloidConicalGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast outer_connection to KlingelnbergCycloPalloidConicalGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_connection_of_type_klingelnberg_cyclo_palloid_hypoid_gear_mesh(self) -> '_2272.KlingelnbergCycloPalloidHypoidGearMesh':
        """KlingelnbergCycloPalloidHypoidGearMesh: 'OuterConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterConnection

        if temp is None:
            return None

        if _2272.KlingelnbergCycloPalloidHypoidGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast outer_connection to KlingelnbergCycloPalloidHypoidGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_connection_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(self) -> '_2273.KlingelnbergCycloPalloidSpiralBevelGearMesh':
        """KlingelnbergCycloPalloidSpiralBevelGearMesh: 'OuterConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterConnection

        if temp is None:
            return None

        if _2273.KlingelnbergCycloPalloidSpiralBevelGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast outer_connection to KlingelnbergCycloPalloidSpiralBevelGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_connection_of_type_spiral_bevel_gear_mesh(self) -> '_2276.SpiralBevelGearMesh':
        """SpiralBevelGearMesh: 'OuterConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterConnection

        if temp is None:
            return None

        if _2276.SpiralBevelGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast outer_connection to SpiralBevelGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_connection_of_type_straight_bevel_diff_gear_mesh(self) -> '_2278.StraightBevelDiffGearMesh':
        """StraightBevelDiffGearMesh: 'OuterConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterConnection

        if temp is None:
            return None

        if _2278.StraightBevelDiffGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast outer_connection to StraightBevelDiffGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_connection_of_type_straight_bevel_gear_mesh(self) -> '_2280.StraightBevelGearMesh':
        """StraightBevelGearMesh: 'OuterConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterConnection

        if temp is None:
            return None

        if _2280.StraightBevelGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast outer_connection to StraightBevelGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_connection_of_type_worm_gear_mesh(self) -> '_2282.WormGearMesh':
        """WormGearMesh: 'OuterConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterConnection

        if temp is None:
            return None

        if _2282.WormGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast outer_connection to WormGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_connection_of_type_zerol_bevel_gear_mesh(self) -> '_2284.ZerolBevelGearMesh':
        """ZerolBevelGearMesh: 'OuterConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterConnection

        if temp is None:
            return None

        if _2284.ZerolBevelGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast outer_connection to ZerolBevelGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_connection_of_type_cycloidal_disc_central_bearing_connection(self) -> '_2288.CycloidalDiscCentralBearingConnection':
        """CycloidalDiscCentralBearingConnection: 'OuterConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterConnection

        if temp is None:
            return None

        if _2288.CycloidalDiscCentralBearingConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast outer_connection to CycloidalDiscCentralBearingConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_connection_of_type_cycloidal_disc_planetary_bearing_connection(self) -> '_2291.CycloidalDiscPlanetaryBearingConnection':
        """CycloidalDiscPlanetaryBearingConnection: 'OuterConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterConnection

        if temp is None:
            return None

        if _2291.CycloidalDiscPlanetaryBearingConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast outer_connection to CycloidalDiscPlanetaryBearingConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_connection_of_type_ring_pins_to_disc_connection(self) -> '_2294.RingPinsToDiscConnection':
        """RingPinsToDiscConnection: 'OuterConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterConnection

        if temp is None:
            return None

        if _2294.RingPinsToDiscConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast outer_connection to RingPinsToDiscConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_connection_of_type_clutch_connection(self) -> '_2295.ClutchConnection':
        """ClutchConnection: 'OuterConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterConnection

        if temp is None:
            return None

        if _2295.ClutchConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast outer_connection to ClutchConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_connection_of_type_concept_coupling_connection(self) -> '_2297.ConceptCouplingConnection':
        """ConceptCouplingConnection: 'OuterConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterConnection

        if temp is None:
            return None

        if _2297.ConceptCouplingConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast outer_connection to ConceptCouplingConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_connection_of_type_coupling_connection(self) -> '_2299.CouplingConnection':
        """CouplingConnection: 'OuterConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterConnection

        if temp is None:
            return None

        if _2299.CouplingConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast outer_connection to CouplingConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_connection_of_type_part_to_part_shear_coupling_connection(self) -> '_2301.PartToPartShearCouplingConnection':
        """PartToPartShearCouplingConnection: 'OuterConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterConnection

        if temp is None:
            return None

        if _2301.PartToPartShearCouplingConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast outer_connection to PartToPartShearCouplingConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_connection_of_type_spring_damper_connection(self) -> '_2303.SpringDamperConnection':
        """SpringDamperConnection: 'OuterConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterConnection

        if temp is None:
            return None

        if _2303.SpringDamperConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast outer_connection to SpringDamperConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_connection_of_type_torque_converter_connection(self) -> '_2305.TorqueConverterConnection':
        """TorqueConverterConnection: 'OuterConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterConnection

        if temp is None:
            return None

        if _2305.TorqueConverterConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast outer_connection to TorqueConverterConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_socket(self) -> '_2229.CylindricalSocket':
        """CylindricalSocket: 'OuterSocket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterSocket

        if temp is None:
            return None

        if _2229.CylindricalSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast outer_socket to CylindricalSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_socket_of_type_bearing_inner_socket(self) -> '_2219.BearingInnerSocket':
        """BearingInnerSocket: 'OuterSocket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterSocket

        if temp is None:
            return None

        if _2219.BearingInnerSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast outer_socket to BearingInnerSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_socket_of_type_bearing_outer_socket(self) -> '_2220.BearingOuterSocket':
        """BearingOuterSocket: 'OuterSocket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterSocket

        if temp is None:
            return None

        if _2220.BearingOuterSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast outer_socket to BearingOuterSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_socket_of_type_cvt_pulley_socket(self) -> '_2227.CVTPulleySocket':
        """CVTPulleySocket: 'OuterSocket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterSocket

        if temp is None:
            return None

        if _2227.CVTPulleySocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast outer_socket to CVTPulleySocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_socket_of_type_inner_shaft_socket(self) -> '_2232.InnerShaftSocket':
        """InnerShaftSocket: 'OuterSocket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterSocket

        if temp is None:
            return None

        if _2232.InnerShaftSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast outer_socket to InnerShaftSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_socket_of_type_inner_shaft_socket_base(self) -> '_2233.InnerShaftSocketBase':
        """InnerShaftSocketBase: 'OuterSocket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterSocket

        if temp is None:
            return None

        if _2233.InnerShaftSocketBase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast outer_socket to InnerShaftSocketBase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_socket_of_type_mountable_component_inner_socket(self) -> '_2235.MountableComponentInnerSocket':
        """MountableComponentInnerSocket: 'OuterSocket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterSocket

        if temp is None:
            return None

        if _2235.MountableComponentInnerSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast outer_socket to MountableComponentInnerSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_socket_of_type_mountable_component_outer_socket(self) -> '_2236.MountableComponentOuterSocket':
        """MountableComponentOuterSocket: 'OuterSocket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterSocket

        if temp is None:
            return None

        if _2236.MountableComponentOuterSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast outer_socket to MountableComponentOuterSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_socket_of_type_mountable_component_socket(self) -> '_2237.MountableComponentSocket':
        """MountableComponentSocket: 'OuterSocket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterSocket

        if temp is None:
            return None

        if _2237.MountableComponentSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast outer_socket to MountableComponentSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_socket_of_type_outer_shaft_socket(self) -> '_2238.OuterShaftSocket':
        """OuterShaftSocket: 'OuterSocket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterSocket

        if temp is None:
            return None

        if _2238.OuterShaftSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast outer_socket to OuterShaftSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_socket_of_type_outer_shaft_socket_base(self) -> '_2239.OuterShaftSocketBase':
        """OuterShaftSocketBase: 'OuterSocket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterSocket

        if temp is None:
            return None

        if _2239.OuterShaftSocketBase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast outer_socket to OuterShaftSocketBase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_socket_of_type_planetary_socket(self) -> '_2241.PlanetarySocket':
        """PlanetarySocket: 'OuterSocket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterSocket

        if temp is None:
            return None

        if _2241.PlanetarySocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast outer_socket to PlanetarySocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_socket_of_type_planetary_socket_base(self) -> '_2242.PlanetarySocketBase':
        """PlanetarySocketBase: 'OuterSocket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterSocket

        if temp is None:
            return None

        if _2242.PlanetarySocketBase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast outer_socket to PlanetarySocketBase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_socket_of_type_pulley_socket(self) -> '_2243.PulleySocket':
        """PulleySocket: 'OuterSocket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterSocket

        if temp is None:
            return None

        if _2243.PulleySocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast outer_socket to PulleySocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_socket_of_type_rolling_ring_socket(self) -> '_2246.RollingRingSocket':
        """RollingRingSocket: 'OuterSocket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterSocket

        if temp is None:
            return None

        if _2246.RollingRingSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast outer_socket to RollingRingSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_socket_of_type_shaft_socket(self) -> '_2247.ShaftSocket':
        """ShaftSocket: 'OuterSocket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterSocket

        if temp is None:
            return None

        if _2247.ShaftSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast outer_socket to ShaftSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_socket_of_type_cylindrical_gear_teeth_socket(self) -> '_2263.CylindricalGearTeethSocket':
        """CylindricalGearTeethSocket: 'OuterSocket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterSocket

        if temp is None:
            return None

        if _2263.CylindricalGearTeethSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast outer_socket to CylindricalGearTeethSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_socket_of_type_cycloidal_disc_axial_left_socket(self) -> '_2286.CycloidalDiscAxialLeftSocket':
        """CycloidalDiscAxialLeftSocket: 'OuterSocket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterSocket

        if temp is None:
            return None

        if _2286.CycloidalDiscAxialLeftSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast outer_socket to CycloidalDiscAxialLeftSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_socket_of_type_cycloidal_disc_axial_right_socket(self) -> '_2287.CycloidalDiscAxialRightSocket':
        """CycloidalDiscAxialRightSocket: 'OuterSocket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterSocket

        if temp is None:
            return None

        if _2287.CycloidalDiscAxialRightSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast outer_socket to CycloidalDiscAxialRightSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_socket_of_type_cycloidal_disc_inner_socket(self) -> '_2289.CycloidalDiscInnerSocket':
        """CycloidalDiscInnerSocket: 'OuterSocket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterSocket

        if temp is None:
            return None

        if _2289.CycloidalDiscInnerSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast outer_socket to CycloidalDiscInnerSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_socket_of_type_cycloidal_disc_outer_socket(self) -> '_2290.CycloidalDiscOuterSocket':
        """CycloidalDiscOuterSocket: 'OuterSocket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterSocket

        if temp is None:
            return None

        if _2290.CycloidalDiscOuterSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast outer_socket to CycloidalDiscOuterSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_socket_of_type_cycloidal_disc_planetary_bearing_socket(self) -> '_2292.CycloidalDiscPlanetaryBearingSocket':
        """CycloidalDiscPlanetaryBearingSocket: 'OuterSocket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterSocket

        if temp is None:
            return None

        if _2292.CycloidalDiscPlanetaryBearingSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast outer_socket to CycloidalDiscPlanetaryBearingSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_socket_of_type_ring_pins_socket(self) -> '_2293.RingPinsSocket':
        """RingPinsSocket: 'OuterSocket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterSocket

        if temp is None:
            return None

        if _2293.RingPinsSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast outer_socket to RingPinsSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_socket_of_type_clutch_socket(self) -> '_2296.ClutchSocket':
        """ClutchSocket: 'OuterSocket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterSocket

        if temp is None:
            return None

        if _2296.ClutchSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast outer_socket to ClutchSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_socket_of_type_concept_coupling_socket(self) -> '_2298.ConceptCouplingSocket':
        """ConceptCouplingSocket: 'OuterSocket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterSocket

        if temp is None:
            return None

        if _2298.ConceptCouplingSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast outer_socket to ConceptCouplingSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_socket_of_type_coupling_socket(self) -> '_2300.CouplingSocket':
        """CouplingSocket: 'OuterSocket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterSocket

        if temp is None:
            return None

        if _2300.CouplingSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast outer_socket to CouplingSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_socket_of_type_part_to_part_shear_coupling_socket(self) -> '_2302.PartToPartShearCouplingSocket':
        """PartToPartShearCouplingSocket: 'OuterSocket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterSocket

        if temp is None:
            return None

        if _2302.PartToPartShearCouplingSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast outer_socket to PartToPartShearCouplingSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_socket_of_type_spring_damper_socket(self) -> '_2304.SpringDamperSocket':
        """SpringDamperSocket: 'OuterSocket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterSocket

        if temp is None:
            return None

        if _2304.SpringDamperSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast outer_socket to SpringDamperSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_socket_of_type_torque_converter_pump_socket(self) -> '_2306.TorqueConverterPumpSocket':
        """TorqueConverterPumpSocket: 'OuterSocket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterSocket

        if temp is None:
            return None

        if _2306.TorqueConverterPumpSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast outer_socket to TorqueConverterPumpSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_socket_of_type_torque_converter_turbine_socket(self) -> '_2307.TorqueConverterTurbineSocket':
        """TorqueConverterTurbineSocket: 'OuterSocket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterSocket

        if temp is None:
            return None

        if _2307.TorqueConverterTurbineSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast outer_socket to TorqueConverterTurbineSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    def house_in(self, shaft: '_2389.AbstractShaft', offset: Optional['float'] = float('nan')) -> '_2225.Connection':
        """ 'HouseIn' is the original name of this method.

        Args:
            shaft (mastapy.system_model.part_model.AbstractShaft)
            offset (float, optional)

        Returns:
            mastapy.system_model.connections_and_sockets.Connection
        """

        offset = float(offset)
        method_result = self.wrapped.HouseIn(shaft.wrapped if shaft else None, offset if offset else 0.0)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def other_component(self, component: '_2397.Component') -> '_2389.AbstractShaft':
        """ 'OtherComponent' is the original name of this method.

        Args:
            component (mastapy.system_model.part_model.Component)

        Returns:
            mastapy.system_model.part_model.AbstractShaft
        """

        method_result = self.wrapped.OtherComponent(component.wrapped if component else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def try_house_in(self, shaft: '_2389.AbstractShaft', offset: Optional['float'] = float('nan')) -> '_2398.ComponentsConnectedResult':
        """ 'TryHouseIn' is the original name of this method.

        Args:
            shaft (mastapy.system_model.part_model.AbstractShaft)
            offset (float, optional)

        Returns:
            mastapy.system_model.part_model.ComponentsConnectedResult
        """

        offset = float(offset)
        method_result = self.wrapped.TryHouseIn(shaft.wrapped if shaft else None, offset if offset else 0.0)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None
