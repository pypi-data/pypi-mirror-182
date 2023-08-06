"""_2769.py

SynchroniserPartSystemDeflection
"""


from mastapy.system_model.part_model.couplings import _2557, _2556, _2558
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.power_flows import _4094, _4093, _4096
from mastapy.system_model.analyses_and_results.system_deflections import _2677
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_PART_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'SynchroniserPartSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('SynchroniserPartSystemDeflection',)


class SynchroniserPartSystemDeflection(_2677.CouplingHalfSystemDeflection):
    """SynchroniserPartSystemDeflection

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_PART_SYSTEM_DEFLECTION

    def __init__(self, instance_to_wrap: 'SynchroniserPartSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2557.SynchroniserPart':
        """SynchroniserPart: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2557.SynchroniserPart.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to SynchroniserPart. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_synchroniser_half(self) -> '_2556.SynchroniserHalf':
        """SynchroniserHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2556.SynchroniserHalf.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to SynchroniserHalf. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_synchroniser_sleeve(self) -> '_2558.SynchroniserSleeve':
        """SynchroniserSleeve: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2558.SynchroniserSleeve.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to SynchroniserSleeve. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results(self) -> '_4094.SynchroniserPartPowerFlow':
        """SynchroniserPartPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _4094.SynchroniserPartPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to SynchroniserPartPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_synchroniser_half_power_flow(self) -> '_4093.SynchroniserHalfPowerFlow':
        """SynchroniserHalfPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _4093.SynchroniserHalfPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to SynchroniserHalfPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_synchroniser_sleeve_power_flow(self) -> '_4096.SynchroniserSleevePowerFlow':
        """SynchroniserSleevePowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _4096.SynchroniserSleevePowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to SynchroniserSleevePowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
