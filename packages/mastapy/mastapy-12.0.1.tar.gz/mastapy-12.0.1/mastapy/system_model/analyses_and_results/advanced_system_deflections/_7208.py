"""_7208.py

BeltDriveAdvancedSystemDeflection
"""


from typing import List

from mastapy.system_model.part_model.couplings import _2528, _2538
from mastapy._internal import constructor, conversion
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.static_loads import _6749, _6782
from mastapy.system_model.analyses_and_results.system_deflections import _2647
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7299
from mastapy._internal.python_net import python_net_import

_BELT_DRIVE_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'BeltDriveAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('BeltDriveAdvancedSystemDeflection',)


class BeltDriveAdvancedSystemDeflection(_7299.SpecialisedAssemblyAdvancedSystemDeflection):
    """BeltDriveAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BELT_DRIVE_ADVANCED_SYSTEM_DEFLECTION

    def __init__(self, instance_to_wrap: 'BeltDriveAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2528.BeltDrive':
        """BeltDrive: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        if _2528.BeltDrive.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast assembly_design to BeltDrive. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6749.BeltDriveLoadCase':
        """BeltDriveLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        if _6749.BeltDriveLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast assembly_load_case to BeltDriveLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_system_deflection_results(self) -> 'List[_2647.BeltDriveSystemDeflection]':
        """List[BeltDriveSystemDeflection]: 'AssemblySystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblySystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
