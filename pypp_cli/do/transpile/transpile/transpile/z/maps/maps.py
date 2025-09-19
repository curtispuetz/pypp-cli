from dataclasses import dataclass

from pypp_cli.do.transpile.load_bridge_json.z.other.models import (
    AlwaysPassByValueModel,
    AnnAssignModel,
    AttrModel,
    CallModel,
    NameModel,
    SubscriptableTypeModel,
)
from pypp_cli.do.transpile.load_bridge_json.node import BridgeJsonModels
from pypp_cli.do.transpile.transpile.transpile.z.d_types import PySpecificImport
from pypp_cli.do.transpile.transpile.transpile.z.maps.ann_assign import ANN_ASSIGN_MAP
from pypp_cli.do.transpile.transpile.transpile.z.maps.attr import ATTR_MAP
from pypp_cli.do.transpile.transpile.transpile.z.maps.call.call import (
    CALL_MAP,
)
from pypp_cli.do.transpile.transpile.transpile.z.maps.fn_arg_passed_by_value import (
    PRIMITIVE_TYPES,
    fn_arg_passed_by_value_warning_msg,
)
from pypp_cli.do.transpile.transpile.transpile.z.maps.d_types import (
    AnnAssignsMap,
    AttrMap,
    CallMap,
    FnArgByValueMap,
    NameMap,
    SubscriptableTypeMap,
)
from pypp_cli.do.transpile.transpile.transpile.z.maps.name import NAME_MAP
from pypp_cli.do.transpile.transpile.transpile.z.maps.subscriptable_types import (
    SUBSCRIPTABLE_TYPE_MAP,
    subscriptable_type_warning_msg,
)
from pypp_cli.do.transpile.transpile.transpile.z.maps.model_to_d_types import (
    calc_custom_mapping_from_lib_entry,
    calc_custom_mapping_starts_with_from_lib_entry,
    calc_left_and_right_entry,
    calc_replace_dot_with_double_colon_entry,
    calc_to_string_entry,
    calc_imp_str,
    calc_required_py_import,
)


@dataclass(frozen=True, slots=True)
class Maps:
    name: NameMap
    call: CallMap
    attr: AttrMap
    fn_arg_passed_by_value: FnArgByValueMap
    subscriptable_type: SubscriptableTypeMap
    ann_assign: AnnAssignsMap


@dataclass(frozen=True, slots=True)
class MapsCltr:
    _bridge_json_models: dict[str, BridgeJsonModels]

    def calc_maps(self) -> Maps:
        name_map: NameMap = NAME_MAP.copy()
        call_map: CallMap = CALL_MAP.copy()
        attr_map: AttrMap = ATTR_MAP.copy()
        fn_arg_passed_by_value: FnArgByValueMap = PRIMITIVE_TYPES.copy()
        subscriptable_type: SubscriptableTypeMap = SUBSCRIPTABLE_TYPE_MAP.copy()
        ann_assign_map: AnnAssignsMap = ANN_ASSIGN_MAP.copy()
        for lib, m in self._bridge_json_models.items():
            if m.name_map is not None:
                self._calc_name_map(lib, m.name_map, name_map)
            if m.call_map is not None:
                self._calc_call_map(lib, m.call_map, call_map)
            if m.attr_map is not None:
                self._calc_attr_map(lib, m.attr_map, attr_map)
            if m.ann_assign_map is not None:
                self._calc_ann_assign_map(lib, m.ann_assign_map, ann_assign_map)
            if m.always_pass_by_value is not None:
                self._calc_fn_arg_passed_by_value(
                    lib, m.always_pass_by_value, fn_arg_passed_by_value
                )
            if m.subscriptable_types is not None:
                self._calc_subscriptable_type_map(
                    lib, m.subscriptable_types, subscriptable_type
                )
        return Maps(
            name_map,
            call_map,
            attr_map,
            fn_arg_passed_by_value,
            subscriptable_type,
            ann_assign_map,
        )

    def _calc_call_map(self, lib: str, model: CallModel, ret: CallMap):
        if model.to_string is not None:
            self._add_mapping_entries_1(
                model.to_string.root,
                calc_to_string_entry,
                lib,
                ret,
            )
        if model.left_and_right is not None:
            self._add_mapping_entries_1(
                model.left_and_right.root,
                calc_left_and_right_entry,
                lib,
                ret,
            )
        if model.custom_mapping is not None:
            self._add_mapping_entries_1(
                model.custom_mapping.root,
                calc_custom_mapping_from_lib_entry,
                lib,
                ret,
            )
        if model.custom_mapping_starts_with is not None:
            self._add_mapping_entries_1(
                model.custom_mapping_starts_with.root,
                calc_custom_mapping_starts_with_from_lib_entry,
                lib,
                ret,
            )
        if model.replace_dot_with_double_colon is not None:
            self._add_mapping_entries_1(
                model.replace_dot_with_double_colon.root,
                calc_replace_dot_with_double_colon_entry,
                lib,
                ret,
            )

    def _calc_name_map(self, lib: str, model: NameModel, ret: NameMap):
        if model.to_string is not None:
            self._add_mapping_entries_1(
                model.to_string.root,
                calc_to_string_entry,
                lib,
                ret,
            )
        if model.custom_mapping is not None:
            self._add_mapping_entries_1(
                model.custom_mapping.root,
                calc_custom_mapping_from_lib_entry,
                lib,
                ret,
            )
        if model.custom_mapping_starts_with is not None:
            self._add_mapping_entries_1(
                model.custom_mapping_starts_with.root,
                calc_custom_mapping_starts_with_from_lib_entry,
                lib,
                ret,
            )

    def _calc_attr_map(self, lib: str, model: AttrModel, ret: AttrMap):
        if model.to_string is not None:
            self._add_mapping_entries_1(
                model.to_string.root,
                calc_to_string_entry,
                lib,
                ret,
            )
        if model.custom_mapping is not None:
            self._add_mapping_entries_1(
                model.custom_mapping.root,
                calc_custom_mapping_from_lib_entry,
                lib,
                ret,
            )
        if model.custom_mapping_starts_with is not None:
            self._add_mapping_entries_1(
                model.custom_mapping_starts_with.root,
                calc_custom_mapping_starts_with_from_lib_entry,
                lib,
                ret,
            )
        if model.replace_dot_with_double_colon is not None:
            self._add_mapping_entries_1(
                model.replace_dot_with_double_colon.root,
                calc_replace_dot_with_double_colon_entry,
                lib,
                ret,
            )

    def _calc_ann_assign_map(self, lib: str, model: AnnAssignModel, ret: AnnAssignsMap):
        if model.custom_mapping is not None:
            self._add_mapping_entries_1(
                model.custom_mapping.root,
                calc_custom_mapping_from_lib_entry,
                lib,
                ret,
            )
        if model.custom_mapping_starts_with is not None:
            self._add_mapping_entries_1(
                model.custom_mapping_starts_with.root,
                calc_custom_mapping_starts_with_from_lib_entry,
                lib,
                ret,
            )

    def _calc_fn_arg_passed_by_value(
        self, lib: str, model: AlwaysPassByValueModel, ret: FnArgByValueMap
    ):
        self._add_mapping_entries_2(
            model.root, fn_arg_passed_by_value_warning_msg, lib, ret
        )

    def _calc_subscriptable_type_map(
        self, lib: str, model: SubscriptableTypeModel, ret: SubscriptableTypeMap
    ):
        self._add_mapping_entries_2(
            model.root, subscriptable_type_warning_msg, lib, ret
        )

    def _add_mapping_entries_2(self, mapping_root, warning_msg, lib, ret):
        # note: We don't need type hints here. If there is a problem with this
        # code, it runs each transpile, so errors will throw.
        for k, v in mapping_root.items():
            required_import = (
                calc_required_py_import(v.required_py_import) if v is not None else None
            )
            if k in ret:
                if required_import in ret[k]:
                    warning_msg(lib, f"{k}{calc_imp_str(required_import)}")
                ret[k].add(required_import)
            else:
                ret[k] = {required_import}

    def _add_mapping_entries_1(self, mapping_root, entry_func, lib, ret):
        # note: We don't need type hints here. If there is a problem with this
        # code, it runs each transpile, so errors will throw.
        for name, value in mapping_root.items():
            required_import = calc_required_py_import(value.required_py_import)
            entry = entry_func(value)
            if name in ret:
                if required_import in ret[name]:
                    self._override_mapping_warning(name, required_import, lib)
                ret[name][required_import] = entry
            else:
                ret[name] = {required_import: entry}

    def _override_mapping_warning(
        self, name: str, required_import: PySpecificImport | None, lib: str
    ):
        print(
            f"warning: Py++ transpiler already maps the name {name}"
            f"{calc_imp_str(required_import)}."
            f"Library {lib} is overriding this mapping."
        )

    # Don't need this one for now
    def _override_mapping_warning_local(
        self, name: str, required_import: PySpecificImport | None
    ):
        print(
            f"warning: Py++ transpiler already maps the name {name}"
            f"{calc_imp_str(required_import)}."
            f"The .pypp/bridge_jsons/name_map.json is overriding this mapping."
        )
