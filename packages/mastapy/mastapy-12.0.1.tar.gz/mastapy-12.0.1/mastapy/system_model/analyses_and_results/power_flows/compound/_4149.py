"""_4149.py

CouplingHalfCompoundPowerFlow
"""


from typing import List

from mastapy.system_model.analyses_and_results.power_flows import _4015
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4187
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'CouplingHalfCompoundPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('CouplingHalfCompoundPowerFlow',)


class CouplingHalfCompoundPowerFlow(_4187.MountableComponentCompoundPowerFlow):
    """CouplingHalfCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_COMPOUND_POWER_FLOW

    def __init__(self, instance_to_wrap: 'CouplingHalfCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_4015.CouplingHalfPowerFlow]':
        """List[CouplingHalfPowerFlow]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_4015.CouplingHalfPowerFlow]':
        """List[CouplingHalfPowerFlow]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
