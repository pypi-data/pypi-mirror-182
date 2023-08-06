"""_5339.py

ClutchMultibodyDynamicsAnalysis
"""


from mastapy.system_model.part_model.couplings import _2530
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6762
from mastapy.system_model.analyses_and_results.mbd_analyses import _5337, _5356
from mastapy._internal.python_net import python_net_import

_CLUTCH_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'ClutchMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ClutchMultibodyDynamicsAnalysis',)


class ClutchMultibodyDynamicsAnalysis(_5356.CouplingMultibodyDynamicsAnalysis):
    """ClutchMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _CLUTCH_MULTIBODY_DYNAMICS_ANALYSIS

    def __init__(self, instance_to_wrap: 'ClutchMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2530.Clutch':
        """Clutch: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6762.ClutchLoadCase':
        """ClutchLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def clutch_connection(self) -> '_5337.ClutchConnectionMultibodyDynamicsAnalysis':
        """ClutchConnectionMultibodyDynamicsAnalysis: 'ClutchConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ClutchConnection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
