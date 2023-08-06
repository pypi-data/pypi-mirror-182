"""_7222.py

CoaxialConnectionAdvancedSystemDeflection
"""


from typing import List

from mastapy.system_model.connections_and_sockets import _2222
from mastapy._internal import constructor, conversion
from mastapy.system_model.connections_and_sockets.cycloidal import _2288
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.static_loads import _6763, _6785
from mastapy.system_model.analyses_and_results.system_deflections import _2661
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7298
from mastapy._internal.python_net import python_net_import

_COAXIAL_CONNECTION_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'CoaxialConnectionAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('CoaxialConnectionAdvancedSystemDeflection',)


class CoaxialConnectionAdvancedSystemDeflection(_7298.ShaftToMountableComponentConnectionAdvancedSystemDeflection):
    """CoaxialConnectionAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _COAXIAL_CONNECTION_ADVANCED_SYSTEM_DEFLECTION

    def __init__(self, instance_to_wrap: 'CoaxialConnectionAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2222.CoaxialConnection':
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
    def connection_load_case(self) -> '_6763.CoaxialConnectionLoadCase':
        """CoaxialConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        if _6763.CoaxialConnectionLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_load_case to CoaxialConnectionLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_system_deflection_results(self) -> 'List[_2661.CoaxialConnectionSystemDeflection]':
        """List[CoaxialConnectionSystemDeflection]: 'ConnectionSystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionSystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
