import ast

from src.handle_expr.h_comp import handle_comp
from src.util.calc_callable_type import is_callable_type, calc_callable_type
from src.util.inner_strings import calc_inside_ang, calc_inside_rd
from src.util.ret_imports import RetImports
from src.util.util import calc_ref_str


def handle_ann_assign(
    node: ast.AnnAssign,
    ret_imports: RetImports,
    ret_h_file: list[str],
    handle_expr,
    handle_stmt,
) -> str:
    if is_callable_type(node.annotation):
        type_cpp: str = calc_callable_type(node.annotation, ret_imports, handle_expr)
    else:
        type_cpp: str = handle_expr(node.annotation, ret_imports)
    target_str = handle_expr(node.target, ret_imports)
    if node.value is None:
        return f"{type_cpp} {target_str};"
    if isinstance(node.value, (ast.ListComp, ast.SetComp, ast.DictComp)):
        return f"{type_cpp} {target_str}; " + handle_comp(
            node.value, ret_imports, ret_h_file, handle_expr, handle_stmt, target_str
        )
    value_str = handle_expr(node.value, ret_imports)
    if value_str == "PyList({})":
        value_str = _empty_initialize("PyList", type_cpp)
    elif value_str == "set()":
        value_str = _empty_initialize("PySet", type_cpp)
    if value_str.startswith("defaultdict("):
        py_value_type = _calc_py_value_type(node.value)
        if py_value_type != "":
            new_value_str = _calc_default_dict_value_str(type_cpp, py_value_type)
            return f"auto {target_str} = {new_value_str};"
    if type_cpp.startswith("PyDict<"):
        # TODO later: consider that dicts are handled differently here than lists
        #  and sets. It might be nice if they are handled the same, but it seems hard
        #  to make it so.
        return f"{type_cpp} {target_str}({value_str});"
    if type_cpp.startswith("PyDefaultDict<") or type_cpp.startswith("Uni<"):
        v: str = calc_inside_rd(value_str)
        if v == "std::monostate":
            v += "{}"
        return f"{type_cpp} {target_str}({v});"
    ref, type_cpp = calc_ref_str(type_cpp)
    return f"{type_cpp}{ref} {target_str} = {value_str};"


def _calc_py_value_type(node: ast.expr) -> str:
    if (
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "defaultdict"
    ):
        assert len(node.args) == 1, "defaultdict should have 1 argument"
        if isinstance(node.args[0], ast.Name):
            value_type = node.args[0].id
            if value_type in ("int", "float", "str", "bool"):
                return value_type
        elif isinstance(node.args[0], ast.Subscript):
            if isinstance(node.args[0].value, ast.Name):
                value_type = node.args[0].value.id
                if value_type in ("list", "dict", "set"):
                    return value_type
    return ""


def _calc_default_dict_value_str(type_cpp: str, py_value_type) -> str:
    key_type = type_cpp[type_cpp.index("<") + 1 : type_cpp.index(",")]
    cpp_value_type = type_cpp[type_cpp.index(",") + 1 : type_cpp.rindex(">")].strip()
    return f"PyDefaultDict<{key_type}, {cpp_value_type}>::{py_value_type}_factory()"


def _empty_initialize(s: str, type_cpp: str):
    return f"{s}<{calc_inside_ang(type_cpp)}>" + "({})"
