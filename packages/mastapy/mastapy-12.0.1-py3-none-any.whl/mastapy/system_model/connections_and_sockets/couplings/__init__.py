"""__init__.py"""


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._2295 import ClutchConnection
    from ._2296 import ClutchSocket
    from ._2297 import ConceptCouplingConnection
    from ._2298 import ConceptCouplingSocket
    from ._2299 import CouplingConnection
    from ._2300 import CouplingSocket
    from ._2301 import PartToPartShearCouplingConnection
    from ._2302 import PartToPartShearCouplingSocket
    from ._2303 import SpringDamperConnection
    from ._2304 import SpringDamperSocket
    from ._2305 import TorqueConverterConnection
    from ._2306 import TorqueConverterPumpSocket
    from ._2307 import TorqueConverterTurbineSocket
