"""_2960.py

ConceptGearSetSteadyStateSynchronousResponse
"""


from typing import List

from mastapy.system_model.part_model.gears import _2474
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6770
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2961, _2959, _2990
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses', 'ConceptGearSetSteadyStateSynchronousResponse')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptGearSetSteadyStateSynchronousResponse',)


class ConceptGearSetSteadyStateSynchronousResponse(_2990.GearSetSteadyStateSynchronousResponse):
    """ConceptGearSetSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE

    def __init__(self, instance_to_wrap: 'ConceptGearSetSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2474.ConceptGearSet':
        """ConceptGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6770.ConceptGearSetLoadCase':
        """ConceptGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def concept_gears_steady_state_synchronous_response(self) -> 'List[_2961.ConceptGearSteadyStateSynchronousResponse]':
        """List[ConceptGearSteadyStateSynchronousResponse]: 'ConceptGearsSteadyStateSynchronousResponse' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConceptGearsSteadyStateSynchronousResponse

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def concept_meshes_steady_state_synchronous_response(self) -> 'List[_2959.ConceptGearMeshSteadyStateSynchronousResponse]':
        """List[ConceptGearMeshSteadyStateSynchronousResponse]: 'ConceptMeshesSteadyStateSynchronousResponse' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConceptMeshesSteadyStateSynchronousResponse

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
