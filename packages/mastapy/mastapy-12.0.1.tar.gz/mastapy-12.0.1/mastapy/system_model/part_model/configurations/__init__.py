"""__init__.py"""


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._2563 import ActiveFESubstructureSelection
    from ._2564 import ActiveFESubstructureSelectionGroup
    from ._2565 import ActiveShaftDesignSelection
    from ._2566 import ActiveShaftDesignSelectionGroup
    from ._2567 import BearingDetailConfiguration
    from ._2568 import BearingDetailSelection
    from ._2569 import PartDetailConfiguration
    from ._2570 import PartDetailSelection
