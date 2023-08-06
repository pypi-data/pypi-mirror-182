"""_2429.py

SpecialisedAssembly
"""


from mastapy.system_model.part_model import _2388
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'SpecialisedAssembly')


__docformat__ = 'restructuredtext en'
__all__ = ('SpecialisedAssembly',)


class SpecialisedAssembly(_2388.AbstractAssembly):
    """SpecialisedAssembly

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY

    def __init__(self, instance_to_wrap: 'SpecialisedAssembly.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
