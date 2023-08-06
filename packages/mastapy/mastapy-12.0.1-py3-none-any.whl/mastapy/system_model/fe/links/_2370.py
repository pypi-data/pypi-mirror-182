"""_2370.py

FELink
"""


from typing import List
from collections import OrderedDict

from mastapy._internal.implicit import overridable, enum_with_selected_value, list_with_selected_item
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.system_model.fe import (
    _2316, _2350, _2354, _2349,
    _2337
)
from mastapy.nodal_analysis.dev_tools_analyses import _197
from mastapy.system_model.part_model import (
    _2397, _2389, _2390, _2393,
    _2395, _2400, _2401, _2405,
    _2406, _2408, _2415, _2416,
    _2417, _2419, _2422, _2424,
    _2425, _2430, _2432
)
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.part_model.shaft_model import _2435
from mastapy.system_model.part_model.gears import (
    _2465, _2467, _2469, _2470,
    _2471, _2473, _2475, _2477,
    _2479, _2480, _2482, _2486,
    _2488, _2490, _2492, _2495,
    _2497, _2499, _2501, _2502,
    _2503, _2505
)
from mastapy.system_model.part_model.cycloidal import _2521, _2522
from mastapy.system_model.part_model.couplings import (
    _2531, _2534, _2536, _2539,
    _2541, _2542, _2548, _2550,
    _2553, _2556, _2557, _2558,
    _2560, _2562
)
from mastapy.system_model.connections_and_sockets import (
    _2249, _2219, _2220, _2227,
    _2229, _2231, _2232, _2233,
    _2235, _2236, _2237, _2238,
    _2239, _2241, _2242, _2243,
    _2246, _2247
)
from mastapy.system_model.connections_and_sockets.gears import (
    _2253, _2255, _2257, _2259,
    _2261, _2263, _2265, _2267,
    _2269, _2270, _2274, _2275,
    _2277, _2279, _2281, _2283,
    _2285
)
from mastapy.system_model.connections_and_sockets.cycloidal import (
    _2286, _2287, _2289, _2290,
    _2292, _2293
)
from mastapy.system_model.connections_and_sockets.couplings import (
    _2296, _2298, _2300, _2302,
    _2304, _2306, _2307
)
from mastapy.materials import _263, _239
from mastapy.shafts import _24
from mastapy.gears.materials import (
    _576, _578, _580, _584,
    _587, _590, _594, _596
)
from mastapy.electric_machines import _1264, _1281, _1291
from mastapy.detailed_rigid_connectors.splines import _1382
from mastapy.cycloidal import _1421, _1427
from mastapy.bolts import _1430, _1434
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_FE_LINK = python_net_import('SMT.MastaAPI.SystemModel.FE.Links', 'FELink')


__docformat__ = 'restructuredtext en'
__all__ = ('FELink',)


class FELink(_0.APIBase):
    """FELink

    This is a mastapy class.
    """

    TYPE = _FE_LINK

    def __init__(self, instance_to_wrap: 'FELink.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angle_of_centre_of_connection_patch(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'AngleOfCentreOfConnectionPatch' is the original name of this property."""

        temp = self.wrapped.AngleOfCentreOfConnectionPatch

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @angle_of_centre_of_connection_patch.setter
    def angle_of_centre_of_connection_patch(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.AngleOfCentreOfConnectionPatch = value

    @property
    def bearing_node_link_option(self) -> 'enum_with_selected_value.EnumWithSelectedValue_BearingNodeOption':
        """enum_with_selected_value.EnumWithSelectedValue_BearingNodeOption: 'BearingNodeLinkOption' is the original name of this property."""

        temp = self.wrapped.BearingNodeLinkOption

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_BearingNodeOption.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @bearing_node_link_option.setter
    def bearing_node_link_option(self, value: 'enum_with_selected_value.EnumWithSelectedValue_BearingNodeOption.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_BearingNodeOption.implicit_type()
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.BearingNodeLinkOption = value

    @property
    def bearing_race_in_fe(self) -> 'overridable.Overridable_bool':
        """overridable.Overridable_bool: 'BearingRaceInFE' is the original name of this property."""

        temp = self.wrapped.BearingRaceInFE

        if temp is None:
            return False

        return constructor.new_from_mastapy_type(overridable.Overridable_bool)(temp) if temp is not None else False

    @bearing_race_in_fe.setter
    def bearing_race_in_fe(self, value: 'overridable.Overridable_bool.implicit_type()'):
        wrapper_type = overridable.Overridable_bool.wrapper_type()
        enclosed_type = overridable.Overridable_bool.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else False, is_overridden)
        self.wrapped.BearingRaceInFE = value

    @property
    def component_name(self) -> 'str':
        """str: 'ComponentName' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentName

        if temp is None:
            return ''

        return temp

    @property
    def connect_to_midside_nodes(self) -> 'bool':
        """bool: 'ConnectToMidsideNodes' is the original name of this property."""

        temp = self.wrapped.ConnectToMidsideNodes

        if temp is None:
            return False

        return temp

    @connect_to_midside_nodes.setter
    def connect_to_midside_nodes(self, value: 'bool'):
        self.wrapped.ConnectToMidsideNodes = bool(value) if value else False

    @property
    def connection(self) -> 'str':
        """str: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Connection

        if temp is None:
            return ''

        return temp

    @property
    def coupling_type(self) -> 'overridable.Overridable_RigidCouplingType':
        """overridable.Overridable_RigidCouplingType: 'CouplingType' is the original name of this property."""

        temp = self.wrapped.CouplingType

        if temp is None:
            return None

        value = overridable.Overridable_RigidCouplingType.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @coupling_type.setter
    def coupling_type(self, value: 'overridable.Overridable_RigidCouplingType.implicit_type()'):
        wrapper_type = overridable.Overridable_RigidCouplingType.wrapper_type()
        enclosed_type = overridable.Overridable_RigidCouplingType.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value if value is not None else None, is_overridden)
        self.wrapped.CouplingType = value

    @property
    def external_node_ids(self) -> 'str':
        """str: 'ExternalNodeIDs' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ExternalNodeIDs

        if temp is None:
            return ''

        return temp

    @property
    def has_teeth(self) -> 'bool':
        """bool: 'HasTeeth' is the original name of this property."""

        temp = self.wrapped.HasTeeth

        if temp is None:
            return False

        return temp

    @has_teeth.setter
    def has_teeth(self, value: 'bool'):
        self.wrapped.HasTeeth = bool(value) if value else False

    @property
    def link_node_source(self) -> 'enum_with_selected_value.EnumWithSelectedValue_LinkNodeSource':
        """enum_with_selected_value.EnumWithSelectedValue_LinkNodeSource: 'LinkNodeSource' is the original name of this property."""

        temp = self.wrapped.LinkNodeSource

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_LinkNodeSource.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @link_node_source.setter
    def link_node_source(self, value: 'enum_with_selected_value.EnumWithSelectedValue_LinkNodeSource.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_LinkNodeSource.implicit_type()
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.LinkNodeSource = value

    @property
    def link_to_get_nodes_from(self) -> 'list_with_selected_item.ListWithSelectedItem_FELink':
        """list_with_selected_item.ListWithSelectedItem_FELink: 'LinkToGetNodesFrom' is the original name of this property."""

        temp = self.wrapped.LinkToGetNodesFrom

        if temp is None:
            return None

        return constructor.new_from_mastapy_type(list_with_selected_item.ListWithSelectedItem_FELink)(temp) if temp is not None else None

    @link_to_get_nodes_from.setter
    def link_to_get_nodes_from(self, value: 'list_with_selected_item.ListWithSelectedItem_FELink.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_FELink.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_FELink.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value is not None else None)
        self.wrapped.LinkToGetNodesFrom = value

    @property
    def node_cone_search_angle(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'NodeConeSearchAngle' is the original name of this property."""

        temp = self.wrapped.NodeConeSearchAngle

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @node_cone_search_angle.setter
    def node_cone_search_angle(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.NodeConeSearchAngle = value

    @property
    def node_cylinder_search_axial_offset(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'NodeCylinderSearchAxialOffset' is the original name of this property."""

        temp = self.wrapped.NodeCylinderSearchAxialOffset

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @node_cylinder_search_axial_offset.setter
    def node_cylinder_search_axial_offset(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.NodeCylinderSearchAxialOffset = value

    @property
    def node_cylinder_search_diameter(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'NodeCylinderSearchDiameter' is the original name of this property."""

        temp = self.wrapped.NodeCylinderSearchDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @node_cylinder_search_diameter.setter
    def node_cylinder_search_diameter(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.NodeCylinderSearchDiameter = value

    @property
    def node_cylinder_search_length(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'NodeCylinderSearchLength' is the original name of this property."""

        temp = self.wrapped.NodeCylinderSearchLength

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @node_cylinder_search_length.setter
    def node_cylinder_search_length(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.NodeCylinderSearchLength = value

    @property
    def node_search_cylinder_thickness(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'NodeSearchCylinderThickness' is the original name of this property."""

        temp = self.wrapped.NodeSearchCylinderThickness

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @node_search_cylinder_thickness.setter
    def node_search_cylinder_thickness(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.NodeSearchCylinderThickness = value

    @property
    def node_selection_depth(self) -> 'overridable.Overridable_NodeSelectionDepthOption':
        """overridable.Overridable_NodeSelectionDepthOption: 'NodeSelectionDepth' is the original name of this property."""

        temp = self.wrapped.NodeSelectionDepth

        if temp is None:
            return None

        value = overridable.Overridable_NodeSelectionDepthOption.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @node_selection_depth.setter
    def node_selection_depth(self, value: 'overridable.Overridable_NodeSelectionDepthOption.implicit_type()'):
        wrapper_type = overridable.Overridable_NodeSelectionDepthOption.wrapper_type()
        enclosed_type = overridable.Overridable_NodeSelectionDepthOption.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value if value is not None else None, is_overridden)
        self.wrapped.NodeSelectionDepth = value

    @property
    def number_of_axial_nodes(self) -> 'int':
        """int: 'NumberOfAxialNodes' is the original name of this property."""

        temp = self.wrapped.NumberOfAxialNodes

        if temp is None:
            return 0

        return temp

    @number_of_axial_nodes.setter
    def number_of_axial_nodes(self, value: 'int'):
        self.wrapped.NumberOfAxialNodes = int(value) if value else 0

    @property
    def number_of_nodes_in_full_fe_mesh(self) -> 'int':
        """int: 'NumberOfNodesInFullFEMesh' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NumberOfNodesInFullFEMesh

        if temp is None:
            return 0

        return temp

    @property
    def number_of_nodes_in_ring(self) -> 'overridable.Overridable_int':
        """overridable.Overridable_int: 'NumberOfNodesInRing' is the original name of this property."""

        temp = self.wrapped.NumberOfNodesInRing

        if temp is None:
            return 0

        return constructor.new_from_mastapy_type(overridable.Overridable_int)(temp) if temp is not None else 0

    @number_of_nodes_in_ring.setter
    def number_of_nodes_in_ring(self, value: 'overridable.Overridable_int.implicit_type()'):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0, is_overridden)
        self.wrapped.NumberOfNodesInRing = value

    @property
    def span_of_patch(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'SpanOfPatch' is the original name of this property."""

        temp = self.wrapped.SpanOfPatch

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @span_of_patch.setter
    def span_of_patch(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.SpanOfPatch = value

    @property
    def support_material_id(self) -> 'list_with_selected_item.ListWithSelectedItem_int':
        """list_with_selected_item.ListWithSelectedItem_int: 'SupportMaterialID' is the original name of this property."""

        temp = self.wrapped.SupportMaterialID

        if temp is None:
            return 0

        return constructor.new_from_mastapy_type(list_with_selected_item.ListWithSelectedItem_int)(temp) if temp is not None else 0

    @support_material_id.setter
    def support_material_id(self, value: 'list_with_selected_item.ListWithSelectedItem_int.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_int.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_int.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0)
        self.wrapped.SupportMaterialID = value

    @property
    def width_of_axial_patch(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'WidthOfAxialPatch' is the original name of this property."""

        temp = self.wrapped.WidthOfAxialPatch

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @width_of_axial_patch.setter
    def width_of_axial_patch(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.WidthOfAxialPatch = value

    @property
    def alignment_in_component_coordinate_system(self) -> '_2349.LinkComponentAxialPositionErrorReporter':
        """LinkComponentAxialPositionErrorReporter: 'AlignmentInComponentCoordinateSystem' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AlignmentInComponentCoordinateSystem

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def alignment_in_fe_coordinate_system(self) -> '_2349.LinkComponentAxialPositionErrorReporter':
        """LinkComponentAxialPositionErrorReporter: 'AlignmentInFECoordinateSystem' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AlignmentInFECoordinateSystem

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def alignment_in_world_coordinate_system(self) -> '_2349.LinkComponentAxialPositionErrorReporter':
        """LinkComponentAxialPositionErrorReporter: 'AlignmentInWorldCoordinateSystem' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AlignmentInWorldCoordinateSystem

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component(self) -> '_2397.Component':
        """Component: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component

        if temp is None:
            return None

        if _2397.Component.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to Component. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_abstract_shaft(self) -> '_2389.AbstractShaft':
        """AbstractShaft: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component

        if temp is None:
            return None

        if _2389.AbstractShaft.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to AbstractShaft. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_abstract_shaft_or_housing(self) -> '_2390.AbstractShaftOrHousing':
        """AbstractShaftOrHousing: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component

        if temp is None:
            return None

        if _2390.AbstractShaftOrHousing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to AbstractShaftOrHousing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_bearing(self) -> '_2393.Bearing':
        """Bearing: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component

        if temp is None:
            return None

        if _2393.Bearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to Bearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_bolt(self) -> '_2395.Bolt':
        """Bolt: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component

        if temp is None:
            return None

        if _2395.Bolt.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to Bolt. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_connector(self) -> '_2400.Connector':
        """Connector: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component

        if temp is None:
            return None

        if _2400.Connector.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to Connector. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_datum(self) -> '_2401.Datum':
        """Datum: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component

        if temp is None:
            return None

        if _2401.Datum.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to Datum. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_external_cad_model(self) -> '_2405.ExternalCADModel':
        """ExternalCADModel: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component

        if temp is None:
            return None

        if _2405.ExternalCADModel.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to ExternalCADModel. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_fe_part(self) -> '_2406.FEPart':
        """FEPart: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component

        if temp is None:
            return None

        if _2406.FEPart.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to FEPart. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_guide_dxf_model(self) -> '_2408.GuideDxfModel':
        """GuideDxfModel: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component

        if temp is None:
            return None

        if _2408.GuideDxfModel.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to GuideDxfModel. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_mass_disc(self) -> '_2415.MassDisc':
        """MassDisc: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component

        if temp is None:
            return None

        if _2415.MassDisc.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to MassDisc. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_measurement_component(self) -> '_2416.MeasurementComponent':
        """MeasurementComponent: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component

        if temp is None:
            return None

        if _2416.MeasurementComponent.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to MeasurementComponent. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_mountable_component(self) -> '_2417.MountableComponent':
        """MountableComponent: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component

        if temp is None:
            return None

        if _2417.MountableComponent.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to MountableComponent. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_oil_seal(self) -> '_2419.OilSeal':
        """OilSeal: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component

        if temp is None:
            return None

        if _2419.OilSeal.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to OilSeal. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_planet_carrier(self) -> '_2422.PlanetCarrier':
        """PlanetCarrier: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component

        if temp is None:
            return None

        if _2422.PlanetCarrier.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to PlanetCarrier. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_point_load(self) -> '_2424.PointLoad':
        """PointLoad: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component

        if temp is None:
            return None

        if _2424.PointLoad.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to PointLoad. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_power_load(self) -> '_2425.PowerLoad':
        """PowerLoad: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component

        if temp is None:
            return None

        if _2425.PowerLoad.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to PowerLoad. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_unbalanced_mass(self) -> '_2430.UnbalancedMass':
        """UnbalancedMass: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component

        if temp is None:
            return None

        if _2430.UnbalancedMass.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to UnbalancedMass. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_virtual_component(self) -> '_2432.VirtualComponent':
        """VirtualComponent: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component

        if temp is None:
            return None

        if _2432.VirtualComponent.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to VirtualComponent. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_shaft(self) -> '_2435.Shaft':
        """Shaft: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component

        if temp is None:
            return None

        if _2435.Shaft.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to Shaft. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_agma_gleason_conical_gear(self) -> '_2465.AGMAGleasonConicalGear':
        """AGMAGleasonConicalGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component

        if temp is None:
            return None

        if _2465.AGMAGleasonConicalGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to AGMAGleasonConicalGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_bevel_differential_gear(self) -> '_2467.BevelDifferentialGear':
        """BevelDifferentialGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component

        if temp is None:
            return None

        if _2467.BevelDifferentialGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to BevelDifferentialGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_bevel_differential_planet_gear(self) -> '_2469.BevelDifferentialPlanetGear':
        """BevelDifferentialPlanetGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component

        if temp is None:
            return None

        if _2469.BevelDifferentialPlanetGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to BevelDifferentialPlanetGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_bevel_differential_sun_gear(self) -> '_2470.BevelDifferentialSunGear':
        """BevelDifferentialSunGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component

        if temp is None:
            return None

        if _2470.BevelDifferentialSunGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to BevelDifferentialSunGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_bevel_gear(self) -> '_2471.BevelGear':
        """BevelGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component

        if temp is None:
            return None

        if _2471.BevelGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to BevelGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_concept_gear(self) -> '_2473.ConceptGear':
        """ConceptGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component

        if temp is None:
            return None

        if _2473.ConceptGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to ConceptGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_conical_gear(self) -> '_2475.ConicalGear':
        """ConicalGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component

        if temp is None:
            return None

        if _2475.ConicalGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to ConicalGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_cylindrical_gear(self) -> '_2477.CylindricalGear':
        """CylindricalGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component

        if temp is None:
            return None

        if _2477.CylindricalGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to CylindricalGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_cylindrical_planet_gear(self) -> '_2479.CylindricalPlanetGear':
        """CylindricalPlanetGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component

        if temp is None:
            return None

        if _2479.CylindricalPlanetGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to CylindricalPlanetGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_face_gear(self) -> '_2480.FaceGear':
        """FaceGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component

        if temp is None:
            return None

        if _2480.FaceGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to FaceGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_gear(self) -> '_2482.Gear':
        """Gear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component

        if temp is None:
            return None

        if _2482.Gear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to Gear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_hypoid_gear(self) -> '_2486.HypoidGear':
        """HypoidGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component

        if temp is None:
            return None

        if _2486.HypoidGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to HypoidGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_klingelnberg_cyclo_palloid_conical_gear(self) -> '_2488.KlingelnbergCycloPalloidConicalGear':
        """KlingelnbergCycloPalloidConicalGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component

        if temp is None:
            return None

        if _2488.KlingelnbergCycloPalloidConicalGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to KlingelnbergCycloPalloidConicalGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_klingelnberg_cyclo_palloid_hypoid_gear(self) -> '_2490.KlingelnbergCycloPalloidHypoidGear':
        """KlingelnbergCycloPalloidHypoidGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component

        if temp is None:
            return None

        if _2490.KlingelnbergCycloPalloidHypoidGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to KlingelnbergCycloPalloidHypoidGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear(self) -> '_2492.KlingelnbergCycloPalloidSpiralBevelGear':
        """KlingelnbergCycloPalloidSpiralBevelGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component

        if temp is None:
            return None

        if _2492.KlingelnbergCycloPalloidSpiralBevelGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to KlingelnbergCycloPalloidSpiralBevelGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_spiral_bevel_gear(self) -> '_2495.SpiralBevelGear':
        """SpiralBevelGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component

        if temp is None:
            return None

        if _2495.SpiralBevelGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to SpiralBevelGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_straight_bevel_diff_gear(self) -> '_2497.StraightBevelDiffGear':
        """StraightBevelDiffGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component

        if temp is None:
            return None

        if _2497.StraightBevelDiffGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to StraightBevelDiffGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_straight_bevel_gear(self) -> '_2499.StraightBevelGear':
        """StraightBevelGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component

        if temp is None:
            return None

        if _2499.StraightBevelGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to StraightBevelGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_straight_bevel_planet_gear(self) -> '_2501.StraightBevelPlanetGear':
        """StraightBevelPlanetGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component

        if temp is None:
            return None

        if _2501.StraightBevelPlanetGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to StraightBevelPlanetGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_straight_bevel_sun_gear(self) -> '_2502.StraightBevelSunGear':
        """StraightBevelSunGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component

        if temp is None:
            return None

        if _2502.StraightBevelSunGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to StraightBevelSunGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_worm_gear(self) -> '_2503.WormGear':
        """WormGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component

        if temp is None:
            return None

        if _2503.WormGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to WormGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_zerol_bevel_gear(self) -> '_2505.ZerolBevelGear':
        """ZerolBevelGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component

        if temp is None:
            return None

        if _2505.ZerolBevelGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to ZerolBevelGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_cycloidal_disc(self) -> '_2521.CycloidalDisc':
        """CycloidalDisc: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component

        if temp is None:
            return None

        if _2521.CycloidalDisc.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to CycloidalDisc. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_ring_pins(self) -> '_2522.RingPins':
        """RingPins: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component

        if temp is None:
            return None

        if _2522.RingPins.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to RingPins. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_clutch_half(self) -> '_2531.ClutchHalf':
        """ClutchHalf: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component

        if temp is None:
            return None

        if _2531.ClutchHalf.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to ClutchHalf. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_concept_coupling_half(self) -> '_2534.ConceptCouplingHalf':
        """ConceptCouplingHalf: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component

        if temp is None:
            return None

        if _2534.ConceptCouplingHalf.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to ConceptCouplingHalf. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_coupling_half(self) -> '_2536.CouplingHalf':
        """CouplingHalf: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component

        if temp is None:
            return None

        if _2536.CouplingHalf.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to CouplingHalf. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_cvt_pulley(self) -> '_2539.CVTPulley':
        """CVTPulley: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component

        if temp is None:
            return None

        if _2539.CVTPulley.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to CVTPulley. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_part_to_part_shear_coupling_half(self) -> '_2541.PartToPartShearCouplingHalf':
        """PartToPartShearCouplingHalf: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component

        if temp is None:
            return None

        if _2541.PartToPartShearCouplingHalf.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to PartToPartShearCouplingHalf. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_pulley(self) -> '_2542.Pulley':
        """Pulley: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component

        if temp is None:
            return None

        if _2542.Pulley.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to Pulley. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_rolling_ring(self) -> '_2548.RollingRing':
        """RollingRing: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component

        if temp is None:
            return None

        if _2548.RollingRing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to RollingRing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_shaft_hub_connection(self) -> '_2550.ShaftHubConnection':
        """ShaftHubConnection: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component

        if temp is None:
            return None

        if _2550.ShaftHubConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to ShaftHubConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_spring_damper_half(self) -> '_2553.SpringDamperHalf':
        """SpringDamperHalf: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component

        if temp is None:
            return None

        if _2553.SpringDamperHalf.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to SpringDamperHalf. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_synchroniser_half(self) -> '_2556.SynchroniserHalf':
        """SynchroniserHalf: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component

        if temp is None:
            return None

        if _2556.SynchroniserHalf.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to SynchroniserHalf. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_synchroniser_part(self) -> '_2557.SynchroniserPart':
        """SynchroniserPart: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component

        if temp is None:
            return None

        if _2557.SynchroniserPart.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to SynchroniserPart. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_synchroniser_sleeve(self) -> '_2558.SynchroniserSleeve':
        """SynchroniserSleeve: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component

        if temp is None:
            return None

        if _2558.SynchroniserSleeve.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to SynchroniserSleeve. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_torque_converter_pump(self) -> '_2560.TorqueConverterPump':
        """TorqueConverterPump: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component

        if temp is None:
            return None

        if _2560.TorqueConverterPump.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to TorqueConverterPump. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_torque_converter_turbine(self) -> '_2562.TorqueConverterTurbine':
        """TorqueConverterTurbine: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component

        if temp is None:
            return None

        if _2562.TorqueConverterTurbine.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to TorqueConverterTurbine. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket(self) -> '_2249.Socket':
        """Socket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Socket

        if temp is None:
            return None

        if _2249.Socket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket to Socket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_of_type_bearing_inner_socket(self) -> '_2219.BearingInnerSocket':
        """BearingInnerSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Socket

        if temp is None:
            return None

        if _2219.BearingInnerSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket to BearingInnerSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_of_type_bearing_outer_socket(self) -> '_2220.BearingOuterSocket':
        """BearingOuterSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Socket

        if temp is None:
            return None

        if _2220.BearingOuterSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket to BearingOuterSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_of_type_cvt_pulley_socket(self) -> '_2227.CVTPulleySocket':
        """CVTPulleySocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Socket

        if temp is None:
            return None

        if _2227.CVTPulleySocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket to CVTPulleySocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_of_type_cylindrical_socket(self) -> '_2229.CylindricalSocket':
        """CylindricalSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Socket

        if temp is None:
            return None

        if _2229.CylindricalSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket to CylindricalSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_of_type_electric_machine_stator_socket(self) -> '_2231.ElectricMachineStatorSocket':
        """ElectricMachineStatorSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Socket

        if temp is None:
            return None

        if _2231.ElectricMachineStatorSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket to ElectricMachineStatorSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_of_type_inner_shaft_socket(self) -> '_2232.InnerShaftSocket':
        """InnerShaftSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Socket

        if temp is None:
            return None

        if _2232.InnerShaftSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket to InnerShaftSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_of_type_inner_shaft_socket_base(self) -> '_2233.InnerShaftSocketBase':
        """InnerShaftSocketBase: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Socket

        if temp is None:
            return None

        if _2233.InnerShaftSocketBase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket to InnerShaftSocketBase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_of_type_mountable_component_inner_socket(self) -> '_2235.MountableComponentInnerSocket':
        """MountableComponentInnerSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Socket

        if temp is None:
            return None

        if _2235.MountableComponentInnerSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket to MountableComponentInnerSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_of_type_mountable_component_outer_socket(self) -> '_2236.MountableComponentOuterSocket':
        """MountableComponentOuterSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Socket

        if temp is None:
            return None

        if _2236.MountableComponentOuterSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket to MountableComponentOuterSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_of_type_mountable_component_socket(self) -> '_2237.MountableComponentSocket':
        """MountableComponentSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Socket

        if temp is None:
            return None

        if _2237.MountableComponentSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket to MountableComponentSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_of_type_outer_shaft_socket(self) -> '_2238.OuterShaftSocket':
        """OuterShaftSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Socket

        if temp is None:
            return None

        if _2238.OuterShaftSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket to OuterShaftSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_of_type_outer_shaft_socket_base(self) -> '_2239.OuterShaftSocketBase':
        """OuterShaftSocketBase: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Socket

        if temp is None:
            return None

        if _2239.OuterShaftSocketBase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket to OuterShaftSocketBase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_of_type_planetary_socket(self) -> '_2241.PlanetarySocket':
        """PlanetarySocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Socket

        if temp is None:
            return None

        if _2241.PlanetarySocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket to PlanetarySocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_of_type_planetary_socket_base(self) -> '_2242.PlanetarySocketBase':
        """PlanetarySocketBase: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Socket

        if temp is None:
            return None

        if _2242.PlanetarySocketBase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket to PlanetarySocketBase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_of_type_pulley_socket(self) -> '_2243.PulleySocket':
        """PulleySocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Socket

        if temp is None:
            return None

        if _2243.PulleySocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket to PulleySocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_of_type_rolling_ring_socket(self) -> '_2246.RollingRingSocket':
        """RollingRingSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Socket

        if temp is None:
            return None

        if _2246.RollingRingSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket to RollingRingSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_of_type_shaft_socket(self) -> '_2247.ShaftSocket':
        """ShaftSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Socket

        if temp is None:
            return None

        if _2247.ShaftSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket to ShaftSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_of_type_agma_gleason_conical_gear_teeth_socket(self) -> '_2253.AGMAGleasonConicalGearTeethSocket':
        """AGMAGleasonConicalGearTeethSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Socket

        if temp is None:
            return None

        if _2253.AGMAGleasonConicalGearTeethSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket to AGMAGleasonConicalGearTeethSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_of_type_bevel_differential_gear_teeth_socket(self) -> '_2255.BevelDifferentialGearTeethSocket':
        """BevelDifferentialGearTeethSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Socket

        if temp is None:
            return None

        if _2255.BevelDifferentialGearTeethSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket to BevelDifferentialGearTeethSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_of_type_bevel_gear_teeth_socket(self) -> '_2257.BevelGearTeethSocket':
        """BevelGearTeethSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Socket

        if temp is None:
            return None

        if _2257.BevelGearTeethSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket to BevelGearTeethSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_of_type_concept_gear_teeth_socket(self) -> '_2259.ConceptGearTeethSocket':
        """ConceptGearTeethSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Socket

        if temp is None:
            return None

        if _2259.ConceptGearTeethSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket to ConceptGearTeethSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_of_type_conical_gear_teeth_socket(self) -> '_2261.ConicalGearTeethSocket':
        """ConicalGearTeethSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Socket

        if temp is None:
            return None

        if _2261.ConicalGearTeethSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket to ConicalGearTeethSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_of_type_cylindrical_gear_teeth_socket(self) -> '_2263.CylindricalGearTeethSocket':
        """CylindricalGearTeethSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Socket

        if temp is None:
            return None

        if _2263.CylindricalGearTeethSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket to CylindricalGearTeethSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_of_type_face_gear_teeth_socket(self) -> '_2265.FaceGearTeethSocket':
        """FaceGearTeethSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Socket

        if temp is None:
            return None

        if _2265.FaceGearTeethSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket to FaceGearTeethSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_of_type_gear_teeth_socket(self) -> '_2267.GearTeethSocket':
        """GearTeethSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Socket

        if temp is None:
            return None

        if _2267.GearTeethSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket to GearTeethSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_of_type_hypoid_gear_teeth_socket(self) -> '_2269.HypoidGearTeethSocket':
        """HypoidGearTeethSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Socket

        if temp is None:
            return None

        if _2269.HypoidGearTeethSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket to HypoidGearTeethSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_of_type_klingelnberg_conical_gear_teeth_socket(self) -> '_2270.KlingelnbergConicalGearTeethSocket':
        """KlingelnbergConicalGearTeethSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Socket

        if temp is None:
            return None

        if _2270.KlingelnbergConicalGearTeethSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket to KlingelnbergConicalGearTeethSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_of_type_klingelnberg_hypoid_gear_teeth_socket(self) -> '_2274.KlingelnbergHypoidGearTeethSocket':
        """KlingelnbergHypoidGearTeethSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Socket

        if temp is None:
            return None

        if _2274.KlingelnbergHypoidGearTeethSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket to KlingelnbergHypoidGearTeethSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_of_type_klingelnberg_spiral_bevel_gear_teeth_socket(self) -> '_2275.KlingelnbergSpiralBevelGearTeethSocket':
        """KlingelnbergSpiralBevelGearTeethSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Socket

        if temp is None:
            return None

        if _2275.KlingelnbergSpiralBevelGearTeethSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket to KlingelnbergSpiralBevelGearTeethSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_of_type_spiral_bevel_gear_teeth_socket(self) -> '_2277.SpiralBevelGearTeethSocket':
        """SpiralBevelGearTeethSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Socket

        if temp is None:
            return None

        if _2277.SpiralBevelGearTeethSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket to SpiralBevelGearTeethSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_of_type_straight_bevel_diff_gear_teeth_socket(self) -> '_2279.StraightBevelDiffGearTeethSocket':
        """StraightBevelDiffGearTeethSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Socket

        if temp is None:
            return None

        if _2279.StraightBevelDiffGearTeethSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket to StraightBevelDiffGearTeethSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_of_type_straight_bevel_gear_teeth_socket(self) -> '_2281.StraightBevelGearTeethSocket':
        """StraightBevelGearTeethSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Socket

        if temp is None:
            return None

        if _2281.StraightBevelGearTeethSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket to StraightBevelGearTeethSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_of_type_worm_gear_teeth_socket(self) -> '_2283.WormGearTeethSocket':
        """WormGearTeethSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Socket

        if temp is None:
            return None

        if _2283.WormGearTeethSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket to WormGearTeethSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_of_type_zerol_bevel_gear_teeth_socket(self) -> '_2285.ZerolBevelGearTeethSocket':
        """ZerolBevelGearTeethSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Socket

        if temp is None:
            return None

        if _2285.ZerolBevelGearTeethSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket to ZerolBevelGearTeethSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_of_type_cycloidal_disc_axial_left_socket(self) -> '_2286.CycloidalDiscAxialLeftSocket':
        """CycloidalDiscAxialLeftSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Socket

        if temp is None:
            return None

        if _2286.CycloidalDiscAxialLeftSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket to CycloidalDiscAxialLeftSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_of_type_cycloidal_disc_axial_right_socket(self) -> '_2287.CycloidalDiscAxialRightSocket':
        """CycloidalDiscAxialRightSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Socket

        if temp is None:
            return None

        if _2287.CycloidalDiscAxialRightSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket to CycloidalDiscAxialRightSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_of_type_cycloidal_disc_inner_socket(self) -> '_2289.CycloidalDiscInnerSocket':
        """CycloidalDiscInnerSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Socket

        if temp is None:
            return None

        if _2289.CycloidalDiscInnerSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket to CycloidalDiscInnerSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_of_type_cycloidal_disc_outer_socket(self) -> '_2290.CycloidalDiscOuterSocket':
        """CycloidalDiscOuterSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Socket

        if temp is None:
            return None

        if _2290.CycloidalDiscOuterSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket to CycloidalDiscOuterSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_of_type_cycloidal_disc_planetary_bearing_socket(self) -> '_2292.CycloidalDiscPlanetaryBearingSocket':
        """CycloidalDiscPlanetaryBearingSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Socket

        if temp is None:
            return None

        if _2292.CycloidalDiscPlanetaryBearingSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket to CycloidalDiscPlanetaryBearingSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_of_type_ring_pins_socket(self) -> '_2293.RingPinsSocket':
        """RingPinsSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Socket

        if temp is None:
            return None

        if _2293.RingPinsSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket to RingPinsSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_of_type_clutch_socket(self) -> '_2296.ClutchSocket':
        """ClutchSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Socket

        if temp is None:
            return None

        if _2296.ClutchSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket to ClutchSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_of_type_concept_coupling_socket(self) -> '_2298.ConceptCouplingSocket':
        """ConceptCouplingSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Socket

        if temp is None:
            return None

        if _2298.ConceptCouplingSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket to ConceptCouplingSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_of_type_coupling_socket(self) -> '_2300.CouplingSocket':
        """CouplingSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Socket

        if temp is None:
            return None

        if _2300.CouplingSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket to CouplingSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_of_type_part_to_part_shear_coupling_socket(self) -> '_2302.PartToPartShearCouplingSocket':
        """PartToPartShearCouplingSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Socket

        if temp is None:
            return None

        if _2302.PartToPartShearCouplingSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket to PartToPartShearCouplingSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_of_type_spring_damper_socket(self) -> '_2304.SpringDamperSocket':
        """SpringDamperSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Socket

        if temp is None:
            return None

        if _2304.SpringDamperSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket to SpringDamperSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_of_type_torque_converter_pump_socket(self) -> '_2306.TorqueConverterPumpSocket':
        """TorqueConverterPumpSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Socket

        if temp is None:
            return None

        if _2306.TorqueConverterPumpSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket to TorqueConverterPumpSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_of_type_torque_converter_turbine_socket(self) -> '_2307.TorqueConverterTurbineSocket':
        """TorqueConverterTurbineSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Socket

        if temp is None:
            return None

        if _2307.TorqueConverterTurbineSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket to TorqueConverterTurbineSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def support_material(self) -> '_263.Material':
        """Material: 'SupportMaterial' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SupportMaterial

        if temp is None:
            return None

        if _263.Material.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast support_material to Material. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def nodes(self) -> 'List[_2337.FESubstructureNode]':
        """List[FESubstructureNode]: 'Nodes' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Nodes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def report_names(self) -> 'List[str]':
        """List[str]: 'ReportNames' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ReportNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)
        return value

    def nodes_grouped_by_angle(self) -> 'OrderedDict[float, List[_2337.FESubstructureNode]]':
        """ 'NodesGroupedByAngle' is the original name of this method.

        Returns:
            OrderedDict[float, List[mastapy.system_model.fe.FESubstructureNode]]
        """

        return conversion.pn_to_mp_objects_in_list_in_ordered_dict(self.wrapped.NodesGroupedByAngle(), float)

    def add_or_replace_node(self, node: '_2337.FESubstructureNode'):
        """ 'AddOrReplaceNode' is the original name of this method.

        Args:
            node (mastapy.system_model.fe.FESubstructureNode)
        """

        self.wrapped.AddOrReplaceNode(node.wrapped if node else None)

    def remove_all_nodes(self):
        """ 'RemoveAllNodes' is the original name of this method."""

        self.wrapped.RemoveAllNodes()

    def output_default_report_to(self, file_path: 'str'):
        """ 'OutputDefaultReportTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else '')

    def get_default_report_with_encoded_images(self) -> 'str':
        """ 'GetDefaultReportWithEncodedImages' is the original name of this method.

        Returns:
            str
        """

        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    def output_active_report_to(self, file_path: 'str'):
        """ 'OutputActiveReportTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else '')

    def output_active_report_as_text_to(self, file_path: 'str'):
        """ 'OutputActiveReportAsTextTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else '')

    def get_active_report_with_encoded_images(self) -> 'str':
        """ 'GetActiveReportWithEncodedImages' is the original name of this method.

        Returns:
            str
        """

        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    def output_named_report_to(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportTo' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(report_name if report_name else '', file_path if file_path else '')

    def output_named_report_as_masta_report(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportAsMastaReport' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(report_name if report_name else '', file_path if file_path else '')

    def output_named_report_as_text_to(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportAsTextTo' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(report_name if report_name else '', file_path if file_path else '')

    def get_named_report_with_encoded_images(self, report_name: 'str') -> 'str':
        """ 'GetNamedReportWithEncodedImages' is the original name of this method.

        Args:
            report_name (str)

        Returns:
            str
        """

        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(report_name if report_name else '')
        return method_result
