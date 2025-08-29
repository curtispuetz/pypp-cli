import ast

from compy_cli.src.transpiler.module.d_types import (
    AngInc,
    PyImport,
    PySpecificImpFrom,
    QInc,
)
from compy_cli.src.transpiler.module.handle_expr.h_call.default_dict_map_fn import (
    good_default_dict,
)
from compy_cli.src.transpiler.module.mapping.d_types import (
    ToStringEntry,
    CustomMappingEntry,
    CustomMappingStartsWithEntry,
    LeftAndRightEntry,
    ReplaceDotWithDoubleColonEntry,
    CallMap,
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


CALL_MAP: CallMap = {
    "print": {None: ToStringEntry("print", [QInc("compy_util/print.h")])},
    "print_address": {
        PySpecificImpFrom("compy_python.printing", "print_address"): LeftAndRightEntry(
            "print(&",
            ")",
            [QInc("compy_util/print.h")],
        )
    },
    "len": {None: LeftAndRightEntry("", ".len()", [])},
    "to_std_string": {
        PySpecificImpFrom("compy_python.strings", "to_std_string"): LeftAndRightEntry(
            "", ".str()", []
        )
    },
    "to_c_string": {
        PySpecificImpFrom("compy_python.strings", "to_c_string"): LeftAndRightEntry(
            "", ".str().c_str()", []
        )
    },
    "PyStr": {None: ToStringEntry("to_pystr", [QInc("compy_util/to_py_str.h")])},
    "PySlice": {None: ToStringEntry("py_slice", [QInc("slice/creators.h")])},
    "mov": {
        PySpecificImpFrom("compy_python.ownership", "mov"): ToStringEntry(
            "std::move", [AngInc("utility")]
        )
    },
    "compy_get_resources": {
        PySpecificImpFrom(
            "compy_python.resources", "compy_get_resources"
        ): ToStringEntry("compy_get_resources", [QInc("compy_resources.h")])
    },
    "int_pow": {
        PySpecificImpFrom("compy_python.math", "int_pow"): ToStringEntry(
            "int_pow", [QInc("compy_util/math.h")]
        )
    },
    "PyDefaultDict": {
        PySpecificImpFrom("collections", "defaultdict"): CustomMappingEntry(
            _default_dict, []
        )
    },
    "tg": {
        PySpecificImpFrom("compy_python.tuple_get", "tg"): CustomMappingEntry(
            _tuple_get, []
        )
    },
    "dg": {
        PySpecificImpFrom("compy_python.dict_get", "dg"): CustomMappingEntry(
            _dict_get, []
        )
    },
    "ug": {
        PySpecificImpFrom("compy_python.union", "ug"): CustomMappingEntry(
            _union_get, []
        )
    },
    "isinst": {
        PySpecificImpFrom("compy_python.union", "isinst"): CustomMappingEntry(
            _union_isinst, []
        )
    },
    "is_none": {
        PySpecificImpFrom("compy_python.union", "is_none"): CustomMappingEntry(
            _union_is_none, []
        )
    },
    "list_reserve": {
        PySpecificImpFrom("compy_python.lists", "list_reserve"): CustomMappingEntry(
            _list_reserve, []
        )
    },
    "PyDefaultDict<": {
        PySpecificImpFrom("collections", "defaultdict"): CustomMappingStartsWithEntry(
            good_default_dict, []
        )
    },
    "os.": {PyImport("os"): ReplaceDotWithDoubleColonEntry([QInc("compy_os.h")])},
    "shutil.": {
        PyImport("shutil"): ReplaceDotWithDoubleColonEntry([QInc("compy_shutil.h")])
    },
    "compy_time.": {
        PyImport(
            "compy_python.stl.compy_time", "compy_time"
        ): ReplaceDotWithDoubleColonEntry([QInc("compy_time.h")])
    },
}
