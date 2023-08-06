"""_7243.py

CycloidalDiscAdvancedSystemDeflection
"""


from typing import List

from mastapy.system_model.part_model.cycloidal import _2521
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6786
from mastapy.system_model.analyses_and_results.system_deflections import _2685
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7196
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'CycloidalDiscAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('CycloidalDiscAdvancedSystemDeflection',)


class CycloidalDiscAdvancedSystemDeflection(_7196.AbstractShaftAdvancedSystemDeflection):
    """CycloidalDiscAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_ADVANCED_SYSTEM_DEFLECTION

    def __init__(self, instance_to_wrap: 'CycloidalDiscAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2521.CycloidalDisc':
        """CycloidalDisc: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6786.CycloidalDiscLoadCase':
        """CycloidalDiscLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_system_deflection_results(self) -> 'List[_2685.CycloidalDiscSystemDeflection]':
        """List[CycloidalDiscSystemDeflection]: 'ComponentSystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentSystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
