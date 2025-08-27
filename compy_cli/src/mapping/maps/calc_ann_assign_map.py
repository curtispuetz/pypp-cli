from compy_cli.src.compy_dirs import CompyDirs
from compy_cli.src.d_types import PySpecificImpFrom
from compy_cli.src.main_scripts.util.load_proj_info import ProjInfo
from compy_cli.src.mapping.d_types import (
    CustomMappingStartsWithEntry,
    AnnAssignsMap,
)
from compy_cli.src.mapping.maps.util.calc_map_1 import (
    BASE_CALC_ENTRY_FN_MAP,
    calc_map_1,
)


def _py_dict(
    type_cpp: str, target_str: str, value_str: str, _value_str_stripped: str
) -> str:
    return f"{type_cpp} {target_str}({value_str})"


def _uni(
    type_cpp: str, target_str: str, _value_str: str, value_str_stripped: str
) -> str:
    if value_str_stripped == "std::monostate":
        value_str_stripped += "{}"
    return f"{type_cpp} {target_str}({value_str_stripped})"


ANN_ASSIGN_MAP: AnnAssignsMap = {
    "PyDict<": {None: CustomMappingStartsWithEntry(_py_dict, [])},
    "Uni<": {
        PySpecificImpFrom("compy_python.union", "Uni"): CustomMappingStartsWithEntry(
            _uni, []
        )
    },
}


def calc_ann_assign_map(proj_info: ProjInfo, dirs: CompyDirs) -> AnnAssignsMap:
    return calc_map_1(
        ANN_ASSIGN_MAP,
        BASE_CALC_ENTRY_FN_MAP,
        "ann_assign_map",
        "ann_assign",
        proj_info,
        dirs,
    )
