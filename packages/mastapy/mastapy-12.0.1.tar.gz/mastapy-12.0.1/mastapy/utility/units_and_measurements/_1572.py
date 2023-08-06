"""_1572.py

MeasurementSettings
"""


from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import list_with_selected_item, overridable
from mastapy.utility.units_and_measurements import _1571
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.utility.units_and_measurements.measurements import (
    _1578, _1579, _1580, _1581,
    _1582, _1583, _1584, _1585,
    _1586, _1587, _1588, _1589,
    _1590, _1591, _1592, _1593,
    _1594, _1595, _1596, _1597,
    _1598, _1599, _1600, _1601,
    _1602, _1603, _1604, _1605,
    _1606, _1607, _1608, _1609,
    _1610, _1611, _1612, _1613,
    _1614, _1615, _1616, _1617,
    _1618, _1619, _1620, _1621,
    _1622, _1623, _1624, _1625,
    _1626, _1627, _1628, _1629,
    _1630, _1631, _1632, _1633,
    _1634, _1635, _1636, _1637,
    _1638, _1639, _1640, _1641,
    _1642, _1643, _1644, _1645,
    _1646, _1647, _1648, _1649,
    _1650, _1651, _1652, _1653,
    _1654, _1655, _1656, _1657,
    _1658, _1659, _1660, _1661,
    _1662, _1663, _1664, _1665,
    _1666, _1667, _1668, _1669,
    _1670, _1671, _1672, _1673,
    _1674, _1675, _1676, _1677,
    _1678, _1679, _1680, _1681,
    _1682, _1683, _1684, _1685,
    _1686, _1687, _1688, _1689,
    _1690, _1691, _1692, _1693,
    _1694, _1695, _1696, _1697,
    _1698, _1699, _1700, _1701,
    _1702, _1703, _1704
)
from mastapy._internal.cast_exception import CastException
from mastapy.units_and_measurements import _7485
from mastapy.utility import _1560
from mastapy._internal.python_net import python_net_import

_MEASUREMENT_SETTINGS = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements', 'MeasurementSettings')


__docformat__ = 'restructuredtext en'
__all__ = ('MeasurementSettings',)


class MeasurementSettings(_1560.PerMachineSettings):
    """MeasurementSettings

    This is a mastapy class.
    """

    TYPE = _MEASUREMENT_SETTINGS

    def __init__(self, instance_to_wrap: 'MeasurementSettings.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def large_number_cutoff(self) -> 'float':
        """float: 'LargeNumberCutoff' is the original name of this property."""

        temp = self.wrapped.LargeNumberCutoff

        if temp is None:
            return 0.0

        return temp

    @large_number_cutoff.setter
    def large_number_cutoff(self, value: 'float'):
        self.wrapped.LargeNumberCutoff = float(value) if value else 0.0

    @property
    def number_decimal_separator(self) -> 'str':
        """str: 'NumberDecimalSeparator' is the original name of this property."""

        temp = self.wrapped.NumberDecimalSeparator

        if temp is None:
            return ''

        return temp

    @number_decimal_separator.setter
    def number_decimal_separator(self, value: 'str'):
        self.wrapped.NumberDecimalSeparator = str(value) if value else ''

    @property
    def number_group_separator(self) -> 'str':
        """str: 'NumberGroupSeparator' is the original name of this property."""

        temp = self.wrapped.NumberGroupSeparator

        if temp is None:
            return ''

        return temp

    @number_group_separator.setter
    def number_group_separator(self, value: 'str'):
        self.wrapped.NumberGroupSeparator = str(value) if value else ''

    @property
    def sample_input(self) -> 'str':
        """str: 'SampleInput' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SampleInput

        if temp is None:
            return ''

        return temp

    @property
    def sample_output(self) -> 'str':
        """str: 'SampleOutput' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SampleOutput

        if temp is None:
            return ''

        return temp

    @property
    def selected_measurement(self) -> 'list_with_selected_item.ListWithSelectedItem_MeasurementBase':
        """list_with_selected_item.ListWithSelectedItem_MeasurementBase: 'SelectedMeasurement' is the original name of this property."""

        temp = self.wrapped.SelectedMeasurement

        if temp is None:
            return None

        return constructor.new_from_mastapy_type(list_with_selected_item.ListWithSelectedItem_MeasurementBase)(temp) if temp is not None else None

    @selected_measurement.setter
    def selected_measurement(self, value: 'list_with_selected_item.ListWithSelectedItem_MeasurementBase.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_MeasurementBase.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_MeasurementBase.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value is not None else None)
        self.wrapped.SelectedMeasurement = value

    @property
    def show_trailing_zeros(self) -> 'bool':
        """bool: 'ShowTrailingZeros' is the original name of this property."""

        temp = self.wrapped.ShowTrailingZeros

        if temp is None:
            return False

        return temp

    @show_trailing_zeros.setter
    def show_trailing_zeros(self, value: 'bool'):
        self.wrapped.ShowTrailingZeros = bool(value) if value else False

    @property
    def small_number_cutoff(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'SmallNumberCutoff' is the original name of this property."""

        temp = self.wrapped.SmallNumberCutoff

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @small_number_cutoff.setter
    def small_number_cutoff(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.SmallNumberCutoff = value

    @property
    def current_selected_measurement(self) -> '_1571.MeasurementBase':
        """MeasurementBase: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1571.MeasurementBase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to MeasurementBase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_acceleration(self) -> '_1578.Acceleration':
        """Acceleration: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1578.Acceleration.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Acceleration. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_angle(self) -> '_1579.Angle':
        """Angle: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1579.Angle.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Angle. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_angle_per_unit_temperature(self) -> '_1580.AnglePerUnitTemperature':
        """AnglePerUnitTemperature: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1580.AnglePerUnitTemperature.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to AnglePerUnitTemperature. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_angle_small(self) -> '_1581.AngleSmall':
        """AngleSmall: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1581.AngleSmall.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to AngleSmall. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_angle_very_small(self) -> '_1582.AngleVerySmall':
        """AngleVerySmall: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1582.AngleVerySmall.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to AngleVerySmall. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_angular_acceleration(self) -> '_1583.AngularAcceleration':
        """AngularAcceleration: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1583.AngularAcceleration.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to AngularAcceleration. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_angular_compliance(self) -> '_1584.AngularCompliance':
        """AngularCompliance: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1584.AngularCompliance.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to AngularCompliance. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_angular_jerk(self) -> '_1585.AngularJerk':
        """AngularJerk: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1585.AngularJerk.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to AngularJerk. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_angular_stiffness(self) -> '_1586.AngularStiffness':
        """AngularStiffness: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1586.AngularStiffness.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to AngularStiffness. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_angular_velocity(self) -> '_1587.AngularVelocity':
        """AngularVelocity: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1587.AngularVelocity.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to AngularVelocity. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_area(self) -> '_1588.Area':
        """Area: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1588.Area.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Area. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_area_small(self) -> '_1589.AreaSmall':
        """AreaSmall: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1589.AreaSmall.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to AreaSmall. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_carbon_emission_factor(self) -> '_1590.CarbonEmissionFactor':
        """CarbonEmissionFactor: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1590.CarbonEmissionFactor.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to CarbonEmissionFactor. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_current_density(self) -> '_1591.CurrentDensity':
        """CurrentDensity: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1591.CurrentDensity.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to CurrentDensity. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_current_per_length(self) -> '_1592.CurrentPerLength':
        """CurrentPerLength: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1592.CurrentPerLength.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to CurrentPerLength. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_cycles(self) -> '_1593.Cycles':
        """Cycles: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1593.Cycles.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Cycles. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_damage(self) -> '_1594.Damage':
        """Damage: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1594.Damage.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Damage. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_damage_rate(self) -> '_1595.DamageRate':
        """DamageRate: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1595.DamageRate.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to DamageRate. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_data_size(self) -> '_1596.DataSize':
        """DataSize: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1596.DataSize.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to DataSize. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_decibel(self) -> '_1597.Decibel':
        """Decibel: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1597.Decibel.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Decibel. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_density(self) -> '_1598.Density':
        """Density: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1598.Density.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Density. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_electrical_resistance(self) -> '_1599.ElectricalResistance':
        """ElectricalResistance: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1599.ElectricalResistance.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to ElectricalResistance. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_electrical_resistivity(self) -> '_1600.ElectricalResistivity':
        """ElectricalResistivity: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1600.ElectricalResistivity.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to ElectricalResistivity. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_electric_current(self) -> '_1601.ElectricCurrent':
        """ElectricCurrent: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1601.ElectricCurrent.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to ElectricCurrent. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_energy(self) -> '_1602.Energy':
        """Energy: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1602.Energy.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Energy. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_energy_per_unit_area(self) -> '_1603.EnergyPerUnitArea':
        """EnergyPerUnitArea: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1603.EnergyPerUnitArea.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to EnergyPerUnitArea. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_energy_per_unit_area_small(self) -> '_1604.EnergyPerUnitAreaSmall':
        """EnergyPerUnitAreaSmall: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1604.EnergyPerUnitAreaSmall.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to EnergyPerUnitAreaSmall. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_energy_small(self) -> '_1605.EnergySmall':
        """EnergySmall: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1605.EnergySmall.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to EnergySmall. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_enum(self) -> '_1606.Enum':
        """Enum: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1606.Enum.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Enum. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_flow_rate(self) -> '_1607.FlowRate':
        """FlowRate: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1607.FlowRate.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to FlowRate. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_force(self) -> '_1608.Force':
        """Force: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1608.Force.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Force. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_force_per_unit_length(self) -> '_1609.ForcePerUnitLength':
        """ForcePerUnitLength: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1609.ForcePerUnitLength.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to ForcePerUnitLength. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_force_per_unit_pressure(self) -> '_1610.ForcePerUnitPressure':
        """ForcePerUnitPressure: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1610.ForcePerUnitPressure.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to ForcePerUnitPressure. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_force_per_unit_temperature(self) -> '_1611.ForcePerUnitTemperature':
        """ForcePerUnitTemperature: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1611.ForcePerUnitTemperature.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to ForcePerUnitTemperature. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_fraction_measurement_base(self) -> '_1612.FractionMeasurementBase':
        """FractionMeasurementBase: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1612.FractionMeasurementBase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to FractionMeasurementBase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_fraction_per_temperature(self) -> '_1613.FractionPerTemperature':
        """FractionPerTemperature: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1613.FractionPerTemperature.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to FractionPerTemperature. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_frequency(self) -> '_1614.Frequency':
        """Frequency: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1614.Frequency.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Frequency. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_fuel_consumption_engine(self) -> '_1615.FuelConsumptionEngine':
        """FuelConsumptionEngine: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1615.FuelConsumptionEngine.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to FuelConsumptionEngine. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_fuel_efficiency_vehicle(self) -> '_1616.FuelEfficiencyVehicle':
        """FuelEfficiencyVehicle: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1616.FuelEfficiencyVehicle.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to FuelEfficiencyVehicle. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_gradient(self) -> '_1617.Gradient':
        """Gradient: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1617.Gradient.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Gradient. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_heat_conductivity(self) -> '_1618.HeatConductivity':
        """HeatConductivity: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1618.HeatConductivity.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to HeatConductivity. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_heat_transfer(self) -> '_1619.HeatTransfer':
        """HeatTransfer: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1619.HeatTransfer.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to HeatTransfer. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_heat_transfer_coefficient_for_plastic_gear_tooth(self) -> '_1620.HeatTransferCoefficientForPlasticGearTooth':
        """HeatTransferCoefficientForPlasticGearTooth: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1620.HeatTransferCoefficientForPlasticGearTooth.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to HeatTransferCoefficientForPlasticGearTooth. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_heat_transfer_resistance(self) -> '_1621.HeatTransferResistance':
        """HeatTransferResistance: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1621.HeatTransferResistance.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to HeatTransferResistance. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_impulse(self) -> '_1622.Impulse':
        """Impulse: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1622.Impulse.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Impulse. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_index(self) -> '_1623.Index':
        """Index: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1623.Index.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Index. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_inductance(self) -> '_1624.Inductance':
        """Inductance: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1624.Inductance.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Inductance. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_integer(self) -> '_1625.Integer':
        """Integer: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1625.Integer.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Integer. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_inverse_short_length(self) -> '_1626.InverseShortLength':
        """InverseShortLength: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1626.InverseShortLength.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to InverseShortLength. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_inverse_short_time(self) -> '_1627.InverseShortTime':
        """InverseShortTime: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1627.InverseShortTime.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to InverseShortTime. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_jerk(self) -> '_1628.Jerk':
        """Jerk: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1628.Jerk.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Jerk. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_kinematic_viscosity(self) -> '_1629.KinematicViscosity':
        """KinematicViscosity: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1629.KinematicViscosity.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to KinematicViscosity. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_length_long(self) -> '_1630.LengthLong':
        """LengthLong: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1630.LengthLong.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to LengthLong. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_length_medium(self) -> '_1631.LengthMedium':
        """LengthMedium: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1631.LengthMedium.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to LengthMedium. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_length_per_unit_temperature(self) -> '_1632.LengthPerUnitTemperature':
        """LengthPerUnitTemperature: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1632.LengthPerUnitTemperature.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to LengthPerUnitTemperature. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_length_short(self) -> '_1633.LengthShort':
        """LengthShort: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1633.LengthShort.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to LengthShort. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_length_to_the_fourth(self) -> '_1634.LengthToTheFourth':
        """LengthToTheFourth: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1634.LengthToTheFourth.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to LengthToTheFourth. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_length_very_long(self) -> '_1635.LengthVeryLong':
        """LengthVeryLong: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1635.LengthVeryLong.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to LengthVeryLong. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_length_very_short(self) -> '_1636.LengthVeryShort':
        """LengthVeryShort: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1636.LengthVeryShort.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to LengthVeryShort. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_length_very_short_per_length_short(self) -> '_1637.LengthVeryShortPerLengthShort':
        """LengthVeryShortPerLengthShort: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1637.LengthVeryShortPerLengthShort.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to LengthVeryShortPerLengthShort. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_linear_angular_damping(self) -> '_1638.LinearAngularDamping':
        """LinearAngularDamping: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1638.LinearAngularDamping.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to LinearAngularDamping. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_linear_angular_stiffness_cross_term(self) -> '_1639.LinearAngularStiffnessCrossTerm':
        """LinearAngularStiffnessCrossTerm: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1639.LinearAngularStiffnessCrossTerm.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to LinearAngularStiffnessCrossTerm. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_linear_damping(self) -> '_1640.LinearDamping':
        """LinearDamping: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1640.LinearDamping.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to LinearDamping. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_linear_flexibility(self) -> '_1641.LinearFlexibility':
        """LinearFlexibility: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1641.LinearFlexibility.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to LinearFlexibility. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_linear_stiffness(self) -> '_1642.LinearStiffness':
        """LinearStiffness: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1642.LinearStiffness.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to LinearStiffness. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_magnetic_field_strength(self) -> '_1643.MagneticFieldStrength':
        """MagneticFieldStrength: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1643.MagneticFieldStrength.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to MagneticFieldStrength. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_magnetic_flux(self) -> '_1644.MagneticFlux':
        """MagneticFlux: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1644.MagneticFlux.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to MagneticFlux. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_magnetic_flux_density(self) -> '_1645.MagneticFluxDensity':
        """MagneticFluxDensity: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1645.MagneticFluxDensity.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to MagneticFluxDensity. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_magnetic_vector_potential(self) -> '_1646.MagneticVectorPotential':
        """MagneticVectorPotential: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1646.MagneticVectorPotential.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to MagneticVectorPotential. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_magnetomotive_force(self) -> '_1647.MagnetomotiveForce':
        """MagnetomotiveForce: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1647.MagnetomotiveForce.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to MagnetomotiveForce. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_mass(self) -> '_1648.Mass':
        """Mass: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1648.Mass.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Mass. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_mass_per_unit_length(self) -> '_1649.MassPerUnitLength':
        """MassPerUnitLength: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1649.MassPerUnitLength.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to MassPerUnitLength. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_mass_per_unit_time(self) -> '_1650.MassPerUnitTime':
        """MassPerUnitTime: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1650.MassPerUnitTime.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to MassPerUnitTime. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_moment_of_inertia(self) -> '_1651.MomentOfInertia':
        """MomentOfInertia: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1651.MomentOfInertia.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to MomentOfInertia. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_moment_of_inertia_per_unit_length(self) -> '_1652.MomentOfInertiaPerUnitLength':
        """MomentOfInertiaPerUnitLength: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1652.MomentOfInertiaPerUnitLength.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to MomentOfInertiaPerUnitLength. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_moment_per_unit_pressure(self) -> '_1653.MomentPerUnitPressure':
        """MomentPerUnitPressure: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1653.MomentPerUnitPressure.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to MomentPerUnitPressure. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_number(self) -> '_1654.Number':
        """Number: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1654.Number.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Number. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_percentage(self) -> '_1655.Percentage':
        """Percentage: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1655.Percentage.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Percentage. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_power(self) -> '_1656.Power':
        """Power: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1656.Power.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Power. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_power_per_small_area(self) -> '_1657.PowerPerSmallArea':
        """PowerPerSmallArea: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1657.PowerPerSmallArea.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to PowerPerSmallArea. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_power_per_unit_time(self) -> '_1658.PowerPerUnitTime':
        """PowerPerUnitTime: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1658.PowerPerUnitTime.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to PowerPerUnitTime. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_power_small(self) -> '_1659.PowerSmall':
        """PowerSmall: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1659.PowerSmall.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to PowerSmall. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_power_small_per_area(self) -> '_1660.PowerSmallPerArea':
        """PowerSmallPerArea: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1660.PowerSmallPerArea.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to PowerSmallPerArea. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_power_small_per_mass(self) -> '_1661.PowerSmallPerMass':
        """PowerSmallPerMass: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1661.PowerSmallPerMass.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to PowerSmallPerMass. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_power_small_per_unit_area_per_unit_time(self) -> '_1662.PowerSmallPerUnitAreaPerUnitTime':
        """PowerSmallPerUnitAreaPerUnitTime: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1662.PowerSmallPerUnitAreaPerUnitTime.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to PowerSmallPerUnitAreaPerUnitTime. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_power_small_per_unit_time(self) -> '_1663.PowerSmallPerUnitTime':
        """PowerSmallPerUnitTime: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1663.PowerSmallPerUnitTime.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to PowerSmallPerUnitTime. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_power_small_per_volume(self) -> '_1664.PowerSmallPerVolume':
        """PowerSmallPerVolume: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1664.PowerSmallPerVolume.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to PowerSmallPerVolume. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_pressure(self) -> '_1665.Pressure':
        """Pressure: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1665.Pressure.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Pressure. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_pressure_per_unit_time(self) -> '_1666.PressurePerUnitTime':
        """PressurePerUnitTime: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1666.PressurePerUnitTime.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to PressurePerUnitTime. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_pressure_velocity_product(self) -> '_1667.PressureVelocityProduct':
        """PressureVelocityProduct: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1667.PressureVelocityProduct.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to PressureVelocityProduct. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_pressure_viscosity_coefficient(self) -> '_1668.PressureViscosityCoefficient':
        """PressureViscosityCoefficient: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1668.PressureViscosityCoefficient.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to PressureViscosityCoefficient. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_price(self) -> '_1669.Price':
        """Price: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1669.Price.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Price. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_price_per_unit_mass(self) -> '_1670.PricePerUnitMass':
        """PricePerUnitMass: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1670.PricePerUnitMass.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to PricePerUnitMass. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_quadratic_angular_damping(self) -> '_1671.QuadraticAngularDamping':
        """QuadraticAngularDamping: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1671.QuadraticAngularDamping.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to QuadraticAngularDamping. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_quadratic_drag(self) -> '_1672.QuadraticDrag':
        """QuadraticDrag: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1672.QuadraticDrag.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to QuadraticDrag. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_rescaled_measurement(self) -> '_1673.RescaledMeasurement':
        """RescaledMeasurement: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1673.RescaledMeasurement.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to RescaledMeasurement. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_rotatum(self) -> '_1674.Rotatum':
        """Rotatum: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1674.Rotatum.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Rotatum. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_safety_factor(self) -> '_1675.SafetyFactor':
        """SafetyFactor: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1675.SafetyFactor.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to SafetyFactor. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_specific_acoustic_impedance(self) -> '_1676.SpecificAcousticImpedance':
        """SpecificAcousticImpedance: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1676.SpecificAcousticImpedance.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to SpecificAcousticImpedance. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_specific_heat(self) -> '_1677.SpecificHeat':
        """SpecificHeat: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1677.SpecificHeat.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to SpecificHeat. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_square_root_of_unit_force_per_unit_area(self) -> '_1678.SquareRootOfUnitForcePerUnitArea':
        """SquareRootOfUnitForcePerUnitArea: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1678.SquareRootOfUnitForcePerUnitArea.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to SquareRootOfUnitForcePerUnitArea. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_stiffness_per_unit_face_width(self) -> '_1679.StiffnessPerUnitFaceWidth':
        """StiffnessPerUnitFaceWidth: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1679.StiffnessPerUnitFaceWidth.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to StiffnessPerUnitFaceWidth. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_stress(self) -> '_1680.Stress':
        """Stress: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1680.Stress.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Stress. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_temperature(self) -> '_1681.Temperature':
        """Temperature: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1681.Temperature.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Temperature. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_temperature_difference(self) -> '_1682.TemperatureDifference':
        """TemperatureDifference: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1682.TemperatureDifference.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to TemperatureDifference. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_temperature_per_unit_time(self) -> '_1683.TemperaturePerUnitTime':
        """TemperaturePerUnitTime: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1683.TemperaturePerUnitTime.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to TemperaturePerUnitTime. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_text(self) -> '_1684.Text':
        """Text: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1684.Text.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Text. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_thermal_contact_coefficient(self) -> '_1685.ThermalContactCoefficient':
        """ThermalContactCoefficient: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1685.ThermalContactCoefficient.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to ThermalContactCoefficient. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_thermal_expansion_coefficient(self) -> '_1686.ThermalExpansionCoefficient':
        """ThermalExpansionCoefficient: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1686.ThermalExpansionCoefficient.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to ThermalExpansionCoefficient. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_thermo_elastic_factor(self) -> '_1687.ThermoElasticFactor':
        """ThermoElasticFactor: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1687.ThermoElasticFactor.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to ThermoElasticFactor. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_time(self) -> '_1688.Time':
        """Time: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1688.Time.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Time. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_time_short(self) -> '_1689.TimeShort':
        """TimeShort: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1689.TimeShort.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to TimeShort. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_time_very_short(self) -> '_1690.TimeVeryShort':
        """TimeVeryShort: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1690.TimeVeryShort.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to TimeVeryShort. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_torque(self) -> '_1691.Torque':
        """Torque: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1691.Torque.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Torque. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_torque_converter_inverse_k(self) -> '_1692.TorqueConverterInverseK':
        """TorqueConverterInverseK: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1692.TorqueConverterInverseK.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to TorqueConverterInverseK. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_torque_converter_k(self) -> '_1693.TorqueConverterK':
        """TorqueConverterK: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1693.TorqueConverterK.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to TorqueConverterK. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_torque_per_current(self) -> '_1694.TorquePerCurrent':
        """TorquePerCurrent: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1694.TorquePerCurrent.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to TorquePerCurrent. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_torque_per_square_root_of_power(self) -> '_1695.TorquePerSquareRootOfPower':
        """TorquePerSquareRootOfPower: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1695.TorquePerSquareRootOfPower.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to TorquePerSquareRootOfPower. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_torque_per_unit_temperature(self) -> '_1696.TorquePerUnitTemperature':
        """TorquePerUnitTemperature: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1696.TorquePerUnitTemperature.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to TorquePerUnitTemperature. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_velocity(self) -> '_1697.Velocity':
        """Velocity: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1697.Velocity.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Velocity. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_velocity_small(self) -> '_1698.VelocitySmall':
        """VelocitySmall: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1698.VelocitySmall.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to VelocitySmall. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_viscosity(self) -> '_1699.Viscosity':
        """Viscosity: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1699.Viscosity.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Viscosity. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_voltage(self) -> '_1700.Voltage':
        """Voltage: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1700.Voltage.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Voltage. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_voltage_per_angular_velocity(self) -> '_1701.VoltagePerAngularVelocity':
        """VoltagePerAngularVelocity: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1701.VoltagePerAngularVelocity.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to VoltagePerAngularVelocity. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_volume(self) -> '_1702.Volume':
        """Volume: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1702.Volume.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Volume. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_wear_coefficient(self) -> '_1703.WearCoefficient':
        """WearCoefficient: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1703.WearCoefficient.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to WearCoefficient. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_yank(self) -> '_1704.Yank':
        """Yank: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1704.Yank.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Yank. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    def default_to_imperial(self):
        """ 'DefaultToImperial' is the original name of this method."""

        self.wrapped.DefaultToImperial()

    def default_to_metric(self):
        """ 'DefaultToMetric' is the original name of this method."""

        self.wrapped.DefaultToMetric()

    def find_measurement_by_name(self, name: 'str') -> '_1571.MeasurementBase':
        """ 'FindMeasurementByName' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.utility.units_and_measurements.MeasurementBase
        """

        name = str(name)
        method_result = self.wrapped.FindMeasurementByName(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_measurement(self, measurement_type: '_7485.MeasurementType') -> '_1571.MeasurementBase':
        """ 'GetMeasurement' is the original name of this method.

        Args:
            measurement_type (mastapy.units_and_measurements.MeasurementType)

        Returns:
            mastapy.utility.units_and_measurements.MeasurementBase
        """

        measurement_type = conversion.mp_to_pn_enum(measurement_type)
        method_result = self.wrapped.GetMeasurement(measurement_type)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None
