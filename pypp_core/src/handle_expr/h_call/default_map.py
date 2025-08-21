import ast

from pypp_core.src.d_types import AngInc, PyImport, PySpecificImpFrom, QInc
from pypp_core.src.handle_expr.h_call.default_dict_map_fn import good_default_dict
from pypp_core.src.mapping.info_types import (
    CallMapInfoCppCall,
    CallMapInfoCustomMapping,
    CallMapInfoCustomMappingStartsWith,
    CallMapInfoLeftAndRight,
    CallMapInfoReplaceDotWithDoubleColon,
    CallsMap,
)


def _default_dict(_node: ast.Call, _d) -> str:
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


CALLS_MAP: CallsMap = {
    "print": {None: CallMapInfoCppCall("print", [QInc("pypp_util/print.h")])},
    "print_address": {
        PySpecificImpFrom(
            "pypp_python.printing", "print_address"
        ): CallMapInfoLeftAndRight(
            "print(&",
            ")",
            [QInc("pypp_util/print.h")],
        )
    },
    "len": {None: CallMapInfoLeftAndRight("", ".len()", [])},
    "PyStr": {None: CallMapInfoCppCall("to_pystr", [QInc("pypp_util/to_py_str.h")])},
    "PySlice": {None: CallMapInfoCppCall("py_slice", [QInc("slice/creators.h")])},
    "mov": {
        PySpecificImpFrom("pypp_python.ownership", "mov"): CallMapInfoCppCall(
            "std::move", [AngInc("utility")]
        )
    },
    "pypp_get_resources": {
        PySpecificImpFrom(
            "pypp_python.resources", "pypp_get_resources"
        ): CallMapInfoCppCall("pypp_get_resources", [QInc("pypp_resources.h")])
    },
    "int_pow": {
        PySpecificImpFrom("pypp_python.math", "int_pow"): CallMapInfoCppCall(
            "int_pow", [QInc("pypp_util/math.h")]
        )
    },
    "PyDefaultDict": {
        PySpecificImpFrom("collections", "defaultdict"): CallMapInfoCustomMapping(
            _default_dict, []
        )
    },
    "tg": {
        PySpecificImpFrom("pypp_python.tuple_get", "tg"): CallMapInfoCustomMapping(
            _tuple_get, []
        )
    },
    "dg": {
        PySpecificImpFrom("pypp_python.dict_get", "dg"): CallMapInfoCustomMapping(
            _dict_get, []
        )
    },
    "ug": {
        PySpecificImpFrom("pypp_python.union", "ug"): CallMapInfoCustomMapping(
            _union_get, []
        )
    },
    "isinst": {
        PySpecificImpFrom("pypp_python.union", "isinst"): CallMapInfoCustomMapping(
            _union_isinst, []
        )
    },
    "is_none": {
        PySpecificImpFrom("pypp_python.union", "is_none"): CallMapInfoCustomMapping(
            _union_is_none, []
        )
    },
    "list_reserve": {
        PySpecificImpFrom(
            "pypp_python.lists", "list_reserve"
        ): CallMapInfoCustomMapping(_list_reserve, [])
    },
    "PyDefaultDict<": {
        PySpecificImpFrom(
            "collections", "defaultdict"
        ): CallMapInfoCustomMappingStartsWith(good_default_dict, [])
    },
    "os.": {PyImport("os"): CallMapInfoReplaceDotWithDoubleColon([QInc("pypp_os.h")])},
    "shutil.": {
        PyImport("shutil"): CallMapInfoReplaceDotWithDoubleColon(
            [QInc("pypp_shutil.h")]
        )
    },
    "pypp_time.": {
        PyImport(
            "pypp_python.stl.pypp_time", "pypp_time"
        ): CallMapInfoReplaceDotWithDoubleColon([QInc("pypp_time.h")])
    },
}
