from dataclasses import dataclass
from pathlib import Path

from compy_cli.src.transpiler.maps.calc_ann_assign_map import (
    calc_ann_assign_map,
)
from compy_cli.src.transpiler.maps.calc_attr_map import calc_attr_map
from compy_cli.src.transpiler.maps.calc_call_map import calc_call_map
from compy_cli.src.transpiler.maps.calc_fn_arg_by_value_map import (
    calc_fn_arg_passed_by_value_map,
)
from compy_cli.src.transpiler.maps.calc_import_map import (
    ImportMap,
    calc_import_map,
)
from compy_cli.src.transpiler.maps.calc_name_map import calc_name_map
from compy_cli.src.transpiler.maps.d_types import (
    AnnAssignsMap,
    AttrMap,
    CallMap,
    FnArgByValueMap,
    NameMap,
    SubscriptableTypeMap,
)
from compy_cli.src.transpiler.maps.calc_subscriptable_type_map import (
    calc_subscriptable_type_map,
)


@dataclass(frozen=True, slots=True)
class Maps:
    name: NameMap
    call: CallMap
    attr: AttrMap
    fn_arg_passed_by_value: FnArgByValueMap
    subscriptable_type: SubscriptableTypeMap
    import_: ImportMap
    ann_assign: AnnAssignsMap


def calc_maps(installed_bridge_libs: dict[str, str], py_env_parent_dir: Path) -> Maps:
    return Maps(
        calc_name_map(installed_bridge_libs, py_env_parent_dir),
        calc_call_map(installed_bridge_libs, py_env_parent_dir),
        calc_attr_map(installed_bridge_libs, py_env_parent_dir),
        calc_fn_arg_passed_by_value_map(installed_bridge_libs, py_env_parent_dir),
        calc_subscriptable_type_map(installed_bridge_libs, py_env_parent_dir),
        calc_import_map(installed_bridge_libs, py_env_parent_dir),
        calc_ann_assign_map(installed_bridge_libs, py_env_parent_dir),
    )
