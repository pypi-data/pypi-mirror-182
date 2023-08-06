"""_6018.py

PartHarmonicAnalysisOfSingleExcitation
"""


from mastapy.system_model.part_model import (
    _2421, _2387, _2388, _2389,
    _2390, _2393, _2395, _2396,
    _2397, _2400, _2401, _2405,
    _2406, _2407, _2408, _2415,
    _2416, _2417, _2419, _2422,
    _2424, _2425, _2427, _2429,
    _2430, _2432
)
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.part_model.shaft_model import _2435
from mastapy.system_model.part_model.gears import (
    _2465, _2466, _2467, _2468,
    _2469, _2470, _2471, _2472,
    _2473, _2474, _2475, _2476,
    _2477, _2478, _2479, _2480,
    _2481, _2482, _2484, _2486,
    _2487, _2488, _2489, _2490,
    _2491, _2492, _2493, _2494,
    _2495, _2496, _2497, _2498,
    _2499, _2500, _2501, _2502,
    _2503, _2504, _2505, _2506
)
from mastapy.system_model.part_model.cycloidal import _2520, _2521, _2522
from mastapy.system_model.part_model.couplings import (
    _2528, _2530, _2531, _2533,
    _2534, _2535, _2536, _2538,
    _2539, _2540, _2541, _2542,
    _2548, _2549, _2550, _2552,
    _2553, _2554, _2556, _2557,
    _2558, _2559, _2560, _2562
)
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5699
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6998
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6000
from mastapy.system_model.analyses_and_results.modal_analyses import (
    _4602, _4515, _4516, _4517,
    _4520, _4521, _4522, _4523,
    _4525, _4527, _4528, _4529,
    _4530, _4532, _4533, _4534,
    _4535, _4537, _4538, _4540,
    _4542, _4543, _4545, _4546,
    _4548, _4549, _4551, _4554,
    _4555, _4557, _4558, _4559,
    _4561, _4564, _4565, _4566,
    _4567, _4570, _4572, _4573,
    _4574, _4575, _4578, _4579,
    _4580, _4582, _4583, _4586,
    _4587, _4589, _4590, _4592,
    _4593, _4594, _4595, _4599,
    _4600, _4604, _4605, _4607,
    _4608, _4609, _4610, _4611,
    _4612, _4614, _4616, _4617,
    _4618, _4619, _4622, _4624,
    _4625, _4627, _4628, _4630,
    _4631, _4633, _4634, _4635,
    _4636, _4637, _4638, _4639,
    _4640, _4642, _4643, _4644,
    _4645, _4646, _4651, _4652,
    _4654, _4655
)
from mastapy.system_model.analyses_and_results.analysis_cases import _7473
from mastapy._internal.python_net import python_net_import

_PART_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation', 'PartHarmonicAnalysisOfSingleExcitation')


__docformat__ = 'restructuredtext en'
__all__ = ('PartHarmonicAnalysisOfSingleExcitation',)


class PartHarmonicAnalysisOfSingleExcitation(_7473.PartStaticLoadAnalysisCase):
    """PartHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _PART_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    def __init__(self, instance_to_wrap: 'PartHarmonicAnalysisOfSingleExcitation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2421.Part':
        """Part: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2421.Part.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to Part. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_assembly(self) -> '_2387.Assembly':
        """Assembly: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2387.Assembly.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to Assembly. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_abstract_assembly(self) -> '_2388.AbstractAssembly':
        """AbstractAssembly: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2388.AbstractAssembly.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to AbstractAssembly. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_abstract_shaft(self) -> '_2389.AbstractShaft':
        """AbstractShaft: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2389.AbstractShaft.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to AbstractShaft. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_abstract_shaft_or_housing(self) -> '_2390.AbstractShaftOrHousing':
        """AbstractShaftOrHousing: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2390.AbstractShaftOrHousing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to AbstractShaftOrHousing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_bearing(self) -> '_2393.Bearing':
        """Bearing: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2393.Bearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to Bearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_bolt(self) -> '_2395.Bolt':
        """Bolt: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2395.Bolt.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to Bolt. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_bolted_joint(self) -> '_2396.BoltedJoint':
        """BoltedJoint: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2396.BoltedJoint.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to BoltedJoint. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_component(self) -> '_2397.Component':
        """Component: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2397.Component.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to Component. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_connector(self) -> '_2400.Connector':
        """Connector: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2400.Connector.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to Connector. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_datum(self) -> '_2401.Datum':
        """Datum: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2401.Datum.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to Datum. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_external_cad_model(self) -> '_2405.ExternalCADModel':
        """ExternalCADModel: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2405.ExternalCADModel.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to ExternalCADModel. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_fe_part(self) -> '_2406.FEPart':
        """FEPart: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2406.FEPart.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to FEPart. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_flexible_pin_assembly(self) -> '_2407.FlexiblePinAssembly':
        """FlexiblePinAssembly: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2407.FlexiblePinAssembly.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to FlexiblePinAssembly. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_guide_dxf_model(self) -> '_2408.GuideDxfModel':
        """GuideDxfModel: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2408.GuideDxfModel.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to GuideDxfModel. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_mass_disc(self) -> '_2415.MassDisc':
        """MassDisc: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2415.MassDisc.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to MassDisc. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_measurement_component(self) -> '_2416.MeasurementComponent':
        """MeasurementComponent: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2416.MeasurementComponent.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to MeasurementComponent. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_mountable_component(self) -> '_2417.MountableComponent':
        """MountableComponent: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2417.MountableComponent.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to MountableComponent. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_oil_seal(self) -> '_2419.OilSeal':
        """OilSeal: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2419.OilSeal.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to OilSeal. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_planet_carrier(self) -> '_2422.PlanetCarrier':
        """PlanetCarrier: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2422.PlanetCarrier.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to PlanetCarrier. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_point_load(self) -> '_2424.PointLoad':
        """PointLoad: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2424.PointLoad.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to PointLoad. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_power_load(self) -> '_2425.PowerLoad':
        """PowerLoad: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2425.PowerLoad.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to PowerLoad. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_root_assembly(self) -> '_2427.RootAssembly':
        """RootAssembly: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2427.RootAssembly.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to RootAssembly. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_specialised_assembly(self) -> '_2429.SpecialisedAssembly':
        """SpecialisedAssembly: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2429.SpecialisedAssembly.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to SpecialisedAssembly. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_unbalanced_mass(self) -> '_2430.UnbalancedMass':
        """UnbalancedMass: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2430.UnbalancedMass.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to UnbalancedMass. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_virtual_component(self) -> '_2432.VirtualComponent':
        """VirtualComponent: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2432.VirtualComponent.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to VirtualComponent. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_shaft(self) -> '_2435.Shaft':
        """Shaft: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2435.Shaft.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to Shaft. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_agma_gleason_conical_gear(self) -> '_2465.AGMAGleasonConicalGear':
        """AGMAGleasonConicalGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2465.AGMAGleasonConicalGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to AGMAGleasonConicalGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_agma_gleason_conical_gear_set(self) -> '_2466.AGMAGleasonConicalGearSet':
        """AGMAGleasonConicalGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2466.AGMAGleasonConicalGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to AGMAGleasonConicalGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_bevel_differential_gear(self) -> '_2467.BevelDifferentialGear':
        """BevelDifferentialGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2467.BevelDifferentialGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to BevelDifferentialGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_bevel_differential_gear_set(self) -> '_2468.BevelDifferentialGearSet':
        """BevelDifferentialGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2468.BevelDifferentialGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to BevelDifferentialGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_bevel_differential_planet_gear(self) -> '_2469.BevelDifferentialPlanetGear':
        """BevelDifferentialPlanetGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2469.BevelDifferentialPlanetGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to BevelDifferentialPlanetGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_bevel_differential_sun_gear(self) -> '_2470.BevelDifferentialSunGear':
        """BevelDifferentialSunGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2470.BevelDifferentialSunGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to BevelDifferentialSunGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_bevel_gear(self) -> '_2471.BevelGear':
        """BevelGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2471.BevelGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to BevelGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_bevel_gear_set(self) -> '_2472.BevelGearSet':
        """BevelGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2472.BevelGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to BevelGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_concept_gear(self) -> '_2473.ConceptGear':
        """ConceptGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2473.ConceptGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to ConceptGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_concept_gear_set(self) -> '_2474.ConceptGearSet':
        """ConceptGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2474.ConceptGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to ConceptGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_conical_gear(self) -> '_2475.ConicalGear':
        """ConicalGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2475.ConicalGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to ConicalGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_conical_gear_set(self) -> '_2476.ConicalGearSet':
        """ConicalGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2476.ConicalGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to ConicalGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_cylindrical_gear(self) -> '_2477.CylindricalGear':
        """CylindricalGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2477.CylindricalGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to CylindricalGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_cylindrical_gear_set(self) -> '_2478.CylindricalGearSet':
        """CylindricalGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2478.CylindricalGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to CylindricalGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_cylindrical_planet_gear(self) -> '_2479.CylindricalPlanetGear':
        """CylindricalPlanetGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2479.CylindricalPlanetGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to CylindricalPlanetGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_face_gear(self) -> '_2480.FaceGear':
        """FaceGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2480.FaceGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to FaceGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_face_gear_set(self) -> '_2481.FaceGearSet':
        """FaceGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2481.FaceGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to FaceGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_gear(self) -> '_2482.Gear':
        """Gear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2482.Gear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to Gear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_gear_set(self) -> '_2484.GearSet':
        """GearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2484.GearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to GearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_hypoid_gear(self) -> '_2486.HypoidGear':
        """HypoidGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2486.HypoidGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to HypoidGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_hypoid_gear_set(self) -> '_2487.HypoidGearSet':
        """HypoidGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2487.HypoidGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to HypoidGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_klingelnberg_cyclo_palloid_conical_gear(self) -> '_2488.KlingelnbergCycloPalloidConicalGear':
        """KlingelnbergCycloPalloidConicalGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2488.KlingelnbergCycloPalloidConicalGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to KlingelnbergCycloPalloidConicalGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_klingelnberg_cyclo_palloid_conical_gear_set(self) -> '_2489.KlingelnbergCycloPalloidConicalGearSet':
        """KlingelnbergCycloPalloidConicalGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2489.KlingelnbergCycloPalloidConicalGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to KlingelnbergCycloPalloidConicalGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_klingelnberg_cyclo_palloid_hypoid_gear(self) -> '_2490.KlingelnbergCycloPalloidHypoidGear':
        """KlingelnbergCycloPalloidHypoidGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2490.KlingelnbergCycloPalloidHypoidGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to KlingelnbergCycloPalloidHypoidGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_klingelnberg_cyclo_palloid_hypoid_gear_set(self) -> '_2491.KlingelnbergCycloPalloidHypoidGearSet':
        """KlingelnbergCycloPalloidHypoidGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2491.KlingelnbergCycloPalloidHypoidGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to KlingelnbergCycloPalloidHypoidGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear(self) -> '_2492.KlingelnbergCycloPalloidSpiralBevelGear':
        """KlingelnbergCycloPalloidSpiralBevelGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2492.KlingelnbergCycloPalloidSpiralBevelGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to KlingelnbergCycloPalloidSpiralBevelGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_set(self) -> '_2493.KlingelnbergCycloPalloidSpiralBevelGearSet':
        """KlingelnbergCycloPalloidSpiralBevelGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2493.KlingelnbergCycloPalloidSpiralBevelGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to KlingelnbergCycloPalloidSpiralBevelGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_planetary_gear_set(self) -> '_2494.PlanetaryGearSet':
        """PlanetaryGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2494.PlanetaryGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to PlanetaryGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_spiral_bevel_gear(self) -> '_2495.SpiralBevelGear':
        """SpiralBevelGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2495.SpiralBevelGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to SpiralBevelGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_spiral_bevel_gear_set(self) -> '_2496.SpiralBevelGearSet':
        """SpiralBevelGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2496.SpiralBevelGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to SpiralBevelGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_straight_bevel_diff_gear(self) -> '_2497.StraightBevelDiffGear':
        """StraightBevelDiffGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2497.StraightBevelDiffGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to StraightBevelDiffGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_straight_bevel_diff_gear_set(self) -> '_2498.StraightBevelDiffGearSet':
        """StraightBevelDiffGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2498.StraightBevelDiffGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to StraightBevelDiffGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_straight_bevel_gear(self) -> '_2499.StraightBevelGear':
        """StraightBevelGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2499.StraightBevelGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to StraightBevelGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_straight_bevel_gear_set(self) -> '_2500.StraightBevelGearSet':
        """StraightBevelGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2500.StraightBevelGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to StraightBevelGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_straight_bevel_planet_gear(self) -> '_2501.StraightBevelPlanetGear':
        """StraightBevelPlanetGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2501.StraightBevelPlanetGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to StraightBevelPlanetGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_straight_bevel_sun_gear(self) -> '_2502.StraightBevelSunGear':
        """StraightBevelSunGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2502.StraightBevelSunGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to StraightBevelSunGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_worm_gear(self) -> '_2503.WormGear':
        """WormGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2503.WormGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to WormGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_worm_gear_set(self) -> '_2504.WormGearSet':
        """WormGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2504.WormGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to WormGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_zerol_bevel_gear(self) -> '_2505.ZerolBevelGear':
        """ZerolBevelGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2505.ZerolBevelGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to ZerolBevelGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_zerol_bevel_gear_set(self) -> '_2506.ZerolBevelGearSet':
        """ZerolBevelGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2506.ZerolBevelGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to ZerolBevelGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_cycloidal_assembly(self) -> '_2520.CycloidalAssembly':
        """CycloidalAssembly: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2520.CycloidalAssembly.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to CycloidalAssembly. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_cycloidal_disc(self) -> '_2521.CycloidalDisc':
        """CycloidalDisc: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2521.CycloidalDisc.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to CycloidalDisc. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_ring_pins(self) -> '_2522.RingPins':
        """RingPins: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2522.RingPins.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to RingPins. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_belt_drive(self) -> '_2528.BeltDrive':
        """BeltDrive: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2528.BeltDrive.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to BeltDrive. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_clutch(self) -> '_2530.Clutch':
        """Clutch: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2530.Clutch.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to Clutch. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_clutch_half(self) -> '_2531.ClutchHalf':
        """ClutchHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2531.ClutchHalf.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to ClutchHalf. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_concept_coupling(self) -> '_2533.ConceptCoupling':
        """ConceptCoupling: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2533.ConceptCoupling.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to ConceptCoupling. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_concept_coupling_half(self) -> '_2534.ConceptCouplingHalf':
        """ConceptCouplingHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2534.ConceptCouplingHalf.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to ConceptCouplingHalf. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_coupling(self) -> '_2535.Coupling':
        """Coupling: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2535.Coupling.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to Coupling. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_coupling_half(self) -> '_2536.CouplingHalf':
        """CouplingHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2536.CouplingHalf.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to CouplingHalf. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_cvt(self) -> '_2538.CVT':
        """CVT: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2538.CVT.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to CVT. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_cvt_pulley(self) -> '_2539.CVTPulley':
        """CVTPulley: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2539.CVTPulley.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to CVTPulley. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_part_to_part_shear_coupling(self) -> '_2540.PartToPartShearCoupling':
        """PartToPartShearCoupling: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2540.PartToPartShearCoupling.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to PartToPartShearCoupling. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_part_to_part_shear_coupling_half(self) -> '_2541.PartToPartShearCouplingHalf':
        """PartToPartShearCouplingHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2541.PartToPartShearCouplingHalf.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to PartToPartShearCouplingHalf. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_pulley(self) -> '_2542.Pulley':
        """Pulley: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2542.Pulley.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to Pulley. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_rolling_ring(self) -> '_2548.RollingRing':
        """RollingRing: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2548.RollingRing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to RollingRing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_rolling_ring_assembly(self) -> '_2549.RollingRingAssembly':
        """RollingRingAssembly: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2549.RollingRingAssembly.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to RollingRingAssembly. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_shaft_hub_connection(self) -> '_2550.ShaftHubConnection':
        """ShaftHubConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2550.ShaftHubConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to ShaftHubConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_spring_damper(self) -> '_2552.SpringDamper':
        """SpringDamper: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2552.SpringDamper.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to SpringDamper. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_spring_damper_half(self) -> '_2553.SpringDamperHalf':
        """SpringDamperHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2553.SpringDamperHalf.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to SpringDamperHalf. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_synchroniser(self) -> '_2554.Synchroniser':
        """Synchroniser: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2554.Synchroniser.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to Synchroniser. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_synchroniser_half(self) -> '_2556.SynchroniserHalf':
        """SynchroniserHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2556.SynchroniserHalf.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to SynchroniserHalf. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_synchroniser_part(self) -> '_2557.SynchroniserPart':
        """SynchroniserPart: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2557.SynchroniserPart.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to SynchroniserPart. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_synchroniser_sleeve(self) -> '_2558.SynchroniserSleeve':
        """SynchroniserSleeve: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2558.SynchroniserSleeve.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to SynchroniserSleeve. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_torque_converter(self) -> '_2559.TorqueConverter':
        """TorqueConverter: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2559.TorqueConverter.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to TorqueConverter. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_torque_converter_pump(self) -> '_2560.TorqueConverterPump':
        """TorqueConverterPump: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2560.TorqueConverterPump.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to TorqueConverterPump. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_torque_converter_turbine(self) -> '_2562.TorqueConverterTurbine':
        """TorqueConverterTurbine: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2562.TorqueConverterTurbine.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to TorqueConverterTurbine. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def harmonic_analysis_options(self) -> '_5699.HarmonicAnalysisOptions':
        """HarmonicAnalysisOptions: 'HarmonicAnalysisOptions' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HarmonicAnalysisOptions

        if temp is None:
            return None

        if _5699.HarmonicAnalysisOptions.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast harmonic_analysis_options to HarmonicAnalysisOptions. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def harmonic_analysis_of_single_excitation(self) -> '_6000.HarmonicAnalysisOfSingleExcitation':
        """HarmonicAnalysisOfSingleExcitation: 'HarmonicAnalysisOfSingleExcitation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HarmonicAnalysisOfSingleExcitation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis(self) -> '_4602.PartModalAnalysis':
        """PartModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4602.PartModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to PartModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_abstract_assembly_modal_analysis(self) -> '_4515.AbstractAssemblyModalAnalysis':
        """AbstractAssemblyModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4515.AbstractAssemblyModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to AbstractAssemblyModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_abstract_shaft_modal_analysis(self) -> '_4516.AbstractShaftModalAnalysis':
        """AbstractShaftModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4516.AbstractShaftModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to AbstractShaftModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_abstract_shaft_or_housing_modal_analysis(self) -> '_4517.AbstractShaftOrHousingModalAnalysis':
        """AbstractShaftOrHousingModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4517.AbstractShaftOrHousingModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to AbstractShaftOrHousingModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_agma_gleason_conical_gear_modal_analysis(self) -> '_4520.AGMAGleasonConicalGearModalAnalysis':
        """AGMAGleasonConicalGearModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4520.AGMAGleasonConicalGearModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to AGMAGleasonConicalGearModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_agma_gleason_conical_gear_set_modal_analysis(self) -> '_4521.AGMAGleasonConicalGearSetModalAnalysis':
        """AGMAGleasonConicalGearSetModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4521.AGMAGleasonConicalGearSetModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to AGMAGleasonConicalGearSetModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_assembly_modal_analysis(self) -> '_4522.AssemblyModalAnalysis':
        """AssemblyModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4522.AssemblyModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to AssemblyModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_bearing_modal_analysis(self) -> '_4523.BearingModalAnalysis':
        """BearingModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4523.BearingModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to BearingModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_belt_drive_modal_analysis(self) -> '_4525.BeltDriveModalAnalysis':
        """BeltDriveModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4525.BeltDriveModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to BeltDriveModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_bevel_differential_gear_modal_analysis(self) -> '_4527.BevelDifferentialGearModalAnalysis':
        """BevelDifferentialGearModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4527.BevelDifferentialGearModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to BevelDifferentialGearModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_bevel_differential_gear_set_modal_analysis(self) -> '_4528.BevelDifferentialGearSetModalAnalysis':
        """BevelDifferentialGearSetModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4528.BevelDifferentialGearSetModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to BevelDifferentialGearSetModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_bevel_differential_planet_gear_modal_analysis(self) -> '_4529.BevelDifferentialPlanetGearModalAnalysis':
        """BevelDifferentialPlanetGearModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4529.BevelDifferentialPlanetGearModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to BevelDifferentialPlanetGearModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_bevel_differential_sun_gear_modal_analysis(self) -> '_4530.BevelDifferentialSunGearModalAnalysis':
        """BevelDifferentialSunGearModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4530.BevelDifferentialSunGearModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to BevelDifferentialSunGearModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_bevel_gear_modal_analysis(self) -> '_4532.BevelGearModalAnalysis':
        """BevelGearModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4532.BevelGearModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to BevelGearModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_bevel_gear_set_modal_analysis(self) -> '_4533.BevelGearSetModalAnalysis':
        """BevelGearSetModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4533.BevelGearSetModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to BevelGearSetModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_bolted_joint_modal_analysis(self) -> '_4534.BoltedJointModalAnalysis':
        """BoltedJointModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4534.BoltedJointModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to BoltedJointModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_bolt_modal_analysis(self) -> '_4535.BoltModalAnalysis':
        """BoltModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4535.BoltModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to BoltModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_clutch_half_modal_analysis(self) -> '_4537.ClutchHalfModalAnalysis':
        """ClutchHalfModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4537.ClutchHalfModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to ClutchHalfModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_clutch_modal_analysis(self) -> '_4538.ClutchModalAnalysis':
        """ClutchModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4538.ClutchModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to ClutchModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_component_modal_analysis(self) -> '_4540.ComponentModalAnalysis':
        """ComponentModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4540.ComponentModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to ComponentModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_concept_coupling_half_modal_analysis(self) -> '_4542.ConceptCouplingHalfModalAnalysis':
        """ConceptCouplingHalfModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4542.ConceptCouplingHalfModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to ConceptCouplingHalfModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_concept_coupling_modal_analysis(self) -> '_4543.ConceptCouplingModalAnalysis':
        """ConceptCouplingModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4543.ConceptCouplingModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to ConceptCouplingModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_concept_gear_modal_analysis(self) -> '_4545.ConceptGearModalAnalysis':
        """ConceptGearModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4545.ConceptGearModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to ConceptGearModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_concept_gear_set_modal_analysis(self) -> '_4546.ConceptGearSetModalAnalysis':
        """ConceptGearSetModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4546.ConceptGearSetModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to ConceptGearSetModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_conical_gear_modal_analysis(self) -> '_4548.ConicalGearModalAnalysis':
        """ConicalGearModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4548.ConicalGearModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to ConicalGearModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_conical_gear_set_modal_analysis(self) -> '_4549.ConicalGearSetModalAnalysis':
        """ConicalGearSetModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4549.ConicalGearSetModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to ConicalGearSetModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_connector_modal_analysis(self) -> '_4551.ConnectorModalAnalysis':
        """ConnectorModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4551.ConnectorModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to ConnectorModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_coupling_half_modal_analysis(self) -> '_4554.CouplingHalfModalAnalysis':
        """CouplingHalfModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4554.CouplingHalfModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to CouplingHalfModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_coupling_modal_analysis(self) -> '_4555.CouplingModalAnalysis':
        """CouplingModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4555.CouplingModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to CouplingModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_cvt_modal_analysis(self) -> '_4557.CVTModalAnalysis':
        """CVTModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4557.CVTModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to CVTModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_cvt_pulley_modal_analysis(self) -> '_4558.CVTPulleyModalAnalysis':
        """CVTPulleyModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4558.CVTPulleyModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to CVTPulleyModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_cycloidal_assembly_modal_analysis(self) -> '_4559.CycloidalAssemblyModalAnalysis':
        """CycloidalAssemblyModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4559.CycloidalAssemblyModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to CycloidalAssemblyModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_cycloidal_disc_modal_analysis(self) -> '_4561.CycloidalDiscModalAnalysis':
        """CycloidalDiscModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4561.CycloidalDiscModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to CycloidalDiscModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_cylindrical_gear_modal_analysis(self) -> '_4564.CylindricalGearModalAnalysis':
        """CylindricalGearModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4564.CylindricalGearModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to CylindricalGearModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_cylindrical_gear_set_modal_analysis(self) -> '_4565.CylindricalGearSetModalAnalysis':
        """CylindricalGearSetModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4565.CylindricalGearSetModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to CylindricalGearSetModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_cylindrical_planet_gear_modal_analysis(self) -> '_4566.CylindricalPlanetGearModalAnalysis':
        """CylindricalPlanetGearModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4566.CylindricalPlanetGearModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to CylindricalPlanetGearModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_datum_modal_analysis(self) -> '_4567.DatumModalAnalysis':
        """DatumModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4567.DatumModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to DatumModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_external_cad_model_modal_analysis(self) -> '_4570.ExternalCADModelModalAnalysis':
        """ExternalCADModelModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4570.ExternalCADModelModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to ExternalCADModelModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_face_gear_modal_analysis(self) -> '_4572.FaceGearModalAnalysis':
        """FaceGearModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4572.FaceGearModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to FaceGearModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_face_gear_set_modal_analysis(self) -> '_4573.FaceGearSetModalAnalysis':
        """FaceGearSetModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4573.FaceGearSetModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to FaceGearSetModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_fe_part_modal_analysis(self) -> '_4574.FEPartModalAnalysis':
        """FEPartModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4574.FEPartModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to FEPartModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_flexible_pin_assembly_modal_analysis(self) -> '_4575.FlexiblePinAssemblyModalAnalysis':
        """FlexiblePinAssemblyModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4575.FlexiblePinAssemblyModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to FlexiblePinAssemblyModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_gear_modal_analysis(self) -> '_4578.GearModalAnalysis':
        """GearModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4578.GearModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to GearModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_gear_set_modal_analysis(self) -> '_4579.GearSetModalAnalysis':
        """GearSetModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4579.GearSetModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to GearSetModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_guide_dxf_model_modal_analysis(self) -> '_4580.GuideDxfModelModalAnalysis':
        """GuideDxfModelModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4580.GuideDxfModelModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to GuideDxfModelModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_hypoid_gear_modal_analysis(self) -> '_4582.HypoidGearModalAnalysis':
        """HypoidGearModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4582.HypoidGearModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to HypoidGearModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_hypoid_gear_set_modal_analysis(self) -> '_4583.HypoidGearSetModalAnalysis':
        """HypoidGearSetModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4583.HypoidGearSetModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to HypoidGearSetModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_klingelnberg_cyclo_palloid_conical_gear_modal_analysis(self) -> '_4586.KlingelnbergCycloPalloidConicalGearModalAnalysis':
        """KlingelnbergCycloPalloidConicalGearModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4586.KlingelnbergCycloPalloidConicalGearModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to KlingelnbergCycloPalloidConicalGearModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_klingelnberg_cyclo_palloid_conical_gear_set_modal_analysis(self) -> '_4587.KlingelnbergCycloPalloidConicalGearSetModalAnalysis':
        """KlingelnbergCycloPalloidConicalGearSetModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4587.KlingelnbergCycloPalloidConicalGearSetModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to KlingelnbergCycloPalloidConicalGearSetModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_klingelnberg_cyclo_palloid_hypoid_gear_modal_analysis(self) -> '_4589.KlingelnbergCycloPalloidHypoidGearModalAnalysis':
        """KlingelnbergCycloPalloidHypoidGearModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4589.KlingelnbergCycloPalloidHypoidGearModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to KlingelnbergCycloPalloidHypoidGearModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_klingelnberg_cyclo_palloid_hypoid_gear_set_modal_analysis(self) -> '_4590.KlingelnbergCycloPalloidHypoidGearSetModalAnalysis':
        """KlingelnbergCycloPalloidHypoidGearSetModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4590.KlingelnbergCycloPalloidHypoidGearSetModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to KlingelnbergCycloPalloidHypoidGearSetModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_modal_analysis(self) -> '_4592.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis':
        """KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4592.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_set_modal_analysis(self) -> '_4593.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis':
        """KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4593.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_mass_disc_modal_analysis(self) -> '_4594.MassDiscModalAnalysis':
        """MassDiscModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4594.MassDiscModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to MassDiscModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_measurement_component_modal_analysis(self) -> '_4595.MeasurementComponentModalAnalysis':
        """MeasurementComponentModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4595.MeasurementComponentModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to MeasurementComponentModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_mountable_component_modal_analysis(self) -> '_4599.MountableComponentModalAnalysis':
        """MountableComponentModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4599.MountableComponentModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to MountableComponentModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_oil_seal_modal_analysis(self) -> '_4600.OilSealModalAnalysis':
        """OilSealModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4600.OilSealModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to OilSealModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_part_to_part_shear_coupling_half_modal_analysis(self) -> '_4604.PartToPartShearCouplingHalfModalAnalysis':
        """PartToPartShearCouplingHalfModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4604.PartToPartShearCouplingHalfModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to PartToPartShearCouplingHalfModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_part_to_part_shear_coupling_modal_analysis(self) -> '_4605.PartToPartShearCouplingModalAnalysis':
        """PartToPartShearCouplingModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4605.PartToPartShearCouplingModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to PartToPartShearCouplingModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_planetary_gear_set_modal_analysis(self) -> '_4607.PlanetaryGearSetModalAnalysis':
        """PlanetaryGearSetModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4607.PlanetaryGearSetModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to PlanetaryGearSetModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_planet_carrier_modal_analysis(self) -> '_4608.PlanetCarrierModalAnalysis':
        """PlanetCarrierModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4608.PlanetCarrierModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to PlanetCarrierModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_point_load_modal_analysis(self) -> '_4609.PointLoadModalAnalysis':
        """PointLoadModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4609.PointLoadModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to PointLoadModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_power_load_modal_analysis(self) -> '_4610.PowerLoadModalAnalysis':
        """PowerLoadModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4610.PowerLoadModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to PowerLoadModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_pulley_modal_analysis(self) -> '_4611.PulleyModalAnalysis':
        """PulleyModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4611.PulleyModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to PulleyModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_ring_pins_modal_analysis(self) -> '_4612.RingPinsModalAnalysis':
        """RingPinsModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4612.RingPinsModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to RingPinsModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_rolling_ring_assembly_modal_analysis(self) -> '_4614.RollingRingAssemblyModalAnalysis':
        """RollingRingAssemblyModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4614.RollingRingAssemblyModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to RollingRingAssemblyModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_rolling_ring_modal_analysis(self) -> '_4616.RollingRingModalAnalysis':
        """RollingRingModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4616.RollingRingModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to RollingRingModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_root_assembly_modal_analysis(self) -> '_4617.RootAssemblyModalAnalysis':
        """RootAssemblyModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4617.RootAssemblyModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to RootAssemblyModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_shaft_hub_connection_modal_analysis(self) -> '_4618.ShaftHubConnectionModalAnalysis':
        """ShaftHubConnectionModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4618.ShaftHubConnectionModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to ShaftHubConnectionModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_shaft_modal_analysis(self) -> '_4619.ShaftModalAnalysis':
        """ShaftModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4619.ShaftModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to ShaftModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_specialised_assembly_modal_analysis(self) -> '_4622.SpecialisedAssemblyModalAnalysis':
        """SpecialisedAssemblyModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4622.SpecialisedAssemblyModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to SpecialisedAssemblyModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_spiral_bevel_gear_modal_analysis(self) -> '_4624.SpiralBevelGearModalAnalysis':
        """SpiralBevelGearModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4624.SpiralBevelGearModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to SpiralBevelGearModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_spiral_bevel_gear_set_modal_analysis(self) -> '_4625.SpiralBevelGearSetModalAnalysis':
        """SpiralBevelGearSetModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4625.SpiralBevelGearSetModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to SpiralBevelGearSetModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_spring_damper_half_modal_analysis(self) -> '_4627.SpringDamperHalfModalAnalysis':
        """SpringDamperHalfModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4627.SpringDamperHalfModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to SpringDamperHalfModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_spring_damper_modal_analysis(self) -> '_4628.SpringDamperModalAnalysis':
        """SpringDamperModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4628.SpringDamperModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to SpringDamperModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_straight_bevel_diff_gear_modal_analysis(self) -> '_4630.StraightBevelDiffGearModalAnalysis':
        """StraightBevelDiffGearModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4630.StraightBevelDiffGearModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to StraightBevelDiffGearModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_straight_bevel_diff_gear_set_modal_analysis(self) -> '_4631.StraightBevelDiffGearSetModalAnalysis':
        """StraightBevelDiffGearSetModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4631.StraightBevelDiffGearSetModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to StraightBevelDiffGearSetModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_straight_bevel_gear_modal_analysis(self) -> '_4633.StraightBevelGearModalAnalysis':
        """StraightBevelGearModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4633.StraightBevelGearModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to StraightBevelGearModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_straight_bevel_gear_set_modal_analysis(self) -> '_4634.StraightBevelGearSetModalAnalysis':
        """StraightBevelGearSetModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4634.StraightBevelGearSetModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to StraightBevelGearSetModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_straight_bevel_planet_gear_modal_analysis(self) -> '_4635.StraightBevelPlanetGearModalAnalysis':
        """StraightBevelPlanetGearModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4635.StraightBevelPlanetGearModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to StraightBevelPlanetGearModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_straight_bevel_sun_gear_modal_analysis(self) -> '_4636.StraightBevelSunGearModalAnalysis':
        """StraightBevelSunGearModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4636.StraightBevelSunGearModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to StraightBevelSunGearModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_synchroniser_half_modal_analysis(self) -> '_4637.SynchroniserHalfModalAnalysis':
        """SynchroniserHalfModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4637.SynchroniserHalfModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to SynchroniserHalfModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_synchroniser_modal_analysis(self) -> '_4638.SynchroniserModalAnalysis':
        """SynchroniserModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4638.SynchroniserModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to SynchroniserModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_synchroniser_part_modal_analysis(self) -> '_4639.SynchroniserPartModalAnalysis':
        """SynchroniserPartModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4639.SynchroniserPartModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to SynchroniserPartModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_synchroniser_sleeve_modal_analysis(self) -> '_4640.SynchroniserSleeveModalAnalysis':
        """SynchroniserSleeveModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4640.SynchroniserSleeveModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to SynchroniserSleeveModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_torque_converter_modal_analysis(self) -> '_4642.TorqueConverterModalAnalysis':
        """TorqueConverterModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4642.TorqueConverterModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to TorqueConverterModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_torque_converter_pump_modal_analysis(self) -> '_4643.TorqueConverterPumpModalAnalysis':
        """TorqueConverterPumpModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4643.TorqueConverterPumpModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to TorqueConverterPumpModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_torque_converter_turbine_modal_analysis(self) -> '_4644.TorqueConverterTurbineModalAnalysis':
        """TorqueConverterTurbineModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4644.TorqueConverterTurbineModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to TorqueConverterTurbineModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_unbalanced_mass_modal_analysis(self) -> '_4645.UnbalancedMassModalAnalysis':
        """UnbalancedMassModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4645.UnbalancedMassModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to UnbalancedMassModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_virtual_component_modal_analysis(self) -> '_4646.VirtualComponentModalAnalysis':
        """VirtualComponentModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4646.VirtualComponentModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to VirtualComponentModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_worm_gear_modal_analysis(self) -> '_4651.WormGearModalAnalysis':
        """WormGearModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4651.WormGearModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to WormGearModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_worm_gear_set_modal_analysis(self) -> '_4652.WormGearSetModalAnalysis':
        """WormGearSetModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4652.WormGearSetModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to WormGearSetModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_zerol_bevel_gear_modal_analysis(self) -> '_4654.ZerolBevelGearModalAnalysis':
        """ZerolBevelGearModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4654.ZerolBevelGearModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to ZerolBevelGearModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def uncoupled_modal_analysis_of_type_zerol_bevel_gear_set_modal_analysis(self) -> '_4655.ZerolBevelGearSetModalAnalysis':
        """ZerolBevelGearSetModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        if _4655.ZerolBevelGearSetModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to ZerolBevelGearSetModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
