"""_6325.py

TorqueConverterDynamicAnalysis
"""


from mastapy.system_model.part_model.couplings import _2559
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6900
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6244
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses', 'TorqueConverterDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('TorqueConverterDynamicAnalysis',)


class TorqueConverterDynamicAnalysis(_6244.CouplingDynamicAnalysis):
    """TorqueConverterDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_DYNAMIC_ANALYSIS

    def __init__(self, instance_to_wrap: 'TorqueConverterDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2559.TorqueConverter':
        """TorqueConverter: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6900.TorqueConverterLoadCase':
        """TorqueConverterLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
