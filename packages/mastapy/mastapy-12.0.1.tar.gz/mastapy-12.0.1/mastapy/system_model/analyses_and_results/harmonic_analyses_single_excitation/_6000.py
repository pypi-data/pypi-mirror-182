"""_6000.py

HarmonicAnalysisOfSingleExcitation
"""


from mastapy.system_model.analyses_and_results.harmonic_analyses import (
    _5616, _5669, _5670, _5671,
    _5672, _5673, _5674, _5675,
    _5676, _5677, _5678, _5679,
    _5689, _5691, _5692, _5694,
    _5723, _5740, _5765
)
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.analysis_cases import _7475
from mastapy._internal.python_net import python_net_import

_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation', 'HarmonicAnalysisOfSingleExcitation')


__docformat__ = 'restructuredtext en'
__all__ = ('HarmonicAnalysisOfSingleExcitation',)


class HarmonicAnalysisOfSingleExcitation(_7475.StaticLoadAnalysisCase):
    """HarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    def __init__(self, instance_to_wrap: 'HarmonicAnalysisOfSingleExcitation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def excitation_detail(self) -> '_5616.AbstractPeriodicExcitationDetail':
        """AbstractPeriodicExcitationDetail: 'ExcitationDetail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ExcitationDetail

        if temp is None:
            return None

        if _5616.AbstractPeriodicExcitationDetail.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast excitation_detail to AbstractPeriodicExcitationDetail. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def excitation_detail_of_type_electric_machine_periodic_excitation_detail(self) -> '_5669.ElectricMachinePeriodicExcitationDetail':
        """ElectricMachinePeriodicExcitationDetail: 'ExcitationDetail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ExcitationDetail

        if temp is None:
            return None

        if _5669.ElectricMachinePeriodicExcitationDetail.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast excitation_detail to ElectricMachinePeriodicExcitationDetail. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def excitation_detail_of_type_electric_machine_rotor_x_force_periodic_excitation_detail(self) -> '_5670.ElectricMachineRotorXForcePeriodicExcitationDetail':
        """ElectricMachineRotorXForcePeriodicExcitationDetail: 'ExcitationDetail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ExcitationDetail

        if temp is None:
            return None

        if _5670.ElectricMachineRotorXForcePeriodicExcitationDetail.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast excitation_detail to ElectricMachineRotorXForcePeriodicExcitationDetail. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def excitation_detail_of_type_electric_machine_rotor_x_moment_periodic_excitation_detail(self) -> '_5671.ElectricMachineRotorXMomentPeriodicExcitationDetail':
        """ElectricMachineRotorXMomentPeriodicExcitationDetail: 'ExcitationDetail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ExcitationDetail

        if temp is None:
            return None

        if _5671.ElectricMachineRotorXMomentPeriodicExcitationDetail.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast excitation_detail to ElectricMachineRotorXMomentPeriodicExcitationDetail. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def excitation_detail_of_type_electric_machine_rotor_y_force_periodic_excitation_detail(self) -> '_5672.ElectricMachineRotorYForcePeriodicExcitationDetail':
        """ElectricMachineRotorYForcePeriodicExcitationDetail: 'ExcitationDetail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ExcitationDetail

        if temp is None:
            return None

        if _5672.ElectricMachineRotorYForcePeriodicExcitationDetail.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast excitation_detail to ElectricMachineRotorYForcePeriodicExcitationDetail. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def excitation_detail_of_type_electric_machine_rotor_y_moment_periodic_excitation_detail(self) -> '_5673.ElectricMachineRotorYMomentPeriodicExcitationDetail':
        """ElectricMachineRotorYMomentPeriodicExcitationDetail: 'ExcitationDetail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ExcitationDetail

        if temp is None:
            return None

        if _5673.ElectricMachineRotorYMomentPeriodicExcitationDetail.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast excitation_detail to ElectricMachineRotorYMomentPeriodicExcitationDetail. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def excitation_detail_of_type_electric_machine_rotor_z_force_periodic_excitation_detail(self) -> '_5674.ElectricMachineRotorZForcePeriodicExcitationDetail':
        """ElectricMachineRotorZForcePeriodicExcitationDetail: 'ExcitationDetail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ExcitationDetail

        if temp is None:
            return None

        if _5674.ElectricMachineRotorZForcePeriodicExcitationDetail.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast excitation_detail to ElectricMachineRotorZForcePeriodicExcitationDetail. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def excitation_detail_of_type_electric_machine_stator_tooth_axial_loads_excitation_detail(self) -> '_5675.ElectricMachineStatorToothAxialLoadsExcitationDetail':
        """ElectricMachineStatorToothAxialLoadsExcitationDetail: 'ExcitationDetail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ExcitationDetail

        if temp is None:
            return None

        if _5675.ElectricMachineStatorToothAxialLoadsExcitationDetail.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast excitation_detail to ElectricMachineStatorToothAxialLoadsExcitationDetail. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def excitation_detail_of_type_electric_machine_stator_tooth_loads_excitation_detail(self) -> '_5676.ElectricMachineStatorToothLoadsExcitationDetail':
        """ElectricMachineStatorToothLoadsExcitationDetail: 'ExcitationDetail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ExcitationDetail

        if temp is None:
            return None

        if _5676.ElectricMachineStatorToothLoadsExcitationDetail.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast excitation_detail to ElectricMachineStatorToothLoadsExcitationDetail. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def excitation_detail_of_type_electric_machine_stator_tooth_radial_loads_excitation_detail(self) -> '_5677.ElectricMachineStatorToothRadialLoadsExcitationDetail':
        """ElectricMachineStatorToothRadialLoadsExcitationDetail: 'ExcitationDetail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ExcitationDetail

        if temp is None:
            return None

        if _5677.ElectricMachineStatorToothRadialLoadsExcitationDetail.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast excitation_detail to ElectricMachineStatorToothRadialLoadsExcitationDetail. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def excitation_detail_of_type_electric_machine_stator_tooth_tangential_loads_excitation_detail(self) -> '_5678.ElectricMachineStatorToothTangentialLoadsExcitationDetail':
        """ElectricMachineStatorToothTangentialLoadsExcitationDetail: 'ExcitationDetail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ExcitationDetail

        if temp is None:
            return None

        if _5678.ElectricMachineStatorToothTangentialLoadsExcitationDetail.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast excitation_detail to ElectricMachineStatorToothTangentialLoadsExcitationDetail. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def excitation_detail_of_type_electric_machine_torque_ripple_periodic_excitation_detail(self) -> '_5679.ElectricMachineTorqueRipplePeriodicExcitationDetail':
        """ElectricMachineTorqueRipplePeriodicExcitationDetail: 'ExcitationDetail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ExcitationDetail

        if temp is None:
            return None

        if _5679.ElectricMachineTorqueRipplePeriodicExcitationDetail.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast excitation_detail to ElectricMachineTorqueRipplePeriodicExcitationDetail. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def excitation_detail_of_type_gear_mesh_excitation_detail(self) -> '_5689.GearMeshExcitationDetail':
        """GearMeshExcitationDetail: 'ExcitationDetail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ExcitationDetail

        if temp is None:
            return None

        if _5689.GearMeshExcitationDetail.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast excitation_detail to GearMeshExcitationDetail. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def excitation_detail_of_type_gear_mesh_misalignment_excitation_detail(self) -> '_5691.GearMeshMisalignmentExcitationDetail':
        """GearMeshMisalignmentExcitationDetail: 'ExcitationDetail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ExcitationDetail

        if temp is None:
            return None

        if _5691.GearMeshMisalignmentExcitationDetail.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast excitation_detail to GearMeshMisalignmentExcitationDetail. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def excitation_detail_of_type_gear_mesh_te_excitation_detail(self) -> '_5692.GearMeshTEExcitationDetail':
        """GearMeshTEExcitationDetail: 'ExcitationDetail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ExcitationDetail

        if temp is None:
            return None

        if _5692.GearMeshTEExcitationDetail.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast excitation_detail to GearMeshTEExcitationDetail. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def excitation_detail_of_type_general_periodic_excitation_detail(self) -> '_5694.GeneralPeriodicExcitationDetail':
        """GeneralPeriodicExcitationDetail: 'ExcitationDetail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ExcitationDetail

        if temp is None:
            return None

        if _5694.GeneralPeriodicExcitationDetail.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast excitation_detail to GeneralPeriodicExcitationDetail. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def excitation_detail_of_type_periodic_excitation_with_reference_shaft(self) -> '_5723.PeriodicExcitationWithReferenceShaft':
        """PeriodicExcitationWithReferenceShaft: 'ExcitationDetail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ExcitationDetail

        if temp is None:
            return None

        if _5723.PeriodicExcitationWithReferenceShaft.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast excitation_detail to PeriodicExcitationWithReferenceShaft. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def excitation_detail_of_type_single_node_periodic_excitation_with_reference_shaft(self) -> '_5740.SingleNodePeriodicExcitationWithReferenceShaft':
        """SingleNodePeriodicExcitationWithReferenceShaft: 'ExcitationDetail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ExcitationDetail

        if temp is None:
            return None

        if _5740.SingleNodePeriodicExcitationWithReferenceShaft.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast excitation_detail to SingleNodePeriodicExcitationWithReferenceShaft. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def excitation_detail_of_type_unbalanced_mass_excitation_detail(self) -> '_5765.UnbalancedMassExcitationDetail':
        """UnbalancedMassExcitationDetail: 'ExcitationDetail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ExcitationDetail

        if temp is None:
            return None

        if _5765.UnbalancedMassExcitationDetail.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast excitation_detail to UnbalancedMassExcitationDetail. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
