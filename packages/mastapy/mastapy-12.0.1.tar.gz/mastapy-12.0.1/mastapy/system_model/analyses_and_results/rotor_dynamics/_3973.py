"""_3973.py

ShaftForcedComplexShape
"""


from mastapy.system_model.analyses_and_results.rotor_dynamics import _3972
from mastapy.utility.units_and_measurements.measurements import _1636, _1581
from mastapy._internal.python_net import python_net_import

_SHAFT_FORCED_COMPLEX_SHAPE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.RotorDynamics', 'ShaftForcedComplexShape')


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftForcedComplexShape',)


class ShaftForcedComplexShape(_3972.ShaftComplexShape['_1636.LengthVeryShort', '_1581.AngleSmall']):
    """ShaftForcedComplexShape

    This is a mastapy class.
    """

    TYPE = _SHAFT_FORCED_COMPLEX_SHAPE

    def __init__(self, instance_to_wrap: 'ShaftForcedComplexShape.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
