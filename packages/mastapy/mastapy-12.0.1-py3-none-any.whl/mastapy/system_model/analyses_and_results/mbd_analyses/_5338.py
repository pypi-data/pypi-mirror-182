"""_5338.py

ClutchHalfMultibodyDynamicsAnalysis
"""


from mastapy.system_model.part_model.couplings import _2531
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6761
from mastapy.system_model.analyses_and_results.mbd_analyses import _5355
from mastapy._internal.python_net import python_net_import

_CLUTCH_HALF_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'ClutchHalfMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ClutchHalfMultibodyDynamicsAnalysis',)


class ClutchHalfMultibodyDynamicsAnalysis(_5355.CouplingHalfMultibodyDynamicsAnalysis):
    """ClutchHalfMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _CLUTCH_HALF_MULTIBODY_DYNAMICS_ANALYSIS

    def __init__(self, instance_to_wrap: 'ClutchHalfMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2531.ClutchHalf':
        """ClutchHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6761.ClutchHalfLoadCase':
        """ClutchHalfLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
