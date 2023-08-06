"""_1669.py

Price
"""


from mastapy.utility.units_and_measurements import _1571
from mastapy._internal.python_net import python_net_import

_PRICE = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'Price')


__docformat__ = 'restructuredtext en'
__all__ = ('Price',)


class Price(_1571.MeasurementBase):
    """Price

    This is a mastapy class.
    """

    TYPE = _PRICE

    def __init__(self, instance_to_wrap: 'Price.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
