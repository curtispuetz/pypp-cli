import ast
from typing import Callable

from compy_cli.src.transpilers.other.transpiler.d_types import AngInc, QInc, PyImport
from compy_cli.src.transpilers.other.transpiler.maps.d_types import (
    AttrMap,
    AttrMapEntry,
    CustomMappingStartsWithEntry,
    ToStringEntry,
)
from compy_cli.src.transpilers.other.transpiler.maps.util.calc_map_1 import (
    BASE_CALC_ENTRY_FN_MAP,
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
