import ast

from pypp_cli.src.transpilers.library.transpiler.d_types import (
    AngInc,
    PyImport,
    PySpecificImpFrom,
)
from pypp_cli.src.transpilers.library.transpiler.maps.d_types import (
    AttrMap,
    CustomMappingStartsWithEntry,
)


def _math_custom_mapping(_node: ast.Attribute, d, res_str: str):
    attr_str: str = res_str[res_str.rfind(".") + 1 :]
    if attr_str == "pi":
        d.add_inc(AngInc("numbers"))
        return "std::numbers::pi"
    if attr_str == "radians":
        d.add_inc(AngInc("numbers"))
        return "(std::numbers::pi / 180.0) * "
    d.add_inc(AngInc("cmath"))
    return f"std::{attr_str}"


def _ctypes_custom_mapping(node: ast.Attribute, _d, res_str: str):
    node.attr
    attr_str: str = res_str[res_str.rfind(".") + 1 :]
    assert attr_str.startswith("c_void_p"), "only ctypes.c_void_p is supported"
    return "(void *)"


ATTR_MAP: AttrMap = {
    "math.": {
        PySpecificImpFrom("pypp_python.stl", "math"): CustomMappingStartsWithEntry(
            _math_custom_mapping,
            [],
        )
    },
    "ctypes.": {
        PySpecificImpFrom("pypp_python.stl", "ctypes"): CustomMappingStartsWithEntry(
            _ctypes_custom_mapping,
            [],
        )
    },
}
