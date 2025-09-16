import ast

from pypp_cli.src.transpilers.library.transpiler.deps import Deps


_LIST_INIT_FNS = {"int_list", "float_list", "str_list"}


def calc_value_str_for_list_init_fns(node: ast.AnnAssign, d: Deps) -> str | None:
    if isinstance(node.value, ast.Call) and isinstance(node.value.func, ast.Name):
        if node.value.func.id in _LIST_INIT_FNS:
            return d.handle_exprs(node.value.args)
    return None
