"""_2640.py

AbstractShaftToMountableComponentConnectionSystemDeflection
"""


from mastapy.system_model.connections_and_sockets import (
    _2218, _2222, _2240, _2248
)
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.connections_and_sockets.cycloidal import _2288, _2291
from mastapy.system_model.analyses_and_results.power_flows import (
    _3980, _4001, _4021, _4022,
    _4061, _4077
)
from mastapy.system_model.analyses_and_results.system_deflections import _2674
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'AbstractShaftToMountableComponentConnectionSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractShaftToMountableComponentConnectionSystemDeflection',)


class AbstractShaftToMountableComponentConnectionSystemDeflection(_2674.ConnectionSystemDeflection):
    """AbstractShaftToMountableComponentConnectionSystemDeflection

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_SYSTEM_DEFLECTION

    def __init__(self, instance_to_wrap: 'AbstractShaftToMountableComponentConnectionSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2218.AbstractShaftToMountableComponentConnection':
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
    def power_flow_results(self) -> '_3980.AbstractShaftToMountableComponentConnectionPowerFlow':
        """AbstractShaftToMountableComponentConnectionPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _3980.AbstractShaftToMountableComponentConnectionPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to AbstractShaftToMountableComponentConnectionPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_coaxial_connection_power_flow(self) -> '_4001.CoaxialConnectionPowerFlow':
        """CoaxialConnectionPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _4001.CoaxialConnectionPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to CoaxialConnectionPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_cycloidal_disc_central_bearing_connection_power_flow(self) -> '_4021.CycloidalDiscCentralBearingConnectionPowerFlow':
        """CycloidalDiscCentralBearingConnectionPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _4021.CycloidalDiscCentralBearingConnectionPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to CycloidalDiscCentralBearingConnectionPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_cycloidal_disc_planetary_bearing_connection_power_flow(self) -> '_4022.CycloidalDiscPlanetaryBearingConnectionPowerFlow':
        """CycloidalDiscPlanetaryBearingConnectionPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _4022.CycloidalDiscPlanetaryBearingConnectionPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to CycloidalDiscPlanetaryBearingConnectionPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_planetary_connection_power_flow(self) -> '_4061.PlanetaryConnectionPowerFlow':
        """PlanetaryConnectionPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _4061.PlanetaryConnectionPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to PlanetaryConnectionPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_shaft_to_mountable_component_connection_power_flow(self) -> '_4077.ShaftToMountableComponentConnectionPowerFlow':
        """ShaftToMountableComponentConnectionPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _4077.ShaftToMountableComponentConnectionPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to ShaftToMountableComponentConnectionPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
