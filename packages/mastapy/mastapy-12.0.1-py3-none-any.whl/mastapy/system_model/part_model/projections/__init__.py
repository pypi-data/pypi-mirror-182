"""__init__.py"""


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._2437 import SpecifiedConcentricPartGroupDrawingOrder
    from ._2438 import SpecifiedParallelPartGroupDrawingOrder
