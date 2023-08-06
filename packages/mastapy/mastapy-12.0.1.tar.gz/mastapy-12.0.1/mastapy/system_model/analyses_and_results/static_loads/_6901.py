"""_6901.py

TorqueConverterPumpLoadCase
"""


from mastapy.system_model.part_model.couplings import _2560
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6779
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_PUMP_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'TorqueConverterPumpLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('TorqueConverterPumpLoadCase',)


class TorqueConverterPumpLoadCase(_6779.CouplingHalfLoadCase):
    """TorqueConverterPumpLoadCase

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_PUMP_LOAD_CASE

    def __init__(self, instance_to_wrap: 'TorqueConverterPumpLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2560.TorqueConverterPump':
        """TorqueConverterPump: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
