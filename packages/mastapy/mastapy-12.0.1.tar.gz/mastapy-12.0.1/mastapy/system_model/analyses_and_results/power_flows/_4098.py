"""_4098.py

TorqueConverterConnectionPowerFlow
"""


from mastapy.system_model.connections_and_sockets.couplings import _2305
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6899
from mastapy.system_model.analyses_and_results.power_flows import _4014
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_CONNECTION_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'TorqueConverterConnectionPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('TorqueConverterConnectionPowerFlow',)


class TorqueConverterConnectionPowerFlow(_4014.CouplingConnectionPowerFlow):
    """TorqueConverterConnectionPowerFlow

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_CONNECTION_POWER_FLOW

    def __init__(self, instance_to_wrap: 'TorqueConverterConnectionPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2305.TorqueConverterConnection':
        """TorqueConverterConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6899.TorqueConverterConnectionLoadCase':
        """TorqueConverterConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
