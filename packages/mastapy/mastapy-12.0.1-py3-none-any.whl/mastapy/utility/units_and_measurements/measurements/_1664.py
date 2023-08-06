"""_1664.py

PowerSmallPerVolume
"""


from mastapy.utility.units_and_measurements import _1571
from mastapy._internal.python_net import python_net_import

_POWER_SMALL_PER_VOLUME = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'PowerSmallPerVolume')


__docformat__ = 'restructuredtext en'
__all__ = ('PowerSmallPerVolume',)


class PowerSmallPerVolume(_1571.MeasurementBase):
    """PowerSmallPerVolume

    This is a mastapy class.
    """

    TYPE = _POWER_SMALL_PER_VOLUME

    def __init__(self, instance_to_wrap: 'PowerSmallPerVolume.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
