from pathlib import Path
from compy_cli.src.transpiler.module.d_types import PySpecificImpFrom
from compy_cli.src.transpiler.maps.d_types import (
    CustomMappingStartsWithEntry,
    AnnAssignsMap,
)
from compy_cli.src.transpiler.maps.util.calc_map_1 import (
    BASE_CALC_ENTRY_FN_MAP,
    calc_map_1,
)


def _uni(
    type_cpp: str, target_str: str, _value_str: str, value_str_stripped: str
) -> str:
    if value_str_stripped == "std::monostate":
        value_str_stripped += "{}"
    return f"{type_cpp} {target_str}({value_str_stripped})"


ANN_ASSIGN_MAP: AnnAssignsMap = {
    "Uni<": {
        PySpecificImpFrom("compy_python.union", "Uni"): CustomMappingStartsWithEntry(
            _uni, []
        )
    },
}


def calc_ann_assign_map(
    installed_bridge_libs: dict[str, str], py_env_parent_dir: Path
) -> AnnAssignsMap:
    return calc_map_1(
        ANN_ASSIGN_MAP,
        BASE_CALC_ENTRY_FN_MAP,
        "ann_assign_map",
        "ann_assign",
        installed_bridge_libs,
        py_env_parent_dir,
    )
