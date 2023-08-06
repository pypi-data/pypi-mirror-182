"""_7239.py

CVTAdvancedSystemDeflection
"""


from mastapy.system_model.part_model.couplings import _2538
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7208
from mastapy._internal.python_net import python_net_import

_CVT_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'CVTAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('CVTAdvancedSystemDeflection',)


class CVTAdvancedSystemDeflection(_7208.BeltDriveAdvancedSystemDeflection):
    """CVTAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CVT_ADVANCED_SYSTEM_DEFLECTION

    def __init__(self, instance_to_wrap: 'CVTAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2538.CVT':
        """CVT: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
