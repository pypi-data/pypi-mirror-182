"""_7316.py

SynchroniserPartAdvancedSystemDeflection
"""


from mastapy.system_model.part_model.couplings import _2557, _2556, _2558
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7238
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_PART_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'SynchroniserPartAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('SynchroniserPartAdvancedSystemDeflection',)


class SynchroniserPartAdvancedSystemDeflection(_7238.CouplingHalfAdvancedSystemDeflection):
    """SynchroniserPartAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_PART_ADVANCED_SYSTEM_DEFLECTION

    def __init__(self, instance_to_wrap: 'SynchroniserPartAdvancedSystemDeflection.TYPE'):
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
