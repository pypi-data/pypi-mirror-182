﻿"""_7196.py

AbstractShaftAdvancedSystemDeflection
"""


from mastapy.system_model.part_model import _2389
from mastapy._internal import constructor
from mastapy.system_model.part_model.shaft_model import _2435
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.part_model.cycloidal import _2521
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7197
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'AbstractShaftAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractShaftAdvancedSystemDeflection',)


class AbstractShaftAdvancedSystemDeflection(_7197.AbstractShaftOrHousingAdvancedSystemDeflection):
    """AbstractShaftAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_ADVANCED_SYSTEM_DEFLECTION

    def __init__(self, instance_to_wrap: 'AbstractShaftAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2389.AbstractShaft':
        """AbstractShaft: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2389.AbstractShaft.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to AbstractShaft. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_shaft(self) -> '_2435.Shaft':
        """Shaft: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2435.Shaft.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to Shaft. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_cycloidal_disc(self) -> '_2521.CycloidalDisc':
        """CycloidalDisc: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2521.CycloidalDisc.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to CycloidalDisc. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
