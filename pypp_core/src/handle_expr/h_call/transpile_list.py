import ast

from pypp_core.src.d_types import AngInc, PyImport, PySpecificImpFrom, QInc
from pypp_core.src.deps import Deps
from pypp_core.src.handle_expr.h_call.d_types import CallsTranspile
from pypp_core.src.handle_expr.h_call.default_dict import good_default_dict


def _default_dict(node: ast.Call, d: Deps, include_in_header: bool) -> str:
    raise Exception(
        "defaultdict must be called with type info "
        "(i.e. defaultdict[KeyType, ValueType])"
    )


def _tuple_get(node: ast.Call, d: Deps, include_in_header: bool) -> str:
    assert len(node.args) == 2, "tg should have 2 arguments"
    d.add_inc(AngInc("any"), include_in_header)
    tuple_arg = d.handle_expr(node.args[0])
    index_arg = d.handle_expr(node.args[1])
    return f"{tuple_arg}.get<{index_arg}>()"


def _dict_get(node: ast.Call, d: Deps, include_in_header: bool) -> str:
    assert len(node.args) == 2, "dg should have 2 arguments"
    dict_arg = d.handle_expr(node.args[0])
    index_arg = d.handle_expr(node.args[1])
    return f"{dict_arg}.dg({index_arg})"


def _union_get(node: ast.Call, d: Deps, include_in_header: bool) -> str:
    assert len(node.args) == 2, "ug should have 2 arguments"
    union_arg = d.handle_expr(node.args[0])
    type_arg = d.handle_expr(node.args[1])
    return f"{union_arg}.ug<{type_arg}>()"


def _union_isinst(node: ast.Call, d: Deps, include_in_header: bool) -> str:
    assert len(node.args) == 2, "isinst should have 2 arguments"
    obj_arg = d.handle_expr(node.args[0])
    type_arg = d.handle_expr(node.args[1])
    return f"{obj_arg}.isinst<{type_arg}>()"


def _union_is_none(node: ast.Call, d: Deps, include_in_header: bool) -> str:
    assert len(node.args) == 1, "is_none should have 1 argument"
    obj_arg = d.handle_expr(node.args[0])
    return f"{obj_arg}.is_none()"


def _list_reserve(node: ast.Call, d: Deps, include_in_header: bool) -> str:
    assert len(node.args) == 2, "list_reserve should have 2 arguments"
    list_arg = d.handle_expr(node.args[0])
    size_arg = d.handle_expr(node.args[1])
    return f"{list_arg}.reserve({size_arg})"


CALLS_TRANSPILE: list[CallsTranspile] = [
    CallsTranspile(
        PySpecificImpFrom("collections", "defaultdict"), "defaultdict", fn=_default_dict
    ),
    CallsTranspile(
        PySpecificImpFrom("pypp_python.tuple_get", "tg"), "tg", fn=_tuple_get
    ),
    CallsTranspile(PySpecificImpFrom("pypp_python.dict_get", "dg"), "dg", fn=_dict_get),
    CallsTranspile(PySpecificImpFrom("pypp_python.union", "ug"), "ug", fn=_union_get),
    CallsTranspile(
        PySpecificImpFrom("pypp_python.union", "isinst"), "isinst", fn=_union_isinst
    ),
    CallsTranspile(
        PySpecificImpFrom("pypp_python.union", "is_none"), "is_none", fn=_union_is_none
    ),
    CallsTranspile(
        PySpecificImpFrom("pypp_python.lists", "list_reserve"),
        "list_reserve",
        fn=_list_reserve,
    ),
    CallsTranspile(
        PySpecificImpFrom("collections", "defaultdict"),
        "PyDefaultDict<",
        fn_starts_with=good_default_dict,
    ),
    CallsTranspile(
        PyImport("os"), "os.", replace_dot_with_double_colon_include=QInc("pypp_os.h")
    ),
    CallsTranspile(
        PyImport("shutil"),
        "shutil.",
        replace_dot_with_double_colon_include=QInc("pypp_shutil.h"),
    ),
    CallsTranspile(
        PyImport("random"),
        "random.",
        replace_dot_with_double_colon_include=QInc("pypp_random.h"),
    ),
    CallsTranspile(
        PyImport("pypp_python.stl.pypp_time", "pypp_time"),
        "pypp_time.",
        replace_dot_with_double_colon_include=QInc("pypp_time.h"),
    ),
]
