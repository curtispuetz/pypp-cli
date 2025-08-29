from typing import Callable

from compy_cli.src.compy_dirs import CompyDirs
from compy_cli.src.transpiler.module.handle_expr.h_call.default_map import CALL_MAP
from compy_cli.src.transpiler.util.load_proj_info import ProjInfo
from compy_cli.src.transpiler.maps.util.util import (
    calc_cpp_includes,
)
from compy_cli.src.transpiler.maps.d_types import (
    CallMapEntry,
    LeftAndRightEntry,
    CallMap,
)
from compy_cli.src.transpiler.maps.util.calc_map_1 import (
    BASE_CALC_ENTRY_FN_MAP,
    calc_map_1,
    calc_replace_dot_with_double_colon_entry,
)


def _calc_left_and_right_entry(obj: dict) -> LeftAndRightEntry:
    return LeftAndRightEntry(obj["left"], obj["right"], calc_cpp_includes(obj))


CALL_CALC_ENTRY_FN_MAP: dict[str, Callable[[dict], CallMapEntry]] = {
    **BASE_CALC_ENTRY_FN_MAP,
    "left_and_right": _calc_left_and_right_entry,
    "replace_dot_with_double_colon": calc_replace_dot_with_double_colon_entry,
}


def calc_call_map(proj_info: ProjInfo, dirs: CompyDirs) -> CallMap:
    return calc_map_1(
        CALL_MAP, CALL_CALC_ENTRY_FN_MAP, "call_map", "call", proj_info, dirs
    )
