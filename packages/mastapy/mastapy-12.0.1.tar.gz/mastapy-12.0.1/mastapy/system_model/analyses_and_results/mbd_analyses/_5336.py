"""_5336.py

BoltMultibodyDynamicsAnalysis
"""


from mastapy.system_model.part_model import _2395
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6759
from mastapy.system_model.analyses_and_results.mbd_analyses import _5342
from mastapy._internal.python_net import python_net_import

_BOLT_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'BoltMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('BoltMultibodyDynamicsAnalysis',)


class BoltMultibodyDynamicsAnalysis(_5342.ComponentMultibodyDynamicsAnalysis):
    """BoltMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _BOLT_MULTIBODY_DYNAMICS_ANALYSIS

    def __init__(self, instance_to_wrap: 'BoltMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2395.Bolt':
        """Bolt: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6759.BoltLoadCase':
        """BoltLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
