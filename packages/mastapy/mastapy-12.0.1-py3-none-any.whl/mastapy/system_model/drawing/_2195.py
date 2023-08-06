"""_2195.py

AbstractSystemDeflectionViewable
"""


from mastapy.system_model.drawing import _2198, _2205
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2773
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3037
from mastapy.system_model.analyses_and_results.stability_analyses import _3816
from mastapy.system_model.analyses_and_results.rotor_dynamics import _3971
from mastapy.system_model.analyses_and_results.modal_analyses import _4597
from mastapy.system_model.analyses_and_results.mbd_analyses import _5398
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5696
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6258
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6511
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SYSTEM_DEFLECTION_VIEWABLE = python_net_import('SMT.MastaAPI.SystemModel.Drawing', 'AbstractSystemDeflectionViewable')


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractSystemDeflectionViewable',)


class AbstractSystemDeflectionViewable(_2205.PartAnalysisCaseWithContourViewable):
    """AbstractSystemDeflectionViewable

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SYSTEM_DEFLECTION_VIEWABLE

    def __init__(self, instance_to_wrap: 'AbstractSystemDeflectionViewable.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def contour_draw_style(self) -> '_2198.ContourDrawStyle':
        """ContourDrawStyle: 'ContourDrawStyle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContourDrawStyle

        if temp is None:
            return None

        if _2198.ContourDrawStyle.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast contour_draw_style to ContourDrawStyle. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def contour_draw_style_of_type_system_deflection_draw_style(self) -> '_2773.SystemDeflectionDrawStyle':
        """SystemDeflectionDrawStyle: 'ContourDrawStyle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContourDrawStyle

        if temp is None:
            return None

        if _2773.SystemDeflectionDrawStyle.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast contour_draw_style to SystemDeflectionDrawStyle. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def contour_draw_style_of_type_steady_state_synchronous_response_draw_style(self) -> '_3037.SteadyStateSynchronousResponseDrawStyle':
        """SteadyStateSynchronousResponseDrawStyle: 'ContourDrawStyle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContourDrawStyle

        if temp is None:
            return None

        if _3037.SteadyStateSynchronousResponseDrawStyle.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast contour_draw_style to SteadyStateSynchronousResponseDrawStyle. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def contour_draw_style_of_type_stability_analysis_draw_style(self) -> '_3816.StabilityAnalysisDrawStyle':
        """StabilityAnalysisDrawStyle: 'ContourDrawStyle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContourDrawStyle

        if temp is None:
            return None

        if _3816.StabilityAnalysisDrawStyle.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast contour_draw_style to StabilityAnalysisDrawStyle. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def contour_draw_style_of_type_rotor_dynamics_draw_style(self) -> '_3971.RotorDynamicsDrawStyle':
        """RotorDynamicsDrawStyle: 'ContourDrawStyle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContourDrawStyle

        if temp is None:
            return None

        if _3971.RotorDynamicsDrawStyle.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast contour_draw_style to RotorDynamicsDrawStyle. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def contour_draw_style_of_type_modal_analysis_draw_style(self) -> '_4597.ModalAnalysisDrawStyle':
        """ModalAnalysisDrawStyle: 'ContourDrawStyle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContourDrawStyle

        if temp is None:
            return None

        if _4597.ModalAnalysisDrawStyle.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast contour_draw_style to ModalAnalysisDrawStyle. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def contour_draw_style_of_type_mbd_analysis_draw_style(self) -> '_5398.MBDAnalysisDrawStyle':
        """MBDAnalysisDrawStyle: 'ContourDrawStyle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContourDrawStyle

        if temp is None:
            return None

        if _5398.MBDAnalysisDrawStyle.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast contour_draw_style to MBDAnalysisDrawStyle. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def contour_draw_style_of_type_harmonic_analysis_draw_style(self) -> '_5696.HarmonicAnalysisDrawStyle':
        """HarmonicAnalysisDrawStyle: 'ContourDrawStyle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContourDrawStyle

        if temp is None:
            return None

        if _5696.HarmonicAnalysisDrawStyle.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast contour_draw_style to HarmonicAnalysisDrawStyle. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def contour_draw_style_of_type_dynamic_analysis_draw_style(self) -> '_6258.DynamicAnalysisDrawStyle':
        """DynamicAnalysisDrawStyle: 'ContourDrawStyle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContourDrawStyle

        if temp is None:
            return None

        if _6258.DynamicAnalysisDrawStyle.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast contour_draw_style to DynamicAnalysisDrawStyle. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def contour_draw_style_of_type_critical_speed_analysis_draw_style(self) -> '_6511.CriticalSpeedAnalysisDrawStyle':
        """CriticalSpeedAnalysisDrawStyle: 'ContourDrawStyle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContourDrawStyle

        if temp is None:
            return None

        if _6511.CriticalSpeedAnalysisDrawStyle.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast contour_draw_style to CriticalSpeedAnalysisDrawStyle. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_draw_style(self) -> '_2773.SystemDeflectionDrawStyle':
        """SystemDeflectionDrawStyle: 'SystemDeflectionDrawStyle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionDrawStyle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    def fe_results(self):
        """ 'FEResults' is the original name of this method."""

        self.wrapped.FEResults()
