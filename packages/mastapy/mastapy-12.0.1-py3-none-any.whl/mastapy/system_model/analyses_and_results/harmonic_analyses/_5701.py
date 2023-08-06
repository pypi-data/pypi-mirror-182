"""_5701.py

HarmonicAnalysisShaftExportOptions
"""


from mastapy.system_model.analyses_and_results.harmonic_analyses import _5697
from mastapy.system_model.analyses_and_results import _2608
from mastapy.system_model.part_model.shaft_model import _2435
from mastapy._internal.python_net import python_net_import

_HARMONIC_ANALYSIS_SHAFT_EXPORT_OPTIONS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'HarmonicAnalysisShaftExportOptions')


__docformat__ = 'restructuredtext en'
__all__ = ('HarmonicAnalysisShaftExportOptions',)


class HarmonicAnalysisShaftExportOptions(_5697.HarmonicAnalysisExportOptions['_2608.IHaveShaftHarmonicResults', '_2435.Shaft']):
    """HarmonicAnalysisShaftExportOptions

    This is a mastapy class.
    """

    TYPE = _HARMONIC_ANALYSIS_SHAFT_EXPORT_OPTIONS

    def __init__(self, instance_to_wrap: 'HarmonicAnalysisShaftExportOptions.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
