"""_2563.py

ActiveFESubstructureSelection
"""


from mastapy.system_model.part_model.configurations import _2570
from mastapy.system_model.part_model import _2406
from mastapy.system_model.fe import _2335
from mastapy._internal.python_net import python_net_import

_ACTIVE_FE_SUBSTRUCTURE_SELECTION = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Configurations', 'ActiveFESubstructureSelection')


__docformat__ = 'restructuredtext en'
__all__ = ('ActiveFESubstructureSelection',)


class ActiveFESubstructureSelection(_2570.PartDetailSelection['_2406.FEPart', '_2335.FESubstructure']):
    """ActiveFESubstructureSelection

    This is a mastapy class.
    """

    TYPE = _ACTIVE_FE_SUBSTRUCTURE_SELECTION

    def __init__(self, instance_to_wrap: 'ActiveFESubstructureSelection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
