﻿"""_2757.py

SpringDamperConnectionSystemDeflection
"""


from mastapy.system_model.connections_and_sockets.couplings import _2303
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6883
from mastapy.system_model.analyses_and_results.power_flows import _4082
from mastapy.system_model.analyses_and_results.system_deflections import _2676
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_CONNECTION_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'SpringDamperConnectionSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('SpringDamperConnectionSystemDeflection',)


class SpringDamperConnectionSystemDeflection(_2676.CouplingConnectionSystemDeflection):
    """SpringDamperConnectionSystemDeflection

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_CONNECTION_SYSTEM_DEFLECTION

    def __init__(self, instance_to_wrap: 'SpringDamperConnectionSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2303.SpringDamperConnection':
        """SpringDamperConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6883.SpringDamperConnectionLoadCase':
        """SpringDamperConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results(self) -> '_4082.SpringDamperConnectionPowerFlow':
        """SpringDamperConnectionPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
