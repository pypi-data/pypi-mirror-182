"""_2567.py

BearingDetailConfiguration
"""


from mastapy.system_model.part_model.configurations import _2569, _2568
from mastapy.system_model.part_model import _2393
from mastapy.bearings.bearing_designs import _2086
from mastapy._internal.python_net import python_net_import

_BEARING_DETAIL_CONFIGURATION = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Configurations', 'BearingDetailConfiguration')


__docformat__ = 'restructuredtext en'
__all__ = ('BearingDetailConfiguration',)


class BearingDetailConfiguration(_2569.PartDetailConfiguration['_2568.BearingDetailSelection', '_2393.Bearing', '_2086.BearingDesign']):
    """BearingDetailConfiguration

    This is a mastapy class.
    """

    TYPE = _BEARING_DETAIL_CONFIGURATION

    def __init__(self, instance_to_wrap: 'BearingDetailConfiguration.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
