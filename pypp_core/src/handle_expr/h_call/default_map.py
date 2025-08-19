import ast

from pypp_core.src.d_types import AngInc, PyImport, PySpecificImpFrom, QInc
from pypp_core.src.handle_expr.h_call.default_dict_map_fn import good_default_dict
from pypp_core.src.mapping.info_types import (
    CallMapInfo,
    CallMapInfoCppType,
    CallMapInfoCustomMapping,
    CallMapInfoCustomMappingStartsWith,
    CallMapInfoLeftAndRight,
    CallMapInfoNone,
    CallMapInfoReplaceDotWithDoubleColon,
)


def _default_dict(node: ast.Call, d) -> str:
    raise Exception(
        "defaultdict must be called with type info "
        "(i.e. defaultdict[KeyType, ValueType])"
    )


def _tuple_get(node: ast.Call, d) -> str:
    assert len(node.args) == 2, "tg should have 2 arguments"
    tuple_arg = d.handle_expr(node.args[0])
    index_arg = d.handle_expr(node.args[1])
    return f"{tuple_arg}.get<{index_arg}>()"


def _dict_get(node: ast.Call, d) -> str:
    assert len(node.args) == 2, "dg should have 2 arguments"
    dict_arg = d.handle_expr(node.args[0])
    index_arg = d.handle_expr(node.args[1])
    return f"{dict_arg}.dg({index_arg})"


def _union_get(node: ast.Call, d) -> str:
    assert len(node.args) == 2, "ug should have 2 arguments"
    union_arg = d.handle_expr(node.args[0])
    type_arg = d.handle_expr(node.args[1])
    return f"{union_arg}.ug<{type_arg}>()"


def _union_isinst(node: ast.Call, d) -> str:
    assert len(node.args) == 2, "isinst should have 2 arguments"
    obj_arg = d.handle_expr(node.args[0])
    type_arg = d.handle_expr(node.args[1])
    return f"{obj_arg}.isinst<{type_arg}>()"


def _union_is_none(node: ast.Call, d) -> str:
    assert len(node.args) == 1, "is_none should have 1 argument"
    obj_arg = d.handle_expr(node.args[0])
    return f"{obj_arg}.is_none()"


def _list_reserve(node: ast.Call, d) -> str:
    assert len(node.args) == 2, "list_reserve should have 2 arguments"
    list_arg = d.handle_expr(node.args[0])
    size_arg = d.handle_expr(node.args[1])
    return f"{list_arg}.reserve({size_arg})"


CALLS_MAP: dict[str, CallMapInfo] = {
    "print": CallMapInfoNone([QInc("pypp_util/print.h")]),
    "print_address": CallMapInfoLeftAndRight(
        "print(&",
        ")",
        [QInc("pypp_util/print.h")],
        PySpecificImpFrom("pypp_python.printing", "print_address"),
    ),
    "len": CallMapInfoLeftAndRight("", ".len()", []),
    "str": CallMapInfoCppType("to_pystr", [QInc("pypp_util/to_py_str.h")]),
    "range": CallMapInfoCppType("PyRange", [QInc("py_range.h")]),
    "slice": CallMapInfoCppType("py_slice", [QInc("slice/creators.h")]),
    "enumerate": CallMapInfoCppType("PyEnumerate", [QInc("py_enumerate.h")]),
    "reversed": CallMapInfoCppType("PyReversed", [QInc("py_reversed.h")]),
    "zip": CallMapInfoCppType("PyZip", [QInc("py_zip.h")]),
    "mov": CallMapInfoCppType(
        "std::move",
        [AngInc("utility")],
        PySpecificImpFrom("pypp_python.ownership", "mov"),
    ),
    "pypp_get_resources": CallMapInfoNone(
        [QInc("pypp_resources.h")],
        PySpecificImpFrom("pypp_python.resources", "pypp_get_resources"),
    ),
    "int_pow": CallMapInfoNone(
        [QInc("pypp_util/math.h")],
        PySpecificImpFrom("pypp_python.math", "int_pow"),
    ),
    "defaultdict": CallMapInfoCustomMapping(
        _default_dict, [], PySpecificImpFrom("collections", "defaultdict")
    ),
    "tg": CallMapInfoCustomMapping(
        _tuple_get, [], PySpecificImpFrom("pypp_python.tuple_get", "tg")
    ),
    "dg": CallMapInfoCustomMapping(
        _dict_get, [], PySpecificImpFrom("pypp_python.dict_get", "dg")
    ),
    "ug": CallMapInfoCustomMapping(
        _union_get, [], PySpecificImpFrom("pypp_python.union", "ug")
    ),
    "isinst": CallMapInfoCustomMapping(
        _union_isinst, [], PySpecificImpFrom("pypp_python.union", "isinst")
    ),
    "is_none": CallMapInfoCustomMapping(
        _union_is_none, [], PySpecificImpFrom("pypp_python.union", "is_none")
    ),
    "list_reserve": CallMapInfoCustomMapping(
        _list_reserve, [], PySpecificImpFrom("pypp_python.lists", "list_reserve")
    ),
    "PyDefaultDict<": CallMapInfoCustomMappingStartsWith(
        good_default_dict, [], PySpecificImpFrom("collections", "defaultdict")
    ),
    "os.": CallMapInfoReplaceDotWithDoubleColon([QInc("pypp_os.h")], PyImport("os")),
    "shutil.": CallMapInfoReplaceDotWithDoubleColon(
        [QInc("pypp_shutil.h")], PyImport("shutil")
    ),
    "random.": CallMapInfoReplaceDotWithDoubleColon(
        [QInc("pypp_random.h")], PyImport("random")
    ),
    "pypp_time.": CallMapInfoReplaceDotWithDoubleColon(
        [QInc("pypp_time.h")], PyImport("pypp_python.stl.pypp_time", "pypp_time")
    ),
}
