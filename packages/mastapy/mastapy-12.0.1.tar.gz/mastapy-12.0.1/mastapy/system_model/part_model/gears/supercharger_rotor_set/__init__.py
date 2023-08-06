"""__init__.py"""


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._2507 import BoostPressureInputOptions
    from ._2508 import InputPowerInputOptions
    from ._2509 import PressureRatioInputOptions
    from ._2510 import RotorSetDataInputFileOptions
    from ._2511 import RotorSetMeasuredPoint
    from ._2512 import RotorSpeedInputOptions
    from ._2513 import SuperchargerMap
    from ._2514 import SuperchargerMaps
    from ._2515 import SuperchargerRotorSet
    from ._2516 import SuperchargerRotorSetDatabase
    from ._2517 import YVariableForImportedData
