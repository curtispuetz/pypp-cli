import ast

from pypp_core.src.d_types import AngInc, QInc, PySpecificImpFrom, PyImport
from pypp_core.src.deps import Deps
from pypp_core.src.handle_expr.h_starred import handle_call_with_starred_arg
from pypp_core.src.mapping.calls import lookup_cpp_call
from pypp_core.src.util.handle_lists import handle_exprs


def handle_call(
    node: ast.Call,
    d: Deps,
    include_in_header: bool,
):
    caller_str: str = d.handle_expr(
        node.func,
        skip_cpp_lookup=True,
        include_in_header=include_in_header,
    )
    # TODO: for bridge library creation, you let users define a function to run if a condition
    #  is met.
    if (
        d.is_imported(PySpecificImpFrom("collections", "defaultdict"))
        and caller_str == "defaultdict"
    ):
        raise Exception(
            "defaultdict must be called with type info "
            "(i.e. defaultdict[KeyType, ValueType])"
        )
    if (
        d.is_imported(PySpecificImpFrom("pypp_python.tuple_get", "tg"))
        and caller_str == "tg"
    ):
        assert len(node.args) == 2, "tg should have 2 arguments"
        d.add_inc(AngInc("any"), include_in_header)
        tuple_arg = d.handle_expr(node.args[0])
        index_arg = d.handle_expr(node.args[1])
        return f"{tuple_arg}.get<{index_arg}>()"
    if (
        d.is_imported(PySpecificImpFrom("pypp_python.dict_get", "dg"))
        and caller_str == "dg"
    ):
        assert len(node.args) == 2, "dg should have 2 arguments"
        dict_arg = d.handle_expr(node.args[0])
        index_arg = d.handle_expr(node.args[1])
        return f"{dict_arg}.dg({index_arg})"
    if (
        d.is_imported(PySpecificImpFrom("pypp_python.union", "ug"))
        and caller_str == "ug"
    ):
        assert len(node.args) == 2, "ug should have 2 arguments"
        union_arg = d.handle_expr(node.args[0])
        type_arg = d.handle_expr(node.args[1])
        return f"{union_arg}.ug<{type_arg}>()"
    if (
        d.is_imported(PySpecificImpFrom("pypp_python.union", "isinst"))
        and caller_str == "isinst"
    ):
        assert len(node.args) == 2, "isinst should have 2 arguments"
        obj_arg = d.handle_expr(node.args[0])
        type_arg = d.handle_expr(node.args[1])
        return f"{obj_arg}.isinst<{type_arg}>()"
    if (
        d.is_imported(PySpecificImpFrom("pypp_python.union", "is_none"))
        and caller_str == "is_none"
    ):
        assert len(node.args) == 1, "is_none should have 1 argument"
        obj_arg = d.handle_expr(node.args[0])
        return f"{obj_arg}.is_none()"
    if (
        d.is_imported(PySpecificImpFrom("pypp_python.lists", "list_reserve"))
        and caller_str == "list_reserve"
    ):
        assert len(node.args) == 2, "list_reserve should have 2 arguments"
        list_arg = d.handle_expr(node.args[0])
        size_arg = d.handle_expr(node.args[1])
        return f"{list_arg}.reserve({size_arg})"
    if len(node.args) == 1:
        first_arg = node.args[0]
        if isinstance(first_arg, ast.Starred):
            return handle_call_with_starred_arg(first_arg, d, caller_str)
    if d.is_imported(PyImport("os")) and caller_str.startswith("os."):
        d.add_inc(QInc("pypp_os.h"), include_in_header)
        caller_str = caller_str.replace(".", "::")
    elif d.is_imported(PyImport("shutil")) and caller_str.startswith("shutil."):
        d.add_inc(QInc("pypp_shutil.h"), include_in_header)
        caller_str = caller_str.replace(".", "::")
    elif d.is_imported(PyImport("random")) and caller_str.startswith("random."):
        d.add_inc(QInc("pypp_random.h"), include_in_header)
        caller_str = caller_str.replace(".", "::")
    elif d.is_imported(
        PyImport("pypp_python.stl.pypp_time", "pypp_time")
    ) and caller_str.startswith("pypp_time."):
        d.add_inc(QInc("pypp_time.h"), include_in_header)
        caller_str = caller_str.replace(".", "::")
    elif caller_str.startswith("PyDefaultDict<"):
        assert len(node.args) == 1, "defaultdict should have 1 argument"
        value_type = _calc_type_for_special_default_dict(node.args[0])
        if value_type is not None:
            return f"{caller_str}::{value_type}_factory()"
        args_str = handle_exprs(node.args, d, include_in_header)
        return f"{caller_str}({args_str})"
    args_str = handle_exprs(node.args, d, include_in_header)
    cpp_call_start, cpp_call_end = lookup_cpp_call(caller_str, d, include_in_header)
    return f"{cpp_call_start}{args_str}{cpp_call_end}"


def _calc_type_for_special_default_dict(arg1: ast.expr) -> str | None:
    if isinstance(arg1, ast.Name):
        value_type = arg1.id
        if value_type in ("int", "float", "str", "bool"):
            return value_type
    elif isinstance(arg1, ast.Subscript):
        if isinstance(arg1.value, ast.Name):
            value_type = arg1.value.id
            if value_type in ("list", "dict", "set"):
                return value_type
    return None
