﻿"""_6028.py

RingPinsHarmonicAnalysisOfSingleExcitation
"""


from mastapy.system_model.part_model.cycloidal import _2522
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6870
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6016
from mastapy._internal.python_net import python_net_import

_RING_PINS_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation', 'RingPinsHarmonicAnalysisOfSingleExcitation')


__docformat__ = 'restructuredtext en'
__all__ = ('RingPinsHarmonicAnalysisOfSingleExcitation',)


class RingPinsHarmonicAnalysisOfSingleExcitation(_6016.MountableComponentHarmonicAnalysisOfSingleExcitation):
    """RingPinsHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _RING_PINS_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    def __init__(self, instance_to_wrap: 'RingPinsHarmonicAnalysisOfSingleExcitation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2522.RingPins':
        """RingPins: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6870.RingPinsLoadCase':
        """RingPinsLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
