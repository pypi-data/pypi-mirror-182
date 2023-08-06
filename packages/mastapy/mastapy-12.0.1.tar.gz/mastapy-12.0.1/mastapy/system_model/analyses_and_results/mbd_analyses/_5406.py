"""_5406.py

PartToPartShearCouplingHalfMultibodyDynamicsAnalysis
"""


from mastapy.system_model.part_model.couplings import _2541
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6857
from mastapy.system_model.analyses_and_results.mbd_analyses import _5355
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_HALF_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'PartToPartShearCouplingHalfMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('PartToPartShearCouplingHalfMultibodyDynamicsAnalysis',)


class PartToPartShearCouplingHalfMultibodyDynamicsAnalysis(_5355.CouplingHalfMultibodyDynamicsAnalysis):
    """PartToPartShearCouplingHalfMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_HALF_MULTIBODY_DYNAMICS_ANALYSIS

    def __init__(self, instance_to_wrap: 'PartToPartShearCouplingHalfMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2541.PartToPartShearCouplingHalf':
        """PartToPartShearCouplingHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6857.PartToPartShearCouplingHalfLoadCase':
        """PartToPartShearCouplingHalfLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
