import ast
from typing import Callable

from compy_cli.src.compy_dirs import CompyDirs
from compy_cli.src.d_types import AngInc, QInc, PyImport
from compy_cli.src.main_scripts.util.load_proj_info import ProjInfo
from compy_cli.src.mapping.d_types import (
    AttrMap,
    AttrMapEntry,
    CustomMappingStartsWithEntry,
    ToStringEntry,
)
from compy_cli.src.mapping.maps.util.calc_map_1 import (
    BASE_CALC_ENTRY_FN_MAP,
    calc_map_a,
    calc_replace_dot_with_double_colon_entry,
)


def _math_custom_mapping(_node: ast.Attribute, d, res_str: str):
    attr_str: str = res_str.split(".")[-1]
    if attr_str == "pi":
        d.add_inc(AngInc("numbers"))
        return "std::numbers::pi"
    if attr_str == "radians":
        d.add_inc(AngInc("numbers"))
        return "(std::numbers::pi / 180.0) * "
    d.add_inc(AngInc("cmath"))
    return f"std::{attr_str}"


ATTR_MAP: AttrMap = {
    "random.Random": {
        PyImport("random"): ToStringEntry(
            "random::Random",
            [QInc("compy_random.h")],
        )
    },
    "math.": {
        PyImport("math"): CustomMappingStartsWithEntry(
            _math_custom_mapping,
            [],
        )
    },
}

ATTR_CALC_ENTRY_FN_MAP: dict[str, Callable[[dict], AttrMapEntry]] = {
    **BASE_CALC_ENTRY_FN_MAP,
    "replace_dot_with_double_colon": calc_replace_dot_with_double_colon_entry,
}


def calc_attr_map(proj_info: ProjInfo, dirs: CompyDirs) -> AttrMap:
    return calc_map_a(
        ATTR_MAP, ATTR_CALC_ENTRY_FN_MAP, "attr_map", "attr", proj_info, dirs
    )
